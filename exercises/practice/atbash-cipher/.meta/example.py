from string import ascii_lowercase


BLOCK_SIZE = 5
trtbl = str.maketrans(ascii_lowercase, ascii_lowercase[::-1])


def base_trans(text):
    return ''.join([character for character in text if character.isalnum()]).lower().translate(trtbl)


def encode(plain):
    cipher = base_trans(plain)
    return ' '.join(cipher[idx:idx + BLOCK_SIZE]
                     for idx in range(0, len(cipher), BLOCK_SIZE))


def decode(ciphered):
    return base_trans(ciphered)
