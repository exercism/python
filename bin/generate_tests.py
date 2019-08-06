#!/usr/bin/env python3.7
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
import argparse
import filecmp
import json
import logging
import os
import re
import shutil
import sys
from glob import glob
from itertools import repeat
from string import punctuation, whitespace
from subprocess import CalledProcessError, check_call
from tempfile import NamedTemporaryFile

from jinja2 import Environment, FileSystemLoader, TemplateNotFound

VERSION = '0.1.0'

DEFAULT_SPEC_LOCATION = os.path.join('..', 'problem-specifications')
RGX_WORDS = re.compile(r'[-_\s]|(?=[A-Z])')

logging.basicConfig()
logger = logging.getLogger('generator')
logger.setLevel(logging.WARN)


def replace_all(string, chars, rep):
    """
    Replace any char in chars with rep, reduce runs and strip terminal ends.
    """
    trans = str.maketrans(dict(zip(chars, repeat(rep))))
    return re.sub("{0}+".format(re.escape(rep)), rep,
                  string.translate(trans)).strip(rep)


def to_snake(string):
    """
    Convert pretty much anything to to_snake.
    """
    clean = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", string)
    clean = re.sub("([a-z0-9])([A-Z])", r"\1_\2", clean).lower()
    return replace_all(clean, whitespace + punctuation, "_")


def camel_case(string):
    """
    Convert pretty much anything to CamelCase.
    """
    return ''.join(w.title() for w in to_snake(string).split('_'))


def get_tested_properties(spec):
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


def error_case(case):
    return (
        "expected" in case and
        isinstance(case["expected"], dict) and
        "error" in case["expected"]
    )


def has_error_case(cases):
    cases = cases[:]
    while cases:
        case = cases.pop(0)
        if error_case(case):
            return True
        cases.extend(case.get("cases", []))
    return False


def load_canonical(exercise, spec_path):
    """
    Loads the canonical data for an exercise as a nested dictionary
    """
    full_path = os.path.join(
        spec_path, 'exercises', exercise, 'canonical-data.json'
    )
    with open(full_path) as f:
        spec = json.load(f)
    spec["properties"] = get_tested_properties(spec)
    return spec


def load_additional_tests(exercise):
    """
    Loads additional tests from .meta/additional_tests.json
    """
    full_path = os.path.join('exercises', exercise, '.meta', 'additional_tests.json')
    try:
        with open(full_path) as f:
            data = json.load(f)
        return data.get("cases", [])
    except FileNotFoundError:
        return []


def format_file(path):
    """
    Runs black auto-formatter on file at path
    """
    check_call(['black', '-q', path])


def compare_existing(rendered, tests_path):
    """
    Returns true if contents of file at tests_path match rendered
    """
    if not os.path.isfile(tests_path):
        return False
    with open(tests_path) as f:
        current = f.read()
    return rendered == current


def generate_exercise(env, spec_path, exercise, check=False):
    """
    Renders test suite for exercise and if check is:
    True: verifies that current tests file matches rendered
    False: saves rendered to tests file
    """
    slug = os.path.basename(exercise)
    try:
        spec = load_canonical(slug, spec_path)
        additional_tests = load_additional_tests(slug)
        spec["additional_cases"] = additional_tests
        template_path = os.path.join(slug, '.meta', 'template.j2')
        try:
            template = env.get_template(template_path)
            tests_path = os.path.join(
                exercise, f'{to_snake(slug)}_test.py'
            )
            spec["has_error_case"] = has_error_case(spec["cases"])
            rendered = template.render(**spec)
            with NamedTemporaryFile('w', delete=False) as tmp:
                tmp.write(rendered)
            format_file(tmp.name)
            if check:
                try:
                    if not filecmp.cmp(tmp.name, tests_path):
                        logger.error(f'{slug}: check failed; tests must be regenerated with bin/generate_tests.py')
                        sys.exit(1)
                finally:
                    os.remove(tmp.name)
            else:
                shutil.move(tmp.name, tests_path)
                print(f'{slug} generated at {tests_path}')
        except TemplateNotFound as e:
            logger.debug(str(e))
            logger.info(f'{slug}: no template found; skipping')
    except FileNotFoundError as e:
        logger.debug(str(e))
        logger.info(f'{slug}: no canonical data found; skipping')


def generate(exercise_glob, spec_path=DEFAULT_SPEC_LOCATION, check=False, **kwargs):
    """
    Primary entry point. Generates test files for all exercises matching exercise_glob
    """
    loader = FileSystemLoader(['config', 'exercises'])
    env = Environment(loader=loader, keep_trailing_newline=True)
    env.filters['to_snake'] = to_snake
    env.filters['camel_case'] = camel_case
    env.tests['error_case'] = error_case
    for exercise in glob(os.path.join('exercises', exercise_glob)):
        generate_exercise(env, spec_path, exercise, check)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'exercise_glob', nargs='?', default='*', metavar='EXERCISE'
    )
    parser.add_argument(
        '--version', action='version',
        version='%(prog)s {} for Python {}'.format(
            VERSION, sys.version.split("\n")[0],
        )
    )
    parser.add_argument('-v', '--verbose', action='store_true')
    parser.add_argument('-p', '--spec-path', default=DEFAULT_SPEC_LOCATION)
    parser.add_argument('--check', action='store_true')
    opts = parser.parse_args()
    if opts.verbose:
        logger.setLevel(logging.DEBUG)
    generate(**opts.__dict__)
