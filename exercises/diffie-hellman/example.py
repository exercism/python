import random


def private_key(p):
    return random.randint(2, p-1)


def public_key(p, g, a):
    return pow(g, a, p)


def secret(p, B, a):
    return pow(B, a, p)
