#!/usr/bin/env python3.7
import argparse
import json
import logging
import os
import re
import sys
import tempfile
from glob import glob
from itertools import repeat
from string import punctuation, whitespace
from subprocess import DEVNULL, CalledProcessError, check_call

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
    return ''.join(w.title() for w in to_snake(string).split('_'))


def load_canonical(exercise, spec_path):
    full_path = os.path.join(
        spec_path, 'exercises', exercise, 'canonical-data.json'
    )
    with open(full_path) as f:
        return json.load(f)


def format_file(path):
    check_call(['black', '-q', path])


def generate_exercise(env, spec_path, exercise, check=False):
    slug = os.path.basename(exercise)
    try:
        spec = load_canonical(slug, spec_path)
        template_path = os.path.join(slug, '.meta', 'template.j2')
        try:
            template = env.get_template(template_path)
            tests_path = os.path.join(
                exercise, f'{to_snake(slug)}_test.py'
            )
            rendered = template.render(**spec)
            if check:
                tmp_f, tmp_path = tempfile.mkstemp()
                tmp_f.write(rendered)
                tmp_f.close()
                try:
                    check_call(['diff', tests_path, tmp_path], stdout=DEVNULL, stderr=DEVNULL)
                except CalledProcessError:
                    logger.error(f'{slug}: check failed; tests must be regenerated with bin/generate_tests.py')
                    sys.exit(1)
                finally:
                    os.remove(tmp_path)
            else:
                with open(tests_path, 'w') as f:
                    f.write(rendered)
            format_file(tests_path)
            print(f'{slug} generated at {tests_path}')
        except TemplateNotFound:
            logger.info(f'{slug}: no template found; skipping')
    except FileNotFoundError:
        logger.info(f'{slug}: no canonical data found; skipping')


def generate(exercise_glob, spec_path=DEFAULT_SPEC_LOCATION, check=False, **kwargs):
    loader = FileSystemLoader('exercises')
    env = Environment(loader=loader, keep_trailing_newline=True)
    env.filters['to_snake'] = to_snake
    env.filters['camel_case'] = camel_case
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
        logger.setLevel(logging.INFO)
    generate(**opts.__dict__)
