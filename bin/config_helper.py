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
    return 0


def edit(*args):
    return 0


def remove(*args):
    return 0


def deprecate(*args):
    return 0


def lint(*args):
    return 0


def main(*args):
    main_parser = argparse.ArgumentParser()
    main_parser.add_argument('command', choices=COMMANDS)
    main_parser.add_argument('args', nargs='*')
    opts = main_parser.parse_args(args[:1])
    func = globals()[opts.command]
    sys.exit(func(*args[1:]))


if __name__ == '__main__':
    sys.exit(main(*sys.argv[1:]))


class ConfigHelperTest(unittest.TestCase):
    pass
