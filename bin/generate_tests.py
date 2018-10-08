#!/usr/bin/env python
import json
import os
import re
import subprocess
import sys
import argparse

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('exercise', nargs='*', default=[],
                        help='exercise(s) for which to generate tests')
arg_parser.add_argument('-A', '--all', default=False, action='store_true',
                        help=('if enabled, will attempt to update tests for '
                              'all known exercises'))
arg_parser.add_argument('-f', '--force', default=False, action='store_true',
                        help=('if enabled, will overwrite existing test cases '
                              'even if they are already up-to-date'))
arg_parser.add_argument('--noop', default=False, action='store_true',
                        help=('if enabled, will report which test cases need '
                              'updating without performing any actions on '
                              'them'))
arg_parser.add_argument('-v', '--verbose', default=False, action='store_true',
                        help='enables verbose output')
arg_parser.add_argument('--style', choices=['method', 'class'],
                        default='method',
                        help='test case style')
arg_parser.add_argument('--spec', default='../problem-specifications/',
                        dest='spec_path',
                        help=('path to clone of exercism/problem-'
                              'specifications repository'))

CANONICAL_DATA = ('# Tests adapted from `problem-specifications//'
                  'canonical-data.json` @ v')
rgxCanonicalDataVersion = re.compile('^' + CANONICAL_DATA +
                                     '(?P<version>\d+\.\d+\.\d+)$')
rgxTestNameRemove = re.compile("[',]+|\b-\b")
rgxTestNameUnderscore = re.compile("[/ \-]+")
rgxCamelCase = re.compile("([A-Z])")


def format_test_name(description):
    description = description.lower()
    description = rgxTestNameRemove.sub('', description)
    description = rgxTestNameUnderscore.sub('_', description)
    return description


class Tabbed(object):
    @staticmethod
    def tab(level=1):
        return ''.rjust(4 * level)

    def __init__(self, file, count=1):
        self.file = file
        self.count = count

    def __enter__(self):
        return self

    def __exit__(self, *args):
        pass

    def write(self, msg):
        self.file.write(Tabbed.tab(self.count) + msg)

    def writeline(self, msg=''):
        self.write(msg + '\n')

    def writelines(self, lines):
        for line in lines:
            self.writeline(line)


def get_all_exercises(track='python'):
    output = subprocess.check_output(['exercism', 'li', track])
    for line in output.decode().split('\n'):
        line = line.strip()
        if line == '':
            break
        yield line


def get_spec(spec_path, exercise):
    path_to_spec = os.path.join(spec_path,
                                'exercises',
                                exercise,
                                'canonical-data.json')
    if not os.path.isfile(path_to_spec):
        return None
    with open(path_to_spec, 'r') as f:
        spec_data = json.load(f)
    if 'version' not in spec_data:
        return None
    return spec_data


def get_impl_dir(exercise):
    return os.path.join('exercises', exercise)


def get_test_file(exercise):
    path_to_impl = get_impl_dir(exercise)
    return os.path.join(path_to_impl,
                        '{}_test.py'.format(exercise.replace('-', '_')))


def is_up_to_date(spec_data):
    if spec_data is None:
        return (False, None)
    exercise = spec_data['exercise']
    path_to_tests = get_test_file(exercise)
    if not os.path.isfile(path_to_tests):
        return (False, '0.0.0')
    current_version = None
    for line in open(path_to_tests):
        m = rgxCanonicalDataVersion.search(line)
        if m is not None:
            current_version = m.group('version')
    return (spec_data['version'] == current_version, current_version)


def get_inputs(test_case):
    if 'input' in test_case:
        for k, v in test_case['input'].items():
            yield '{}={}'.format(k, json.dumps(v))
    else:
        for k, v in test_case.items():
            if k in ['description', 'property', 'expected', 'comments']:
                continue
            yield '{}={}'.format(k, json.dumps(v))


