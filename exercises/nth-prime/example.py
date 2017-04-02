from itertools import count
from math import sqrt


def nth_prime(n):
    if n < 1:
        raise ValueError('The parameter `n` has to be a positive number.')

    known = []
    candidates = prime_candidates()

    def is_prime(m):
        sqrt_m = sqrt(m)
        for k in known:
            if k > sqrt_m:
                return True
            elif m % k == 0:
                return False
        return True

    while len(known) < n:
        x = next(candidates)
        if is_prime(x):
            known.append(x)

    return known[n - 1]


def prime_candidates():
    yield 2
    yield 3
    for n in count(6, 6):
        yield n - 1
        yield n + 1
