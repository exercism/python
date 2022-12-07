# Performance

In this approach, we'll find out how to most efficiently calculate the RNA Transcription.

The [approaches page][approaches] lists two idiomatic approaches to this exercise:

1. [Using `translate()` with `maketrans()` approach][approach-translate-maketrans]
2. [Using dictionary look-up with `join()` approach][approach-dictionary-join]


## Benchmarks

To benchmark the approaches, we wrote a [small benchmark application][benchmark-application] using the [`timeit`][timeit] library.

```
translate maketrans: 2.502872000914067e-07
dictionary join:     1.0920033999718725e-06
```

At about `250` nanoseconds, the `translate()` with `maketrans()` approach is more than four times faster than the dictionary with `join()` approach,
which takes about `1092` nanoseconds.

[approaches]: https://exercism.org/tracks/python/exercises/rna-transcription/approaches
[approach-translate-maketrans]: https://exercism.org/tracks/python/exercises/rna-transcription/approaches/translate-maketrans
[approach-dictionary-join]: https://exercism.org/tracks/python/exercises/rna-transcription/approaches/dictionary-join
[benchmark-application]: https://github.com/exercism/python/blob/main/exercises/practice/rna-transcription/.articles/performance/code/Benchmark.py
[timeit]: https://docs.python.org/3/library/timeit.html
