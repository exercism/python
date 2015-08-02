import re

def word_count(text):
    """Return a Counter object that maps from the words contained in
    the phrase to their respective counts
    """
    count = {}
    for w in re.split('\W',re.sub('[^A-Za-z0-9]',' ', text)):
        if w:
            count[w] = count.get(w, 0) + 1
    return count
