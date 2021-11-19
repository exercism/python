from math import ceil, sqrt
from itertools import zip_longest


def cipher_text(plain_text):
    plain_text = _cleanse(plain_text)
    square_size = int(ceil(sqrt(len(plain_text))))
    square = _chunks_of(plain_text, square_size)
    return ' '.join([''.join(column)
                     for column in zip_longest(*square, fillvalue=' ')])


def _cleanse(text):
    """Lowercase a string and remove punctuation and whitespace
    """
    return ''.join([character for character in text
                    if character.isalnum()]).lower()


def _chunks_of(text, num):
    if len(text) <= num:
        return [text]
    return [text[:num]] + _chunks_of(text[num:], num)
