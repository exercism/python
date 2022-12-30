# Performance

In this approach, we'll find out how to most efficiently calculate Collatz Conjecture in Python.

The [approaches page][approaches] lists three approaches to this exercise:

1. [Using recursion][approach-recursion]
2. [Using the ternary operator][approach-ternary-operator]
3. [Using the if/else][approach-if-else]

## Benchmarks

To benchmark the approaches, we wrote a [small benchmark application][benchmark-application] using the [`timeit`][timeit] library.
These test where run in windows 11, using Python 3.11.1.

```
Steps with recursion : 0.00015059998258948326
Steps with ternary : 1.8699909560382366e-05
Steps with if/else : 1.8799910321831703e-05
```

## Conclusion

The fastest approach is the one using the ternary operator or the if/else statement.
The slowest approach is the one using recursion, that is because Python isn't optimized for recursion.

[approaches]: https://exercism.org/tracks/python/exercises/collatz-conjecture/approaches
[approach-if-else]: https://exercism.org/tracks/python/exercises/collatz-conjecture/approaches/if-else
[approach-recursion]: https://exercism.org/tracks/python/exercises/collatz-conjecture/approaches/recursion
[approach-ternary-operator]: https://exercism.org/tracks/python/exercises/collatz-conjecture/approaches/ternary-operator
[benchmark-application]: https://github.com/exercism/python/blob/main/exercises/practice/collatz-conjecture/.articles/performance/code/Benchmark.py
[timeit]: https://docs.python.org/3/library/timeit.html
