# Performance

In this article, we'll examine the performance difference between approaches for `rotational cipher` in Python.

The [approaches page][approaches] lists four approaches to this exercise:

1. [Using recursion][approach-recursion]
2. [Using `str.translate`][approach-str-translate]
3. [Using ascii values][approach-ascii-values]
4. [Using the alphabet][approach-alphabet]

## Benchmarks

To benchmark the approaches, we wrote a [small benchmark application][benchmark-application] using the [`timeit`][timeit] library.
These tests were run in `Windows 11`, using Python `3.11.1`.
Your system results may vary.

```
rotate ascii long : 0.000189200000022538
rotate alphabet long : 0.0002604000037536025
rotate translate long : 1.3999990187585354e-05
rotate recursion long : 0.001309900006162934

rotate ascii short : 4.999994416721165e-06
rotate alphabet short : 3.6999990697950125e-06
rotate translate short : 1.0200004908256233e-05
rotate recursion short : 5.4000120144337416e-06
```

## Conclusion

For a long string as input, the `str.translate` approach is the fastest, followed by ascii, alphabet, and finally recursion.
For a short string as input, is the alphabet approach the fastest, followed by ascii, recursion and finally `str.translate`.

This means that if you know the input is a short string, the fastest approach is to use the alphabet, and forgo the overhead of making and saving a translation dictionary.
On the other hand, if the input is a long string, the overhead of making a dictionary is amortized over the length of the text to be translated, and the fastest approach becomes `str.translate`.

[approach-recursion]: https://exercism.org/tracks/python/exercises/rotational-cipher/approaches/recursion
[approach-str-translate]: https://exercism.org/tracks/python/exercises/rotational-cipher/approaches/str-translate
[approach-ascii-values]: https://exercism.org/tracks/python/exercises/rotational-cipher/approaches/ascii-values
[approach-alphabet]: https://exercism.org/tracks/python/exercises/rotational-cipher/approaches/alphabet
[benchmark-application]: https://github.com/exercism/python/blob/main/exercises/practice/rotational-cipher/.articles/performance/code/Benchmark.py
[timeit]: https://docs.python.org/3/library/timeit.html
