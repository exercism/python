from collections import Counter


def word_count(text):
    """Return a Counter object that maps from the words contained in
    the phrase to their respective counts
    """
    return Counter(text.split())
