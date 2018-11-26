from math import sqrt, ceil
try:
    # Python 3
    from math import gcd
except ImportError:
    # Python 2
    from fractions import gcd


def triplets_in_range(range_start, range_end):
    result = []
    for b in range(4, range_end + 1, 4):
        for x, y, z in primitive_triplets(b):
            a, b, c = (x, y, z)
            while a < range_start:
                a, b, c = (a + x, b + y, c + z)
            while c <= range_end:
                result.append((a, b, c))
                a, b, c = (a + x, b + y, c + z)
    return result


def primitive_triplets(b):
    """See Euclid's formula
    (https://en.wikipedia.org/wiki/Pythagorean_triple#Generating_a_triple)
    for more information
    """
    # Since b = 2mn, divide out the 2 beforehand
    # b_div_2 = mn
    b_div_2 = b // 2
    sqrt_b_div_2 = sqrt(b_div_2)
    # Since m > n > 0, 1 <= n < ceil(sqrt_b_div_2)
    n_range = range(1, int(ceil(sqrt_b_div_2)))
    return {
        (a, b, c)
        for (a, b), c in (
            # m2 - n2 <> b, so guarantee order by sorting them
            (sorted((m2 - n2, b)), m2 + n2)
            # Square m and n
            for m2, n2 in (
                (m * m, n * n)
                # Get (m, n) pairs
                for m, n in (
                    (b_div_2 // n, n)
                    for n in n_range
                    if b_div_2 % n == 0
                )
                # (m, n) pair is only valid if (m - n) is odd and
                # gcd(m, n) = 1
                if (m - n) % 2 == 1 and gcd(m, n) == 1
            )
        )
    }


def is_triplet(x):
    a, b, c = sorted(x)
    return a * a + b * b == c * c


def triplets_with_sum(triplet_sum):
    # Incidentally, the above algorithm guarantees no duplicates,
    # so converting to a set in not technically required.
    # However, the tests require a set, so use set comprehension anyway.
    return {
        triplet
        for triplet in triplets_in_range(1, triplet_sum // 2)
        if sum(triplet) == triplet_sum
    }
