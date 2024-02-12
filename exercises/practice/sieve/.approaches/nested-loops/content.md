# Nested Loops


```python
def primes(number):
    not_prime = []
    prime = []
    
    for item in range(2, number+1):
        if item not in not_prime:
            prime.append(item) 
            for element in range (item*item, number+1, item):
                not_prime.append(element)
    
    return prime
```

This is the type of code that many people might write as a first attempt.

It is very readable and passes the tests.

The clear disadvantage is that run time is quadratic in the input size: `O(n**2)`, so this approach scales poorly to large input values.

Part of the problem is the line `if item not in not_prime`, where `not-prime` is a list that may be long and unsorted.

This operation requires searching the entire list, so run time is linear in list length: not ideal within a loop repeated many times.

```python
def primes(number):
    number += 1
    prime = [True for item in range(number)]
    for index in range(2, number):
        if not prime[index]:
            continue
        for candidate in range(2 * index, number, index):
            prime[candidate] = False
    return [index for index, value in enumerate(prime) if index > 1 and value]
```


At first sight, this second example looks quite similar to the first.

However, on testing it performs much better, scaling linearly with `number` rather than quadratically.

A key difference is that list entries are tested by index: `if not prime[index]`.

This is a constant-time operation independent of the list length.

Relatively few programmers would have predicted such a major difference just by looking at the code, so if performance matters we should always test, not guess.
