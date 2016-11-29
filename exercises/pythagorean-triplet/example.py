from itertools import product
from functools import reduce
from operator import mul
from math import sqrt


def primitive_triplets(nbr):
    if nbr % 4 != 0:
        raise ValueError('Argument must be divisible by 4')
    prime_factors, powers = factor(nbr / 2)
    args = [(1, prime_factors[i1] ** powers[i1]) for i1 in range(len(powers))]
    a = [reduce(mul, p) for p in product(*args)]
    a.sort()
    factors = [(m, n) for m, n in zip(reversed(a), a) if m > n]
    ts = set()
    for m, n in factors:
        ts.update([tuple(sorted([nbr, m * m - n * n, m * m + n * n]))])
    return ts


def is_triplet(t):
    t = list(t)
    t.sort()
    a, b, c = t
    return c * c == a * a + b * b


def triplets_in_range(m, n):
    t = set()
    for a in range(m, n + 1):
        for b in range(a + 1, n + 1):
            c = int(sqrt(a * a + b * b) + 0.5)
            if c * c == a * a + b * b and c >= m and c <= n:
                t.update([(a, b, c)])
    return t


primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61,
          67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137,
          139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211,
          223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283,
          293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379,
          383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461,
          463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563,
          569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643,
          647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739,
          743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829,
          839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937,
          941, 947, 953, 967, 971, 977, 983, 991, 997]


def factor(n):
    global primes
    if n == 1:
        return (1,), (0,)
    factors = []
    powers = []
    idx = 0
    while n > 1:
        prime = primes[idx]
        idx += 1
        if n % prime != 0:
            continue
        factors.append(prime)
        p = 0
        while n % prime == 0:
            p += 1
            n /= prime
        powers.append(p)
    return factors, powers
