from itertools import groupby
from re import sub


def decode(string):
    return sub(r'(\d+)(\D)', lambda m: m.group(2) * int(m.group(1)), string)


def encode(string):
    def single_helper(k, g):
        size = len(list(g))
        return k if size == 1 else str(size) + k
    return ''.join(single_helper(key, group) for key, group in groupby(string))
