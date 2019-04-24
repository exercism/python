BLKSZ = 5
ALPHSZ = 26


def modInverse(a, ALPHSZ):
    a = a % ALPHSZ
    for x in range(1, ALPHSZ):
        if ((a * x) % ALPHSZ == 1):
            return x
    return 1


def translate(text, a, b, mode):
    inv = modInverse(a, ALPHSZ)
    if inv == 1:
        raise ValueError("a and alphabet size must be coprime.")

    chars = []
    for c in text:
        if c.isalnum():
            orig = ord(c.lower()) - 97
            if orig < 0:
                chars.append(c)
                continue
            if mode == 0:
                new = (a * orig + b) % ALPHSZ
            elif mode == 1:
                new = (inv * (orig - b)) % ALPHSZ
            chars.append(chr(new + 97))

    return ''.join(chars)


def encode(plain, a, b):
    cipher = translate(plain, a, b, 0)
    return " ".join([cipher[i:i + BLKSZ]
                     for i in range(0, len(cipher), BLKSZ)])


def decode(ciphered, a, b):
    return translate(ciphered, a, b, 1)
