from math import sqrt, ceil
try:
    # Python 3
    from math import gcd
except ImportError:
    # Python 2
    from fractions import gcd


def triplets_in_range(start, end):
    for b in range(4, end + 1, 4):
        for x, y, z in primitive_triplets(b):
            a, b, c = (x, y, z)
            while a < start:
                a, b, c = (a + x, b + y, c + z)
            while c <= end:
                yield [a, b, c]
                a, b, c = (a + x, b + y, c + z)


def euclidian_coprimes(limit):
    mn = limit // 2
    for n in range(1, int(ceil(sqrt(mn)))):
        if mn % n == 0:
            m = mn // n
            if (m - n) % 2 == 1 and gcd(m, n) == 1:
                yield m, n


def primitive_triplets(limit):
    """See Euclid's formula
    (https://en.wikipedia.org/wiki/Pythagorean_triple#Generating_a_triple)
    for more information
    """
    for m, n in euclidian_coprimes(limit):
        m2, n2 = m * m, n * n
        a, b, c = m2 - n2, 2 * m * n, m2 + n2
        if a > b:
            a, b = b, a
        yield a, b, c


def triplets_with_sum(number):
    return [
        triplet for triplet
        in triplets_in_range(1, number // 2)
        if sum(triplet) == number
        ]
