# Comprehensions

```python
def primes(number):
    prime = (item for item in range(2, number+1) 
              if item not in (not_prime for item in range(2, number+1) 
              for not_prime in range(item*item, number+1, item)))
    return list(prime)
```

Many of the solutions to Sieve use `comprehensions` or `generator-expressions` at some point, but this page is about examples that put almost *everything* into a single, elaborate `generator-expression` or `comprehension`.

The above example uses a `generator-expression` to do all the calculation.

There are at least two problems with this:
- Readability is poor.
- Performance is exceptionally bad, making this the slowest solution tested, for all input sizes.

Notice the many `for` clauses in the generator.

This makes the code similar to [nested loops][nested-loops], and run time scales quadratically with the size of `number`.
In fact, when this code is compiled, it _compiles to nested loops_ that have the additional overhead of generator setup and tracking.

```python
def primes(limit):
    return [number for number in range(2, limit + 1)
            if all(number % divisor != 0 for divisor in range(2, number))]
```

This second example using a `list-comprehension` with `all()` is certainly concise and _relatively_ readable, but the performance is again quite poor.

This is not quite a fully nested loop (_there is a short-circuit when `all()` evaluates to `False`_), but it is by no means "performant".
In this case, scaling with input size is intermediate between linear and quadratic, so not quite as bad as the first example.


[nested-loops]: https://exercism.org/tracks/python/exercises/sieve/approaches/nested-loops
