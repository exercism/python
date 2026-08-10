# Performance

In this approach, we'll find out how to most efficiently determine if a string is a Pangram in Python.

The [approaches page][approaches] lists three idiomatic approaches to this exercise:

1. [Using `all()` on lowercased letters][approach-all]
2. [Using `set` with `issubset()`][approach-set-issubset]
3. [Using `set` with `len()`][approach-set-len]

For our performance investigation, we'll also include a fourth approach that [uses a bit field to keep track of used letters][approach-bitfield].

## Benchmarks

To benchmark the approaches, we wrote a [small benchmark application][benchmark-application] using the [`timeit`][timeit] library.

```
all:   1.8692991019000146e-05
all:   1.686682232399926e-05  // with sentence.casefold()
set:   2.5181135439997888e-06
len:   5.848111433000668e-06
bit:   1.2118699087000096e-05
```

- The `set` `len()` approach is not as fast as the `set` `issubset()` approach.
- The `all()` approach is significantly slower than either `set` approach (approximately 6-8x slower).
  Using `casefold()` versus `lower()` showed variable performance, with each being faster in different runs.
- Although the bit field approach may be faster in other languages, it is significantly slower in Python.
  It is faster than the `all()` approach, but much slower than either `set` approach.

[benchmark-application]: https://github.com/exercism/python/blob/main/exercises/practice/pangram/.articles/performance/code/Benchmark.py
[timeit]: https://docs.python.org/3/library/timeit.html
[approaches]: https://exercism.org/tracks/python/exercises/pangram/approaches
[approach-all]: https://exercism.org/tracks/python/exercises/pangram/approaches/all
[approach-set-issubset]: https://exercism.org/tracks/python/exercises/pangram/approaches/set-issubset
[approach-set-len]: https://exercism.org/tracks/python/exercises/pangram/approaches/set-len
[approach-bitfield]: https://exercism.org/tracks/python/exercises/pangram/approaches/bitfield
