# Performance

In this article, we'll find out how to most efficiently form an acronym from an input string.

The [approaches page][approaches] lists many idiomatic approaches to this exercise:


1. [Using a `loop`][approach-loop]
2. [Using a `list-comprehension`][approach-list-comprehension]
3. [Using `functools.reduce()`][approach-functools-reduce]
4. [Using `map()`][approach-map-function]
5. [Using a `generator-expression`][approach-generator-expression]
6. [Using `re.finditer()` with `str.join()`][approach-regex-join]
7. [Using `re.findall()` with `str.join()`][approach-regex-join]
8. [Using `re.sub()`][approach-regex-sub]
9. [Using two `generator-expression`s][approach-double-generator-expression] and `str.join()`

We will also include a tenth approach, which is a variant of the `re.findall()` approach. This variant uses a regex to select the _first letters_ of each word, instead of the _entirety_ of each word.

## Benchmarks

To benchmark these approaches, we wrote a [small benchmarking script][benchmark-application] using the [`timeit`][timeit] module along with the third party libraries [`numpy`][numpy] and [`pandas`][pandas].

All approaches are `O(n)` — they require (_at minimum_) a loop through the entire input to create results, and the work scales in line with the length of the function input.
That doesn't mean that all of these approaches take the _same amount of time to run_.
Despite being `O(n)`, overhead such as number of function calls, module importing/loading, regex backtracking, generator tracking, string concatenation, and `lambda` evaluation can add significant time.
Some of the slowest strategies (_mostly regex solutions_) are _**10 (or more) times times slower**_ than the fastest methods (_straight looping and list comprehensions_).

Of these variants, the `loop` approach is by far the fastest (and easiest to read) for inputs under length 45.
Above length 45, repeated string creation and concatenation via `+` starts to slow things down, and the `list-comprehension` approach becomes more efficient due to its loop optimizations and use of `str.join()`.


At the largest input sizes, `map()` and `generator expressions` become more efficient (_as does `functools.reduce()` for certain inputs_), as they are not saving intermediary results to memory in the same way `list comprehensions` or string concatenation do.

The least efficient and least readable are the regex solutions.
While regex definitely has its place, the lack of readability and significant slowdown in this case become an issue.
Of particular interest is the `re.sub()` vs `re.findall()` (_first letters_) solutions.
Even though the `re.sub()` solution takes only 652 steps in the regex engine, `re.sub()` and its unpacking is slow enough that the 1766 steps for the first letters `re.findall()` solution is faster.


