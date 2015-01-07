def sieve(limit):
    primes = []

    sv = [True] * (limit + 1)
    sv[:2] = [False, False]     # 0 and 1 aren't prime

    for n in range(limit + 1):
        if sv[n]:  # n is prime
            for i in range(n * 2, limit + 1, n):    # mark all multiples of n
                sv[i] = False
            primes.append(n)

    return primes
