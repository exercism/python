import random


def private_key(prime):
    return random.randint(2, prime - 1)


def public_key(prime_p, prime_g, private_key):
    return pow(prime_g, private_key, prime_p)


def secret(prime, public_key_b, private_key_a):
    return pow(public_key_b, private_key_a, prime)
