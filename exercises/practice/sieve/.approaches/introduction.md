# Introduction

The key to this exercise is to keep track of:
- A list of numbers.
- Their status of possibly being prime.


## General Guidance

To solve this exercise, it is necessary to choose one or more appropriate data structures to store numbers and status, then decide the best way to scan through them.

There are many ways to implement the code, and the three broad approaches listed below are not sharply separated.


## Approach: Using nested loops

```python
def primes(number):
    not_prime = []
    prime = []
    
    for item in range(2, number+1):
        if item not in not_prime:
            prime.append(item) 
            for element in range(item*item, number+1, item):
                not_prime.append(element)
    
    return prime
```

The theme here is nested, explicit `for` loops to move through ranges, testing validity as we go.

For details and another example see [`nested-loops`][approaches-nested].


## Approach: Using set operations

```python
def primes(number):
    not_prime = set()
    primes = []

    for num in range(2, number+1):
        if num not in not_prime:
            primes.append(num)
            not_prime.update(range (num*num, number+1, num))

    return primes
```

In this group, the code uses the special features of the Python [`set`][sets] to improve efficiency.

For details and other examples see [`set-operations`][approaches-sets].


## Approach: Using complex or nested comprehensions


```python
def primes(limit):
    return [number for number in range(2, limit + 1) if 
            all(number % divisor != 0 for divisor in range(2, number))]
```

Here, the emphasis is on implementing a solution in the minimum number of lines, even at the expense of readability or performance.

For details and another example see [`comprehensions`][approaches-comps].


## Using packages outside base Python


In statically typed languages, common approaches include bit arrays and arrays of booleans.

Neither of these is a natural fit for core Python, but there are external packages that could perhaps provide a better implementation:

- For bit arrays, there is the [`bitarray`][bitarray] package and [`bitstring.BitArray()`][bitstring].
- For arrays of booleans, we could use the NumPy package: `np.ones((number,), dtype=np.bool_)` will create a pre-dimensioned array of `True`.

It should be stressed that these will not work in the Exercism test runner, and are mentioned here only for completeness.

## Which Approach to Use?


This exercise is for learning, and is not directly relevant to production code.

The point is to find a solution which is correct, readable, and remains reasonably fast for larger input values.

The "set operations" example above is clean, readable, and in benchmarking was the fastest code tested.

Further details of performance testing are given in the [Performance article][article-performance].

[approaches-nested]: https://exercism.org/tracks/python/exercises/sieve/approaches/nested-loops
[approaches-sets]: https://exercism.org/tracks/python/exercises/sieve/approaches/set-operations
[approaches-comps]: https://exercism.org/tracks/python/exercises/sieve/approaches/comprehensions
[article-performance]:https://exercism.org/tracks/python/exercises/sieve/articles/performance
[sets]: https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset
[bitarray]: https://pypi.org/project/bitarray/
[bitstring]: https://bitstring.readthedocs.io/en/latest/
