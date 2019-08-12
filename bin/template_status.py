#!/usr/bin/env python3.7
import argparse
from enum import Enum, auto
from fnmatch import fnmatch
import json
import logging
import os
import shlex
from subprocess import check_output, STDOUT, CalledProcessError
import sys

DEFAULT_SPEC_LOCATION = os.path.join("..", "problem-specifications")

logging.basicConfig(format="%(levelname)s:%(message)s")
logger = logging.getLogger("generator")
logger.setLevel(logging.WARN)


class TemplateStatus(Enum):
    OK = auto()
    MISSING = auto()
    INVALID = auto()
    TEST_FAILURE = auto()


with open("config.json") as f:
    config = json.load(f)

exercises_dir = os.path.abspath("exercises")


def get_template_path(exercise):
    return os.path.join(exercises_dir, exercise, ".meta", "template.j2")


def exec_cmd(cmd, verbose=False):
    try:
        out = check_output(shlex.split(cmd), stderr=STDOUT)
        logger.debug(out.decode())
        return True
    except CalledProcessError as e:
        logger.debug(out.decode())
        logger.debug(str(e))
        return False


def generate_template(exercise, spec_path):
    return exec_cmd(f'bin/generate_tests.py --verbose --spec-path "{spec_path}" {exercise}')


def run_tests(exercise):
    return exec_cmd(f"test/check-exercises.py {exercise}")


def get_status(exercise, spec_path):
    template_path = get_template_path(exercise)
    if os.path.isfile(template_path):
        if generate_template(exercise, spec_path):
            if run_tests(exercise):
                logging.info(f"{exercise}: OK")
                return TemplateStatus.OK
            else:
                return TemplateStatus.TEST_FAILURE
        else:
            return TemplateStatus.INVALID
    else:
        return TemplateStatus.MISSING


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("exercise_pattern", nargs="?", default="*", metavar="EXERCISE")
    parser.add_argument("-v", "--verbose", action="store_true")
    parser.add_argument("-q", "--quiet", action="store_true")
    parser.add_argument("--stop-on-failure", action="store_true")
    parser.add_argument(
        "-p",
        "--spec-path",
        default=DEFAULT_SPEC_LOCATION,
        help=(
            "path to clone of exercism/problem-specifications " "(default: %(default)s)"
        ),
    )
    opts = parser.parse_args()
    if opts.quiet:
        logger.setLevel(logging.FATAL)
    elif opts.verbose:
        logger.setLevel(logging.DEBUG)

    if not os.path.isdir(opts.spec_path):
        logger.error(f'{opts.spec_path} is not a directory')
        sys.exit(1)
    opts.spec_path = os.path.abspath(opts.spec_path)
    logger.debug(f'problem-specifications path is {opts.spec_path}')

    result = True
    for exercise in filter(
        lambda e: fnmatch(e["slug"], opts.exercise_pattern), config["exercises"]
    ):
        slug = exercise["slug"]
        status = get_status(slug, opts.spec_path)
        if status != TemplateStatus.OK:
            result = False
            logger.error(f"{slug}: {status.name}")
            if opts.stop_on_failure:
                break
        else:
            logger.info(f"{slug}: {status.name}")

    if not result:
        sys.exit(1)
