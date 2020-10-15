#!/usr/bin/env python3
"""
Generates exercise test suites using an exercise's canonical-data.json
(found in problem-specifications) and $exercise/.meta/template.j2.
If either does not exist, generation will not be attempted.

Usage:
    generate_tests.py           Generates tests for all exercises
    generate_tests.py two-fer   Generates tests for two-fer exercise
    generate_tests.py t*        Generates tests for all exercises matching t*

    generate_tests.py --check           Checks if test files are out of sync with templates
    generate_tests.py --check two-fer   Checks if two-fer test file is out of sync with template
"""
import sys

_py = sys.version_info
if _py.major < 3 or (_py.major == 3 and _py.minor < 6):
    print("Python version must be at least 3.6")
    sys.exit(1)

import argparse
from contextlib import contextmanager
from datetime import datetime
import difflib
import filecmp
import importlib.util
import json
import logging
from pathlib import Path
import re
import shutil
from itertools import repeat
from string import punctuation, whitespace
from subprocess import check_call
import toml
from tempfile import NamedTemporaryFile
from textwrap import wrap
from typing import Any, Dict, List, NoReturn, Union

from jinja2 import Environment, FileSystemLoader, TemplateNotFound, UndefinedError
from dateutil.parser import parse

VERSION = "0.3.0"

TypeJSON = Dict[str, Any]

PROBLEM_SPEC_REPO = "https://github.com/exercism/problem-specifications.git"
DEFAULT_SPEC_LOCATION = Path(".problem-specifications")
RGX_WORDS = re.compile(r"[-_\s]|(?=[A-Z])")

logging.basicConfig()
logger = logging.getLogger("generator")
logger.setLevel(logging.WARN)


def replace_all(string: str, chars: Union[str, List[str]], rep: str) -> str:
    """
    Replace any char in chars with rep, reduce runs and strip terminal ends.
    """
    trans = str.maketrans(dict(zip(chars, repeat(rep))))
    return re.sub("{0}+".format(re.escape(rep)), rep, string.translate(trans)).strip(
        rep
    )


def to_snake(string: str, wordchars_only: bool = False) -> str:
    """
    Convert pretty much anything to to_snake.

    By default whitespace and punctuation will be converted
    to underscores as well, pass wordchars_only=True to preserve these as is.
    """
    clean = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", string)
    clean = re.sub("([a-z0-9])([A-Z])", r"\1_\2", clean).lower()
    return clean if wordchars_only else replace_all(clean, whitespace + punctuation, "_")


def camel_case(string: str) -> str:
    """
    Convert pretty much anything to CamelCase.
    """
    return "".join(w.title() for w in to_snake(string).split("_"))


def wrap_overlong(string: str, width: int = 70) -> List[str]:
    """
    Break an overly long string literal into escaped lines.
    """
    return ["{0!r} \\".format(w) for w in wrap(string, width)]


def parse_datetime(string: str, strip_module: bool = False) -> datetime:
    """
    Parse a (hopefully ISO 8601) datestamp to a datetime object and
    return its repr for use in a jinja2 template.

    If used the template will need to import the datetime module.

        import datetime

    However if strip_module is True then the template will need to
    import the datetime _class_ instead.

        from datetime import datetime
    """
    result = repr(parse(string))
    if strip_module:
        return result.replace("datetime.", "", 1)
    return result

INVALID_ESCAPE_RE = re.compile(
    r"""
    \\(?!                           # a backslash NOT followed by
        newline                     # the literal newline
    |[                              # OR precisely one of
        \\                          # another backslash
        '                           # the single quote
        "                           # the double quote
        a                           # the ASCII bell
        b                           # the ASCII backspace
        f                           # the ASCII formfeed
        n                           # the ASCII linefeed
        r                           # the ASCII carriage return
        t                           # the ASCII horizontal tab
        v                           # the ASCII vertical tab
    ]|                              # OR
        o(?:[0-8]{1,3})             # an octal value
    |                               # OR
        x(?:[0-9A-Fa-f]{2})         # a hexidecimal value
    |                               # OR
        N                           # a unicode char name composed of
        \{                          # an opening brace
            [A-Z][A-Z\ \-]*[A-Z]    # uppercase WORD, WORDs (or WORD-WORDs)
        \}                          # and a closing brace
    |                               # OR
        u(?:[0-9A-Fa-f]{4})         # a 16-bit unicode char
    |                               # OR
        U(?:[0-9A-Fa-f]{8})         # a 32-bit unicode char
    )""", flags=re.VERBOSE)

def escape_invalid_escapes(string: str) -> str:
    """
    Some canonical data includes invalid escape sequences, which
    need to be properly escaped before template render.
    """
    return INVALID_ESCAPE_RE.sub(r"\\\\", string)

