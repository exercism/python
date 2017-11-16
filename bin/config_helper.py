#!/usr/bin/env python
import argparse
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


OK = 0
RUN_FAIL = 1
INVALID_USAGE = 2
RGX_EXERCISE = r'^[a-z\-]+$'
RGX_SNAKE_CASE = r'^[a-z_]+$'
RGX_UUID = r'^[a-f\d]{8}(-[a-f\d]{4}){3}-[a-f\d]{12}$'


def get_json_line(*patterns):
    with open('config.json', 'r') as f:
        lines = f.readlines()
    line_no = 0
    for pattern in patterns:
        try:
            while not lines[line_no].strip().startswith(pattern):
                line_no += 1
            line_no += 1
        except IndexError:
            return line_no
    return line_no + 1


class StyleViolation(object):
    def __init__(self, code, line_no=-1, msg=None):
        self.code = code
        self.code = code
        self.msg = msg

    def __str__(self):
        msg = 'config.json({}): [CH{}]'.format(self.line_no, self.code)
        if self.msg is not None:
            msg += ' ' + self.msg
        return msg

    def __repr__(self):
        return json.dumps(self.__dict__)


class InvalidKeyValueFormat(StyleViolation):
    code = 100
    msg = {
        'uuid': ('{exercise}.uuid: invalid; please generate '
                 'a new UUID with configlet'),
        'slug': ('{exercise}.slug: expected a string of the '
                 'form "exercise-slug", found "{value}"'),
        'core': '{exercise}.core: expected true or false, found "{value}"',
        'unlocked_by': ('{exercise}.unlocked_by: expected null or a string '
                        'of the form "exercise-slug", found "{value}"'),
        'difficulty': ('{exercise}.difficulty: expected an integer in '
                       'range [1..10], found {value}'),
        'topics': ('{exercise}.topics: expected a string of the form '
                   '"snake_case", found "{value}"')
    }

    def __init__(self, exercise, key, value, line_no):
        self.exercise = exercise
        self.key = key
        self.value = value
        msg = InvalidKeyValueFormat.msg[key].format(exercise=exercise,
                                                    key=key,
                                                    value=value)
        StyleViolation.__init__(self,
                                InvalidKeyValueFormat.code,
                                line_no=line_no,
                                msg=msg)


class IncorrectKeyOrder(StyleViolation):
    code = 110

    def __init__(self, exercise, expected, actual, line_no):
        self.exercise = exercise
        self.expected = expected
        self.actual = actual
        msg = '{}: keys out of order; expected "{}", found "{}"'
        msg = msg.format(exercise, expected, actual)
        StyleViolation.__init__(self,
                                IncorrectKeyOrder.code,
                                line_no=line_no,
                                msg=msg)


class MissingKey(StyleViolation):
    code = 120

    def __init__(self, exercise, key, line_no):
        self.exercise = exercise
        self.key = key
        msg = '{}.{} not found'.format(exercise, key)
        StyleViolation.__init__(self,
                                MissingKey.code,
                                line_no=line_no,
                                msg=msg)


class NonExistentExercise(StyleViolation):
    code = 201

    def __init__(self, exercise, unlocked_by, line_no):
        self.exercise = exercise
        self.unlocked_by = unlocked_by
        msg = '{}.unlocked_by: exercise "{}" not found'
        msg = msg.format(exercise, unlocked_by)
        StyleViolation.__init__(self,
                                NonExistentExercise.code,
                                line_no=line_no,
                                msg=msg)


class NonExistentTopic(StyleViolation):
    code = 202

    def __init__(self, exercise, topic, line_no):
        self.exercise = exercise
        self.topic = topic
        msg = '{}.topics: topic "{}" not found'
        msg = msg.format(exercise, topic)
        StyleViolation.__init__(self,
                                NonExistentTopic.code,
                                line_no=line_no,
                                msg=msg)


def create_blank_config():
    return {
        'language': 'Python',
        'active': True,
        'exercises': [],
        'foregone': []
    }


def load_config():
    with open('config.json', 'r') as f:
        return json.load(f)


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
        with open('config.json', 'r') as f:
            config = json.load(f)
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

EXERCISE_PARSER = argparse.ArgumentParser(parents=[BASE_PARSER])

EXERCISE_PARSER_EXT = argparse.ArgumentParser(parents=[BASE_PARSER])
EXERCISE_PARSER_EXT.add_argument('--core', action='store_true', default=False)
EXERCISE_PARSER_EXT.add_argument('--unlocked-by', dest='unlocked_by',
                                 default=None, type=valid_exercise)
