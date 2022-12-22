# About

Python has three different types of built-in numbers: integers ([`int`][int]), floating-point ([`float`][float]), and complex ([`complex`][complex]). Fractions ([`fractions.Fraction`][fractions]) and Decimals ([`decimal.Decimal`][decimals]) are also available via import from the standard library.

Whole numbers (_including hex, octals and binary numbers_) **without** decimal places are identified as `ints`:

```python
# Ints are whole numbers.
>>> 1234
1234
>>> type(1234)
<class 'int'>

>>> -12
-12
```

Numbers containing a decimal point (with or without fractional parts) are identified as `floats`:

```python
>>> 3.45
3.45
>>> type(3.45)
<class 'float'>
```

## Arithmetic

Python fully supports arithmetic between these different number types, and will convert narrower numbers to match their less narrow counterparts when used with the binary arithmetic operators (`+`, `-`, `*`, `/`, `//`, and `%`).

### Addition and subtraction

Addition and subtraction act like in normal math.
If one of the operands is a `float`, the other will be converted to a `float` as well.
Otherwise both operands will be converted to `ints`:

```python
>>> 5 - 3
2
# The int is widened to a float here, and a float is returned.
>>> 3 + 4.0
7.0
```

### Multiplication

As with addition and subtraction, multiplication will convert narrower numbers to match their less narrow counterparts:

```python
>>> 3 * 2
6

>>> 3 * 2.0
6.0
```

### Division

Division always returns a `float`, even if the result is a whole number:

```python
>>> 6/5
1.2

>>> 6/2
3.0
```

### Floor division

If an `int` result is needed, you can use floor division to truncate the result.
Floor division is performed using the `//` operator:

```python
>>> 6//5
1

>>> 6//2
3
```

### Modulo

The modulo operator (`%`) returns the remainder of the division of the two operands:

```python
>>> 5 % 3
2
```

### Exponentiation

Exponentiation is performed using the `**` operator:

```python
>>> 2 ** 3
8
```

All numbers (except complex) support all [arithmetic operations][arethmetic-operations], evaluated according to [operator precedence][operator precedence]. Support for mathematical functions (beyond `+`, `-`, `/`) for complex numbers can be found in the [cmath][cmath] module.

## Conversions

Numbers can be converted from one type to another using the built-in functions `int()` and `float()`:

```python
>>> int(3.45)
3

>>> float(3)
3.0
```

## Round

Python provides a built-in function `round()` to round off a floating point number to a given number of decimal places.
If no number of decimal places is specified, the number is rounded off to the nearest integer and will return an `int`:

```python
>>> round(3.1415926535, 2)
3.14

>>> round(3.1415926535)
3
```

## Precision & Representation

Integers in Python have [arbitrary precision](https://en.wikipedia.org/wiki/Arbitrary-precision_arithmetic) -- the amount of digits is limited only by the available memory of the host system.

Floating point numbers are usually implemented using a `double` in C (_15 decimal places of precision_), but will vary in representation based on the host system. Complex numbers have a `real` and an `imaginary` part, both of which are represented by floating point numbers.

For a more detailed discussions of the issues and limitations of floating point arithmetic across programming langages, take a look at [0.30000000000000004.com][0.30000000000000004.com] and [The Python Tutorial][floating point math].

[int]: https://docs.python.org/3/library/functions.html#int
[float]: https://docs.python.org/3/library/functions.html#float
[complex]: https://docs.python.org/3/library/functions.html#complex
[fractions]: https://docs.python.org/3/library/fractions.html
[decimals]: https://docs.python.org/3/library/decimal.html#module-decimal
[0.30000000000000004.com]: https://0.30000000000000004.com/
[cmath]: https://docs.python.org/3.9/library/cmath.html
[arethmetic-operations]: https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex
[operator precedence]: https://docs.python.org/3/reference/expressions.html#operator-precedence
[floating point math]: https://docs.python.org/3.9/tutorial/floatingpoint.html
