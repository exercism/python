from collections import Counter


def word_count(text):
    def replace_nonalpha(char):
        return char.lower() if char.isalnum() else ' '
    text = ''.join(replace_nonalpha(c) for c in text)
    return Counter(text.split())
