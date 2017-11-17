#!/usr/bin/env python
import argparse
from collections import OrderedDict
import contextlib
import json
import os
import re
from subprocess import check_output
import sys
import unittest

QUICK_UUID = False

LANGUAGE = 'Python'
COMMANDS = [
    'add',
    'edit',
    'remove',
    'deprecate',
    'lint'
]
KEYS = [
    'uuid',
    'slug',
    'core',
    'unlocked_by',
    'difficulty',
    'topics'
]

DEPRECATED_KEYS = [
    'uuid',
    'slug',
    'deprecated'
]


OK = 0
RUN_FAIL = 1
INVALID_USAGE = 2
RGX_EXERCISE = r'^[a-z\-]+$'
RGX_SNAKE_CASE = r'^[a-z_]+$'
RGX_UUID = r'^[a-f\d]{8}(-[a-f\d]{4}){3}-[a-f\d]{12}$'


def json_ordered_load(file_obj):
    return json.load(file_obj, object_pairs_hook=OrderedDict)


def json_get_line_no(*patterns):
    with open('config.json', 'r') as f:
        lines = f.readlines()
    line_no = 0
    for pattern in patterns:
        try:
            while not lines[line_no].strip().startswith(pattern):
                line_no += 1
            line_no += 1
        except IndexError:
            return -1
    return line_no


class StyleViolation(object):
    code = -1

    def __init__(self, line_no=-1):
        self.code = type(self).code
        self.line_no = line_no

    def __str__(self):
        msg = 'config.json:{}: [CH{}]'.format(self.line_no, self.code)
        if self.msg is not None:
            return ' '.join([msg, self.msg])
        return msg

    def __repr__(self):
        return json.dumps(self.__dict__)


class MissingRootKey(StyleViolation):
    code = 10

    def __init__(self, key, line_no):
        self.key = key
        self.msg = 'root key "{}" not found'.format(key)
        StyleViolation.__init__(self, line_no=line_no)


class InvalidRootKeyValue(StyleViolation):
    code = 20

    def __init__(self, key, value, line_no):
        self.key = key
        self.value = value
        StyleViolation.__init__(self, line_no=line_no)

    @property
    def msg(self):
        return ('Invalid root key value: ' +
                {
                    'language': ('language must be "{}"'.format(LANGUAGE)),
                    'active': ('active must be either true or false'),
                    'exercises': ('exercises must be a list'),
                    'foregone': ('foregone must be a list')
                }[self.key].format(self.__dict__))


class InvalidKeyValueFormat(StyleViolation):
    code = 100

    def __init__(self, exercise, key, value, line_no):
        self.exercise = exercise
        self.key = key
        self.value = value
        StyleViolation.__init__(self, line_no=line_no)

    @property
    def msg(self):
        return {
            'uuid': ('{exercise}.uuid: invalid; please generate '
                     'a new UUID with configlet'),
            'slug': ('{exercise}.slug: expected a string of the '
                     'form "exercise-slug", found "{value}"'),
            'deprecated': ('{exercise}.core: expected true or false, '
                           'found "{value}"'),
            'core': '{exercise}.core: expected true or false, found "{value}"',
            'unlocked_by': ('{exercise}.unlocked_by: expected null or a '
                            'string of the form "exercise-slug", found '
                            '"{value}"'),
            'difficulty': ('{exercise}.difficulty: expected an integer in '
                           'range [1..10], found {value}'),
            'topics': ('{exercise}.topics: expected a string of the form '
                       '"snake_case", found "{value}"')
        }.format(self.__dict__)


class IncorrectKeyOrder(StyleViolation):
    code = 110

    def __init__(self, exercise, expected, actual, line_no):
        self.exercise = exercise
        self.expected = expected
        self.actual = actual
        msg = '{}: keys out of order; expected "{}", found "{}"'
        self.msg = msg.format(exercise, expected, actual)
        StyleViolation.__init__(self, line_no=line_no)


class MissingKey(StyleViolation):
    code = 120

    def __init__(self, exercise, key, line_no):
        self.exercise = exercise
        self.key = key
        self.msg = '{}.{} not found'.format(exercise, key)
        StyleViolation.__init__(self, line_no=line_no)


class NonExistentExercise(StyleViolation):
    code = 201

    def __init__(self, exercise, unlocked_by, line_no):
        self.exercise = exercise
        self.unlocked_by = unlocked_by
        msg = '{}.unlocked_by: exercise "{}" not found'
        self.msg = msg.format(exercise, unlocked_by)
        StyleViolation.__init__(self, line_no=line_no)


