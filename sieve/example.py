def sieve(limit):
    primes = [2]
    pRange = list(range(3, limit+1, 2))
    while pRange:
        p = pRange.pop(0)
        pRange = filter(lambda x: x % p, pRange)
        primes.append(p)
    return primes
