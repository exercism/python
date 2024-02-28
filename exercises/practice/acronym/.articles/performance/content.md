# Performance

In this article, we'll find out how to most efficiently form an acronym from an input string.

The [approaches page][approaches] lists seven idiomatic approaches to this exercise:


1. [Using a `loop`][approach-loop]
2. [Using a `list-comprehension`][approach-list-comprehension]
3. [Using `functools.reduce()`][approach-functools-reduce]
4. [Using `map()`][approach-map-function]
5. [Using a `generator-expression`][approach-generator-expression]
6. [Using `re.finditer()` with `str.join()`][approach-regex-join]
7. [Using `re.findall()` with `str.join()`][approach-regex-join]
8. [Using `re.sub()`][approach-regex-sub]

We'll include a ninth approach using `re.findall()` with a regex to select the first letters of each word, and `str.join()` to make the acronym.


## Benchmarks

To benchmark these approaches, we wrote a [small benchmarking script][benchmark-application] using the [`timeit`][timeit] module along with the third party libraries [`numbpy`][numpy] and [`pandas`][pandas].

All approaches are `O(n)` - they require (_at minimum_) a loop through the entire input to create results, and the work scales in line with the length of the function input.
That doesn't mean that all of these approaches take the _same amount of run time_.
Despite being `O(n)`, overhead such as number of function calls, module importing/loading, regex backtracking, generator tracking, string concatenation, and `lambda` evaluation can add significant time.
Some of the slowest strategies (_mostly regex solutions_) are _**10x or more times slower**_ than the fastest methods (_straight looping and list-comprehensions_).

Of these variants, the `loop` approach is by far the fastest (and easiest read) for inputs under length 45.
Above length 45, repeated string creation and concatenation via `+` starts to slow things down, and the `list-comprehension` approach becomes more efficient due to its loop optimizations and use of `str.join()`.


At the largest input sizes, `map()` and `generator expressions` become more efficient (_as does `functools.reduce()` for certain inputs_), as they are not saving intermediary results to memory in the same way `list comprehensions` or string concatenation do.

The least efficient and least readable are the regex solutions.
While regex definitely has its place, the lack of readability and significant slowdown in this case become an issue.
Of particular interest is the `re.sub()` vs `re.findall()` (_first letters_) solutions.
Even though the `re.sub()` solution takes only 652 steps in the regex engine, `re.sub()` and its unpacking is slow enough that the 1766 steps for the first letters `re.findall()` solution is faster.



