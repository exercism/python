# Performance

In this approach, we'll find out how to most efficiently validate a number with the Luhn algorithm.

The [approaches page][approaches] lists two idiomatic approaches to this exercise:

1. [Using `reversed()` with a `for` loop][approach-reversed-for]
2. [Using `replace()`, reverse, `enumerate()`][approach-replace-reverse-enumerate]

For our performance investigation, we'll also include a third approach that [uses recursion][approach-recursion].

## Benchmarks

To benchmark the approaches, we wrote a [small benchmark application][benchmark-application] using the [`timeit`][timeit] library.

```
reversed for:                 1.0783263299963438e-05
replace reverse enumerate:    9.933844099985436e-06
recursion:                    2.4321520800003783e-05
```

At an avergae time per call of `9934` nanoseconds, the `replace()`, reverse, `enumerate()` approach was the fastest.
The `reversed()` with a `for` loop approach was a bit slower, at `10783` nanoseconds.
The recursive approach was much slower, at about `24321` nanoseconds.

[approaches]: https://exercism.org/tracks/python/exercises/luhn/approaches
[approach-reversed-for]:  https://exercism.org/tracks/python/exercises/luhn/approaches/reversed-for
[approach-replace-reverse-enumerate]: https://exercism.org/tracks/python/exercises/luhn/approaches/replace-reverse-enumerate
[approach-recursion]: https://exercism.org/tracks/python/exercises/luhn/approaches/recursion
[benchmark-application]: https://github.com/exercism/python/blob/main/exercises/practice/luhn/.articles/performance/code/Benchmark.py
[timeit]: https://docs.python.org/3/library/timeit.html
