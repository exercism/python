import re

from collections import Counter


WORDS = re.compile("[a-z0-9]+(['][a-z]+)?")


def word_count(text):
    return Counter(word.group(0) for word in WORDS.finditer(text.lower()))
