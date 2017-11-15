#!/usr/bin/env python
import argparse
import contextlib
import json
import os
import re
import shutil
from subprocess import check_output
import sys
import tempfile
import unittest

QUICK_UUID = False

OK = 0
RUN_FAIL = 1
INVALID_USAGE = 2
RGX_EXERCISE = r'^[a-z\-]+$'
RGX_SNAKE_CASE = r'^[a-z_]+$'
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
    if slug == 'null':
        return None
    if not re.match(RGX_EXERCISE, slug):
        raise ValueError('exercise "{}" is not of the form '
                         '"exercise-slug"'.format(slug))
    return slug


def difficulty(value):
    n = int(value)
    if n < 1 or n > 10:
        raise ValueError('difficulty must be an integer in range 1..10')
    return n


def existing_topic(candidate):
    if not re.match(RGX_SNAKE_CASE, candidate):
        raise ValueError('topic "{}" is not in snake_case '
                         'format'.format(candidate))
    if os.path.isfile(os.path.join(os.getcwd(), 'TOPICS.txt')):
        with open('TOPICS.txt', 'r') as f:
            lines = f.readlines()
        topics = {line for line in map(lambda s: s.strip(), lines)
                  if re.match(RGX_SNAKE_CASE, line) is not None}
        if candidate in topics:
            return candidate
    raise ValueError('topic "{}" not found'.format(candidate))


def generate_uuid():
    return check_output(['bin/configlet', 'uuid']).decode().strip()


CONFIG_PARSER = argparse.ArgumentParser(add_help=False)
CONFIG_PARSER.add_argument('--config', default='config.json',
                           dest='config_file')

EXERCISE_PARSER = argparse.ArgumentParser(add_help=False)
EXERCISE_PARSER.add_argument('exercise', type=valid_exercise)
EXERCISE_PARSER.add_argument('--core', action='store_true', default=False)
EXERCISE_PARSER.add_argument('--unlocked-by', dest='unlocked_by', default=None,
                             type=valid_exercise)
EXERCISE_PARSER.add_argument('--difficulty', type=difficulty, default=1)
EXERCISE_PARSER.add_argument('--topics', nargs='*', type=existing_topic,
                             default=[])

BASE_PARSER = argparse.ArgumentParser(parents=[CONFIG_PARSER, EXERCISE_PARSER])


def add(*args):
    opts = BASE_PARSER.parse_args(args)
    # For testing purposes
    if QUICK_UUID:
        uuid = 'aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa'
    else:
        uuid = generate_uuid()
    entry = {
        'slug': opts.exercise,
        'uuid': uuid,
        'core': opts.core,
        'unlocked_by': opts.unlocked_by,
        'difficulty': opts.difficulty,
        'topics': opts.topics
    }
    config = load_config(opts.config_file)
    if find_exercise(opts.exercise, config=config) is not None:
        raise KeyError('exercise "{}" already exists!'.format(opts.exercise))
    config['exercises'].append(entry)
    save_config(config, opts.config_file)
    return entry


def edit(*args):
    # return modified entry
    opts = BASE_PARSER.parse_args(args)
    config = load_config(opts.config_file)
    entry = find_exercise(opts.exercise, config)
    if entry is None:
        raise KeyError('exercise "{}" does not exist!'.format(opts.exercise))
    if '--core' in args:
        entry['core'] = opts.core
    if '--unlocked-by' in args:
        entry['unlocked_by'] = opts.unlocked_by
    if '--difficulty' in args:
        entry['difficulty'] = opts.difficulty
    if '--topics' in args:
        entry['topics'] = opts.topics
    save_config(config, opts.config_file)
    return entry


def remove(*args):
    parser = argparse.ArgumentParser(parents=[CONFIG_PARSER])
    parser.add_argument('exercise', type=valid_exercise)
    opts = parser.parse_args(args)
    config = load_config(opts.config_file)
    for i in range(len(config['exercises'])):
        if config['exercises'][i]['slug'] == opts.exercise:
            del config['exercises'][i]
            save_config(config, opts.config_file)
            return
    raise KeyError('exercise "{}" does not exist!'.format(opts.exercise))


def deprecate(*args):
    parser = argparse.ArgumentParser(parents=[CONFIG_PARSER])
    parser.add_argument('exercise', type=valid_exercise)
    opts = parser.parse_args(args)
    entry = find_exercise(opts.exercise, config_file=opts.config_file)
    if entry is None:
        raise KeyError('exercise "{}" does not exist!'.format(opts.exercise))
    remove(opts.exercise, '--config', opts.config_file)
    config = load_config(opts.config_file)
    entry = {
        'uuid': entry['uuid'],
        'slug': opts.exercise,
        'deprecated': True
    }
    config['exercises'].append(entry)
    save_config(config, opts.config_file)
    return entry


