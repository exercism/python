from string import maketrans, lowercase, digits, punctuation, whitespace

BLKSZ = 5
trtbl = maketrans(lowercase+digits, "".join(reversed(lowercase))+digits)

def base_trans(text):
    return text.lower().translate(trtbl, punctuation+whitespace)

def encode(plain):
    cipher = base_trans(plain)
    return " ".join([cipher[i:i+BLKSZ] for i in range(0,len(cipher),BLKSZ)])

def decode(ciphered):
    return base_trans(ciphered)