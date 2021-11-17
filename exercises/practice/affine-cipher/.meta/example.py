BLOCK_SIZE = 5
ALPHABET = 26


def mod_inverse(a, alphabet):
    a = a % alphabet
    for idx in range(1, alphabet):
        if (a * idx) % alphabet == 1:
            return idx
    return 1


def translate(text, a, b, mode):
    inv = mod_inverse(a, ALPHABET)
    if inv == 1:
        raise ValueError("a and m must be coprime.")

    chars = []
    for c in text:
        if c.isalnum():
            orig = ord(c.lower()) - 97
            if orig < 0:
                chars.append(c)
                continue
            if mode == 0:
                new = (a * orig + b) % ALPHABET
            elif mode == 1:
                new = (inv * (orig - b)) % ALPHABET
            chars.append(chr(new + 97))

    return "".join(chars)


def encode(plain, a, b):
    cipher = translate(plain, a, b, 0)
    return " ".join([cipher[idx:idx + BLOCK_SIZE]
                     for idx in range(0, len(cipher), BLOCK_SIZE)])


def decode(ciphered, a, b):
    return translate(ciphered, a, b, 1)

print(mod_inverse(5, ALPHABET))
