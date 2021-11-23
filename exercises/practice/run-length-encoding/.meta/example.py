from itertools import groupby
from re import sub


def decode(string):
    return sub(r'(\d+)(\D)', lambda main: main.group(2) * int(main.group(1)), string)


def encode(string):
    def single_helper(key, group):
        size = len(list(group))
        return key if size == 1 else str(size) + key
    return ''.join(single_helper(key, group) for key, group in groupby(string))