| **String Length >>>**                    |   Length: 13 |   Length: 14 |   Length: 19 |   Length: 20 |   Length: 25 |   Length: 30 |   Length: 35 |   Length: 39 |   Length: 42 |   Length: 45 |   Length: 60 |   Length: 63 |   Length: 74 |   Length: 78 |   Length: 93 |   Length: 108 |   Length: 120 |   Length: 140 |   Length: 150 |   Length: 200 |   Length: 210 |   Length: 225 |   Length: 260 |   Length: 310 |   Length: 360 |   Length: 400 |   Length: 2940 |
|:-----------------------------------------|-------------:|-------------:|-------------:|-------------:|-------------:|-------------:|-------------:|-------------:|-------------:|-------------:|-------------:|-------------:|-------------:|-------------:|-------------:|--------------:|--------------:|--------------:|--------------:|--------------:|--------------:|--------------:|--------------:|--------------:|--------------:|--------------:|---------------:|
| loop with str.replace                    |     2.78e-07 |     2.46e-07 |     3.23e-07 |     3.42e-07 |     2.88e-07 |     3.32e-07 |     4.69e-07 |     3.58e-07 |     5.53e-07 |     4.29e-07 |     7.27e-07 |     7.70e-07 |     8.26e-07 |     5.97e-07 |     7.18e-07 |      1.10e-06 |      7.72e-07 |      1.57e-06 |      1.08e-06 |      2.07e-06 |      2.18e-06 |      2.20e-06 |      1.60e-06 |      2.11e-06 |      3.56e-06 |      2.20e-06 |       2.51e-05 |
| list comprehension with str.join()       |     2.92e-07 |     2.67e-07 |     3.24e-07 |     3.47e-07 |     2.99e-07 |     3.29e-07 |     4.59e-07 |     3.57e-07 |     5.28e-07 |     4.31e-07 |     6.35e-07 |     6.65e-07 |     7.50e-07 |     5.58e-07 |     6.62e-07 |      9.84e-07 |      7.28e-07 |      1.34e-06 |      1.06e-06 |      1.76e-06 |      1.85e-06 |      1.96e-06 |      1.44e-06 |      1.85e-06 |      2.97e-06 |      1.99e-06 |       1.95e-05 |
| map() with str.replace()                 |     4.18e-07 |     3.75e-07 |     4.74e-07 |     4.90e-07 |     4.30e-07 |     4.88e-07 |     6.54e-07 |     5.03e-07 |     7.57e-07 |     5.89e-07 |     9.02e-07 |     9.45e-07 |     1.08e-06 |     7.59e-07 |     9.44e-07 |      1.46e-06 |      1.00e-06 |      1.97e-06 |      1.45e-06 |      2.60e-06 |      2.65e-06 |      2.87e-06 |      2.10e-06 |      2.66e-06 |      4.52e-06 |      2.83e-06 |       2.95e-05 |
| functools.reduce() with str.replace()    |     4.35e-07 |     3.63e-07 |     5.07e-07 |     5.28e-07 |     4.41e-07 |     5.17e-07 |     7.63e-07 |     5.42e-07 |     9.34e-07 |     6.90e-07 |     1.14e-06 |     1.18e-06 |     1.40e-06 |     9.33e-07 |     1.18e-06 |      1.95e-06 |      1.23e-06 |      2.66e-06 |      1.85e-06 |      3.49e-06 |      3.56e-06 |      3.95e-06 |      2.72e-06 |      3.58e-06 |      6.15e-06 |      3.74e-06 |       4.30e-05 |
| generator expression with str.join()     |     4.20e-07 |     3.76e-07 |     4.64e-07 |     4.94e-07 |     4.28e-07 |     4.80e-07 |     6.30e-07 |     5.01e-07 |     7.15e-07 |     5.78e-07 |     8.68e-07 |     9.00e-07 |     4.03e-07 |     7.28e-07 |     8.80e-07 |      1.34e-06 |      9.30e-07 |      1.77e-06 |      1.28e-06 |      2.31e-06 |      2.40e-06 |      2.55e-06 |      1.86e-06 |      2.39e-06 |      3.94e-06 |      2.53e-06 |       2.58e-05 |
| regex to clean with str.join()           |     9.28e-07 |     8.42e-07 |     1.06e-06 |     1.08e-06 |     9.72e-07 |     1.09e-06 |     1.42e-06 |     1.09e-06 |     1.68e-06 |     1.37e-06 |     2.07e-06 |     2.10e-06 |     2.29e-06 |     1.72e-06 |     2.11e-06 |      3.12e-06 |      2.13e-06 |      4.06e-06 |      3.05e-06 |      5.24e-06 |      5.37e-06 |      5.76e-06 |      4.19e-06 |      5.50e-06 |      8.69e-06 |      5.64e-06 |       5.67e-05 |
| re.finditer() with str.join()            |     1.12e-06 |     9.80e-07 |     1.28e-06 |     1.30e-06 |     1.14e-06 |     1.29e-06 |     1.72e-06 |     1.29e-06 |     2.09e-06 |     1.67e-06 |     2.53e-06 |     2.64e-06 |     2.92e-06 |     2.12e-06 |     2.59e-06 |      3.89e-06 |      2.61e-06 |      5.08e-06 |      3.69e-06 |      6.80e-06 |      6.93e-06 |      7.34e-06 |      5.19e-06 |      6.76e-06 |      1.09e-05 |      6.81e-06 |       7.67e-05 |
| re.sub() to clean and join               |     1.04e-06 |     8.86e-07 |     1.32e-06 |     1.30e-06 |     1.09e-06 |     1.29e-06 |     1.87e-06 |     1.36e-06 |     2.28e-06 |     1.78e-06 |     3.04e-06 |     3.01e-06 |     3.31e-06 |     2.41e-06 |     3.00e-06 |      4.73e-06 |      3.12e-06 |      6.22e-06 |      4.56e-06 |      9.04e-06 |      9.03e-06 |      9.30e-06 |      6.70e-06 |      8.86e-06 |      1.45e-05 |      9.24e-06 |       9.89e-05 |
| re.findall() 1st letters with str.join() |     1.09e-06 |     1.09e-06 |     1.33e-06 |     1.40e-06 |     1.43e-06 |     1.61e-06 |     1.93e-06 |     1.88e-06 |     2.22e-06 |     2.22e-06 |     2.90e-06 |     3.12e-06 |     3.42e-06 |     3.30e-06 |     3.87e-06 |      4.75e-06 |      4.67e-06 |      6.00e-06 |      6.02e-06 |      8.31e-06 |      9.05e-06 |      9.29e-06 |      9.61e-06 |      1.15e-05 |      1.45e-05 |      1.42e-05 |       1.11e-04 |
| two generator expressions                |     1.14e-06 |     1.12e-06 |     1.47e-06 |     1.49e-06 |     1.79e-06 |     2.09e-06 |     2.48e-06 |     2.54e-06 |     2.90e-06 |     2.85e-06 |     3.87e-06 |     3.92e-06 |     4.79e-06 |     4.88e-06 |     5.81e-06 |      6.92e-06 |      7.14e-06 |      8.99e-06 |      8.80e-06 |      1.24e-05 |      1.26e-05 |      1.41e-05 |      1.53e-05 |      1.83e-05 |      2.21e-05 |      2.25e-05 |       1.65e-04 |


