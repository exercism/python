#!/usr/bin/env python
from __future__ import print_function

import argparse
import json
import os
import re
import sys
from glob import glob

from create_issue import GitHub

if sys.version_info[0] == 3:
    FileNotFoundError = OSError
else:
    FileNotFoundError = IOError

VERSION_PATTERN = r'(\d+\.\d+\.\d+)'
CANONICAL_PATTERN = (
    '# Tests adapted from `?problem-specifications//canonical-data.json`? '
    '@ v' + VERSION_PATTERN
)
rgx_version = re.compile(VERSION_PATTERN)
rgx_canonical = re.compile(CANONICAL_PATTERN)
DEFAULT_SPEC_PATH = os.path.join(
    '..',
    'problem-specifications'
)
gh = None

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


def cjust(string, width, fillchar=' '):
    while len(string) < width:
        string = fillchar + string
        if len(string) >= width:
            break
        string += fillchar
    return string


def verify_spec_location(path):
    with open(os.path.join(path, 'package.json')) as f:
        data = json.load(f)
    if data['name'] != 'problem-specifications':
        raise ValueError(
            '{} is not the problem-specifications directory'.format(path)
        )


def get_test_file_path(exercise):
    return os.path.join(
        'exercises',
        exercise,
        exercise.replace('-', '_') + '_test.py'
    )


def get_test_file_url(exercise):
    return '/'.join([
        'https://github.com',
        'exercism',
        'python',
        'blob',
        'master',
        'exercises',
        exercise,
        exercise.replace('-', '_') + '_test.py'
    ])


def get_canonical_data_path(exercise, spec_path=DEFAULT_SPEC_PATH):
    return os.path.join(
        spec_path,
        'exercises',
        exercise,
        'canonical-data.json'
    )


def get_canonical_data_url(exercise):
    return '/'.join([
        'https://github.com',
        'exercism',
        'problem-specifications',
        'blob',
        'master',
        'exercises',
        exercise,
        'canonical-data.json'
    ])


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


def create_issue_for_exercise(
    exercise,
    available_data_version,
    extra_labels=None
):
    title = '{}: update tests to v{}'.format(exercise, available_data_version)
    body = (
        'The [test suite]({}) for {} is out of date and needs updated to '
        'conform to the [latest canonical data]({}).'
    ).format(
        get_test_file_url(exercise),
        exercise,
        get_canonical_data_url(exercise),
    )
    labels = [
        'beginner friendly',
        'help wanted',
        'enhancement',
    ]
    if extra_labels is not None:
        labels = list(set(labels + extra_labels))
    issue = gh.create_issue(
        'exercism',
        'python',
        title,
        body=body,
        labels=labels
    )
    return issue['number']


def check_test_version(
    exercise,
    spec=DEFAULT_SPEC_PATH,
    no_color=True,
    print_ok=True,
    name_only=False,
    has_data=False,
    include_deprecated=False,
    create_issue=False,
    token=None,
    extra_labels=None,
):
    if not include_deprecated and is_deprecated(exercise):
        return True
    available = get_available_version(exercise, spec)
    if available == '0.0.0' and has_data:
        return True
    referenced = get_referenced_version(exercise)
    up_to_date = available == referenced
    if up_to_date:
        status, status_color = 'OK', bcolors.OKGREEN
    else:
        status, status_color = 'NOT OK', bcolors.FAIL
    status = cjust(status, 8)
    if not no_color:
        status = status_color + status + bcolors.ENDC
    if not up_to_date or print_ok:
        if create_issue:
            issue_number = create_issue_for_exercise(
                exercise,
                available,
                extra_labels
            )
            issue_info = '(#{})'.format(issue_number)
        else:
            issue_info = ''
        if name_only:
            baseline = exercise
        else:
            baseline = '[{}] {}: {}{}{}'.format(
                status,
                exercise,
                referenced,
                '=' if up_to_date else '!=',
                available
            )
        print(' '.join((baseline, issue_info)))
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
        default='*',
        metavar='<exercise>',
        help='Check just the exercise specified (by the slug).',
    )
    parser.add_argument(
        '--ignore',
        action='append',
        help='Check all except exercise[s] specified (by the slug).',
    )
    parser.add_argument(
        '-p', '--spec-path',
        default=DEFAULT_SPEC_PATH,
        metavar='<path/to/spec>',
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
    g = parser.add_argument_group('issue creation')
    g.add_argument(
        '--create-issue',
        action='store_true',
        help='Create issue for out-of-date exercises'
    )
    g.add_argument(
        '-t', '--token',
        help='GitHub personal access token (permissions: repo)'
    )
    g.add_argument(
        '--labels',
        nargs='+',
        metavar='LABEL',
        help=(
            'additional issue labels ("beginner friendly", "enhancement", and '
            '"help wanted" are always set)'
        )
    )
    opts = parser.parse_args()
    verify_spec_location(opts.spec_path)
    if opts.create_issue:
        if opts.token is not None:
            gh = GitHub(api_token=opts.token)
        else:
            gh = GitHub()
    kwargs = dict(
        spec=opts.spec_path,
        no_color=opts.no_color,
        print_ok=opts.verbose,
        name_only=opts.name_only,
        has_data=opts.has_data,
        create_issue=opts.create_issue,
        extra_labels=opts.labels,
    )
    if opts.version:
        print('check-test-version.py v1.1')
        sys.exit(0)
    result = True
    for exercise in glob(os.path.join('exercises', opts.only)):
        exercise = exercise.split(os.path.sep)[-1]
        if opts.ignore and exercise in opts.ignore:
            continue
        if os.path.isdir(os.path.join('exercises', exercise)):
            result = check_test_version(exercise, **kwargs) and result
    sys.exit(0 if result else 1)
