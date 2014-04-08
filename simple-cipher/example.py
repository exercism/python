from string import ascii_lowercase,punctuation,whitespace,digits
from time import time
import random

class Cipher:
    def __init__(self, k=None):
        if k:
            self.key = k.translate(None,punctuation+whitespace+digits).lower()
        else:
            random.seed(time())
            self.key = ''.join(random.choice(ascii_lowercase) for i in range(100))
    
    def base_encode(self, s, shift):
        xkey = self.key*(len(s)//len(self.key)+1)
        return ''.join(shift(c,k) for c,k in zip(s,xkey))
    
    def encode(self, s):
        s = s.translate(None,punctuation+whitespace+digits).lower()
        shift = lambda c,k: chr(((ord(c)+ord(k)-2*ord('a'))\
            % len(ascii_lowercase)) + ord('a'))
        return self.base_encode(s, shift)

    def decode(self, s):
        shift = lambda c,k: chr(((ord(c)-ord(k)+len(ascii_lowercase))\
            % len(ascii_lowercase)) + ord('a'))
        return self.base_encode(s, shift)

class Caesar(Cipher):
    def __init__(self):
        Cipher.__init__(self, 'd')

if __name__ == '__main__':
    print(Caesar().encode('venividivici'))
    print(Caesar().encode('\'Twas the night before Christmas'))