def lint(*args):
    # return list of violations
    # parser = argparse.ArgumentParser(parents=[CONFIG_PARSER])
    # opts = parser.parse_args(args)
    return []


def main(*args):
    main_parser = argparse.ArgumentParser()
    main_parser.add_argument('command', choices=COMMANDS)
    main_parser.add_argument('args', nargs='*')
    opts = main_parser.parse_args(args[:1])
    func = globals()[opts.command]
    return func(*args[1:])


if __name__ == '__main__':
    try:
        ret = main(*sys.argv[1:])
    except KeyError:
        sys.exit(INVALID_USAGE)
    if isinstance(ret, dict):
        for k, v in ret.items():
            print('{}: {}'.format(k, v))
    elif isinstance(ret, list):
        for item in ret:
            print(str(item))
        if sys.argv[1] == 'lint' and any(ret):
            sys.exit(RUN_FAIL)
    elif isinstance(ret, int):
        sys.exit(ret)
    elif ret is not None:
        print(str(ret))
    sys.exit(OK)


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
        global QUICK_UUID
        QUICK_UUID = True

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

    @contextlib.contextmanager
    def assertExits(self, status_code=INVALID_USAGE):
        with self.assertRaises(SystemExit) as cm:
            yield
        actual = cm.exception.code
        msg = 'Status code "{}" received, expected "{}"'
        msg = msg.format(actual, status_code)
        self.assertEqual(actual, status_code, msg)

    def test_add_requires_exercise(self):
        with stash_config():
            with self.assertExits():
                main('add')

    def test_add_returns_new_entry(self):
        global QUICK_UUID
        QUICK_UUID = False
        with stash_config():
            exercise = 'test-exercise'
            entry = main('add', exercise)
            self.assert_entry_fields(entry, exercise)
        QUICK_UUID = True

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
            entry = main('add', exercise, '--topics', 'lists')
            self.assert_entry_fields(entry, exercise, topics=['lists'])

    def test_add_flag_topics_multiple(self):
        with stash_config():
            exercise = 'test-exercise'
            self.assertIsNone(find_exercise(exercise))
            entry = main('add', exercise, '--topics', 'lists', 'trees', 'maps')
            self.assert_entry_fields(entry, exercise,
                                     topics=['lists', 'trees', 'maps'])

    def test_add_cannot_add_existing_exercise(self):
        with stash_config():
            exercise = 'test-exercise'
            self.assertIsNone(find_exercise(exercise))
            main('add', exercise)
            with self.assertRaises(KeyError):
                main('add', exercise)

    def test_add_invalid_exercise(self):
        with stash_config():
            exercise = 'Try_me'
            with self.assertExits():
                main('add', exercise)

    def test_add_invalid_topic(self):
        with stash_config():
            exercise = 'test-exercise'
            with self.assertExits():
                main('add', exercise, '--topics', 'Topic')

    def test_add_non_existent_topic(self):
        with stash_config():
            exercise = 'test-exercise'
            with self.assertExits():
                main('add', exercise, '--topics', 'topic')

    def test_edit_requires_exercise(self):
        with stash_config():
            with self.assertExits():
                main('edit')

    def test_edit_returns_modified_entry(self):
        with stash_config():
            exercise = 'test-exercise'
            before = dict(main('add', exercise))
            after = main('edit', exercise, '--core', '--difficulty', '3')
            self.assert_entry_fields(after, exercise, core=True,
                                     unlocked_by=before['unlocked_by'],
                                     difficulty=3, topics=before['topics'])

    def test_edit_modifies_entry_in_config(self):
        with stash_config():
            exercise = 'test-exercise'
            before = dict(main('add', exercise))
            self.assertIsNotNone(before)
            main('edit', exercise, '--core', '--difficulty', '3')
            after = find_exercise(exercise)
            self.assert_entry_fields(after, exercise, core=True,
                                     unlocked_by=before['unlocked_by'],
                                     difficulty=3, topics=before['topics'])

    def test_edit_flag_core(self):
        with stash_config():
            exercise = 'test-exercise'
            before = dict(main('add', exercise))
            self.assertIs(before['core'], False)
            after = main('edit', exercise, '--core')
            self.assertIs(after['core'], True)

    def test_edit_flag_config(self):
        with stash_config():
            exercise = 'test-exercise'
            before = dict(main('add', exercise, '--config', self.config_file))
            main('edit', exercise, '--config', self.config_file, '--core')
            after = find_exercise(exercise, config_file=self.config_file)
            self.assertNotEqual(before['core'], after['core'])

    def test_edit_flag_unlocked_by(self):
        with stash_config():
            parent_name = 'parent-exercise'
            exercise = 'test-exercise'
            main('add', parent_name)
            before = dict(main('add', exercise))
            self.assertIsNone(before['unlocked_by'])
            after = main('edit', exercise, '--unlocked-by', parent_name)
            self.assertNotEqual(before['unlocked_by'], after['unlocked_by'])
            self.assertEqual(after['unlocked_by'], parent_name)

    def test_edit_flag_unlocked_by_null(self):
        with stash_config():
            parent_name = 'parent-exercise'
            exercise = 'test-exercise'
            main('add', parent_name)
            before = dict(main('add', exercise, '--unlocked-by', parent_name))
            self.assertEqual(before['unlocked_by'], parent_name)
            after = main('edit', exercise, '--unlocked-by', 'null')
            self.assertIsNone(after['unlocked_by'])

    def test_edit_flag_difficulty(self):
        with stash_config():
            exercise = 'test-exercise'
            before = dict(main('add', exercise))
            self.assertEqual(before['difficulty'], 1)
            after = main('edit', exercise, '--difficulty', '3')
            self.assertEqual(after['difficulty'], 3)

    def test_edit_flag_topics_single(self):
        with stash_config():
            exercise = 'test-exercise'
            before = dict(main('add', exercise))
            self.assertEqual(before['topics'], [])
            after = main('edit', exercise, '--topics', 'lists')
            self.assertEqual(after['topics'], ['lists'])

    def test_edit_flag_topics_multiple(self):
        with stash_config():
            exercise = 'test-exercise'
            before = dict(main('add', exercise))
            self.assertEqual(before['topics'], [])
            after = main('edit', exercise, '--topics', 'lists', 'maps')
            self.assertEqual(after['topics'], ['lists', 'maps'])

    def test_edit_cannot_edit_non_existent_exercise(self):
        with stash_config():
            exercise = 'test-exercise'
            with self.assertRaises(KeyError):
                main('edit', exercise, '--core')

    def test_edit_invalid_topic(self):
        with stash_config():
            exercise = 'test-exercise'
            main('add', exercise)
            with self.assertExits():
                main('edit', exercise, '--topics', 'Topic')

    def test_edit_non_existent_topic(self):
        with stash_config():
            exercise = 'test-exercise'
            main('add', exercise)
            with self.assertExits():
                main('edit', exercise, '--topics', 'topic')

    def test_remove_requires_exercise(self):
        with stash_config():
            with self.assertExits():
                main('remove')

    def test_remove_removes_entry_in_config(self):
        with stash_config():
            exercise = 'test-exercise'
            main('add', exercise)
            self.assertIsNotNone(find_exercise(exercise))
            main('remove', exercise)
            self.assertIsNone(find_exercise(exercise))

    def test_remove_flag_config(self):
        with stash_config():
            exercise = 'test-exercise'
            main('add', exercise, '--config', self.config_file)
            self.assertIsNotNone(find_exercise(exercise,
                                               config_file=self.config_file))
            main('remove', exercise, '--config', self.config_file)
            self.assertIsNone(find_exercise(exercise,
                                            config_file=self.config_file))

    def test_remove_cannot_remove_non_existent_exercise(self):
        with stash_config():
            exercise = 'test-exercise'
            self.assertIsNone(find_exercise(exercise))
            with self.assertRaises(KeyError):
                main('remove', exercise)

    def test_deprecate_requires_exercise(self):
        with stash_config():
            with self.assertExits():
                main('deprecate')

    def test_deprecate_returns_modified_entry(self):
        with stash_config():
            exercise = 'test-exercise'
            entry = main('add', exercise)
            self.assertNotIn('deprecated', entry)
            entry = main('deprecate', exercise)
            self.assertIs(entry['deprecated'], True)

    def test_deprecate_modifies_entry_in_config(self):
        with stash_config():
            exercise = 'test-exercise'
            entry = main('add', exercise)
            self.assertNotIn('deprecated', entry)
            main('deprecate', exercise)
            entry = find_exercise(exercise)
            self.assertIs(entry['deprecated'], True)

    def test_deprecate_flag_config(self):
        with stash_config():
            exercise = 'test-exercise'
            entry = main('add', exercise, '--config', self.config_file)
            self.assertNotIn('deprecated', entry)
            main('deprecate', exercise, '--config', self.config_file)
            entry = find_exercise(exercise, config_file=self.config_file)
            self.assertIs(entry['deprecated'], True)

    def test_deprecate_cannot_deprecate_non_existent_exercise(self):
        with stash_config():
            exercise = 'test-exercise'
            self.assertIsNone(find_exercise(exercise))
            with self.assertRaises(KeyError):
                main('deprecate', exercise)

    def test_deprecate_removes_unnecessary_keys(self):
        with stash_config():
            exercise = 'test-exercise'
            entry = main('add', exercise)
            self.assert_entry_fields(entry, exercise)
            after = main('deprecate', exercise)
            for key in entry.keys():
                if key in ['uuid', 'slug']:
                    continue
                self.assertNotIn(key, after)
            self.assertEqual(after['slug'], exercise)
            self.assertIn('uuid', after)
            self.assertIs(after['deprecated'], True)
