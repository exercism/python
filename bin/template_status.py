#!/usr/bin/env python3.7
import argparse
import json
import logging
import shlex
import shutil
import sys
from argparse import Namespace
from contextlib import contextmanager
from enum import IntEnum, auto
from fnmatch import fnmatch
from pathlib import Path
from subprocess import DEVNULL, CalledProcessError, check_call
from typing import Any, Dict, Iterator, List, Union

from githelp import Repo, clone_if_missing

TypeContextManager = Iterator[None]

DEFAULT_SPEC_LOCATION = Path(".problem-specifications")
EXERCISES_DIR = Path("exercises")
CONFIG_FILE = Path("config.json")

logging.basicConfig(format="%(levelname)s:%(message)s")
logger = logging.getLogger("generator")
logger.setLevel(logging.WARN)


class TemplateStatus(IntEnum):
    OK = auto()
    MISSING = auto()
    INVALID = auto()
    TEST_FAILURE = auto()


def get_template_path(exercise: str):
    return EXERCISES_DIR / exercise / ".meta/template.j2"


def exec_cmd(cmd: str) -> bool:
    try:
        args = shlex.split(cmd)
        if logger.isEnabledFor(logging.DEBUG):
            check_call(args)
        else:
            check_call(args, stderr=DEVNULL, stdout=DEVNULL)
        return True
    except CalledProcessError as e:
        logger.debug(str(e))
        return False


def generate_template(exercise: str, spec_path: Path) -> bool:
    script = Path("bin/generate_tests.py").resolve()
    return exec_cmd(f'{script} --verbose --spec-path "{spec_path}" {exercise}')


def run_tests(exercise: str) -> bool:
    script = Path("test/check-exercises.py").resolve()
    return exec_cmd(f"{script} {exercise}")


def get_status(exercise: Dict[str, Any], spec_path: Path) -> TemplateStatus:
    template_path = get_template_path(exercise).resolve()
    if template_path.is_file():
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


def set_loglevel(opts: Namespace):
    if opts.quiet:
        logger.setLevel(logging.FATAL)
    elif opts.verbose >= 2:
        logger.setLevel(logging.DEBUG)
    elif opts.verbose >= 1:
        logger.setLevel(logging.INFO)


def filter_exercises(exercises: List[Dict[str, Any]], pattern: str) -> Iterator[Dict[str, Any]]:
    for exercise in exercises:
        if not exercise.get("deprecated", False):
            if fnmatch(exercise["slug"], pattern):
                yield exercise


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("exercise_pattern", nargs="?", default="*", metavar="EXERCISE")
    parser.add_argument("-v", "--verbose", action="count", default=0)
    parser.add_argument("-q", "--quiet", action="store_true")
    parser.add_argument("--stop-on-failure", action="store_true")
    parser.add_argument(
        "-p",
        "--spec-path",
        default=DEFAULT_SPEC_LOCATION,
        type=Path,
        help=(
            "path to clone of exercism/problem-specifications " "(default: %(default)s)"
        ),
    )
    opts = parser.parse_args()
    set_loglevel(opts)

    with CONFIG_FILE.open() as f:
        config = json.load(f)

    with clone_if_missing(repo=Repo.ProblemSpecifications, directory=opts.spec_path):
        result = True
        buckets = {
            TemplateStatus.MISSING: [],
            TemplateStatus.INVALID: [],
            TemplateStatus.TEST_FAILURE: [],
        }
        for exercise in filter_exercises(config["exercises"], opts.exercise_pattern):
            slug = exercise["slug"]
            status = get_status(slug, opts.spec_path)
            if status == TemplateStatus.OK:
                logger.info(f"{slug}: {status.name}")
            else:
                buckets[status].append(slug)
                result = False
                if opts.stop_on_failure:
                    logger.error(f"{slug}: {status.name}")
                    break

        if not opts.quiet and not opts.stop_on_failure:
            for status, bucket in sorted(buckets.items()):
                if bucket:
                    print(f"The following exercises have status '{status.name}'")
                    for exercise in sorted(bucket):
                        print(f'  {exercise}')

        if not result:
            sys.exit(1)
