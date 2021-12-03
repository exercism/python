BLOCK_SIZE = 5
ALPHABET = 26


def mod_inverse(a_key, alphabet):
    a_key = a_key % alphabet
    for idx in range(1, alphabet):
        if (a_key * idx) % alphabet == 1:
            return idx
    return 1


def translate(text, a_key, b_key, mode):
    inverse = mod_inverse(a_key, ALPHABET)
    if inverse == 1:
        raise ValueError('a and m must be coprime.')

    chars = []
    for character in text:
        if character.isalnum():
            origin = ord(character.lower()) - 97
            if origin < 0:
                chars.append(character)
                continue
            if mode == 0:
                new = (a_key * origin + b_key) % ALPHABET
            elif mode == 1:
                new = (inverse * (origin - b_key)) % ALPHABET
            chars.append(chr(new + 97))

    return ''.join(chars)


def encode(plain, a, b):
    cipher = translate(plain, a, b, 0)
    return ' '.join([cipher[idx:idx + BLOCK_SIZE]
                     for idx in range(0, len(cipher), BLOCK_SIZE)])


def decode(ciphered, a, b):
    return translate(ciphered, a, b, 1)
