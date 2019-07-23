#!/usr/bin/env python3.7
import argparse
import json
import logging
import os
import re
import sys
from glob import glob
from subprocess import check_call

from jinja2 import Environment, FileSystemLoader, TemplateNotFound

VERSION = '0.1.0'

DEFAULT_SPEC_LOCATION = os.path.join('..', 'problem-specifications')
RGX_WORDS = re.compile(r'[-_\s]|(?=[A-Z])')

logging.basicConfig()
logger = logging.getLogger('generator')
logger.setLevel(logging.WARN)


def snake_case(string):
    return '_'.join(RGX_WORDS.split(string)).lower()


def title_case(string):
    return''.join(word.title() for word in RGX_WORDS.split(string))


def load_canonical(exercise, spec_path):
    full_path = os.path.join(
        spec_path, 'exercises', exercise, 'canonical-data.json'
    )
    with open(full_path) as f:
        return json.load(f)


def format_file(path):
    check_call(['black', '-q', path])


def generate_exercise(env, spec_path, exercise):
    slug = os.path.basename(exercise)
    try:
        spec = load_canonical(slug, spec_path)
        template_path = os.path.join(slug, '.meta', 'template.j2')
        try:
            template = env.get_template(template_path)
            tests_path = os.path.join(
                exercise, f'{snake_case(slug)}_test.py'
            )
            with open(tests_path, 'w') as f:
                f.write(template.render(**spec))
            format_file(tests_path)
            print(f'{slug} generated at {tests_path}')
        except TemplateNotFound:
            logger.info(f'{slug}: no template found; skipping')
    except FileNotFoundError:
        logger.info(f'{slug}: no canonical data found; skipping')


def generate(exercise_glob, spec_path=DEFAULT_SPEC_LOCATION, **kwargs):
    loader = FileSystemLoader('exercises')
    env = Environment(loader=loader, keep_trailing_newline=True)
    env.filters['snake_case'] = snake_case
    env.filters['title_case'] = title_case
    for exercise in glob(os.path.join('exercises', exercise_glob)):
        generate_exercise(env, spec_path, exercise)


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
    opts = parser.parse_args()
    if opts.verbose:
        logger.setLevel(logging.INFO)
    generate(**opts.__dict__)
