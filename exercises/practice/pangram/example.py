from string import ascii_lowercase


def is_pangram(sentence):
    return all(char in sentence.lower() for char in ascii_lowercase)
