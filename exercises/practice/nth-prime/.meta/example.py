from itertools import count
from math import sqrt


def prime(number):
    if number < 1:
        raise ValueError('there is no zeroth prime')

    known = []
    candidates = prime_candidates()

    def is_prime(candidate):
        sqrt_candidate = sqrt(candidate)
        for item in known:
            if item > sqrt_candidate:
                return True
            elif candidate % item == 0:
                return False
        return True

    while len(known) < number:
        next_one = next(candidates)
        if is_prime(next_one):
            known.append(next_one)

    return known[number - 1]


def prime_candidates():
    yield 2
    yield 3
    for number in count(6, 6):
        yield number - 1
        yield number + 1
