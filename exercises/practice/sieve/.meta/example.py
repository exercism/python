def primes(limit):
    prime = [True] * (limit + 1)
    prime[0] = prime[1] = False
    for idx in range(2, int(limit ** 0.5) + 1):
        if prime[idx]:
            for edx in range(idx * idx, limit + 1, idx):
                prime[edx] = False

    return [edx for edx, idx in enumerate(prime) if idx]