ALL_VALID = r"\newline\\\'\"\a\b\f\n\r\t\v\o123" \
            r"\xFF\N{GREATER-THAN SIGN}\u0394\U00000394"

assert ALL_VALID == escape_invalid_escapes(ALL_VALID)

def get_tested_properties(spec: TypeJSON) -> List[str]:
    """
    Get set of tested properties from spec. Include nested cases.
    """
    props = set()
    for case in spec["cases"]:
        if "property" in case:
            props.add(case["property"])
        if "cases" in case:
            props.update(get_tested_properties(case))
    return sorted(props)


def error_case(case: TypeJSON) -> bool:
    return (
        "expected" in case
        and isinstance(case["expected"], dict)
        and "error" in case["expected"]
    )


def has_error_case(cases: List[TypeJSON]) -> bool:
    cases = cases[:]
    while cases:
        case = cases.pop(0)
        if error_case(case):
            return True
        cases.extend(case.get("cases", []))
    return False


def regex_replace(s: str, find: str, repl: str) -> str:
    return re.sub(find, repl, s)


def regex_find(s: str, find: str) -> List[Any]:
    return re.findall(find, s)


def regex_split(s: str, find: str) -> List[str]:
    return re.split(find, s)


def load_tests_toml(exercise: str) -> Dict[str, bool]:
    """
    Loads test case opt-in/out data for an exercise as a dictionary
    """
    full_path = Path("exercises") / exercise / ".meta/tests.toml"
    with full_path.open() as f:
        opts = toml.load(f)
    return opts


def filter_test_cases(cases: List[TypeJSON], opts: Dict[str, bool]) -> List[TypeJSON]:
    """
    Returns a filtered copy of `cases` where only cases whose UUID is marked True in
    `opts` are included.
    """
    filtered = []
    for case in cases:
        if "uuid" in case:
            uuid = case["uuid"]
            if opts.get(uuid, False):
                filtered.append(case)
            else:
                logger.debug(f"uuid {uuid} either missing or marked false")
        elif "cases" in case:
            subfiltered = filter_test_cases(case["cases"], opts)
            if subfiltered:
                case_copy = dict(case)
                case_copy["cases"] = subfiltered
                filtered.append(case_copy)
    return filtered


def load_canonical(exercise: str, spec_path: Path, test_opts: Dict[str, bool]) -> TypeJSON:
    """
    Loads the canonical data for an exercise as a nested dictionary
    """
    full_path = spec_path / "exercises" / exercise / "canonical-data.json"
    with full_path.open() as f:
        spec = json.load(f)
    spec["properties"] = get_tested_properties(spec)
    spec["cases"] = filter_test_cases(spec["cases"], test_opts["canonical-tests"])
    return spec


def load_additional_tests(exercise: str) -> List[TypeJSON]:
    """
    Loads additional tests from .meta/additional_tests.json
    """
    full_path = Path("exercises") / exercise / ".meta/additional_tests.json"
    try:
        with full_path.open() as f:
            data = json.load(f)
        return data.get("cases", [])
    except FileNotFoundError:
        return []


def format_file(path: Path) -> NoReturn:
    """
    Runs black auto-formatter on file at path
    """
    check_call(["black", "-q", path])


@contextmanager
def clone_if_missing(repo: str, directory: Union[str, Path, None] = None):
    if directory is None:
        directory = repo.split("/")[-1].split(".")[0]
    directory = Path(directory)
    if not directory.is_dir():
        temp_clone = True
        check_call(["git", "clone", repo, str(directory)])
    else:
        temp_clone = False
    try:
        yield directory
    finally:
        if temp_clone:
            shutil.rmtree(directory)


