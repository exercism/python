#!/usr/bin/env python
from __future__ import print_function

import os
import glob
import shutil
import subprocess
import sys
import tempfile
import json

# Allow high-performance tests to be skipped
ALLOW_SKIP = ['alphametics', 'largest-series-product']


def check_assignment(name, test_file):
    # Returns the exit code of the tests
    workdir = tempfile.mkdtemp(name)
    example_name = name.replace("-", "_")
    try:
        test_file_out = os.path.join(workdir, os.path.basename(test_file))
        if name in ALLOW_SKIP:
            shutil.copyfile(test_file, test_file_out)
        else:
            with open(test_file, 'r') as src_file:
                lines = [line for line in src_file.readlines()
                         if not line.strip().startswith('@unittest.skip')]
            with open(test_file_out, 'w') as dst_file:
                dst_file.writelines(lines)
        shutil.copyfile(os.path.join(os.path.dirname(test_file), 'example.py'),
                        os.path.join(workdir, '{}.py'.format(example_name)))
        return subprocess.call([sys.executable, test_file_out])
    finally:
        shutil.rmtree(workdir)


def load_config():
    try:
        with open('./config.json') as json_file:
            data = json.load(json_file)
    except IOError:
        print('FAIL: config.json file not found')
        raise SystemExit(1)

    try:
        problems = [entry['slug'] for entry in data['exercises']
                    if "deprecated" not in entry]
    except KeyError:
        print('FAIL: config.json has an incorrect format')
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
    for exercise in exercises:
        test_file = glob.glob('./exercises/{}/*_test.py'.format(exercise))
        print('# ', exercise)
        if not test_file:
            print('FAIL: File with test cases not found')
            failures.append('{} (FileNotFound)'.format(exercise))
        else:
            if check_assignment(exercise, test_file[0]):
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
