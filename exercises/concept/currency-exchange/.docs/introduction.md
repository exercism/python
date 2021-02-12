# Introduction

## Numbers

There are three different kinds of built-in numbers in Python : `ints`, `floats`, and `complex`. However, in this exercise you'll be dealing only with `ints` and `floats`.

### ints

`ints` are whole numbers. e.g. `1234`, `-10`, `20201278`.

Integers in Python have [arbitrary precision][arbitrary-precision] -- the amount of digits is limited only by the available memory of the host system.

### floats

`floats` are numbers containing a decimal point. e.g. `0.0`,`3.14`,`-9.01`.

Floating point numbers are usually implemented in Python using a `double` in C (_15 decimal places of precision_), but will vary in representation based on the host system and other implementation details. This can create some surprises when working with floats, but is "good enough" for most situations.

You can see more details and discussions in the following resources:

- [Python numeric type documentation][numeric-type-docs]
- [The Python Tutorial][floating point math]
- [Documentation for `int()` built in][`int()` built in]
- [Documentation for `float()` built in][`float()` built in]
- [0.30000000000000004.com][0.30000000000000004.com]

## Arithmetic

Python fully supports arithmetic between `ints` and `floats`. It will convert narrower numbers to match their less narrow counterparts when used with the binary arithmetic operators (`+`, `-`, `*`, `/`, `//`, and `%`). When division with `/`, `//` returns the quotient and `%` returns the remainder.

Python considers `ints` narrower than `floats`. So, using a float in an expression ensures the result will be a float too. However, when doing division, the result will always be a float, even if only integers are used.

```python
# The int is widened to a float here, and a float type is returned.
>>> 3 + 4.0
7.0
>>> 3 * 4.0
12.0
>>> 3 - 2.0
1.0
# Division always returns a float.
>>> 6 / 2
3.0
>>> 7 / 4
1.75
# Calculating remainders.
>>> 7 % 4
3
>>> 2 % 4
2
>>> 12.75 % 3
0.75
```

If an int result is needed, you can use `//` to truncate the result.

```python
>>> 6 // 2
3
>>> 7 // 4
1
```

To convert a float to an integer, you can use `int()`. Also, to convert an integer to a float, you can use `float()`.

```python
>>> int(6 / 2)
3
>>> float(1 + 2)
3.0
```

[arbitrary-precision]: https://en.wikipedia.org/wiki/Arbitrary-precision_arithmetic#:~:text=In%20computer%20science%2C%20arbitrary%2Dprecision,memory%20of%20the%20host%20system.
[numeric-type-docs]: https://docs.python.org/3/library/stdtypes.html#typesnumeric
[`int()` built in]: https://docs.python.org/3/library/functions.html#int
[`float()` built in]: https://docs.python.org/3/library/functions.html#float
[0.30000000000000004.com]: https://0.30000000000000004.com/
[floating point math]: https://docs.python.org/3.9/tutorial/floatingpoint.html
