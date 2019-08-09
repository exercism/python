#!/usr/bin/env python3.7
import argparse
from enum import Enum, auto
from fnmatch import fnmatch
import json
import logging
import os
import shlex
from subprocess import check_call, DEVNULL, CalledProcessError
import sys

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


def exec_cmd(cmd):
    try:
        check_call(shlex.split(cmd), stdout=DEVNULL, stderr=DEVNULL)
        return True
    except CalledProcessError:
        return False


def generate_template(exercise, spec_path="../problem-specifications"):
    return exec_cmd(f'bin/generate_tests.py -p "{spec_path}" {exercise}')


def run_tests(exercise):
    return exec_cmd(f"test/check-exercises.py {exercise}")


def get_status(exercise):
    template_path = get_template_path(exercise)
    if os.path.isfile(template_path):
        if generate_template(exercise):
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
    opts = parser.parse_args()
    if opts.quiet:
        logger.setLevel(logging.FATAL)
    elif opts.verbose:
        logger.setLevel(logging.DEBUG)

    result = True
    for exercise in filter(
        lambda e: fnmatch(e["slug"], opts.exercise_pattern), config["exercises"]
    ):
        slug = exercise["slug"]
        status = get_status(slug)
        if status != TemplateStatus.OK:
            result = False
            logger.error(f"{slug}: {status.name}")
            if opts.stop_on_failure:
                break
        else:
            logger.info(f"{slug}: {status.name}")

    if not result:
        sys.exit(1)
