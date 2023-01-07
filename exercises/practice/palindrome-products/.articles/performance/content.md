# Performance

In this article, we'll examine the performance difference between approaches for `palindrome-products` in Python.

The [approaches page][approaches] lists two approaches to this exercise:

1. [Using a nested for loop][approach-nested-for-loop]
2. [Using a nested for loop, optimized edition][approach-nested-for-loop-optimized]

## Benchmarks

To benchmark the approaches, we wrote a [small benchmark application][benchmark-application] using the [`timeit`][timeit] library.
These tests were run in windows 11, using Python 3.11.1.
Your system results may vary.

```
largest, min=1, max=1000 : 0.05235219991300255
largest_optimized, min=1, max=1000 : 0.000758000067435205
smallest, min=1, max=1000 : 0.04553140001371503
smallest_optimized, min=1, max=1000 : 0.00010269996710121632

largest, min=100, max=100000 : 512.5731259000022
largest_optimized, min=100, max=100000 : 0.013197900028899312
smallest, min=100, max=100000 : 549.5989698000485
smallest_optimized, min=100, max=100000 : 0.03933039994444698
```

## Conclusion

As we can see, the optimized approach is much faster than the original approach.
Although the difference becomes most noticeable when the range is large, the optimized approach is still faster in the small range.

[approaches]: https://exercism.org/tracks/python/exercises/palindrome-products/approaches
[approach-nested-for-loop]: https://exercism.org/tracks/python/exercises/palindrome-products/approaches/nested-for-loop
[approach-nested-for-loop-optimized]: https://exercism.org/tracks/python/exercises/palindrome-products/approaches/nested-for-loop-optimized
[benchmark-application]: https://github.com/exercism/python/blob/main/exercises/practice/palindrome-products/.articles/performance/code/Benchmark.py
[timeit]: https://docs.python.org/3/library/timeit.html
