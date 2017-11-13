#!/usr/bin/env python
import argparse
import sys
import unittest


COMMANDS = [
    'add',
    'edit',
    'remove',
    'deprecate',
    'lint'
]


def add(*args):
    # sys.exit(1) on error
    # return modified entry
    return {}


def edit(*args):
    # sys.exit(1) on error
    # return modified entry
    return {}


def remove(*args):
    # sys.exit(1) on error
    pass


def deprecate(*args):
    # sys.exit(1) on error
    # return modified entry
    return {}


def lint(*args):
    # sys.exit(1) on error
    # return list of violations
    return []


def main(*args):
    main_parser = argparse.ArgumentParser()
    main_parser.add_argument('command', choices=COMMANDS)
    main_parser.add_argument('args', nargs='*')
    opts = main_parser.parse_args(args[:1])
    func = globals()[opts.command]
    func(*args[1:])
    return 0


if __name__ == '__main__':
    sys.exit(main(*sys.argv[1:]))


class ConfigHelperTest(unittest.TestCase):
    pass
