#!/usr/bin/env python3.7
import argparse
from enum import Enum, auto
from fnmatch import fnmatch
import json
import logging
from pathlib import Path
import shlex
from subprocess import check_call, DEVNULL, CalledProcessError
import sys

from data import Config, ExerciseInfo
from test_exercises import check_assignment

DEFAULT_SPEC_LOCATION = Path('spec')

logging.basicConfig(format="%(levelname)s:%(message)s")
logger = logging.getLogger("generator")
logger.setLevel(logging.WARN)


class TemplateStatus(Enum):
    OK = auto()
    MISSING = auto()
    INVALID = auto()
    TEST_FAILURE = auto()

    def __lt__(self, other):
        return self.value < other.value


def exec_cmd(cmd):
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


def generate_template(exercise: ExerciseInfo, spec_path: Path) -> bool:
    script = Path('bin/generate_tests.py')
    return exec_cmd(f'{script} --verbose --spec-path "{spec_path}" {exercise.slug}')


def run_tests(exercise: ExerciseInfo) -> bool:
    return check_assignment(exercise, quiet=True) == 0


def get_status(exercise: ExerciseInfo, spec_path: Path):
    if exercise.template_path.is_file():
        if generate_template(exercise, spec_path):
            if run_tests(exercise):
                logging.info(f"{exercise.slug}: OK")
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
    if opts.quiet:
        logger.setLevel(logging.FATAL)
    elif opts.verbose >= 2:
        logger.setLevel(logging.DEBUG)
    elif opts.verbose >= 1:
        logger.setLevel(logging.INFO)

    if not opts.spec_path.is_dir():
        logger.error(f"{opts.spec_path} is not a directory")
        sys.exit(1)
    opts.spec_path = opts.spec_path.absolute()
    logger.debug(f"problem-specifications path is {opts.spec_path}")

    result = True
    buckets = {
        TemplateStatus.MISSING: [],
        TemplateStatus.INVALID: [],
        TemplateStatus.TEST_FAILURE: [],
    }
    config = Config.load()
    for exercise in filter(
        lambda e: fnmatch(e.slug, opts.exercise_pattern),
        config.exercises.all()
    ):
        if exercise.deprecated:
            continue
        if exercise.type == 'concept':
            # Concept exercises are not generated
            continue
        status = get_status(exercise, opts.spec_path)
        if status == TemplateStatus.OK:
            logger.info(f"{exercise.slug}: {status.name}")
        else:
            buckets[status].append(exercise.slug)
            result = False
            if opts.stop_on_failure:
                logger.error(f"{exercise.slug}: {status.name}")
                break

    if not opts.quiet and not opts.stop_on_failure:
        for status, bucket in sorted(buckets.items()):
            if bucket:
                print(f"The following exercises have status '{status.name}'")
                for exercise in sorted(bucket):
                    print(f'  {exercise}')

    if not result:
        sys.exit(1)
