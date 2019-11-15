from string import ascii_lowercase
from time import time
import random
from itertools import cycle


class Cipher:

    def __init__(self, key=None):
        if key is None:
            random.seed(time())
            key = ''.join(random.choice(ascii_lowercase) for i in range(100))
        self.key = key

    def encode(self, text):
        return ''.join(
            chr(((ord(c) - 2 * ord('a') + ord(k)) % 26) + ord('a'))
            for c, k in zip(text, cycle(self.key))
        )

    def decode(self, text):
        return ''.join(
            chr(((ord(c) - ord(k) + 26) % 26) + ord('a'))
            for c, k in zip(text, cycle(self.key))
        )
