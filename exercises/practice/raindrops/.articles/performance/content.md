# Performance

In this approach, we'll find out how to most efficiently complete the Raindrops exercise.

The [approaches page][approaches] lists seven idiomatic approaches to this exercise:

1. [Using `if` Statements][approach-if-statements]
2. [Using a `loop` and an `f-string`][approach-loop-and-fstring]
3. [Using a `tuple` with `str.join()`][ approach-tuple-with-join ]
4. [Using "Truthy" and "Falsey" Values with an `f-string`][approach-truthy-and-falsey-with-fstring]
5. [Using a `dict` with `str.join()`][ approach-dict-and-join ]
6. [Using `itertools.compress()` with a `list` Mask][approach-itertools-compress]
7. [Using `functools.reduce()` with `zip()`][approach-functools-reduce]


For our performance investigation, we'll also include a final approach that [uses Python 3.10's `structural pattern matching`][approach-spm].


## Benchmarks

To benchmark these approaches, we wrote a [small benchmark application][benchmark-application] using [].
The benchmark checks the various approaches against
Besides the regular CPU-time columns, the amount of memory used was also tracked.

These are the results:





[approach-if-statements]:  https://exercism.org/tracks/python/exercises/raindrops/approaches/if-statements
[approach-loop-and-fstring]: https://exercism.org/tracks/python/exercises/raindrops/approaches/loop-and-fstring
[ approach-tuple-with-join ]:   https://exercism.org/tracks/python/exercises/raindrops/approaches/tuple-with-join
[approach-truthy-and-falsey-with-fstring]:   https://exercism.org/tracks/python/exercises/raindrops/approaches/truthy-and-falsey-with-fstring
[ approach-dict-and-join ]:  https://exercism.org/tracks/python/exercises/raindrops/approaches/dict-and-join
[approach-itertools-compress]:  https://exercism.org/tracks/python/exercises/raindrops/approaches/itertools-compress
[approach-functools-reduce]:  https://exercism.org/tracks/python/exercises/raindrops/approaches/functools-reduce
