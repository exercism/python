#!/usr/bin/python
"""
Generates exercise_test.py files for tests with canonical data.
"""
import json
import re
import logging
from argparse import ArgumentParser
from pathlib import Path
from itertools import repeat
from string import punctuation, whitespace

# 3rd party imports:
from jinja2 import Environment, PackageLoader, select_autoescape, TemplateError
from yapf.yapflib.yapf_api import FormatFile, style

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


def format_input(case):
    """
    Format the case's input values for use in a function call.
    """
    raw = case["input"]
    if len(raw) == 1:
        return repr(list(raw.values())[0])
    if any(k.isdigit() for k in raw):
        return repr(raw)
    return ", ".join("{0}={1!r}".format(*i) for i in raw.items())


def format_expect(case):
    """
    Format the case's expected values for use in a function call.
    """
    if is_error(case):
        return repr(case["expected"]["error"])
    return repr(case["expected"])


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
        "--output",
        type=Path,
        default="./exercises",
        help="path to the output directory: (%(default)s)")
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

    # build the Jinja2 template environment
    env = Environment(
        loader=PackageLoader(__name__, "templates"),
        autoescape=select_autoescape([]))
    env.filters["to_snake"] = to_snake
    env.filters["to_camel"] = to_camel
    env.filters["is_error"] = is_error
    env.filters["format_input"] = format_input
    env.filters["format_expect"] = format_expect

    # get the (possibly limited) list of exercises to generate
    config = json.loads(args.config.read_text())
    exercises = {
        e["slug"]
        for e in config["exercises"] if not e.get("deprecated")
    }
    if args.exercises:
        exercises = set(args.exercises).intersection(exercises)

    for exercise in sorted(exercises):
        canonical = args.spec_path.joinpath("exercises", exercise,
                                            "canonical-data.json")
        if not canonical.is_file():
            LOGGER.warning("No canonical data found for %s: skipping",
                           exercise)
            continue
        data = json.loads(canonical.read_text(), object_pairs_hook=dict)
        data["has_error"] = has_error(data)
        data["properties"] = get_properties(data)
        template = env.select_template(
            ["{0}.j2".format(exercise), "_default.j2"])
        try:
            code = template.render(data=data)
            out_dir = args.output.joinpath(exercise)
            if not out_dir.exists():
                out_dir.mkdir(parents=True)
            out_file = out_dir.joinpath("{0}_test.py".format(
                to_snake(exercise)))
            out_file.write_text(code)
            try:
                FormatFile(
                    str(out_file),
                    style_config=args.style,
                    in_place=True,
                    verify=True)
            except SyntaxError:
                LOGGER.exception("Unable to reformat %s: skipping", exercise)
        except TemplateError:
            LOGGER.exception("Unable to render %s: skipping", exercise)
            continue


if __name__ == "__main__":
    main()
