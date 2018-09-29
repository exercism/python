#!/usr/bin/python
import json
import os
import re
import logging
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
from pathlib import Path
from string import whitespace, punctuation
from itertools import repeat

# 3rd party imports
from jinja2 import Environment, PackageLoader, select_autoescape
from yapf.yapflib.yapf_api import FormatCode

logging.basicConfig(format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

BADCHARS = str.maketrans(dict(zip(punctuation + whitespace, repeat("_"))))

def _module_name(name):
    return name.replace("-", "_")

def _test_class_name(name):
    return "".join("".join(word.title() for word in name.split("-")).split())

def _test_name(name):
    return re.sub("_+", "_", name.lower().translate(BADCHARS)).strip("_")

def _func_name(name):
    return re.sub(r"([a-z][A-Z]+[a-z])", lambda m: m.group(1)[0] + "_" + m.group(1)[1:], name).lower()

def _is_error_case(case):
    expect = case.get("expected")
    return expect and isinstance(expect, dict) and "error" in expect

def _sanitize_data(data):
    data["PY_MODULE"] = _module_name(data["exercise"])
    data["PY_FROM_IMPORTS"] = []

    def _sanitize_case(case):
        if "description" in case:
            case["PY_TEST_NAME"] = _test_name(case["description"])
        if "property" in case:
            func_name = case["PY_TEST_FUNC"] = _func_name(case["property"])
            if func_name not in data["PY_FROM_IMPORTS"]:
                data["PY_FROM_IMPORTS"].append(func_name)
        is_error = False
        if "expected" in case:
            is_error = case["PY_TEST_IS_ERROR"] = _is_error_case(case)
        return is_error

    for case in data["cases"]:
        # grouped tests
        if "cases" in case:
            case["PY_TEST_CLASS"] = _test_class_name(case["description"])
            case["PY_TEST_CLASS_HAS_ERROR"] = False
            for grouped_case in case["cases"]:
                if _sanitize_case(grouped_case) and not case["PY_TEST_CLASS_HAS_ERROR"]:
                    case["PY_TEST_CLASS_HAS_ERROR"] = True
            case["PY_TEST_CLASS_NEEDS_SETUP"] = case["PY_TEST_CLASS_HAS_ERROR"]
        # ungrouped tests
        else:
            if "PY_TEST_CLASS" not in data:
                data["PY_TEST_CLASS"] = _test_class_name(data["exercise"])
                data["PY_TEST_CLASS_HAS_ERROR"] = False
            if _sanitize_case(case) and not data.get("PY_BASE_TEST_CLASS_HAS_ERROR"):
                data["PY_TEST_CLASS_HAS_ERROR"] = True
    if "PY_TEST_CLASS" in data:
        data["PY_TEST_CLASS_NEEDS_SETUP"] = data.get("PY_TEST_CLASS_HAS_ERROR", False)
    return data

def main():
    parser = ArgumentParser(
        formatter_class=ArgumentDefaultsHelpFormatter
    )
    parser.add_argument('-v', '--verbose', action='count')
    parser.add_argument(
        '-p', '--spec-path', default='../problem-specifications', type=Path
    )
    parser.add_argument(
        '-c', '--config', default='./config.json', type=Path
    )
    parser.add_argument('exercises', nargs='*')
    
    args = parser.parse_args()

    # validate the config file
    if not args.config.is_file():
        parser.error("config must be an extant file, got: {0.config}".format(args))
    elif args.config.suffix != ".json":
        parser.error("config must be a *.json file, got: {0.config}".format(args))

    # validate the spec path
    if not args.spec_path.is_dir():
        parser.error("spec-path must be a directory, got: {0.spec_path}".format(args))

    # set verbosity
    if args.verbose:
        logger.setLevel(logging.DEBUG if args.verbose > 1 else logging.INFO)

    # build the Jinja2 template environment
    env = Environment(
        loader=PackageLoader(__name__, 'templates'),
        autoescape=select_autoescape([])
    )

    # get the (possibly limited) list of exercises to generate
    config = json.loads(args.config.read_text())
    exercises = {e["slug"] for e in config["exercises"] if not e.get("deprecated")}
    if args.exercises:
        exercises = set(args.exercises).intersection(exercises)

    for exercise in sorted(exercises):
        canonical = args.spec_path.joinpath("exercises", exercise, "canonical-data.json")
        if not canonical.is_file():
            logger.warning("No canonical data found for {0}: skipping".format(exercise))
            continue
        data = _sanitize_data(json.loads(canonical.read_text()))
        
        template = env.select_template(["{0}.j2".format(exercise), "_default.j2"])
        rendered = template.render(**data)
        print(FormatCode(template.render(**data), style_config="facebook")[0])
        
if __name__ == '__main__':
    main()
