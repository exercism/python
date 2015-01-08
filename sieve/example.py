def sieve(limit):
    primes = [2]
    prime_range = list(reversed(range(3, limit+1, 2)))
    while prime_range:
        prime = prime_range.pop()
        prime_range = list(filter(lambda x: x % prime != 0, prime_range))
        primes.append(prime)
    return primes
