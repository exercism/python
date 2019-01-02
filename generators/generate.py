#!/usr/bin/python
"""
Generates exercise_test.py files for tests with canonical data.
"""
import json
import re
import logging
from argparse import ArgumentParser
from collections import OrderedDict
from functools import partial
from itertools import repeat
from pathlib import Path
from string import punctuation, whitespace

# 3rd party imports:
from jinja2 import Environment, PackageLoader, select_autoescape, TemplateError
from yapf.yapflib.yapf_api import FormatFile, style
from yaml import load, dump
try:
    # attempt to load libyaml C-extension if available
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    # otherwise fall back on slower pure-Python version
    from yaml import Loader, Dumper

logging.basicConfig(format="%(levelname)s: %(message)s")
LOGGER = logging.getLogger(__name__)


def replace_all(string, chars, rep):
    """
    Replace any char in chars with rep, reduce runs and strip terminal ends.
    """
    trans = str.maketrans(dict(zip(chars, repeat(rep))))
    return re.sub("{0}+".format(re.escape(rep)), rep,
                  string.translate(trans)).strip(rep)


def to_snake(string):
    """
    Convert pretty much anything to snake_case.
    """
    clean = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", string)
    clean = re.sub("([a-z0-9])([A-Z])", r"\1_\2", clean).lower()
    return replace_all(clean, whitespace + punctuation, "_")


def to_camel(string):
    """
    Convert pretty much anything to CamelCase.
    """
    return "".join(w.title() for w in to_snake(string).split("_"))


def should_skip(case, tests=None):
    """
    Determins if the given case should be skipped.
    """
    for test in tests or []:
        prop = case.get("property")
        description = case.get("description")
        if prop and prop == test["property"]:
            if description and re.match(test["description"], description):
                return test.get("message", "extra-credit")
    return False


def is_error(case):
    """
    Determines if the given case is an error.
    """
    expect = case.get("expected")
    return expect and isinstance(expect, dict) and "error" in expect


def has_error(data):
    """
    Check if any case in the data is an error.
    """
    if "cases" in data:
        for case in data["cases"]:
            if has_error(case):
                return True
        return False
    return is_error(data)


def get_properties(data):
    """
    Get the list of the unique property values accessed in all tests.
    """

    def _get_properties(obj):
        if "cases" in obj:
            for case in obj["cases"]:
                for prop in get_properties(case):
                    yield prop
            return
        yield obj["property"]

    return sorted(set(_get_properties(data)))


def remap_property(string, properties_map=None):
    """
    Builds a function that maps a property name to a new name, if required.
    """
    return (properties_map or {}).get(string, string)


def prefer_double_quotes(string):
    """
    Prefer double quotes on a string that does not embed them.
    """
    if string.startswith("'") and string.endswith("'"):
        if '"' not in string:
            return '"' + string[1:-1] + '"'
    return string


def format_input(case, n_args=None):
    format_input_with_mappings({})


def format_input_with_mappings(input_mappings, case, n_args=None):
    """
    Format the case's input values for use in a function call.

    By default converts all arguments to positional form.

    If n_args is provided, convert only the first n argss to positional form.
    """
    if isinstance(case["input"], str):
        return case["input"]
    raw = list(case["input"].items())
    n_args = len(raw) if n_args is None else n_args
    result = []
    for _ in range(n_args):
        name, arg = raw.pop(0)
        if name in input_mappings:
            result.append(input_mappings[name](arg))
        elif isinstance(arg, dict):
            result.extend(map(prefer_double_quotes, map(repr, arg.values())))
        elif isinstance(arg, list):
            result.append("[" + ", ".join(
                map(prefer_double_quotes, map(repr, arg))) + "]")
        else:
            result.append(prefer_double_quotes(repr(arg)))
    while raw:
        result.append("{0}={1!s}".format(raw.pop(0)))
    return ", ".join(result)


def format_expect(case):
    """
    Format the case's expected values for use in a function call.
    """
    if is_error(case):
        return prefer_double_quotes(repr(case["expected"]["error"]))
    expected = case["expected"]
    if isinstance(expected, dict):
        pairs = []
        for k, v in expected.items():
            pairs.append("{0}: {1}".format(
                prefer_double_quotes(repr(k)), prefer_double_quotes(repr(v))))
        return "{" + ", ".join(pairs) + "}"
    if isinstance(expected, list):
        return "[" + ", ".join(map(prefer_double_quotes, map(repr,
                                                             expected))) + "]"
    return prefer_double_quotes(repr(case["expected"]))