class NonExistentTopic(StyleViolation):
    code = 202

    def __init__(self, exercise, topic, line_no):
        self.exercise = exercise
        self.topic = topic
        msg = '{}.topics: topic "{}" not found'
        self.msg = msg.format(exercise, topic)
        StyleViolation.__init__(self, line_no=line_no)


class InvalidForegoneExercise(StyleViolation):
    code = 300

    def __init__(self, exercise, line_no):
        self.exercise = exercise
        self.msg = ('invalid foregone exercise; expected a string of the form '
                    '"foregone-exercise", found "{}"'.format(exercise))
        StyleViolation.__init__(self, line_no=line_no)


def create_blank_config():
    return OrderedDict({
        'language': 'Python',
        'active': True,
        'exercises': [],
        'foregone': []
    }.items())


def load_config():
    with open('config.json', 'r') as f:
        return json_ordered_load(f)


@contextlib.contextmanager
def open_config():
    config = load_config()
    yield config
    save_config(config)


def save_config(config=None):
    if config is None:
        config = create_blank_config()
    with open('config.json', 'w') as f:
        f.write(json.dumps(config, indent=2))


def find_exercise(slug, config=None):
    if config is None:
        config = load_config()
    if 'exercises' in config:
        for exercise in config['exercises']:
            if 'slug' in exercise and exercise['slug'] == slug:
                return exercise


def valid_uuid(uuid):
    return re.match(RGX_UUID, uuid) is not None


def valid_exercise(slug):
    if slug is None:
        raise ValueError('exercise cannot be null')
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
    raise KeyError('topic "{}" not found'.format(candidate))


def generate_uuid():
    return check_output(['bin/configlet', 'uuid']).decode().strip()


BASE_PARSER = argparse.ArgumentParser(add_help=False)
BASE_PARSER.add_argument('exercise', type=valid_exercise)

EXERCISE_PARSER = argparse.ArgumentParser(parents=[BASE_PARSER],
                                          add_help=False)
EXERCISE_PARSER.add_argument('--core', action='store_true', default=False)
EXERCISE_PARSER.add_argument('--unlocked-by', dest='unlocked_by',
                             default=None, type=valid_exercise)
EXERCISE_PARSER.add_argument('--difficulty', type=difficulty, default=1)
EXERCISE_PARSER.add_argument('--topics', nargs='*', type=existing_topic,
                             default=[])


def add(*args):
    usage = 'config_helper.py add [-h] exercise'
    parser = argparse.ArgumentParser(parents=[EXERCISE_PARSER],
                                     usage=usage)
    opts = parser.parse_args(args)
    # For testing purposes
    if QUICK_UUID:
        uuid = 'aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa'
    else:
        uuid = generate_uuid()
    entry = {
        'uuid': uuid,
        'slug': opts.exercise,
        'core': opts.core,
        'unlocked_by': opts.unlocked_by,
        'difficulty': opts.difficulty,
        'topics': opts.topics
    }
    entry = OrderedDict((k, entry[k]) for k in KEYS)
    with open_config() as config:
        if find_exercise(opts.exercise, config=config) is not None:
            msg = 'exercise "{}" already exists!'.format(opts.exercise)
            raise KeyError(msg)
        config['exercises'].append(entry)
    return entry


def edit(*args):
    usage = 'config_helper.py edit [-h] exercise'
    parser = argparse.ArgumentParser(parents=[EXERCISE_PARSER],
                                     usage=usage)
    opts = parser.parse_args(args)
    with open_config() as config:
        entry = find_exercise(opts.exercise, config)
        if entry is None:
            msg = 'exercise "{}" does not exist!'.format(opts.exercise)
            raise KeyError(msg)
        if '--core' in args:
            entry['core'] = opts.core
        if '--unlocked-by' in args:
            entry['unlocked_by'] = opts.unlocked_by
        if '--difficulty' in args:
            entry['difficulty'] = opts.difficulty
        if '--topics' in args:
            entry['topics'] = opts.topics
    return entry


def remove(*args):
    usage = 'config_helper.py remove [-h] exercise'
    parser = argparse.ArgumentParser(parents=[BASE_PARSER],
                                     usage=usage)
    opts = parser.parse_args(args)
    config = load_config()
    for i in range(len(config['exercises'])):
        if config['exercises'][i]['slug'] == opts.exercise:
            del config['exercises'][i]
            save_config(config)
            return
    raise KeyError('exercise "{}" does not exist!'.format(opts.exercise))


