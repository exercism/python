#!/usr/bin/env python3

import shutil
import subprocess
import sys
import tempfile
import json
from pathlib import Path

# Allow high-performance tests to be skipped
ALLOW_SKIP = ['alphametics', 'largest-series-product']


def check_assignment(name: str, test_file: Path) -> int:
    # Returns the exit code of the tests
    workdir = Path(tempfile.mkdtemp(name))
    example_name = name.replace("-", "_")
    try:
        test_file_out = workdir / test_file.name
        if name in ALLOW_SKIP:
            shutil.copyfile(test_file, test_file_out)
        else:
            with test_file.open('r') as src_file:
                lines = [line for line in src_file.readlines()
                         if not line.strip().startswith('@unittest.skip')]
            with test_file_out.open('w') as dst_file:
                dst_file.writelines(lines)
        exemplar_file = test_file.with_name('exemplar.py')
        if not exemplar_file.is_file():
            exemplar_file = exemplar_file.with_name('example.py')
        print(exemplar_file)
        shutil.copyfile(exemplar_file, workdir / '{}.py'.format(example_name))
        return subprocess.call([sys.executable, test_file_out])
    finally:
        shutil.rmtree(workdir)


def load_config():
    config_file = Path('config.json')
    try:
        with config_file.open() as json_file:
            data = json.load(json_file)
    except IOError:
        print('FAIL: {} file not found'.format(config_file))
        raise SystemExit(1)

    try:
        problems = [entry['slug'] for entry in data['exercises']
                    if "deprecated" not in entry]
    except KeyError:
        print('FAIL: {} has an incorrect format'.format(config_file))
        raise SystemExit(1)

    return problems


def main():
    if len(sys.argv) >= 2:
        # test specific exercises
        exercises = [exercise.strip('/') for exercise in sys.argv[1:]]
    else:
        # load exercises from config-file
        exercises = load_config()

    failures = []
    exercises_dir = Path('exercises')
    for exercise in exercises:
        test_file = next((exercises_dir / exercise).glob('*_test.py'), None)
        print('# ', exercise)
        if not test_file:
            print('FAIL: File with test cases not found')
            failures.append('{} (FileNotFound)'.format(exercise))
        else:
            if check_assignment(exercise, test_file):
                failures.append('{} (TestFailed)'.format(exercise))
        print('')

    print('TestEnvironment:', sys.executable.capitalize(), '\n\n')

    if failures:
        print('FAILURES: ', ', '.join(failures))
        raise SystemExit(1)
    else:
        print('SUCCESS!')


if __name__ == '__main__':
    main()
