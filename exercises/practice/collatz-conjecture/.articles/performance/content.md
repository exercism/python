# Performance

In this article, we'll find out how to most efficiently calculate the Collatz Conjecture in Python.

The [approaches page][approaches] lists three approaches to this exercise:

1. [Using `recursion`][approach-recursion]
2. [Using the `ternary operator`][approach-ternary-operator]
3. [Using `if`/`else`][approach-if-else]

## Benchmarks

To benchmark the approaches, we wrote a [small benchmark application][benchmark-application] using the [`timeit`][timeit] library.
These tests were conducted on Windows 11, using Python `3.11.1`.

```
Steps with recursion : 4.1499966755509377e-05
Steps with ternary : 2.1900050342082977e-05
Steps with if/else : 2.0900042727589607e-05
```

## Conclusion

The fastest approach is the one using the `if`/`else` statement, followed by the one using the `ternary operator`/`conditional expression`.
The slowest approach is the one using `recursion`, probably due to Python's lack of `tail-call optimization` and  focus on efficient `iteration`.


[approach-if-else]: https://exercism.org/tracks/python/exercises/collatz-conjecture/approaches/if-else
[approach-recursion]: https://exercism.org/tracks/python/exercises/collatz-conjecture/approaches/recursion
[approach-ternary-operator]: https://exercism.org/tracks/python/exercises/collatz-conjecture/approaches/ternary-operator
[approaches]: https://exercism.org/tracks/python/exercises/collatz-conjecture/approaches
[benchmark-application]: https://github.com/exercism/python/blob/main/exercises/practice/collatz-conjecture/.articles/performance/code/Benchmark.py
[timeit]: https://docs.python.org/3/library/timeit.html
