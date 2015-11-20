from collections import Counter


def word_count(text):
    replace_nonalpha = lambda c: c.lower() if c.isalnum() else ' '
    text = ''.join(replace_nonalpha(c) for c in text)
    return Counter(text.split())
