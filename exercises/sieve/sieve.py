def sieve(limit):
    isprimes = [True] * (limit+1)
    primes = [2]
    for n in range(3,limit+1,2):
        if isprimes[n] is True:
            primes.append(n)
            for i in range(n*n,limit+1,n):
                isprimes[i] = False
    return primes
