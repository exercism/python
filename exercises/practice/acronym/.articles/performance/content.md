# Performance

In this approach, we'll find out how to most efficiently form an acronym from an input string.

The [approaches page][approaches] lists seven idiomatic approaches to this exercise:

1. [Using a `list-comprehension`][approach-list-comprehension]
2. [Using a `loop`][approach-loop]
3. [Using `functools.reduce()`][approach-functools-reduce]
4. [Using `map()`][approach-map-function]
5. [Using a `generator-expression`][approach-generator-expression]
6. [Using a `regex` with `str.join()`][approach-regex-join]
7. [Using `re.sub()`][approach-regex-sub]


## Benchmarks

To benchmark these approaches, we wrote a [small benchmark application][benchmark-application] using [].
The benchmark checks the various approaches against
Besides the regular CPU-time columns, the amount of memory used was also tracked.

These are the results:

[approach-functools-reduce]: https://exercism.org/tracks/python/exercises/acronym/approaches/functools-reduce
[approach-generator-expression]: https://exercism.org/tracks/python/exercises/acronym/approaches/generator-expression
[approach-list-comprehension]: https://exercism.org/tracks/python/exercises/acronym/approaches/list-comprehension
[approach-loop]: https://exercism.org/tracks/python/exercises/acronym/approaches/loop
[approach-map-function]: https://exercism.org/tracks/python/exercises/acronym/approaches/map-function
[approach-regex-join]: https://exercism.org/tracks/python/exercises/acronym/approaches/regex-join
[approach-regex-sub]: https://exercism.org/tracks/python/exercises/acronym/approaches/regex-sub