EXERCISE_PARSER_EXT.add_argument('--difficulty', type=difficulty, default=1)
EXERCISE_PARSER_EXT.add_argument('--topics', nargs='*', type=existing_topic,
                                 default=[])


def add(*args):
    opts = EXERCISE_PARSER_EXT.parse_args(args)
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
    with open_config() as config:
        if find_exercise(opts.exercise, config=config) is not None:
            msg = 'exercise "{}" already exists!'.format(opts.exercise)
            raise KeyError(msg)
        config['exercises'].append(entry)
    return entry


def edit(*args):
    # return modified entry
    opts = EXERCISE_PARSER_EXT.parse_args(args)
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
    opts = EXERCISE_PARSER.parse_args(args)
    config = load_config()
    for i in range(len(config['exercises'])):
        if config['exercises'][i]['slug'] == opts.exercise:
            del config['exercises'][i]
            save_config(config)
            return
    raise KeyError('exercise "{}" does not exist!'.format(opts.exercise))


def deprecate(*args):
    opts = EXERCISE_PARSER.parse_args(args)
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
        config['exercises'].append(entry)
    return entry


def lint_exercise(entry, line_markers):
    if 'slug' in entry:
        slug = entry['slug']
    else:
        slug = None
    line_markers.append('{')
    keys = list(entry.keys())
    for i, key in enumerate(KEYS):
        line_markers.append('"')
        line_no = get_json_line(*line_markers)
        if key not in entry:
            return MissingKey(slug, key, line_no)
        line_markers[-1] += key
        if keys[i] != key:
            return IncorrectKeyOrder(slug, key, keys[i], line_no)
        else:
            if key == 'uuid':
                uuid = entry[key]
                if not valid_uuid(uuid):
                    return InvalidKeyValueFormat(slug, key, uuid, line_no)
            elif key == 'slug':
                try:
                    valid_exercise(slug).upper()
                except ValueError:
                    return InvalidKeyValueFormat(slug, key, slug, line_no)
            elif key == 'core':
                core = entry[key]
                if not isinstance(core, bool):
                    return InvalidKeyValueFormat(slug, key, core, line_no)
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
                    line_no = get_json_line(*line_markers)
                    try:
                        existing_topic(topic)
                    except KeyError:
                        return NonExistentTopic(slug, topic, line_no)
                    except ValueError:
                        return InvalidKeyValueFormat(slug, key, topic, line_no)


def lint(*args):
    parser = argparse.ArgumentParser()
    parser.parse_args(args)
    config = load_config()
    if 'language' not in config:
        raise 'TODO: CH11 language missing'
    elif config['language'] != LANGUAGE:
        raise 'TODO: CH21 language incorrect'
    elif 'active' not in config:
        raise 'TODO: CH12 active missing'
    elif not isinstance(config['active'], bool):
        raise 'TODO: CH22 active invalid'
    if 'exercises' not in config:
        raise 'TODO: CH13 exercises missing'
    violations = []
    line_markers = ['exercises']
    for entry in config['exercises']:
        violation = lint_exercise(entry, line_markers)
        if violation is not None:
            violations.append(violation)
    if 'foregone' in config:
        # TODO: lint foregone
        pass
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