def write_test_case(exercise, style, case, f):
    def blank():
        f.writeline()
    module = exercise.replace('-', '_')
    titlized = exercise.title().replace('-', '')
    snake_cased = format_test_name(case['description'])
    has_any_error = False
    with Tabbed(f) as _f:
        _f.writeline('def test_{}(self):'.format(snake_cased))
        with Tabbed(_f) as __f:
            expected = case['expected']
            with Tabbed(__f) as ___f:
                has_error = False
                if isinstance(expected, dict) and 'error' in expected:
                    has_error = True
                    has_any_error = True
                    writer = ___f
                    line = 'with self.assertRaisesWithMessage(ValueError):'
                    __f.writeline(line)
                else:
                    writer = __f
                if style == 'class':
                    writer.writeline('sut = {}('.format(titlized))
                else:
                    if has_error:
                        fmt = '{}.{}('
                    else:
                        fmt = 'actual = {}.{}('
                    prop_name = rgxCamelCase.sub(r'_\1', case['property'])
                    writer.writeline(fmt.format(module, prop_name.lower()))
                with Tabbed(writer) as _writer:
                    for arg in get_inputs(case):
                        _writer.writeline('{},'.format(arg))
                writer.writeline(')')
                if not has_error:
                    literal = expected in [False, True, None]
                    if literal:
                        test_call = 'assertIs'
                    else:
                        expected = json.dumps(case['expected'])
                        test_call = 'assertEqual'
                        writer.writeline('expected = {}'.format(expected))
                    if style == 'class':
                        fmt = 'self.{}(sut.{}(), {})'
                    else:
                        fmt = 'self.{0}(actual, {2})'
                    writer.writeline(fmt.format(
                        test_call,
                        case['property'],
                        expected if literal else 'expected'
                    ))
    blank()
    return has_any_error


def create_tests(spec_data, style='method'):
    exercise = spec_data['exercise']
    module = exercise.replace('-', '_')
    titlized = exercise.title().replace('-', '')
    path_to_impl = get_impl_dir(exercise)
    if not os.path.isdir(path_to_impl):
        os.makedirs(path_to_impl)
    path_to_tests = get_test_file(exercise)
    with open(path_to_tests, 'w') as f_:
        with Tabbed(f_, 0) as f:
            def blank():
                f.writeline()
            f.writeline('import unittest')
            blank()
            if style == 'class':
                f.writeline('from {} import {}'.format(module, titlized))
            else:
                f.writeline('import {}'.format(module))
            blank()
            blank()
            f.writeline(CANONICAL_DATA + spec_data['version'])
            blank()
            f.writeline('class {}Test(unittest.TestCase):'.format(titlized))
            with Tabbed(f) as _f:
                cases = list(spec_data['cases'])
                while cases:
                    case = cases.pop(0)
                    if 'cases' in case:
                        for _case in case['cases']:
                            _case['description'] = (case['description'] + '_' +
                                                    _case['description'])
                        cases = case['cases'] + cases
                        continue
                    has_errors = write_test_case(exercise, style, case, f)

                # Utility Functions
                if has_errors:
                    _f.writelines([
                        '# Utility Functions',
                        'def setUp(self):'
                    ])
                    with Tabbed(_f) as __f:
                        __f.writeline('try:')
                        with Tabbed(__f) as ___f:
                            ___f.writeline('self.assertRaisesRegex')
                            __f.writeline('except AttributeError:')
                            ___f.writeline(
                                'self.assertRaisesRegex = '
                                'self.assertRaisesRegexp'
                            )
                        blank()
                        _f.writeline(
                            'def assertRaisesWithMessage(self, exception):'
                        )
                        __f.writeline(
                            'return self.assertRaisesRegex(exception, r".+")'
                        )
                    blank()
                blank()
                f.writeline('if __name__ == "__main__":')
                _f.writeline('unittest.main()')


def main(opts):
    if opts.all:
        opts.exercise = get_all_exercises('python')
    no_data = []
    needs_update = []
    for exercise in opts.exercise:
        spec_data = get_spec(opts.spec_path, exercise)
        up_to_date, current_version = is_up_to_date(spec_data)
        if spec_data is None:
            no_data.append(exercise)
        elif not opts.force and up_to_date:
            if opts.verbose:
                print('{}: up-to-date ({})'.format(exercise, current_version))
        else:
            needs_update.append((
                exercise,
                current_version,
                spec_data['version'],
            ))
            if not opts.noop:
                create_tests(spec_data, opts.style)
    if any(no_data):
        print('The following exercises have no canonical data:')
        for exercise in no_data:
            print('  {}'.format(exercise))
    if any(needs_update):
        if opts.noop:
            print('The following exercises need updating:')
        else:
            print('The following exercises were updated:')
        for exercise, current_version, spec_version in needs_update:
            print('  {} ({} -> {})'.format(
                exercise,
                current_version,
                spec_version
            ))
    return 0


if __name__ == '__main__':
    sys.exit(main(arg_parser.parse_args()))