def deprecate(*args):
    usage = 'config_helper.py deprecate [-h] exercise'
    parser = argparse.ArgumentParser(parents=[BASE_PARSER],
                                     usage=usage)
    opts = parser.parse_args(args)
    entry = find_exercise(opts.exercise)
    if entry is None:
        raise KeyError('exercise "{}" does not exist!'.format(opts.exercise))
    remove(opts.exercise)
    with open_config() as config:
        entry = {
            'uuid': entry['uuid'],
            'slug': opts.exercise,
            'deprecated': True
        }
        entry = OrderedDict((k, entry[k]) for k in DEPRECATED_KEYS)
        config['exercises'].append(entry)
    return entry


def lint_key(entry, slug, key, line_markers):
    line_no = json_get_line_no(*line_markers)
    if key == 'uuid':
        uuid = entry[key]
        if not valid_uuid(uuid):
            return InvalidKeyValueFormat(slug, key, uuid, line_no)
    elif key == 'slug':
        try:
            valid_exercise(slug).upper()
        except ValueError:
            return InvalidKeyValueFormat(slug, key, slug, line_no)
    elif key in ['core', 'deprecated']:
        value = entry[key]
        if not isinstance(value, bool):
            return InvalidKeyValueFormat(slug, key, value, line_no)
    elif key == 'unlocked_by':
        unlocked_by = entry[key]
        try:
            if unlocked_by is not None:
                valid_exercise(unlocked_by)
                parent = find_exercise(unlocked_by)
                if parent is None:
                    return NonExistentExercise(slug, unlocked_by,
                                               line_no)
        except ValueError:
            return InvalidKeyValueFormat(slug, key, unlocked_by,
                                         line_no)
    elif key == 'difficulty':
        diff = entry[key]
        try:
            difficulty(diff)
        except ValueError:
            return InvalidKeyValueFormat(slug, key, diff, line_no)
    elif key == 'topics':
        if not isinstance(entry[key], list):
            return InvalidKeyValueFormat(slug, key, entry[key],
                                         line_no)
        for topic in entry[key]:
            line_markers.append('"')
            line_no = json_get_line_no(*line_markers)
            try:
                existing_topic(topic)
            except KeyError:
                return NonExistentTopic(slug, topic, line_no)
            except ValueError:
                return InvalidKeyValueFormat(slug, key, topic, line_no)


def lint_exercise(entry, line_markers):
    if 'slug' in entry:
        slug = entry['slug']
    else:
        slug = None
    line_markers.append('{')
    keys = list(entry.keys())
    expected_keys = KEYS
    if 'deprecated' in entry:
        if entry['deprecated'] is not False:
            expected_keys = ['uuid', 'slug', 'deprecated']
    else:
        expected_keys = KEYS
    for i, key in enumerate(expected_keys):
        line_markers.append('"')
        line_no = json_get_line_no(*line_markers)
        if key not in entry:
            return MissingKey(slug, key, line_no)
        line_markers[-1] += key
        if keys[i] != key:
            return IncorrectKeyOrder(slug, key, keys[i], line_no)
        else:
            violation = lint_key(entry, slug, key, line_markers)
            if violation is not None:
                return violation


def lint(*args):
    usage = 'config_helper.py lint [-h] exercise'
    parser = argparse.ArgumentParser(usage=usage)
    parser.parse_args(args)
    config = load_config()
    violations = []
    line_markers = ['"exercises"']
    line_no = json_get_line_no(*line_markers) - 1
    if 'language' not in config:
        violations.append(MissingRootKey('language', line_no))
    elif config['language'] != LANGUAGE:
        violations.append(InvalidRootKeyValue('language', config['language'],
                                              line_no))
    if 'active' not in config:
        violations.append(MissingRootKey('active', line_no))
    elif not isinstance(config['active'], bool):
        violations.append(InvalidRootKeyValue('active', config['active'],
                                              line_no))
    if 'exercises' not in config:
        violations.append(MissingRootKey('exercises', line_no))
    elif not isinstance(config['exercises'], list):
        violations.append(InvalidRootKeyValue('exercises', config['exercises'],
                                              line_no))
    else:
        for entry in config['exercises']:
            violation = lint_exercise(entry, line_markers)
            if violation is not None:
                violations.append(violation)
    line_markers.append(']')
    line_no = json_get_line_no(*line_markers)
    if 'foregone' not in config:
        violations.append(MissingRootKey('foregone', line_no))
    elif not isinstance(config['foregone'], list):
        violations.append(InvalidRootKeyValue('foregone', config['foregone'],
                                              line_no))
    else:
        for exercise in config['foregone']:
            line_markers.append('"')
            line_no = json_get_line_no(*line_markers)
            try:
                valid_exercise(exercise)
            except ValueError:
                violation = InvalidForegoneExercise(exercise, line_no)
                violations.append(violation)
    return violations


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
def stash_config():
    config = load_config()
    yield
    save_config(config)