Keep in mind that all these approaches are very fast, and that [benchmarking at this granularity can be unstable, especially on modern CPUs][timeit-issue]. Note that there can also be [bias in benchmarking][biased-benchmarks].

Measurements were taken on an M3 Mac running MacOS Sonoma.
Tests used `timeit.Timer.autorange()`, repeated 3 times.
Time is reported in seconds taken per string after calculating the 'best of' time.
The [timeit module][timeit] docs have more details, and [note.nkmk.me][note_nkmk_me] has a nice summary of methods.

[approaches]: https://exercism.org/tracks/python/exercises/acronym/dig_deeper
[approach-double-generator-expression]: https://exercism.org/tracks/python/exercises/acronym/approaches/double-generator-expression
[approach-functools-reduce]: https://exercism.org/tracks/python/exercises/acronym/approaches/functools-reduce
[approach-generator-expression]: https://exercism.org/tracks/python/exercises/acronym/approaches/generator-expression
[approach-list-comprehension]: https://exercism.org/tracks/python/exercises/acronym/approaches/list-comprehension
[approach-loop]: https://exercism.org/tracks/python/exercises/acronym/approaches/loop
[approach-map-function]: https://exercism.org/tracks/python/exercises/acronym/approaches/map-function
[approach-regex-join]: https://exercism.org/tracks/python/exercises/acronym/approaches/regex-join
[approach-regex-sub]: https://exercism.org/tracks/python/exercises/acronym/approaches/regex-sub
[benchmark-application]: https://github.com/exercism/python/tree/main/exercises/practice/acronym/.articles/performance/code/Benchmark.py
[biased-benchmarks]: https://matthewrocklin.com/blog/work/2017/03/09/biased-benchmarks
[note_nkmk_me]: https://note.nkmk.me/en/python-timeit-measure/
[numpy]: https://numpy.org/
[pandas]: https://pandas.pydata.org/docs/index.html
[timeit]: https://docs.python.org/3.11/library/timeit.html
[timeit-issue]: https://github.com/python/cpython/issues/89424
