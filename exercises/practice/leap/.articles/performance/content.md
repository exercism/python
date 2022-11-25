# Performance

In this approach, we'll find out how to most efficiently calculate if a year is a leap year in Python.

The [approaches page][approaches] lists two idiomatic approaches to this exercise:

1. [Using the boolean chain][approach-boolean-chain]
2. [Using the ternary operator][approach-ternary-operator]

For our performance investigation, we'll also include a third approach that [uses datetime addition][approach-datetime-addition].

## Benchmarks

To benchmark the approaches, we wrote a [small benchmark application][benchmark-application] using the [`timeit`][timeit] library.

```
if statements 1900: 1.468243999988772e-07
if statements 2000: 1.3710349999018945e-07
if statements 2019: 8.861289999913425e-08
if statements 2020: 1.21072500012815e-07
ternary 1900:       1.091794999956619e-07
ternary 2000:       1.0275900000124239e-07
ternary 2019:       1.0278620000462979e-07
ternary 2020:       1.0290379999787546e-07
datetime add 2019:  6.689728000201284e-07
```

- The boolean chain is the fastest approach when testing a year that is not evenly divisible by `100` and is not a leap year.
Since most years fit those conditions, it is overall the most efficient approach.
- The ternary operator is faster in benchmarking when the year is a leap year or is evenly divisible by `100`,
but those are the least likely conditions.
- Adding to the `datetime` may not only be a "cheat", but it is slower than the other approaches.

[approaches]: https://exercism.org/tracks/python/exercises/leap/approaches
[approach-boolean-chain]: https://exercism.org/tracks/python/exercises/leap/approaches/boolean-chain
[approach-ternary-operator]: https://exercism.org/tracks/python/exercises/leap/approaches/ternary-operator
[approach-datetime-addition]: https://exercism.org/tracks/python/exercises/leap/approaches/datetime-addition
[benchmark-application]: https://github.com/exercism/python/blob/main/exercises/practice/leap/.articles/performance/code/Benchmark.py
[timeit]: https://docs.python.org/3/library/timeit.html
