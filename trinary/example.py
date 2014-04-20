from functools import reduce


def trinary(s):
    if set(s) - set('012'):
        return 0
    return reduce(lambda x, y: x * 3 + int(y), s, 0)
