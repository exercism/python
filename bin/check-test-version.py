#!/usr/bin/env python
from __future__ import print_function
import json
import re
import argparse
import os
import sys

if sys.version_info[0] == 3:
    FileNotFoundError = OSError
else:
    FileNotFoundError = IOError

VERSION_PATTERN = '(\d+\.\d+\.\d+)'
CANONICAL_PATTERN = (
    '# Tests adapted from `problem-specifications//canonical-data.json` '
    '@ v' + VERSION_PATTERN
)
rgx_version = re.compile(VERSION_PATTERN)
rgx_canonical = re.compile(CANONICAL_PATTERN)
DEFAULT_SPEC_PATH = os.path.join(
    '..',
    'problem-specifications'
)

with open('config.json') as f:
    config = json.load(f)


class CustomFormatter(
    argparse.ArgumentDefaultsHelpFormatter,
    argparse.RawDescriptionHelpFormatter
):
    pass


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def get_test_file_path(exercise):
    return os.path.join(
        'exercises',
        exercise,
        exercise.replace('-', '_') + '_test.py'
    )


def get_canonical_data_path(exercise, spec_path=DEFAULT_SPEC_PATH):
    return os.path.join(
        spec_path,
        'exercises',
        exercise,
        'canonical-data.json'
    )


def get_referenced_version(exercise):
    with open(get_test_file_path(exercise)) as f:
        for line in f.readlines():
            m = rgx_canonical.match(line)
            if m is not None:
                return m.group(1)
    return '0.0.0'


def get_available_version(exercise, spec_path=DEFAULT_SPEC_PATH):
    try:
        with open(get_canonical_data_path(exercise, spec_path)) as f:
            data = json.load(f)
        m = rgx_version.match(data['version'])
        return m.group(1)
    except FileNotFoundError:
        return '0.0.0'


def is_deprecated(exercise):
    for e in config['exercises']:
        if e['slug'] == exercise:
            return e.get('deprecated', False)
    return False


def check_test_version(
    exercise,
    spec=DEFAULT_SPEC_PATH,
    no_color=True,
    print_ok=True,
    name_only=False,
    has_data=False,
    include_deprecated=False,
):
    if not include_deprecated and is_deprecated(exercise):
        return True
    available = get_available_version(exercise, spec)
    if available == '0.0.0' and has_data:
        return True
    referenced = get_referenced_version(exercise)
    up_to_date = available == referenced
    if up_to_date:
        status, status_color = '  OK  ', bcolors.OKGREEN
    else:
        status, status_color = 'NOT OK', bcolors.FAIL
    if not no_color:
        status = status_color + status + bcolors.ENDC
    if not up_to_date or print_ok:
        if name_only:
            print(exercise)
        else:
            print('[ {} ] {}: {}{}{}'.format(
                status,
                exercise,
                referenced,
                '=' if up_to_date else '!=',
                available
            ))
    return up_to_date


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        formatter_class=CustomFormatter,
        epilog=(
            "Results are of the form:\n  <exercise>: <referenced>!=<current>"
        )
    )
    parser._optionals.title = 'options'
    parser.add_argument(
        '--version',
        action='store_true',
        help='Print version info.'
    )
    parser.add_argument(
        '-o', '--only',
        metavar='<exercise>',
        help='Check just the exercise specified (by the slug)/'
    )
    parser.add_argument(
        '-p', '--spec-path',
        default=DEFAULT_SPEC_PATH,
        metavar='<path/to/track>',
        help='The location of the problem-specifications directory.'
    )
    g = parser.add_argument_group('output')
    g.add_argument(
        '-w', '--no-color',
        action='store_true',
        help='Disable colored output.'
    )
    g.add_argument(
        '-s', '--has-data',
        action='store_true',
        help='Only print exercises with existing canonical data.'
    )
    g.add_argument(
        '-d', '--include-deprecated',
        action='store_true',
        help='Include deprecated exercises'
    )
    mut_g = g.add_mutually_exclusive_group()
    mut_g.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Enable verbose output.'
    )
    mut_g.add_argument(
        '-n', '--name-only',
        action='store_true',
        help='Print exercise names only.'
    )
    opts = parser.parse_args()
    kwargs = dict(
        spec=opts.spec_path,
        no_color=opts.no_color,
        print_ok=opts.verbose,
        name_only=opts.name_only,
        has_data=opts.has_data,
    )
    if opts.version:
        print('check-test-version.py v1.0')
        sys.exit(0)
    result = True
    if opts.only is None:
        for exercise in os.listdir('exercises'):
            if os.path.isdir(os.path.join('exercises', exercise)):
                result = check_test_version(exercise, **kwargs) and result
    else:
        result = check_test_version(opts.only, **kwargs)
    sys.exit(0 if result else 1)
