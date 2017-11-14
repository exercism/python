#!/usr/bin/env python
import argparse
import contextlib
import json
import os
import shutil
import sys
import tempfile
import unittest

INVALID_USAGE = 2
RGX_UUID = r'^[a-f\d]{8}(-[a-f\d]{4}){3}-[a-f\d]{12}$'
COMMANDS = [
    'add',
    'edit',
    'remove',
    'deprecate',
    'lint'
]


def blank_config():
    return {
        'language': 'Python',
        'active': True,
        'exercises': [],
        'foregone': []
    }


def load_config(config_file='config.json'):
    with open(config_file, 'r') as f:
        return json.load(f)


def save_config(config=None, config_file='config.json'):
    if config is None:
        config = blank_config()
    with open(config_file, 'w') as f:
        f.write(json.dumps(config, indent=2))


def find_exercise(slug, config=None, config_file='config.json'):
    if config is None:
        with open(config_file, 'r') as f:
            config = json.load(f)
    if 'exercises' in config:
        for exercise in config['exercises']:
            if 'slug' in exercise and exercise['slug'] == slug:
                return exercise


def valid_exercise(slug):
    # TODO validate format
    # raise argparse.ArgumentTypeError('exercise "{}" is not of the form "exercise-slug"'.format(slug))
    return slug


def difficulty(value):
    n = int(value)
    if n < 1 or n > 10:
        raise argparse.ArgumentTypeError('difficulty must be an integer in '
                                         'range 1..10')
    return n


def existing_topic(candidate):
    # TODO validate format and confirm existence
    # raise argparse.ArgumentTypeError('topic "{}" is not in snake_case format'.format(candidate))
    # raise argparse.ArgumentError('topic "{}" not found'.format(candidate))
    return candidate


CONFIG_PARSER = argparse.ArgumentParser(add_help=False)
CONFIG_PARSER.add_argument('--config', default='config.json')


EXERCISE_PARSER = argparse.ArgumentParser(add_help=False)
EXERCISE_PARSER.add_argument('exercise', type=valid_exercise)
EXERCISE_PARSER.add_argument('--core', action='store_true', default=False)
EXERCISE_PARSER.add_argument('--unlocked-by',
                             default=None,
                             dest='unlocked_by',
                             type=valid_exercise)
EXERCISE_PARSER.add_argument('--difficulty', default=1, type=difficulty)
EXERCISE_PARSER.add_argument('--topics',
                             nargs='*',
                             default=[],
                             type=existing_topic)


def add(*args):
    # sys.exit(1) on error
    # return modified entry
    parser = argparse.ArgumentParser(parents=[CONFIG_PARSER, EXERCISE_PARSER])
    opts = parser.parse_args(args)
    entry = {
        'slug': opts.exercise,
        'uuid': 'aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee',
        'core': opts.core,
        'unlocked_by': opts.unlocked_by,
        'difficulty': opts.difficulty,
        'topics': opts.topics
    }
    config = load_config(opts.config)
    if find_exercise(opts.exercise, config=config) is not None:
        raise KeyError('exercise "{}" already exists!'.format(opts.exercise))
    config['exercises'].append(entry)
    save_config(config, opts.config)
    return entry


def edit(*args):
    # sys.exit(1) on error
    # return modified entry
    parser = argparse.ArgumentParser(parents=[CONFIG_PARSER, EXERCISE_PARSER])
    opts = parser.parse_args(args)
    return {}


def remove(*args):
    # sys.exit(1) on error
    parser = argparse.ArgumentParser(parents=[CONFIG_PARSER, EXERCISE_PARSER])
    opts = parser.parse_args(args)
    pass


def deprecate(*args):
    # sys.exit(1) on error
    # return modified entry
    parser = argparse.ArgumentParser(parents=[CONFIG_PARSER])
    opts = parser.parse_args(args)
    return {}


def lint(*args):
    # sys.exit(1) on error
    # return list of violations
    parser = argparse.ArgumentParser(parents=[CONFIG_PARSER])
    opts = parser.parse_args(args)
    return []


def main(*args):
    main_parser = argparse.ArgumentParser()
    main_parser.add_argument('command', choices=COMMANDS)
    main_parser.add_argument('args', nargs='*')
    opts = main_parser.parse_args(args[:1])
    func = globals()[opts.command]
    return func(*args[1:])


