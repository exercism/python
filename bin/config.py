#!/usr/bin/env python
from inspect import currentframe
import json
import re
import subprocess
import sys

FILENAME = 'config.py'

USAGE = FILENAME + ' <a[dd]|e[dit]|r[emove]|deprecate|lint> <exercise-slug>'

DEFAULT_TEMPLATE = [
    'core',
    'difficulty',
    'slug',
    'topics',
    'unlocked_by',
    'uuid'
]


def abort(msg, line=None, code=1):
    if line is None:
        line = currentframe().f_back.f_lineno
    print('{} (L{}): {}'.format(FILENAME, line, msg))
    sys.exit(code)


def get_json_line(*patterns):
    with open('config.json', 'r') as f:
        lines = f.readlines()
    line_no = 0
    for pattern in patterns:
        while not lines[line_no].strip().startswith(pattern):
            line_no += 1
    return line_no + 1


def get_or_default(_dict, key, default=None):
    if _dict is None:
        return default
    try:
        return _dict[key]
    except KeyError:
        return default


def get_exercise_index(exercises, key):
    for i in range(len(exercises)):
        if key(exercises[i]):
            return i
    return -1


def edit_exercise(slug, exercise=None, template=DEFAULT_TEMPLATE):
    results = {}
    if slug is None:
        slug = input('exercise slug: ')
        if slug == '':
            return None
    for k in template:
        current = get_or_default(exercise, k)
        if k == 'uuid':
            if exercise is None:
                print('Generating uuid...')
                results[k] = subprocess.check_output('configlet uuid')
                results[k] = results[k].decode().strip()
            else:
                results[k] = current
            print('uuid ({})'.format(results[k]))
        elif k == 'slug':
            results[k] = slug
            print('slug ({})'.format(slug))
        else:
            result = input('{} ({}): '.format(k, current))
            if result == 'null':
                result = None
            elif result == '':
                result = current
            else:
                result = eval(result)
            results[k] = result
    return results


def main(command, slug=None, *args):
    with open('config.json', 'r') as f:
        config_data = json.load(f)

    try:
        template = list(config_data['exercises'][0].keys())
    except IndexError:
        template = DEFAULT_TEMPLATE

    def get_current_exercise(exercise):
        return get_or_default(exercise, 'slug') == slug

    def get_deprecated_exercise(exercise):
        return get_or_default(exercise, 'deprecated', False)

    current_index = get_exercise_index(config_data['exercises'],
                                       get_current_exercise)
    deprecated_index = get_exercise_index(config_data['exercises'],
                                          get_deprecated_exercise)
    if command in ['a', 'add']:
        if current_index >= 0:
            print('exercise \'{}\' already exists!'.format(slug))
            sys.exit(1)
        exercise = edit_exercise(slug, template=template)
        config_data['exercises'].insert(deprecated_index, exercise)

    elif command in ['e', 'edit']:
        if current_index < 0:
            print('exercise \'{}\' not found!'.format(slug))
            sys.exit(1)
        current = config_data['exercises'][current_index]
        edited = edit_exercise(slug, current, template)
        config_data['exercises'][current_index] = edited

    elif command in ['r', 'remove']:
        if current_index < 0:
            print('exercise \'{}\' not found!'.format(slug))
            sys.exit(1)
        del config_data['exercises'][current_index]

    elif command == 'deprecate':
        if current_index < 0:
            print('exercise \'{}\' not found!'.format(slug))
            sys.exit(1)
        current = config_data['exercises'][current_index]
        del config_data['exercises'][current_index]
        for k in list(current.keys()):
            if k not in ['uuid', 'slug']:
                del current[k]
        current['deprecated'] = True
        config_data['exercises'].append(current)

    elif command == 'lint':
        rgxSnakeCase = re.compile(r'^[a-z_]+$')
        last_slug = None
        for entry in config_data['exercises'][:deprecated_index]:
            if 'slug' not in entry:
                if last_slug is None:
                    abort('first entry missing field "slug"')
                else:
                    fmt = 'entry after "{}" missing field "slug"'
                    abort(fmt.format(last_slug))
            slug = entry['slug']
            for i, key in enumerate(entry.keys()):
                expected = template[i]
                if key != expected:
                    fmt = '{}: Unknown or out-of-order key "{}"; expected "{}"'
                    if last_slug is None:
                        patterns = ['"{}"'.format(key)]
                    else:
                        patterns = ['"slug": "{}"'.format(last_slug),
                                    '}',
                                    '"{}"'.format(key)]
                    line_no = get_json_line(*patterns)
                    abort(fmt.format(slug, key, expected), line=line_no)
                if key == 'topics':
                    for topic in entry[key]:
                        if not rgxSnakeCase.search(topic):
                            fmt = '{}: topic "{}" not in snake_case format'
                            patterns = ['"slug": "{}"'.format(slug),
                                        '"topics":',
                                        '"{}"'.format(topic)]
                            line_no = get_json_line(*patterns)
                            abort(fmt.format(slug, topic), line=line_no)
            last_slug = slug
        return 0

    else:
        print(USAGE)
        sys.exit(1)

    with open('config.json', 'w') as f:
        f.write(json.dumps(config_data, indent=2))

    return 0


if __name__ == '__main__':
    sys.exit(main(*sys.argv[1:]))
