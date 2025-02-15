# Performance

In this article, we'll find out how to most efficiently reverse a string in Python.

The approaches [introduction][introduction] lists six groups of approaches:

1.  [Sequence Slice with Negative Step][approach-sequence-slicing]
2.  [Iteration with String Concatenation][approach-iteration-and-concatenation]
3.  [Reverse Iteration with Range()][approach-backward-iteration-with-range]
4.  [Make a list and Use str.join()][approach-list-and-join]
5.  [Make a list and use list.reverse()][approach-built-in-list-reverse]
6.  [Use the built-in reversed()][approach-built-in-reversed]
7.  Other [interesting approaches][approach-additional-approaches]

For our performance investigations, we will compare the most performant from each group and a seventh approach using [`map()`][map in alternative approaches].

## Benchmarks

To benchmark these functions, we wrote a small [benchmarking script][benchmark script] using the [timeit][timeit] module along with third-party libraries [numpy][numpy] and [pandas][pandas].


The reverse slice is by far the most performant, followed by the built-ins `list.reverse()` and `reversed()`.
Iteration and concatenation is next, due to the CPython string optimization (_see the [iteration and concatenation][approach-iteration-and-concatenation] approach for all the details_), but this approach slows radically for strings longer than 142 characters.


With more than 142 characters, using a list, swapping positions, and joining via `join()` is the most performant method that doesn't use built-ins.
Using `map()` with `join()` was the least performant approach overall.



|             **string length >>>>**       	|     5    	|    11    	|    22    	|    52    	|    66    	|    86    	|    142   	|   1420   	|   14200  	|  142000  	|
|--------------------	|:--------:	|:--------:	|:--------:	|:--------:	|:--------:	|:--------:	|:--------:	|:--------:	|:--------:	|:--------:	|
| reverse slice      	| 1.71e-07 	| 1.73e-07 	| 1.86e-07 	| 2.07e-07 	| 2.19e-07 	| 2.36e-07 	| 3.49e-07 	| 1.51e-06 	| 1.19e-05 	| 1.18e-04 	|
| list reverse       	| 3.29e-07 	| 4.28e-07 	| 5.73e-07 	| 8.92e-07 	| 1.20e-06 	| 1.51e-06 	| 2.34e-06 	| 1.94e-05 	| 1.90e-04 	| 1.91e-03 	|
| reversed builtin   	| 3.68e-07 	| 4.83e-07 	| 6.98e-07 	| 1.20e-06 	| 1.62e-06 	| 2.03e-06 	| 2.71e-06 	| 2.42e-05 	| 2.35e-04 	| 2.36e-03 	|
| iterate & concatenate  	| 4.18e-07 	| 8.10e-07 	| 1.49e-06 	| 3.49e-06 	| 4.35e-06 	| 6.18e-06 	| 4.12e-06 	| 2.03e-04 	| 3.31e-03 	| 4.61e-01 	|
| list swap          	| 6.43e-07 	| 4.00e-07 	| 1.54e-06 	| 3.01e-06 	| 2.06e-06 	| 4.71e-06 	| 7.47e-06 	| 8.97e-05 	| 2.52e-03 	| 1.02e-02 	|
| iterate with range 	| 9.19e-07 	| 1.35e-06 	| 2.12e-06 	| 4.15e-06 	| 5.23e-06 	| 6.60e-06 	| 1.10e-05 	| 1.05e-04 	| 1.02e-03 	| 1.07e-02 	|
| map and join       	| 9.56e-07 	| 1.72e-06 	| 3.08e-06 	| 6.27e-06 	| 7.96e-06 	| 1.03e-05 	| 1.71e-05 	| 1.70e-04 	| 1.68e-03 	| 1.70e-02 	|


Measurements were taken on a  3.1 GHz Quad-Core Intel Core i7 Mac running MacOS Ventura.
Tests used `timeit.Timer.autorange()`, repeated 3 times.
Time is reported in seconds taken per string after calculating the 'best of' time.
The [`timeit`][timeit] module docs have more details, and [note.nkmk.me][note_nkmk_me] has a nice summary of methods.

[approach-additional-approaches]: https://exercism.org/tracks/python/exercises/reverse-string/.approaches/additional-approaches
[approach-backward-iteration-with-range]: https://exercism.org/tracks/python/exercises/reverse-string/.approaches/backward-iteration-with-range
[approach-built-in-list-reverse]: https://exercism.org/tracks/python/exercises/reverse-string/.approaches/built-in-list-reverse
[approach-built-in-reversed]: https://exercism.org/tracks/python/exercises/reverse-string/.approaches/built-in-reversed
[approach-iteration-and-concatenation]: https://exercism.org/tracks/python/exercises/reverse-string/.approaches/iteration-and-concatenation
[approach-list-and-join]: https://exercism.org/tracks/python/exercises/reverse-string/.approaches/list-and-join
[approach-sequence-slicing]: https://exercism.org/tracks/python/exercises/reverse-string/.approaches/sequence-slicing
[introduction]: https://exercism.org/tracks/python/exercises/reverse-string/.approaches/introduction.md
[map in alternative approaches]: .org/tracks/python/exercises/reverse-string/.approaches/additional-approaches#Using-`map()`-and-`lambbda`-with-`Join()`-Instead-of-a-Loop
[numpy]: https://numpy.org/
[pandas]: https://pandas.pydata.org/
[note_nkmk_me]: https://note.nkmk.me/en/python-timeit-measure/
[timeit]: https://docs.python.org/3/library/timeit.html#python-interface
[benchmark script]:   https://exercism.org/tracks/python/exercises/reverse-string/.articles/code/Benchmark.py