@contextlib.contextmanager
def blank_config():
    with stash_config():
        save_config()
        yield


@contextlib.contextmanager
def singleton_config(exercise='test-exercise'):
    with blank_config():
        main('add', exercise)
        yield


class ConfigHelperCommandTest(unittest.TestCase):
    def setUp(self):
        self.ctx = stash_config()
        self.ctx.__enter__()
        global QUICK_UUID
        QUICK_UUID = True

    def tearDown(self):
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


class AddTest(ConfigHelperCommandTest):
    def test_requires_exercise(self):
        with stash_config():
            with self.assertExits():
                main('add')

    def test_returns_new_entry(self):
        global QUICK_UUID
        QUICK_UUID = False
        with stash_config():
            exercise = 'test-exercise'
            entry = main('add', exercise)
            self.assert_entry_fields(entry, exercise)
        QUICK_UUID = True

    def test_creates_new_entry_in_config(self):
        with stash_config():
            exercise = 'test-exercise'
            self.assertIsNone(find_exercise(exercise))
            main('add', exercise)
            entry = find_exercise(exercise)
            self.assertIsNotNone(entry)
            self.assert_entry_fields(entry, exercise)

    def test_flag_core(self):
        with stash_config():
            exercise = 'test-exercise'
            self.assertIsNone(find_exercise(exercise))
            entry = main('add', exercise, '--core')
            self.assert_entry_fields(entry, exercise, core=True)

    def test_flag_unlocked_by(self):
        with stash_config():
            unlocked_by = 'parent-exercise'
            exercise = 'test-exercise'
            self.assertIsNone(find_exercise(unlocked_by))
            main('add', unlocked_by)
            self.assertIsNone(find_exercise(exercise))
            entry = main('add', exercise, '--unlocked-by', unlocked_by)
            self.assert_entry_fields(entry, exercise, unlocked_by=unlocked_by)

    def test_flag_difficulty(self):
        with stash_config():
            exercise = 'test-exercise'
            self.assertIsNone(find_exercise(exercise))
            entry = main('add', exercise, '--difficulty', '9')
            self.assert_entry_fields(entry, exercise, difficulty=9)

    def test_flag_topics_single(self):
        with stash_config():
            exercise = 'test-exercise'
            self.assertIsNone(find_exercise(exercise))
            entry = main('add', exercise, '--topics', 'lists')
            self.assert_entry_fields(entry, exercise, topics=['lists'])

    def test_flag_topics_multiple(self):
        with stash_config():
            exercise = 'test-exercise'
            self.assertIsNone(find_exercise(exercise))
            entry = main('add', exercise, '--topics', 'lists', 'trees', 'maps')
            self.assert_entry_fields(entry, exercise,
                                     topics=['lists', 'trees', 'maps'])

    def test_cannot_add_existing_exercise(self):
        with stash_config():
            exercise = 'test-exercise'
            self.assertIsNone(find_exercise(exercise))
            main('add', exercise)
            with self.assertRaises(KeyError):
                main('add', exercise)

    def test_invalid_exercise(self):
        with stash_config():
            exercise = 'Try_me'
            with self.assertExits():
                main('add', exercise)

    def test_invalid_topic(self):
        with stash_config():
            exercise = 'test-exercise'
            with self.assertExits():
                main('add', exercise, '--topics', 'Topic')

    def test_non_existent_topic(self):
        with stash_config():
            exercise = 'test-exercise'
            with self.assertRaises(KeyError):
                main('add', exercise, '--topics', 'topic')


