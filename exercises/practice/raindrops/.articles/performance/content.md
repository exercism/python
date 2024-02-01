# Performance

In this article, we will find out how to most efficiently complete the Raindrops exercise.

The [introduction page][approaches-intro] lists seven idiomatic approaches to this exercise:

1.  Using [`if` statements and `+`][approach-if-statements] to assemble a return string
2.  Exploiting ["Truthy" and "Falsy" values in ternary checks][approach-truthy-and-falsey-with-fstring] and an `f-string`
3.  Using one or more sequences, a [`loop`, and an `f-string`][approach-loop-and-fstring]
4.  Using one or more [sequences and a `generator-expression` within `join()`][approach-sequence-with-join].
5.  Using a [`dict` of `{factors : sounds}` for lookup and `join()`][approach-dict-and-join]
6.  Using [`itertools.compress()`][approach-itertools-compress]
7.  Using [`functools.reduce()`][approach-functools-reduce]


For our performance investigation, we'll also include an 8th approach that [uses Python 3.10's `structural pattern matching`][PEP0622].


## Benchmarks

To benchmark these functions, we wrote a small [benchmarking script][benchmark-application] using the [timeit][timeit] module along with third-party libraries [numpy][numpy] and [pandas][pandas].


|                             	|    10    	|    14    	|    15    	|    70    	|    105   	|    182   	|    189   	|    203   	|    204   	|    399   	|    409   	|    525   	|    735   	|   1575   	|   3250   	|
|-----------------------------	|:--------:	|:--------:	|:--------:	|:--------:	|:--------:	|:--------:	|:--------:	|:--------:	|:--------:	|:--------:	|:--------:	|:--------:	|:--------:	|:--------:	|:--------:	|
| if&nbsp;statements               	| 2.12e-07 	| 2.16e-07 	| 2.60e-07 	| 2.76e-07 	| 2.98e-07 	| 2.10e-07 	| 2.59e-07 	| 2.15e-07 	| 2.10e-07 	| 2.75e-07 	| 2.61e-07 	| 3.41e-07 	| 2.99e-07 	| 2.98e-07 	| 2.13e-07 	|
| ternary&nbsp;with&nbsp;truthy/falsy   	| 2.65e-07 	| 2.65e-07 	| 2.80e-07 	| 2.70e-07 	| 2.91e-07 	| 2.67e-07 	| 2.73e-07 	| 2.75e-07 	| 2.69e-07 	| 3.56e-07 	| 2.02e-07 	| 3.06e-07 	| 3.06e-07 	| 3.04e-07 	| 2.89e-07 	|
| loop&nbsp;with&nbsp;tuple             	| 4.01e-07 	| 4.09e-07 	| 5.05e-07 	| 4.94e-07 	| 6.48e-07 	| 3.97e-07 	| 5.25e-07 	| 4.10e-07 	| 2.04e-07 	| 5.51e-07 	| 4.06e-07 	| 9.04e-07 	| 6.16e-07 	| 6.89e-07 	| 4.33e-07 	|
| structural&nbsp;pattern&nbsp;matching 	| 7.55e-07 	| 7.31e-07 	| 6.09e-07 	| 5.87e-07 	| 5.21e-07 	| 7.11e-07 	| 6.42e-07 	| 7.19e-07 	| 6.90e-07 	| 6.49e-07 	| 8.43e-07 	| 5.00e-07 	| 5.12e-07 	| 5.21e-07 	| 7.48e-07 	|
| dictionary&nbsp;with&nbsp;join        	| 8.31e-07 	| 8.18e-07 	| 9.34e-07 	| 1.02e-06 	| 9.75e-07 	| 8.55e-07 	| 9.13e-07 	| 8.25e-07 	| 8.32e-07 	| 2.28e-06 	| 9.22e-07 	| 1.05e-06 	| 2.42e-06 	| 9.94e-07 	| 8.46e-07 	|
| sequence&nbsp;with&nbsp;join          	| 8.29e-07 	| 8.17e-07 	| 9.27e-07 	| 9.10e-07 	| 9.62e-07 	| 8.73e-07 	| 9.70e-07 	| 8.87e-07 	| 9.40e-07 	| 2.52e-06 	| 9.74e-07 	| 2.44e-06 	| 2.57e-06 	| 9.79e-07 	| 8.67e-07 	|
| itertools&nbsp;with&nbsp;join         	| 9.46e-07 	| 9.33e-07 	| 4.04e-07 	| 9.88e-07 	| 1.01e-06 	| 9.41e-07 	| 9.91e-07 	| 9.65e-07 	| 9.80e-07 	| 2.51e-06 	| 1.10e-06 	| 2.50e-06 	| 1.02e-06 	| 1.00e-06 	| 9.60e-07 	|
| functools&nbsp;reduce            	| 1.35e-06 	| 1.38e-06 	| 1.41e-06 	| 1.39e-06 	| 1.48e-06 	| 1.33e-06 	| 1.42e-06 	| 1.37e-06 	| 1.34e-06 	| 1.39e-06 	| 1.43e-06 	| 1.45e-06 	| 1.46e-06 	| 1.45e-06 	| 1.37e-06 	|


Keep in mind that all these approaches are _very fast_, and that benchmarking at this granularity can be unstable.
That caveat in mind, the two `if-statement` based approaches benchmark fastest, and the approach using `functools.reduce()` was the slowest.

The 'recommended' approach came in 4th, though it can be argued that the slowdown is justified by the increased readability and maintainability.

Measurements were taken on a  3.1 GHz Quad-Core Intel Core i7 Mac running MacOS Ventura.
Tests used `timeit.Timer.autorange()`, repeated 3 times.
Time is reported in seconds taken per string after calculating the 'best of' time.
The [`timeit`][timeit] module docs have more details, and [note.nkmk.me][note_nkmk_me] has a nice summary of methods.


[PEP0622]: https://peps.python.org/pep-0622/
[approach-dict-and-join ]: https://exercism.org/tracks/python/exercises/raindrops/approaches/dict-and-join
[approach-functools-reduce]:  https://exercism.org/tracks/python/exercises/raindrops/approaches/functools-reduce
[approach-if-statements]:  https://exercism.org/tracks/python/exercises/raindrops/approaches/if-statements
[approach-itertools-compress]:  https://exercism.org/tracks/python/exercises/raindrops/approaches/itertools-compress
[approach-loop-and-fstring]: https://exercism.org/tracks/python/exercises/raindrops/approaches/loop-and-fstring
[approach-sequence-with-join]: https://exercism.org/tracks/python/exercises/raindrops/approaches/sequence-with-join
[approach-truthy-and-falsey-with-fstring]: https://exercism.org/tracks/python/exercises/raindrops/approaches/truthy-and-falsey-with-fstring
[approaches-intro]: https://exercism.org/tracks/python/exercises/raindrops/approaches/introduction.md
[benchmark-application]: https://exercism.org/tracks/python/exercises/raindrops/.articles/code/Benchmark.py
[note_nkmk_me]: https://note.nkmk.me/en/python-timeit-measure/
[numpy]: https://numpy.org/
[pandas]: https://pandas.pydata.org/
[timeit]: https://docs.python.org/3/library/timeit.html#python-interface
