def sieve(limit):
    primes = []

    sv = [True] * limit
    sv[:2] = [False, False]     # 0 and 1 aren't prime

    for n in range(limit):
        if sv[n]:  # n is prime
            for i in range(n * 2, limit, n):    # mark all multiples of n
                sv[i] = False
            primes.append(n)

    return primes
