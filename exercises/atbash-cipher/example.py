from string import ascii_lowercase
import sys

if sys.version_info[0] == 2:
    from string import maketrans
else:
    maketrans = str.maketrans


BLKSZ = 5
trtbl = maketrans(ascii_lowercase, ascii_lowercase[::-1])


def base_trans(text):
    return ''.join([c for c in text if c.isalnum()]).lower().translate(trtbl)


def encode(plain):
    cipher = base_trans(plain)
    return " ".join([cipher[i:i + BLKSZ]
                     for i in range(0, len(cipher), BLKSZ)])


def decode(ciphered):
    return base_trans(ciphered)