def main(args=None):
    """
    Provide the CLI.
    """
    parser = ArgumentParser()
    parser.add_argument("-v", "--verbose", action="count")
    parser.add_argument(
        "-p",
        "--spec-path",
        type=Path,
        default="../problem-specifications",
        help="path to the problem specifications directory: (%(default)s)",
    )
    parser.add_argument(
        "-c",
        "--config",
        type=Path,
        default="./config.json",
        help="path to the Python track config.json file: (%(default)s)")
    parser.add_argument(
        "-o",
        "--only",
        help="generate tests for just the exercise specified")
    parser.add_argument(
        "-d",
        "--output-dir",
        type=Path,
        default="./exercises",
        help="path to the output directory: (%(default)s)")
    parser.add_argument(
        "-n",
        "--no-autoformat",
        action="store_true",
        help="disable yapf autoreformat")
    parser.add_argument(
        "-s",
        "--style",
        default=style.DEFAULT_STYLE,
        help="yapf autoreformat style to use: (%(default)s)")
    parser.add_argument("exercises", nargs="*")

    args = parser.parse_args(args)

    # validate the config file
    if not args.config.is_file():
        parser.error(
            "config must be an extant file, got: {0.config}".format(args))
    elif args.config.suffix != ".json":
        parser.error(
            "config must be a *.json file, got: {0.config}".format(args))

    # validate the spec path
    if not args.spec_path.is_dir():
        parser.error(
            "spec-path must be a directory, got: {0.spec_path}".format(args))

    # set verbosity
    if args.verbose:
        LOGGER.setLevel(logging.DEBUG if args.verbose > 1 else logging.INFO)

    # get the (possibly limited) list of exercises to generate
    config = json.loads(args.config.read_text())
    exercises = {
        e["slug"]
        for e in config["exercises"] if not e.get("deprecated")
    }
    if args.only is not None:
        if args.only not in exercises:
            LOGGER.error(f'"{args.only}" is not a valid exercise')
            exit(1)
        exercises = {args.only}
    if args.exercises:
        exercises = set(args.exercises).intersection(exercises)

    for exercise in sorted(exercises):
        canonical = args.spec_path.joinpath("exercises", exercise,
                                            "canonical-data.json")
        if not canonical.is_file():
            LOGGER.warning("No canonical data found for %s: skipping",
                           exercise)
            continue

        exercise_overrides = {}
        exercise_override_file = args.output_dir.joinpath(exercise, '.meta',
                                                      'generate.yml')
        if exercise_override_file.is_file():
            LOGGER.info("Using override file for %s", exercise)
            exercise_overrides = load(exercise_override_file.read_text())

        # build the Jinja2 template environment
        env = Environment(
            loader=PackageLoader(__name__, "templates"),
            autoescape=select_autoescape([]),
            trim_blocks=True, lstrip_blocks=True, keep_trailing_newline=True)
        env.filters["to_snake"] = to_snake
        env.filters["to_camel"] = to_camel
        env.filters["is_error"] = is_error
        env.filters["format_input"] = format_input
        env.filters["format_expect"] = format_expect
        env.filters["should_skip"] = lambda c: False
        env.filters["remap_property"] = lambda p: p

        exercise_properties_map = exercise_overrides.get("properties_map", {})
        if "skip_tests" in exercise_overrides:
            env.filters["should_skip"] = partial(
                should_skip, tests=exercise_overrides["skip_tests"])

        if "properties_map" in exercise_overrides:
            env.filters["remap_property"] = partial(
                remap_property,
                properties_map=exercise_overrides["properties_map"])

        if "inputs_map" in exercise_overrides:
            env.filters["format_input"] = partial(
                format_input_with_mappings,
                {
                    k: eval(v)
                    for k, v in exercise_overrides["inputs_map"].items()
                }
            )

        data = json.loads(canonical.read_text(), object_pairs_hook=OrderedDict)
        data["has_error"] = has_error(data)
        data["properties"] = get_properties(data)
        data["track_cases"] = []
        data["imports"] = exercise_overrides.get("imports", [])

        if "cases" in exercise_overrides:
            exercise_cases = exercise_overrides["cases"]
            data["has_error"] = data["has_error"] or has_error({"cases": exercise_cases})
            data["track_cases"] = exercise_cases

        template = env.select_template(
            ["{0}.j2".format(exercise), "_default.j2"])
        try:
            code = template.render(data=data)
            out_dir = args.output_dir.joinpath(exercise)
            if not out_dir.exists():
                out_dir.mkdir(parents=True)
            out_file = out_dir.joinpath("{0}_test.py".format(
                to_snake(exercise)))
            out_file.write_text(code)
            if not args.no_autoformat:
                try:
                    FormatFile(
                        str(out_file),
                        style_config=args.style,
                        in_place=True,
                        verify=True)
                except SyntaxError:
                    LOGGER.exception("Unable to reformat %s: skipping",
                                     exercise)
        except TemplateError:
            LOGGER.exception("Unable to render %s: skipping", exercise)
            continue


if __name__ == "__main__":
    main()