def generate_exercise(env: Environment, spec_path: Path, exercise: Path, check: bool = False):
    """
    Renders test suite for exercise and if check is:
    True: verifies that current tests file matches rendered
    False: saves rendered to tests file
    """
    slug = exercise.name
    meta_dir = exercise / ".meta"
    plugins_module = None
    plugins_name = "plugins"
    plugins_source = meta_dir / f"{plugins_name}.py"
    try:
        if plugins_source.is_file():
            plugins_spec = importlib.util.spec_from_file_location(
                plugins_name, plugins_source
            )
            plugins_module = importlib.util.module_from_spec(plugins_spec)
            sys.modules[plugins_name] = plugins_module
            plugins_spec.loader.exec_module(plugins_module)
        try:
            test_opts = load_tests_toml(slug)
        except FileNotFoundError:
            logger.error(f"{slug}: tests.toml not found; please run canonical_data_syncer")
            return False
        spec = load_canonical(slug, spec_path, test_opts)
        additional_tests = load_additional_tests(slug)
        spec["additional_cases"] = additional_tests
        template_path = Path(slug) / ".meta" / "template.j2"
        template = env.get_template(str(template_path))
        tests_path = exercise / f"{to_snake(slug)}_test.py"
        spec["has_error_case"] = has_error_case(spec["cases"])
        if plugins_module is not None:
            spec[plugins_name] = plugins_module
        logger.debug(f"{slug}: attempting render")
        rendered = template.render(**spec)
        with NamedTemporaryFile("w", delete=False) as tmp:
            logger.debug(f"{slug}: writing render to tmp file {tmp.name}")
            tmpfile = Path(tmp.name)
            tmp.write(rendered)
        try:
            logger.debug(f"{slug}: formatting tmp file {tmpfile}")
            format_file(tmpfile)
        except FileNotFoundError as e:
            logger.error(f"{slug}: the black utility must be installed")
            return False

        if check:
            try:
                check_ok = True
                if not tmpfile.is_file():
                    logger.debug(f"{slug}: tmp file {tmpfile} not found")
                    check_ok = False
                if not tests_path.is_file():
                    logger.debug(f"{slug}: tests file {tests_path} not found")
                    check_ok = False
                if check_ok and not filecmp.cmp(tmpfile, tests_path):
                    with tests_path.open() as f:
                        current_lines = f.readlines()
                    with tmpfile.open() as f:
                        rendered_lines = f.readlines()
                    diff = difflib.unified_diff(
                        current_lines,
                        rendered_lines,
                        fromfile=f"[current] {tests_path.name}",
                        tofile=f"[generated] {tmpfile.name}",
                    )
                    logger.debug(f"{slug}: ##### DIFF START #####")
                    for line in diff:
                        logger.debug(line.strip())
                    logger.debug(f"{slug}: ##### DIFF END #####")
                    check_ok = False
                if not check_ok:
                    logger.error(
                        f"{slug}: check failed; tests must be regenerated with bin/generate_tests.py"
                    )
                    return False
                logger.debug(f"{slug}: check passed")
            finally:
                logger.debug(f"{slug}: removing tmp file {tmpfile}")
                tmpfile.unlink()
        else:
            logger.debug(f"{slug}: moving tmp file {tmpfile}->{tests_path}")
            shutil.move(tmpfile, tests_path)
            print(f"{slug} generated at {tests_path}")
    except (TypeError, UndefinedError, SyntaxError) as e:
        logger.debug(str(e))
        logger.error(f"{slug}: generation failed")
        return False
    except TemplateNotFound as e:
        logger.debug(str(e))
        logger.info(f"{slug}: no template found; skipping")
    except FileNotFoundError as e:
        logger.debug(str(e))
        logger.info(f"{slug}: no canonical data found; skipping")
    return True


def generate(
    exercise_glob: str,
    spec_path: Path = DEFAULT_SPEC_LOCATION,
    stop_on_failure: bool = False,
    check: bool = False,
    **_,
):
    """
    Primary entry point. Generates test files for all exercises matching exercise_glob
    """
    # black must be installed or all test files will error
    if not shutil.which("black"):
        logger.error("the black utility must be installed")
        sys.exit(1)
    loader = FileSystemLoader(["config", "exercises"])
    env = Environment(loader=loader, keep_trailing_newline=True)
    env.filters["to_snake"] = to_snake
    env.filters["camel_case"] = camel_case
    env.filters["wrap_overlong"] = wrap_overlong
    env.filters["regex_replace"] = regex_replace
    env.filters["regex_find"] = regex_find
    env.filters["regex_split"] = regex_split
    env.filters["zip"] = zip
    env.filters["parse_datetime"] = parse_datetime
    env.filters["escape_invalid_escapes"] = escape_invalid_escapes
    env.tests["error_case"] = error_case
    result = True
    for exercise in sorted(Path("exercises").glob(exercise_glob)):
        if not generate_exercise(env, spec_path, exercise, check):
            result = False
            if stop_on_failure:
                break
    if not result:
        sys.exit(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("exercise_glob", nargs="?", default="*", metavar="EXERCISE")
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s {} for Python {}".format(VERSION, sys.version.split("\n")[0]),
    )
    parser.add_argument("-v", "--verbose", action="store_true")
    parser.add_argument(
        "-p",
        "--spec-path",
        default=DEFAULT_SPEC_LOCATION,
        type=Path,
        help=(
            "path to clone of exercism/problem-specifications " "(default: %(default)s)"
        ),
    )
    parser.add_argument("--stop-on-failure", action="store_true")
    parser.add_argument(
        "--check",
        action="store_true",
        help="check if tests are up-to-date, but do not modify test files",
    )
    opts = parser.parse_args()
    if opts.verbose:
        logger.setLevel(logging.DEBUG)
    with clone_if_missing(repo=PROBLEM_SPEC_REPO, directory=opts.spec_path):
        generate(**opts.__dict__)
