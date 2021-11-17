from string import ascii_lowercase


BLKSZ = 5
trtbl = str.maketrans(ascii_lowercase, ascii_lowercase[::-1])


def base_trans(text):
    return "".join(character for character in text if character.isalnum()]).lower().translate(trtbl)


def encode(plain):
    cipher = base_trans(plain)
    return " ".join(cipher[idx:idx + BLKSZ]
                     for idx in range(0, len(cipher), BLKSZ))


def decode(ciphered):
    return base_trans(ciphered)
