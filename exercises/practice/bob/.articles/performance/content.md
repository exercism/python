# Performance

In this approach, we'll find out how to most efficiently determine the response for Bob in Python.

The [approaches page][approaches] lists two idiomatic approaches to this exercise:

1. [Using `if` statements][approach-if].
2. [Using `if` statements nested][approach-if-nested].

For our performance investigation, we'll also include a third approach that [uses an answer list][approach-answer-list].

## Benchmarks

To benchmark the approaches, we wrote a [small benchmark application][benchmark-application] using the [`timeit`][timeit] library.

```
if statements: 2.4691750000056346e-07
if statements nested: 2.3319310000078987e-07
answer list: 2.5469370000064373e-07
```

The nested `if` approach is fastest, but some may consider nested `if` statements a bit less readable than the unnested `if` statements.
The answer list approach is slowest, but some may prefer doing away with the chain of `if` statements.
Since the difference between them is a few nanoseconds, which one is used may be a matter of stylistic preference.

[approaches]: https://exercism.org/tracks/python/exercises/bob/approaches
[approach-if]: https://exercism.org/tracks/python/exercises/bob/approaches/if-statements
[approach-if-nested]: https://exercism.org/tracks/python/exercises/bob/approaches/if-statements-nested
[approach-answer-list]: https://exercism.org/tracks/python/exercises/bob/approaches/answer-list
[benchmark-application]: https://github.com/exercism/python/blob/main/exercises/practice/bob/.articles/performance/code/Benchmark.py
[timeit]: https://docs.python.org/3/library/timeit.html
