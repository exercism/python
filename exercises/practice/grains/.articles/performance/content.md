# Performance

In this approach, we'll find out how to most efficiently calculate the value for Grains in Python.

The [approaches page][approaches] lists three idiomatic approaches to this exercise:

1. [Using bit shifting][approach-bit-shifting]
2. [Using exponentiation][approach-exponentiation]
3. [Using `pow`][approach-pow]

## Benchmarks

To benchmark the approaches, we wrote a [small benchmark application][benchmark-application] using the [timeit][timeit] library.

```
bit shifting square 64:   1.2760140001773835e-07
bit shifting total 64:    6.096410000463947e-08
exponentiation square 64: 4.122742000035942e-07
exponentiation total 64:  6.094090000260621e-08
pow square 64:            4.2468130000634117e-07
pow total 64:             3.1965399999171494e-07
```

- Bit shifting was the fastest for `square`.
- Bit shifting and exponentiation were about the same for `total`.
- Exponentiation and `pow` were about the same for `square`.
- `pow` was significantly the slowest for `total`.

Benchmarks were also done to substitute `if number not in range(1, 65):` for `if number < 1 or number > 64:`.

```
bit shifting square 64:   2.708769000018947e-07
exponentiation square 64: 5.56936200009659e-07
pow square 64:            5.738279999932274e-07
```

Using `if number not in range(1, 65):` was over `125` nanoseconds longer than using `if number < 1 or number > 64:` for all approaches.

[approaches]: https://exercism.org/tracks/python/exercises/grains/approaches
[approach-bit-shifting]: https://exercism.org/python/csharp/exercises/grains/approaches/bit-shifting
[approach-pow]: https://exercism.org/tracks/python/exercises/grains/approaches/pow
[approach-exponentiation]: https://exercism.org/tracks/python/exercises/grains/approaches/exponentiation
[benchmark-application]: https://github.com/exercism/python/blob/main/exercises/practice/grains/.articles/performance/code/Benchmark.py
[timeit]: https://docs.python.org/3/library/timeit.html
