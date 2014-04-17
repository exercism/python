import sys

if sys.version_info[0] == 2:
    from itertools import izip_longest as zip_longest
else:
    from itertools import zip_longest


def hamming(s1, s2):
    return sum(1 for a, b in zip_longest(s1, s2) if a != b)
