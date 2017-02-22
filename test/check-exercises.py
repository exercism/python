#!/usr/bin/env python
from __future__ import print_function

import os
import ast
import imp
import glob
import shutil
import subprocess
import sys
import tempfile
import json


def check_assignment(name, test_file):
    # Returns the exit code of the tests
    workdir = tempfile.mkdtemp(name)
    example_name = modname_heuristic(test_file)
    try:
        test_file_out = os.path.join(workdir, os.path.basename(test_file))
        shutil.copyfile(test_file, test_file_out)
        shutil.copyfile(os.path.join(os.path.dirname(test_file), 'example.py'),
                        os.path.join(workdir, '{}.py'.format(example_name)))
        return subprocess.call(['python', test_file_out])
    finally:
        shutil.rmtree(workdir)


def modname_heuristic(test_file):
    with open(test_file) as f:
        tree = ast.parse(f.read(), filename=test_file)
    # return the first nonexistent module that the tests import
    for node in ast.walk(tree):
        for modname in possible_module_names(node):
            if is_module_missing(modname):
                return modname


def possible_module_names(node):
    if isinstance(node, ast.Import):
        for alias in node.names:
            yield alias.name
    elif isinstance(node, ast.ImportFrom):
        yield node.module


def is_module_missing(modname):
    try:
        imp.find_module(modname)
    except ImportError:
        return True
    else:
        return False


def load_config():
    try:
        with open('./config.json') as json_file:
            data = json.load(json_file)
    except IOError:
        print('FAIL: config.json file not found')
        raise SystemExit(1)

    try:
        problems = [entry['slug'] for entry in data['exercises']]
        deprecated_problems = data['deprecated']
    except KeyError:
        print('FAIL: config.json has an incorrect format')
        raise SystemExit(1)

    return problems, deprecated_problems


def main():
    if len(sys.argv) >= 2:
        # test specific exercises
        exercises = [exercise.strip('/') for exercise in sys.argv[1:]]
    else:
        # load exercises from config-file
        exercises, _ = load_config()

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

    if failures:
        print('FAILURES: ', ', '.join(failures))
        raise SystemExit(1)
    else:
        print('SUCCESS!')


if __name__ == '__main__':
    main()
