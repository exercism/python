def recite(start, take=1):
    results = []
    for i in range(start, start - take, -1):
        results.extend(verse(i))
        if i > start - take + 1:
            results.append('')
    return results


def verse(number):
    return [
        ''.join([
            "{} of beer on the wall, ".format(_bottles(number).capitalize()),
            "{} of beer.".format(_bottles(number))
        ]),
        ''.join([
            _action(number),
            _next_bottle(number)
        ])
    ]


def _action(current_verse):
    if current_verse == 0:
        return "Go to the store and buy some more, "
    else:
        return "Take {} down and pass it around, ".format(
            "one" if current_verse > 1 else "it",
        )


def _next_bottle(current_verse):
    return "{} of beer on the wall.".format(
        _bottles(_next_verse(current_verse)),
    )


def _bottles(number):
    if number == 0:
        return 'no more bottles'
    if number == 1:
        return '1 bottle'
    else:
        return '{} bottles'.format(number)


def _next_verse(current_verse):
    return current_verse - 1 if current_verse > 0 else 99