class EditTest(ConfigHelperCommandTest):
    def test_requires_exercise(self):
        with stash_config():
            with self.assertExits():
                main('edit')

    def test_returns_modified_entry(self):
        with stash_config():
            exercise = 'test-exercise'
            before = dict(main('add', exercise))
            after = main('edit', exercise, '--core', '--difficulty', '3')
            self.assert_entry_fields(after, exercise, core=True,
                                     unlocked_by=before['unlocked_by'],
                                     difficulty=3, topics=before['topics'])

    def test_modifies_entry_in_config(self):
        with stash_config():
            exercise = 'test-exercise'
            before = dict(main('add', exercise))
            self.assertIsNotNone(before)
            main('edit', exercise, '--core', '--difficulty', '3')
            after = find_exercise(exercise)
            self.assert_entry_fields(after, exercise, core=True,
                                     unlocked_by=before['unlocked_by'],
                                     difficulty=3, topics=before['topics'])

    def test_flag_core(self):
        with stash_config():
            exercise = 'test-exercise'
            before = dict(main('add', exercise))
            self.assertIs(before['core'], False)
            after = main('edit', exercise, '--core')
            self.assertIs(after['core'], True)

    def test_flag_unlocked_by(self):
        with stash_config():
            parent_name = 'parent-exercise'
            exercise = 'test-exercise'
            main('add', parent_name)
            before = dict(main('add', exercise))
            self.assertIsNone(before['unlocked_by'])
            after = main('edit', exercise, '--unlocked-by', parent_name)
            self.assertNotEqual(before['unlocked_by'], after['unlocked_by'])
            self.assertEqual(after['unlocked_by'], parent_name)

    def test_flag_unlocked_by_null(self):
        with stash_config():
            parent_name = 'parent-exercise'
            exercise = 'test-exercise'
            main('add', parent_name)
            before = dict(main('add', exercise, '--unlocked-by', parent_name))
            self.assertEqual(before['unlocked_by'], parent_name)
            after = main('edit', exercise, '--unlocked-by', 'null')
            self.assertIsNone(after['unlocked_by'])

    def test_flag_difficulty(self):
        with stash_config():
            exercise = 'test-exercise'
            before = dict(main('add', exercise))
            self.assertEqual(before['difficulty'], 1)
            after = main('edit', exercise, '--difficulty', '3')
            self.assertEqual(after['difficulty'], 3)

    def test_flag_topics_single(self):
        with stash_config():
            exercise = 'test-exercise'
            before = dict(main('add', exercise))
            self.assertEqual(before['topics'], [])
            after = main('edit', exercise, '--topics', 'lists')
            self.assertEqual(after['topics'], ['lists'])

    def test_flag_topics_multiple(self):
        with stash_config():
            exercise = 'test-exercise'
            before = dict(main('add', exercise))
            self.assertEqual(before['topics'], [])
            after = main('edit', exercise, '--topics', 'lists', 'maps')
            self.assertEqual(after['topics'], ['lists', 'maps'])

    def test_cannot_edit_non_existent_exercise(self):
        with stash_config():
            exercise = 'test-exercise'
            with self.assertRaises(KeyError):
                main('edit', exercise, '--core')

    def test_invalid_topic(self):
        with stash_config():
            exercise = 'test-exercise'
            main('add', exercise)
            with self.assertExits():
                main('edit', exercise, '--topics', 'Topic')

    def test_non_existent_topic(self):
        with stash_config():
            exercise = 'test-exercise'
            main('add', exercise)
            with self.assertRaises(KeyError):
                main('edit', exercise, '--topics', 'topic')


class RemoveTest(ConfigHelperCommandTest):
    def test_requires_exercise(self):
        with stash_config():
            with self.assertExits():
                main('remove')

    def test_removes_entry_in_config(self):
        with stash_config():
            exercise = 'test-exercise'
            main('add', exercise)
            self.assertIsNotNone(find_exercise(exercise))
            main('remove', exercise)
            self.assertIsNone(find_exercise(exercise))

    def test_cannot_remove_non_existent_exercise(self):
        with stash_config():
            exercise = 'test-exercise'
            self.assertIsNone(find_exercise(exercise))
            with self.assertRaises(KeyError):
                main('remove', exercise)


class DeprecateTest(ConfigHelperCommandTest):
    def test_requires_exercise(self):
        with stash_config():
            with self.assertExits():
                main('deprecate')

    def test_returns_modified_entry(self):
        with stash_config():
            exercise = 'test-exercise'
            entry = main('add', exercise)
            self.assertNotIn('deprecated', entry)
            entry = main('deprecate', exercise)
            self.assertIs(entry['deprecated'], True)

    def test_modifies_entry_in_config(self):
        with stash_config():
            exercise = 'test-exercise'
            entry = main('add', exercise)
            self.assertNotIn('deprecated', entry)
            main('deprecate', exercise)
            entry = find_exercise(exercise)
            self.assertIs(entry['deprecated'], True)

    def test_cannot_deprecate_non_existent_exercise(self):
        with stash_config():
            exercise = 'test-exercise'
            self.assertIsNone(find_exercise(exercise))
            with self.assertRaises(KeyError):
                main('deprecate', exercise)

    def test_removes_unnecessary_keys(self):
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
            self.assertEqual(after['uuid'], entry['uuid'])
            self.assertIs(after['deprecated'], True)


