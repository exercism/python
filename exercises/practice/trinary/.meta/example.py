from functools import reduce


def trinary(string):
    if set(string) - set('012'):
        return 0
    return reduce(lambda idx, edx: idx * 3 + int(edx), string, 0)