|      **String Length >>>** 	| **13** 	| **14** 	| **19** 	| **20** 	| **25** 	| **30** 	| **35** 	| **39** 	| **42** 	| **45** 	| **60** 	| **63** 	| **74** 	| **150** 	| **210** 	| **360** 	| **400** 	| **2940** 	|
|------------------------------	|:-----------:	|:-----------:	|:-----------:	|:-----------:	|:-----------:	|:-----------:	|:-----------:	|:-----------:	|:-----------:	|:-----------:	|:-----------:	|:-----------:	|:-----------:	|:------------:	|:------------:	|:------------:	|:------------:	|:-------------:	|
| **loop**                     	|   5.79e-07  	|   4.96e-07  	|   6.98e-07  	|   7.41e-07  	|   6.18e-07  	|   7.25e-07  	|   1.03e-06  	|   7.33e-07  	|   1.16e-06  	|   8.71e-07  	|   1.51e-06  	|   1.65e-06  	|   1.83e-06  	|   2.43e-06   	|   4.63e-06   	|   7.76e-06   	|   4.85e-06   	|    5.94e-05   	|
| **list&nbsp;comprehension**       	|   7.28e-07  	|   6.57e-07  	|   8.26e-07  	|   8.62e-07  	|   7.67e-07  	|   8.30e-07  	|   1.08e-06  	|   8.68e-07  	|   1.24e-06  	|   4.00e-07  	|   1.49e-06  	|   1.55e-06  	|   1.76e-06  	|   2.19e-06   	|   4.08e-06   	|   7.21e-06   	|   4.40e-06   	|    5.42e-05   	|
| **functools.reduce()**       	|   7.93e-07  	|   6.65e-07  	|   9.50e-07  	|   2.43e-06  	|   8.19e-07  	|   9.56e-07  	|   1.36e-06  	|   4.12e-07  	|   1.64e-06  	|   1.21e-06  	|   2.03e-06  	|   2.14e-06  	|   2.45e-06  	|   3.15e-06   	|   6.03e-06   	|   1.03e-05   	|   6.19e-06   	|    8.10e-05   	|
| **map()**                   	|   8.05e-07  	|   7.21e-07  	|   9.34e-07  	|   9.46e-07  	|   8.32e-07  	|   9.16e-07  	|   1.23e-06  	|   9.52e-07  	|   1.44e-06  	|   1.14e-06  	|   1.71e-06  	|   1.80e-06  	|   2.00e-06  	|   2.58e-06   	|   4.81e-06   	|   8.02e-06   	|   4.95e-06   	|    5.64e-05   	|
| **generator&nbsp;expression**     	|   8.85e-07  	|   7.90e-07  	|   1.01e-06  	|   1.01e-06  	|   9.26e-07  	|   2.49e-06  	|   1.30e-06  	|   1.06e-06  	|   1.49e-06  	|   1.19e-06  	|   1.81e-06  	|   1.86e-06  	|   2.10e-06  	|   2.67e-06   	|   5.12e-06   	|   8.61e-06   	|   5.12e-06   	|    5.81e-05   	|
| **re.finditer()**            	|   1.05e-06  	|   1.74e-06  	|   2.44e-06  	|   2.40e-06  	|   2.09e-06  	|   2.45e-06  	|   3.28e-06  	|   2.42e-06  	|   8.15e-06  	|   3.12e-06  	|   5.15e-06  	|   5.18e-06  	|   5.94e-06  	|   7.89e-06   	|   1.46e-05   	|   2.35e-05   	|   1.48e-05   	|    1.68e-04   	|
| **regex with str.join()**    	|   1.62e-06  	|   1.42e-06  	|   1.85e-06  	|   1.91e-06  	|   1.66e-06  	|   1.88e-06  	|   2.61e-06  	|   4.41e-06  	|   3.14e-06  	|   2.47e-06  	|   3.92e-06  	|   4.11e-06  	|   4.61e-06  	|   6.24e-06   	|   1.13e-05   	|   1.86e-05   	|   1.19e-05   	|    1.36e-04   	|
| **re.findall() 1st letters** 	|   1.63e-06  	|   1.57e-06  	|   2.04e-06  	|   2.12e-06  	|   2.16e-06  	|   2.50e-06  	|   3.18e-06  	|   2.90e-06  	|   3.73e-06  	|   3.41e-06  	|   4.84e-06  	|   5.22e-06  	|   5.94e-06  	|   1.00e-05   	|   1.54e-05   	|   2.48e-05   	|   2.28e-05   	|    1.95e-04   	|
| **re.sub()**                 	|   2.35e-06  	|   1.10e-06  	|   3.06e-06  	|   2.94e-06  	|   2.51e-06  	|   2.92e-06  	|   4.10e-06  	|   2.91e-06  	|   4.95e-06  	|   3.80e-06  	|   6.48e-06  	|   6.39e-06  	|   6.90e-06  	|   9.29e-06   	|   1.90e-05   	|   2.98e-05   	|   1.83e-05   	|    2.03e-04   	|


Keep in mind that all these approaches are very fast, and that benchmarking at this granularity can be unstable.

Measurements were taken on a 3.1 GHz Quad-Core Intel Core i7 Mac running MacOS Ventura.
Tests used `timeit.Timer.autorange()`, repeated 3 times.
Time is reported in seconds taken per string after calculating the 'best of' time.
The [timeit module][timeit] docs have more details, and [note.nkmk.me][note_nkmk_me] has a nice summary of methods.

[approaches]: https://exercism.org/tracks/python/exercises/acronym/dig_deeper
[approach-functools-reduce]: https://exercism.org/tracks/python/exercises/acronym/approaches/functools-reduce
[approach-generator-expression]: https://exercism.org/tracks/python/exercises/acronym/approaches/generator-expression
[approach-list-comprehension]: https://exercism.org/tracks/python/exercises/acronym/approaches/list-comprehension
[approach-loop]: https://exercism.org/tracks/python/exercises/acronym/approaches/loop
[approach-map-function]: https://exercism.org/tracks/python/exercises/acronym/approaches/map-function
[approach-regex-join]: https://exercism.org/tracks/python/exercises/acronym/approaches/regex-join
[approach-regex-sub]: https://exercism.org/tracks/python/exercises/acronym/approaches/regex-sub
[benchmark-application]: https://github.com/exercism/python/tree/main/exercises/practice/acronym/.articles/performance/code/Benchmark.py
[note_nkmk_me]: https://note.nkmk.me/en/python-timeit-measure/
[numpy]: https://numpy.org/
[pandas]: https://pandas.pydata.org/docs/index.html
[timeit]: https://docs.python.org/3.11/library/timeit.html