class ConfigHelperTest(unittest.TestCase):
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
            with self.assertRaises(KeyError):
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
            with self.assertRaises(KeyError):
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

    def assertViolation(self, violation_type, violation, **kwargs):
        kwargs = dict(kwargs)
        self.assertIsInstance(violation, violation_type)
        self.assertEqual(violation.code, violation_type.code)
        if violation_type == InvalidKeyValueFormat:
            if violation.key == 'slug':
                self.assertEqual(violation.exercise, kwargs['value'])
            else:
                self.assertEqual(violation.exercise, kwargs['exercise'])
            self.assertEqual(violation.key, kwargs['key'])
        elif violation_type == MissingKey:
            if violation.key != 'slug':
                self.assertEqual(violation.exercise, kwargs['exercise'])
            self.assertEqual(violation.key, kwargs['key'])
        elif violation_type == IncorrectKeyOrder:
            self.assertEqual(violation.exercise, kwargs['exercise'])
            self.assertEqual(violation.expected, kwargs['expected'])
            self.assertEqual(violation.actual, kwargs['actual'])
        elif violation_type == NonExistentExercise:
            self.assertEqual(violation.exercise, kwargs['exercise'])
            self.assertEqual(violation.unlocked_by, kwargs['unlocked_by'])
        elif violation_type == NonExistentTopic:
            self.assertEqual(violation.exercise, kwargs['exercise'])
            self.assertEqual(violation.topic, kwargs['topic'])
        
    def assertInvalidKeyValue(self, key, value):
        with blank_config():
            exercise = 'test-exercise'
            entry = main('add', exercise)
            with open_config() as config:
                entry = find_exercise(exercise, config)
                entry[key] = value
            violations = main('lint')
            self.assertEqual(len(violations), 1)
            self.assertViolation(InvalidKeyValueFormat, violations[0],
                                 exercise=exercise, key=key, value=value)

    def test_lint_ch100_invalid_key_value_format_uuid(self):
        self.assertInvalidKeyValue('uuid', 'bad_uuid')
        legacy_uuid = 'aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaaaaaaaa'
        self.assertInvalidKeyValue('uuid', legacy_uuid)

    def test_lint_ch100_invalid_key_value_format_slug(self):
        self.assertInvalidKeyValue('slug', '123_')
        self.assertInvalidKeyValue('slug', None)

    def test_lint_ch100_invalid_key_value_format_core(self):
        self.assertInvalidKeyValue('core', None)
        self.assertInvalidKeyValue('core', 'true')
        self.assertInvalidKeyValue('core', 'false')
        self.assertInvalidKeyValue('core', 'yes')
        self.assertInvalidKeyValue('core', 'no')

    def test_lint_ch100_invalid_key_value_format_unlocked_by(self):
        self.assertInvalidKeyValue('unlocked_by', '123_')
        self.assertInvalidKeyValue('unlocked_by', 'NONE')
        self.assertInvalidKeyValue('unlocked_by', 'None')

    def test_lint_ch100_invalid_key_value_format_difficulty(self):
        self.assertInvalidKeyValue('difficulty', '123_')
        self.assertInvalidKeyValue('difficulty', 'hard')
        self.assertInvalidKeyValue('difficulty', 11)
        self.assertInvalidKeyValue('difficulty', 0)

    def test_lint_ch100_invalid_key_value_format_topics(self):
        self.assertInvalidKeyValue('topics', ['TOPIC'])
        self.assertInvalidKeyValue('topics', ['LISTS'])
        self.assertInvalidKeyValue('topics', None)
        self.assertInvalidKeyValue('topics', 'lists')

    def test_lint_ch110_bad_key_order(self):
        with blank_config():
            exercise = 'test-exercise'
            main('add', exercise)
            with open_config() as config:
                entry = config['exercises'][0]
                entry = dict(reversed([t for t in entry.items()]))
                config['exercises'][0] = entry
            violations = main('lint')
            self.assertEqual(len(violations), 1)
            self.assertViolation(IncorrectKeyOrder, violations[0],
                                 exercise=exercise, expected=KEYS[0],
                                 actual=list(entry.keys())[0])

    def test_lint_ch120_missing_key(self):
        with blank_config():
            exercise = 'test-exercise'
            with open_config() as config:
                entry = {
                    'slug': exercise
                }
                key = [k for k in KEYS if k not in entry][0]
                config['exercises'].append(entry)
            violations = main('lint')
            self.assertEqual(len(violations), 1)
            self.assertViolation(MissingKey, violations[0],
                                 exercise=exercise, key=key)

    def test_lint_ch120_missing_key_slug(self):
        with blank_config():
            exercise = 'test-exercise'
            main('add', exercise)
            with open_config() as config:
                entry = find_exercise(exercise, config)
                key = 'slug'
                del entry[key]
            violations = main('lint')
            self.assertEqual(len(violations), 1)
            self.assertViolation(MissingKey, violations[0],
                                 exercise=exercise, key=key)

    def test_lint_ch201_non_existent_exercise(self):
        with blank_config():
            exercise = 'test-exercise'
            parent = 'non-existent'
            main('add', exercise)
            with open_config() as config:
                entry = find_exercise(exercise, config)
                key = 'unlocked_by'
                entry[key] = parent
            violations = main('lint')
            self.assertEqual(len(violations), 1)
            self.assertViolation(NonExistentExercise, violations[0],
                                 exercise=exercise, unlocked_by=parent)

    def test_lint_ch202_non_existent_topic(self):
        with blank_config():
            exercise = 'test-exercise'
            topic = 'topic_parsing'
            main('add', exercise)
            with open_config() as config:
                entry = find_exercise(exercise, config)
                entry['topics'].append(topic)
            violations = main('lint')
            self.assertEqual(len(violations), 1)
            self.assertViolation(NonExistentTopic, violations[0],
                                 exercise=exercise, topic=topic)
