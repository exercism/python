# Performance

In this approach, we'll find out how to most efficiently determine if a string is an Isogram in Python.

The [approaches page][approaches] lists four idiomatic approaches to this exercise:

1. [Using a list comprehension and `set`][approach-scrub-comprehension]
2. [Using `replace` and `set`][approach-scrub-replace]
3. [Using a `re.sub` and `set`][approach-scrub-regex]
4. [Using a `re.findall` and `set`][approach-findall-regex]

For our performance investigation, we'll also include a fifth approach that [uses a bit field to keep track of used letters][approach-bitfield].

## Benchmarks

To benchmark the approaches, we wrote a [small benchmark application][benchmark-application] using the [`timeit`][timeit] library.

```
scrubbed comprehension: 3.118929599993862e-06
scrubbed replace:       9.586393000063253e-07
scrubbed regex:         1.8171838999987813e-06
findall regex:          4.059006099996623e-06
bitfield:               5.4183307999919636e-06
```

The four fastest approaches use `set`.

- Calling a series of `replace` methods to scrub the input was the fastest approach at about 959 nanoseconds.
- Next fastest was using `re.sub` to scrub the input, at about 1817 nanoseconds.
- Third fastest was using a list comprehension to scrub the input, at about 3119 nanoseconds.
- Using `re.findall` to scrub the input was fourth fastest, at about 4059 nanoseconds.
- Although the bit field approach may be faster in other languages, it is significantly slower in Python.
It was slower than all of the `set` approaches, at about 5418 nanoseconds.

[approaches]: https://exercism.org/tracks/python/exercises/isogram/approaches
[approach-scrub-comprehension]: https://exercism.org/tracks/python/exercises/isogram/approaches/scrub-comprehension
[approach-scrub-replace]: https://exercism.org/tracks/python/exercises/isogram/approaches/scrub-replace
[approach-scrub-regex]: https://exercism.org/tracks/python/exercises/isogram/approaches/scrub-regex
[approach-findall-regex]: https://exercism.org/tracks/python/exercises/isogram/approaches/findall-regex
[approach-bitfield]: https://exercism.org/tracks/python/exercises/isogram/approaches/bitfield
[benchmark-application]: https://github.com/exercism/python/blob/main/exercises/practice/isogram/.articles/performance/code/Benchmark.py
[timeit]: https://docs.python.org/3/library/timeit.html
