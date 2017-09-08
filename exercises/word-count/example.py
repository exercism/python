from collections import Counter
import re

regex = r"'([\w]+)?'|\s?([\w']+)\s?"


def word_count(text):
    words = [match_and_lower(match) for match in re.finditer(regex, text)]
    return Counter(words)


def match_and_lower(match):
    return (match.group(2) or match.group(1)).lower()