class LintTest(ConfigHelperCommandTest):
    def matchesViolation(self, violation, **kwargs):
        kwargs = dict(kwargs)
        violation_type = type(violation)
        if violation_type == MissingRootKey:
            return violation.key == kwargs['key']
        elif violation_type == InvalidRootKeyValue:
            return (violation.key == kwargs['key'] and
                    violation.value == kwargs['value'])
        elif violation_type == InvalidKeyValueFormat:
            if violation.key == 'slug':
                exercise_key = 'value'
            else:
                exercise_key = 'exercise'
            return (violation.exercise == kwargs[exercise_key] and
                    violation.key == kwargs['key'])
        elif violation_type == MissingKey:
            return ((violation.key == 'slug' or
                     violation.exercise == kwargs['exercise']) and
                    violation.key == kwargs['key'])
        elif violation_type == IncorrectKeyOrder:
            return (violation.exercise == kwargs['exercise'] and
                    violation.expected == kwargs['expected'] and
                    violation.actual == kwargs['actual'])
        elif violation_type == NonExistentExercise:
            return (violation.exercise == kwargs['exercise'] and
                    violation.unlocked_by == kwargs['unlocked_by'])
        elif violation_type == NonExistentTopic:
            return (violation.exercise == kwargs['exercise'] and
                    violation.topic == kwargs['topic'])
        elif violation_type == InvalidForegoneExercise:
            return violation.exercise == kwargs['exercise']
        return False

    def assertViolation(self, violation_type, **kwargs):
        for violation in self.violations(violation_type):
            if violation.code == violation_type.code:
                if self.matchesViolation(violation, **kwargs):
                    return
        fail_msg = 'matching violation of type "{}" not found'
        self.fail(fail_msg.format(violation_type))

    def assertNoViolations(self, violation_type):
        violations = self.violations(violation_type)
        self.assertEqual(violations, [])

    def violations(self, *types):
        return [v for v in main('lint')
                if type(v) in types]


class CH10Test(LintTest):
    def assertMissingRootKey(self, key):
        with blank_config():
            key = 'language'
            with open_config() as config:
                del config[key]
            self.assertViolation(MissingRootKey, key=key)

    def test_no_missing_root_keys(self):
        with blank_config():
            self.assertNoViolations(MissingRootKey)

    def test_missing_root_key_language(self):
        self.assertMissingRootKey('language')

    def test_missing_root_key_active(self):
        self.assertMissingRootKey('active')

    def test_missing_root_key_exercises(self):
        self.assertMissingRootKey('exercises')

    def test_missing_root_key_foregone(self):
        self.assertMissingRootKey('foregone')


class CH20Test(LintTest):
    def assertRootKeyValue(self, key, value, valid=False):
        with blank_config():
            with open_config() as config:
                config[key] = value
            if valid:
                self.assertNoViolations(InvalidRootKeyValue)
            else:
                self.assertViolation(InvalidRootKeyValue,
                                     key=key,
                                     value=value)

    def test_language_valid(self):
        self.assertRootKeyValue('language', LANGUAGE, valid=True)

    def test_language_none(self):
        self.assertRootKeyValue('language', None)

    def test_language_different_language(self):
        self.assertRootKeyValue('language', 'Pseudocode')

    def test_language_lowercase(self):
        self.assertRootKeyValue('language', LANGUAGE.lower())

    def test_language_uppercase(self):
        self.assertRootKeyValue('language', LANGUAGE.upper())

    def test_active_true(self):
        self.assertRootKeyValue('active', True, valid=True)

    def test_active_false(self):
        self.assertRootKeyValue('active', False, valid=True)

    def test_active_none(self):
        self.assertRootKeyValue('active', None)

    def test_active_true_string(self):
        self.assertRootKeyValue('active', 'true')

    def test_active_false_string(self):
        self.assertRootKeyValue('active', 'false')

    def test_active_yes(self):
        self.assertRootKeyValue('active', 'yes')

    def test_active_no(self):
        self.assertRootKeyValue('active', 'no')

    def test_exercises_empty(self):
        self.assertRootKeyValue('exercises', [], valid=True)

    def test_exercises_none(self):
        self.assertRootKeyValue('exercises', None)

    def test_exercises_non_list(self):
        self.assertRootKeyValue('exercises', {})

    def test_foregone_empty(self):
        self.assertRootKeyValue('foregone', [], valid=True)

    def test_foregone_single(self):
        self.assertRootKeyValue('foregone', ['test-exercise'], valid=True)

    def test_foregone_multiple(self):
        foregone = ['parent', 'test-exercise', 'outdated']
        self.assertRootKeyValue('foregone', foregone, valid=True)

    def test_foregone_none(self):
        self.assertRootKeyValue('foregone', None)

    def test_foregone_non_list(self):
        self.assertRootKeyValue('foregone', {})


