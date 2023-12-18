# Introduction
Nth Prime in Python is a very interesting exercise that can be solved in multiple ways.

## General guidance
Every approach has to a) validate the input, b) calculate the prime numbers until n - 1, and c) return the nth prime number.

As the previous numbers are calculated multiple times, it's advisable to extract that piece of code as a function and use `functools.cache` for greater speeds at higher numbers.

## Approach: Tracking
Using this approach, we manually track the primes/number of primes until the nth prime, after which we quit the loop and return the last number in the list/currently tracked prime.
There are many possible code implementations, such as this one:
```python
def prime(number):
    if number == 0:
        raise ValueError('there is no zeroth prime')
    counter = 2
    primes = [2]
    while len(primes) < number: 
        counter += 1
        if all(counter % test != 0 for test in primes):
            primes.append(counter)
    return primes[-1]
```

If you're interested in learning more about this approach (and discover a lesser known Python feature!), go [here][approach-tracking].

## Approach: Generator Fun
A far more idiomatic approach that utilizes Python's powerful standard library is to use `itertools` and generator expression related functions.

```python
from itertools import islice, count

def is_prime(n):
    return not any(n % k == 0 for k in range(2, int(n ** 0.5) + 1))

def prime(number):
    if number == 0:
        raise ValueError('there is no zeroth prime')
    gen = islice(filter(is_prime, count(2)), number)
    for _ in range(number - 1): next(gen)
    return next(gen)
```
If you'd like to understand this approach better, [read more][approach-generator-fun].

[approach-tracking]: https://exercism.org/tracks/python/exercises/nth-prime/approaches/tracking
[approach-generator-fun]: https://exercism.org/tracks/python/exercises/nth-prime/approaches/generator-fun