if __name__ == '__main__':
    ret = main(*sys.argv[1:])
    if isinstance(ret, dict):
        for k, v in ret.items():
            print('{}: {}'.format(k, v))
    elif isinstance(ret, list):
        for item in ret:
            print(str(item))
    elif isinstance(ret, int):
        sys.exit(ret)
    elif ret is not None:
        print(str(ret))
    sys.exit(0)


@contextlib.contextmanager
def stash_config(config_file='config.json'):
    config = load_config(config_file)
    yield
    save_config(config, config_file=config_file)


class ConfigHelperTest(unittest.TestCase):
    def setUp(self):
        self.dir = tempfile.mkdtemp()
        self.config_file = os.path.join(self.dir, 'test.config.json')
        with open(self.config_file, 'w') as f:
            f.write(json.dumps(blank_config()))
        save_config(config_file=self.config_file)
        self.ctx = stash_config()
        self.ctx.__enter__()

    def tearDown(self):
        shutil.rmtree(self.dir)
        self.ctx.__exit__(None, None, None)

    def assert_entry_fields(self, entry, slug, core=False, unlocked_by=None,
                            difficulty=1, topics=[]):
        self.assertIn('slug', entry)
        self.assertEqual(entry['slug'], slug)
        self.assertIn('uuid', entry)
        self.assertRegexpMatches(entry['uuid'], RGX_UUID)
        self.assertIn('core', entry)
        self.assertEqual(entry['core'], core)
        self.assertIn('unlocked_by', entry)
        self.assertEqual(entry['unlocked_by'], unlocked_by)
        self.assertIn('difficulty', entry)
        self.assertEqual(entry['difficulty'], difficulty)
        self.assertIn('topics', entry)
        self.assertEqual(entry['topics'], topics)

    def test_add_supported(self):
        with stash_config():
            main('add', 'test-exercise')

    def test_add_requires_exercise(self):
        with stash_config():
            with self.assertRaises(SystemExit) as cm:
                main('add')
            self.assertEqual(cm.exception.code, INVALID_USAGE)

    def test_add_returns_new_entry(self):
        with stash_config():
            exercise = 'test-exercise'
            entry = main('add', exercise)
            self.assert_entry_fields(entry, exercise)

    def test_add_creates_new_entry_in_config(self):
        with stash_config():
            exercise = 'test-exercise'
            self.assertIsNone(find_exercise(exercise))
            main('add', exercise)
            entry = find_exercise(exercise)
            self.assertIsNotNone(entry)
            self.assert_entry_fields(entry, exercise)

    def test_add_flag_config(self):
        with stash_config():
            exercise = 'test-exercise'
            self.assertIsNone(find_exercise(exercise,
                                            config_file=self.config_file))
            main('add', exercise, '--config', self.config_file)
            self.assertIsNotNone(find_exercise(exercise,
                                               config_file=self.config_file))

    def test_add_flag_core(self):
        with stash_config():
            exercise = 'test-exercise'
            self.assertIsNone(find_exercise(exercise))
            entry = main('add', exercise, '--core')
            self.assert_entry_fields(entry, exercise, core=True)

    def test_add_flag_unlocked_by(self):
        with stash_config():
            unlocked_by = 'parent-exercise'
            exercise = 'test-exercise'
            self.assertIsNone(find_exercise(unlocked_by))
            main('add', unlocked_by)
            self.assertIsNone(find_exercise(exercise))
            entry = main('add', exercise, '--unlocked-by', unlocked_by)
            self.assert_entry_fields(entry, exercise, unlocked_by=unlocked_by)

    def test_add_flag_difficulty(self):
        with stash_config():
            exercise = 'test-exercise'
            self.assertIsNone(find_exercise(exercise))
            entry = main('add', exercise, '--difficulty', '9')
            self.assert_entry_fields(entry, exercise, difficulty=9)

    def test_add_flag_topics_single(self):
        with stash_config():
            exercise = 'test-exercise'
            self.assertIsNone(find_exercise(exercise))
            entry = main('add', exercise, '--topics', 'topic1')
            self.assert_entry_fields(entry, exercise, topics=['topic1'])

    def test_add_flag_topics_multiple(self):
        with stash_config():
            exercise = 'test-exercise'
            self.assertIsNone(find_exercise(exercise))
            entry = main('add', exercise, '--topics', 't1', 't2', 't3')
            self.assert_entry_fields(entry, exercise,
                                     topics=['t1', 't2', 't3'])

    def test_add_cannot_add_existing_exercise(self):
        with stash_config():
            exercise = 'test-exercise'
            self.assertIsNone(find_exercise(exercise))
            main('add', exercise)
            with self.assertRaises(KeyError):
                main('add', exercise)
