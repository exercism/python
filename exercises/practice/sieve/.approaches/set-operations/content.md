# Set Operations


```python
def primes(number):
    not_prime = set()
    primes = []

    for num in range(2, number+1):
        if num not in not_prime:
            primes.append(num)
            not_prime.update(range(num*num, number+1, num))

    return primes
```


This is the fastest method so far tested, at all input sizes.

With only a single loop, performance scales linearly: `O(n)`.

A key step is the set `update()`.

Less commonly seen than `add()`, which takes single element, `update()` takes any iterator of hashable values as its parameter and efficiently adds all the elements in a single operation.

In this case, the iterator is a range resolving to all multiples, up to the limit, of the prime we just found.

Primes are collected in a list, in ascending order, so there is no need for a separate sort operation at the end.


```python
def primes(number):
    numbers = set(item for item in range(2, number+1))
    
    not_prime = set(not_prime for item in range(2, number+1)
                    for not_prime in range(item**2, number+1, item))
    
    return  sorted(list((numbers - not_prime)))
```

After a set comprehension in place of an explicit loop, the second example uses set-subtraction as a key feature in the return statement. 

The resulting set needs to be converted to a list then sorted, which adds some overhead, [scaling as O(n *log* n)][sort-performance].

In performance testing, this code is about 4x slower than the first example, but still scales as `O(n)`.


```python
def primes(number: int) -> list[int]:
    start = set(range(2, number + 1))
    return sorted(start - {m for n in start for m in range(2 * n, number + 1, n)})
```

The third example is quite similar to the second, just moving the comprehension into the return statement.

Performance is very similar between examples 2 and 3 at all input values.


## Sets: strengths and weaknesses

Sets offer two main benefits which can be useful in this exercise:
- Entries are guaranteed to be unique.
- Determining whether the set contains a given value is a fast, constant-time operation.

Less positively:
- The exercise specification requires a list to be returned, which may involve a conversion.
- Sets have no guaranteed ordering, so two of the above examples incur the time penalty of sorting a list at the end.

[sort-performance]: https://en.wikipedia.org/wiki/Timsort
