def recite(start, take=1):
    results = []
    for idx in range(start, start - take, -1):
        results.extend(verse(idx))
        if idx > start - take + 1:
            results.append('')
    return results


def verse(number):
    return [
        f'{_bottles(number).capitalize()} of beer on the wall, {_bottles(number)} of beer.',
        f'{_action(number)}{_next_bottle(number)}'
    ]


def _action(current_verse):
    if current_verse == 0:
        return 'Go to the store and buy some more, '
    else:
        return f'Take {"one" if current_verse > 1 else "it"} down and pass it around, '


def _next_bottle(current_verse):
    return f'{_bottles(_next_verse(current_verse))} of beer on the wall.'


def _bottles(number):
    if number == 0:
        return 'no more bottles'
    if number == 1:
        return '1 bottle'
    else:
        return f'{number} bottles'


def _next_verse(current_verse):
    return current_verse - 1 if current_verse > 0 else 99
