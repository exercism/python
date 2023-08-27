# Tracking
This approach includes building a list of all the previous primes until it reaches the nth number, after which it quits the loop and return the last number in the list.
```python
def prime(number):
    if number == 0:
        raise ValueError('there is no zeroth prime')
    counter = 2
    primes = [2]
    while len(primes) < number: 
        counter += 1
        if all(counter % test != 0 for test in range(2, counter)):
            primes.append(counter)
    return primes[-1]
```
Efficiency can be improved slightly by reducing the factor check to the square root of the number...
```python
...
if all(counter % test != 0 for test in range(2, int(counter ** 0.5) + 1)):
    ...
```
... or even better, checking whether a new number is merely not divisible by any of the primes (in which case it's a prime itself):
```python
...
if all(counter % test != 0 for test in primes):
    ...
```
Instead of building the list, it's more memory efficient to just save the number of primes found until now, and return the currently stored number when the nth prime is found. 
However, this elongates the code.
```python
def prime(number):
    if number == 0:
        raise ValueError('there is no zeroth prime')
    counter = 2
    prime_count = 0
    while True:
        isprime = True
        for test in range(2, int(counter ** 0.5) + 1):
            if counter % test == 0:
                isprime = False
                break
        if isprime:
            prime_count += 1
        if prime_count == number:
            return counter
        counter += 1
```

~~~~exercism/advanced
Tip: you can use `for... else` to make your code more idiomatic here.
```python
...
for test in range(2, int(counter ** 0.5) + 1):
    if counter % test == 0:
        break
else:
    prime_count += 1
if prime_count == number:
    return counter
```
The else block is executed if the `for` loop completes normally - that is, without `break`ing.
Read more on [for/else][for-else]
~~~~


[for-else]: https://book.pythontips.com/en/latest/for_-_else.html