def song(first, last=0):
    verses = ''
    for number in reversed(range(last, first + 1)):
        verses += verse(number) + '\n'

    return verses


def verse(number):
    return ''.join([
        "%s of beer on the wall, " % _bottles(number).capitalize(),
        "%s of beer.\n" % _bottles(number),
        _action(number),
        _next_bottle(number),
    ])


def _action(current_verse):
    if current_verse == 0:
        return "Go to the store and buy some more, "
    else:
        return "Take %s down and pass it around, " % (
            "one" if current_verse > 1 else "it"
        )


def _next_bottle(current_verse):
    return "%s of beer on the wall.\n" % _bottles(_next_verse(current_verse))


def _bottles(number):
    if number == 0:
        return 'no more bottles'
    if number == 1:
        return '1 bottle'
    else:
        return '%d bottles' % number


def _next_verse(current_verse):
    return current_verse - 1 if current_verse > 0 else 99
