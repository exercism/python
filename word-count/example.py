from collections import Counter
import re


WORD_RE = re.compile(r'\w+')


def word_count(text):
    """Return a Counter object that maps from the words contained in
    the phrase to their respective counts
    """
    return Counter(_words(text))


def _words(text):
    """Yield all the words, i.e. alphanumeric sequences, in the text """
    return (match.group() for match in WORD_RE.finditer(text.lower()))