class CH100Test(LintTest):
    def assertKeyValue(self, key, value, valid=False, deprecate=False):
        exercise = 'test-exercise'
        with singleton_config(exercise):
            if deprecate:
                main('deprecate', exercise)
            with open_config() as config:
                find_exercise(exercise, config)[key] = value
            if valid:
                self.assertNoViolations(InvalidKeyValueFormat)
            else:
                self.assertViolation(InvalidKeyValueFormat,
                                     exercise=exercise,
                                     key=key, value=value)

    def test_uuid_valid(self):
        valid_uuid = generate_uuid()
        self.assertKeyValue('uuid', valid_uuid, valid=True)

    def test_uuid_invalid(self):
        self.assertKeyValue('uuid', 'bad_uuid')

    def test_uuid_legacy(self):
        legacy_uuid = 'aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaaaaaaaa'
        self.assertKeyValue('uuid', legacy_uuid)

    def test_slug_valid(self):
        self.assertKeyValue('slug', 'test-exercise', valid=True)

    def test_slug_uppercase(self):
        self.assertKeyValue('slug', 'TEST-EXERCISE')

    def test_slug_snake_case(self):
        self.assertKeyValue('slug', 'test_exercise')

    def test_slug_numeric(self):
        self.assertKeyValue('slug', '123')

    def test_slug_none(self):
        self.assertKeyValue('slug', None)

    def test_core_true(self):
        self.assertKeyValue('core', True, valid=True)

    def test_core_false(self):
        self.assertKeyValue('core', False, valid=True)

    def test_core_none(self):
        self.assertKeyValue('core', None)

    def test_core_true_string(self):
        self.assertKeyValue('core', 'true')

    def test_core_false_string(self):
        self.assertKeyValue('core', 'false')

    def test_core_yes(self):
        self.assertKeyValue('core', 'yes')

    def test_core_no(self):
        self.assertKeyValue('core', 'no')

    def test_unlocked_by_null(self):
        self.assertKeyValue('unlocked_by', None, valid=True)

    def test_unlocked_by_valid_exercise(self):
        self.assertKeyValue('unlocked_by', 'test-exercise', valid=True)

    def test_unlocked_by_uppercase(self):
        self.assertKeyValue('unlocked_by', 'TEST-EXERCISE')

    def test_unlocked_by_snake_case(self):
        self.assertKeyValue('unlocked_by', 'test_exercise')

    def test_unlocked_by_numeric(self):
        self.assertKeyValue('unlocked_by', '123')

    def test_unlocked_by_none_string(self):
        self.assertKeyValue('unlocked_by', 'NONE')
        self.assertKeyValue('unlocked_by', 'None')

    def test_difficulty(self):
        for i in range(1, 11):
            self.assertKeyValue('difficulty', i, valid=True)

    def test_difficulty_alphanumeric(self):
        self.assertKeyValue('difficulty', '123_abc')

    def test_difficulty_semantic(self):
        self.assertKeyValue('difficulty', 'hard')

    def test_difficulty_too_high(self):
        self.assertKeyValue('difficulty', 11)

    def test_difficulty_too_low(self):
        self.assertKeyValue('difficulty', 0)

    def test_topics_valid_empty(self):
        self.assertKeyValue('topics', [], valid=True)

    def test_topics_valid_single(self):
        self.assertKeyValue('topics', ['lists'], valid=True)

    def test_topics_valid_multiple(self):
        self.assertKeyValue('topics', ['lists', 'maps', 'trees'], valid=True)

    def test_topics_uppercase_non_existent(self):
        self.assertKeyValue('topics', ['TOPIC'])

    def test_topics_uppercase_existing(self):
        self.assertKeyValue('topics', ['LISTS'])

    def test_topics_none(self):
        self.assertKeyValue('topics', None)

    def test_topics_non_list(self):
        self.assertKeyValue('topics', 'lists')

    def test_deprecate_true(self):
        self.assertKeyValue('deprecated', True, valid=True, deprecate=True)

    def test_deprecate_false(self):
        self.assertKeyValue('deprecated', False, valid=True, deprecate=True)

    def test_deprecate_none(self):
        self.assertKeyValue('deprecated', None, deprecate=True)

    def test_deprecate_true_string(self):
        self.assertKeyValue('deprecated', 'true', deprecate=True)

    def test_deprecate_false_string(self):
        self.assertKeyValue('deprecated', 'false', deprecate=True)

    def test_deprecate_yes(self):
        self.assertKeyValue('deprecated', 'yes', deprecate=True)

    def test_deprecate_no(self):
        self.assertKeyValue('deprecated', 'no', deprecate=True)


