import re

from collections import Counter


WORDS = re.compile("[a-zA-Z0-9]+(['][a-z]+)?")


def word_count(text):
    return Counter(word.group(0).lower() for word in WORDS.finditer(text))
