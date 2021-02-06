#!/usr/bin/env python3

import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from data import Config, ExerciseInfo

# Allow high-performance tests to be skipped
ALLOW_SKIP = ['alphametics', 'largest-series-product']


def check_assignment(exercise: ExerciseInfo, quiet=False) -> int:
    # Returns the exit code of the tests
    workdir = Path(tempfile.mkdtemp(exercise.slug))
    solution_file = exercise.solution_stub.name
    try:
        test_file_out = workdir / exercise.test_file.name
        if exercise.slug in ALLOW_SKIP:
            shutil.copyfile(exercise.test_file, test_file_out)
        else:
            with exercise.test_file.open('r') as src_file:
                lines = [line for line in src_file.readlines()
                         if not line.strip().startswith('@unittest.skip')]
            with test_file_out.open('w') as dst_file:
                dst_file.writelines(lines)
        shutil.copyfile(exercise.exemplar_file, workdir / solution_file)
        kwargs = {}
        if quiet:
            kwargs['stdout'] = subprocess.DEVNULL
            kwargs['stderr'] = subprocess.DEVNULL
        return subprocess.run([sys.executable, '-m', 'pytest', test_file_out], **kwargs).returncode
    finally:
        shutil.rmtree(workdir)


def main():
    config = Config.load()
    exercises = config.exercises.all()
    if len(sys.argv) >= 2:
        # test specific exercises
        exercises = [
            e for e in exercises if e.slug in sys.argv[1:]
        ]

    failures = []
    for exercise in exercises:
        print('# ', exercise.slug)
        if not exercise.test_file:
            print('FAIL: File with test cases not found')
            failures.append('{} (FileNotFound)'.format(exercise.slug))
        else:
            if check_assignment(exercise):
                failures.append('{} (TestFailed)'.format(exercise.slug))
        print('')

    print('TestEnvironment:', sys.executable.capitalize(), '\n\n')

    if failures:
        print('FAILURES: ', ', '.join(failures))
        raise SystemExit(1)
    else:
        print('SUCCESS!')


if __name__ == '__main__':
    main()
