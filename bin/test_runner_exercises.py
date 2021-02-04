#!/usr/bin/env python3
"""Meant to be run from inside python-test-runner container,
where this track repo is mounted at /python
"""
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
from data import Config, ExerciseInfo

# Allow high-performance tests to be skipped
ALLOW_SKIP = ['alphametics', 'largest-series-product']


def check_assignment(exercise: ExerciseInfo) -> int:
    # Returns the exit code of the tests
    workdir = Path(tempfile.mkdtemp(exercise.slug))
    solution_file = exercise.solution_stub.name
    try:
        test_file_out = workdir / exercise.test_file.name
        if exercise.slug in ALLOW_SKIP:
            shutil.copy2(exercise.test_file, test_file_out)
        else:
            with exercise.test_file.open('r') as src_file:
                lines = [line for line in src_file.readlines()
                         if not line.strip().startswith('@unittest.skip')]
            with test_file_out.open('w') as dst_file:
                dst_file.writelines(lines)
        shutil.copyfile(exercise.exemplar_file, workdir / solution_file)
        if exercise.config_file.is_file():
            tmp_meta = workdir / '.meta'
            tmp_meta.mkdir(exist_ok=True)
            shutil.copy2(exercise.config_file, tmp_meta / exercise.config_file.name)
        args = ['./bin/run.sh', exercise.slug, workdir, workdir]
        subprocess.run(args, cwd='/opt/test-runner')
        results_file = workdir / 'results.json'
        if results_file.is_file():
            with results_file.open() as f:
                results = json.load(f)
            if results['status'] == 'pass':
                return 0
        return 1
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

    if failures:
        print('FAILURES: ', ', '.join(failures))
        raise SystemExit(1)
    else:
        print('SUCCESS!')


if __name__ == "__main__":
    main()
