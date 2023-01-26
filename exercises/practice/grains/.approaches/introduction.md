# Introduction

There are various idiomatic approaches to solve Grains.
You can use [bit shifting][bit-shifting] to calculate the number on grains on a square.
Or you can use [exponentiation][exponentiation].
Another approach is to use [`pow`][pow].

## General guidance

The key to solving Grains is to focus on each square having double the amount of grains as the square before it.
This means that the amount of grains grows exponentially.
The first square has one grain, which is `2` to the power of `0`.
The second square has two grains, which is `2` to the power of `1`.
The third square has four grains, which is `2` to the power of `2`.
You can see that the exponent, or power, that `2` is raised by is always one less than the square number.

| Square | Power | Value                   |
| ------ | ----- | ----------------------- |
| 1      | 0     | 2 to the power of 0 = 1 |
| 2      | 1     | 2 to the power of 1 = 2 |
| 3      | 2     | 2 to the power of 2 = 4 |
| 4      | 3     | 2 to the power of 3 = 8 |


## Approach: Bit-shifting

```python
def square(number):
    if number < 1 or number > 64:
        raise ValueError('square must be between 1 and 64')

    return 1 << number - 1


def total():
    return (1 << 64) - 1

```

For more information, check the [bit-shifting approach][approach-bit-shifting].

## Approach: Exponentiation

```python
def square(number):
    if number < 1 or number > 64:
        raise ValueError('square must be between 1 and 64')

    return 2 ** (number - 1)


def total():
    return 2 ** 64 - 1

```

For more information, check the [exponentiation approach][approach-exponentiation].

## Approach: `pow`

```python
def square(number):
    if number < 1 or number > 64:
        raise ValueError('square must be between 1 and 64')

    return pow(2, number - 1)


def total():
    return pow(2, 64) - 1

```

For more information, check the [`pow` approach][approach-pow].

## Which approach to use?

- Bit shifting is the fastest for `square`.
- Bit shifting and exponentiation are about the same for `total`.
- Exponentiation and `pow` are about the same for `square`.
- `pow` is significantly the slowest for `total`.

For more information, check the [Performance article][article-performance].

[bit-shifting]: https://realpython.com/python-bitwise-operators/
[exponentiation]: https://www.codingem.com/python-exponent-maths/
[pow]: https://docs.python.org/3/library/functions.html#pow
[approach-bit-shifting]: https://exercism.org/tracks/python/exercises/grains/approaches/bit-shifting
[approach-exponentiation]: https://exercism.org/tracks/python/exercises/grains/approaches/exponentiation
[approach-pow]: https://exercism.org/tracks/python/exercises/grains/approaches/pow
[article-performance]: https://exercism.org/tracks/python/exercises/grains/articles/performance