class CH110Test(LintTest):
    def test_correct_key_order(self):
        exercise = 'test-exercise'
        with singleton_config(exercise):
            self.assertNoViolations(IncorrectKeyOrder)

    def test_bad_key_order(self):
        exercise = 'test-exercise'
        with singleton_config(exercise):
            with open_config() as config:
                entry = config['exercises'][0]
                entry = OrderedDict(reversed([t for t in entry.items()]))
                config['exercises'][0] = entry
            self.assertViolation(IncorrectKeyOrder,
                                 exercise=exercise,
                                 expected=KEYS[0],
                                 actual=list(entry.keys())[0])


class CH120Test(LintTest):
    def test_no_keys_missing(self):
        exercise = 'test-exercise'
        with singleton_config(exercise):
            self.assertNoViolations(MissingKey)

    def test_missing_key(self):
        with blank_config():
            exercise = 'test-exercise'
            with open_config() as config:
                entry = {
                    'slug': exercise
                }
                missing_keys = [k for k in KEYS if k not in entry]
                key = missing_keys[0]
                config['exercises'].append(entry)
            if len(missing_keys) == 1:
                self.assertNoViolations(MissingKey)
            else:
                self.assertViolation(MissingKey, exercise=exercise, key=key)

    def test_missing_key_slug(self):
        exercise = 'test-exercise'
        with singleton_config(exercise):
            with open_config() as config:
                entry = find_exercise(exercise, config)
                key = 'slug'
                del entry[key]
            violations = main('lint')
            self.assertEqual(len(violations), 1)
            self.assertViolation(MissingKey, exercise=exercise, key=key)


class CH201Test(LintTest):
    @contextlib.contextmanager
    def setup_test(self, parent, exists):
        exercise = 'test-exercise'
        with singleton_config(exercise):
            if exists:
                main('add', parent)
            with open_config() as config:
                entry = find_exercise(exercise, config)
                entry['unlocked_by'] = parent
            yield

    def test_existing_exercise(self):
        parent = 'existent'
        with self.setup_test(parent, True):
            self.assertNoViolations(NonExistentExercise)

    def test_non_existent_exercise(self):
        parent = 'non-existent'
        with self.setup_test(parent, False):
            self.assertViolation(NonExistentExercise,
                                 exercise='test-exercise',
                                 unlocked_by=parent)


class CH202Test(LintTest):
    @contextlib.contextmanager
    def setup_test(self, topic):
        exercise = 'test-exercise'
        with singleton_config(exercise):
            with open_config() as config:
                entry = find_exercise(exercise, config)
                entry['topics'].append(topic)
            yield

    def test_existing_topic(self):
        with self.setup_test('lists'):
            self.assertNoViolations(NonExistentTopic)

    def test_non_existent_topic(self):
        topic = 'topic_parsing'
        with self.setup_test(topic):
            self.assertViolation(NonExistentTopic,
                                 exercise='test-exercise',
                                 topic=topic)


class CH300Test(LintTest):
    @contextlib.contextmanager
    def setup_test(self, exercise):
        with blank_config():
            with open_config() as config:
                config['foregone'].append(exercise)
            yield

    def assertInvalidForegoneExercise(self, exercise):
        with self.setup_test(exercise):
            self.assertViolation(InvalidForegoneExercise,
                                 exercise=exercise)

    def test_valid_exercise_name(self):
        with self.setup_test('test-exercise'):
            self.assertNoViolations(InvalidForegoneExercise)

    def test_invalid_exercise_name_uppercase(self):
        self.assertInvalidForegoneExercise('TEST-EXERCISE')

    def test_invalid_exercise_name_numeric(self):
        self.assertInvalidForegoneExercise('123_')

    def test_invalid_exercise_name_none(self):
        self.assertInvalidForegoneExercise(None)
