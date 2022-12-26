# Introduction

Python has three different types of built-in numbers: integers ([`int`][int]), floating-point ([`float`][float]), and complex ([`complex`][complex]).
Fractions ([`fractions.Fraction`][fractions]) and Decimals ([`decimal.Decimal`][decimals]) are also available via import from the standard library.

Whole numbers including hexadecimal ([_`hex()`_][hex]), octal ([_`oct()`_][oct]) and binary ([_`bin()`_][bin]) numbers **without** decimal places are also identified as `ints`:

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

Addition and subtraction operators behave as they do in normal math.
If one or more of the operands is a `float`, the remaining `int`s will be converted to `float`s as well:

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
# The result of % is zero here, because dividing 8 by 2 leaves no remainder
>>> 8 % 2
0

# The result of % is 2 here, because 3 only goes into 5 once, with 2 leftover
>>> 5 % 3
2
```

Another way to look at 5 % 3:

```python
>>> whole_part = int(5/3)
1

>>> decimal_part = 5/3 - whole_part
0.6666666666666667

>>> whole_remainder = decimal_part * 3
2.0
```

## Round

Python provides a built-in function [`round(number, <decimal_places>)`][round] to round off a floating point number to a given number of decimal places.
If no number of decimal places is specified, the number is rounded off to the nearest integer and will return an `int`:

```python
>>> round(3.1415926535, 2)
3.14

>>> round(3.1415926535)
3
```

## Priority and parentheses

Python allows you to use parentheses to group expressions.
This is useful when you want to override the default order of operations.

```python
>>> 2 + 3 * 4
14

>>> (2 + 3) * 4
20
```

Python follows the [PEMDAS][pemdas] rule for operator precedence.
This means calculations within `()` have the highest priority, followed by `**`, then `*`, `/`, `//`, `%`, `+`, and `-`:

```python
>>> 2 + 3 - 4 * 4
-11

>>> (2 + 3 - 4) * 4
4

# In the following example, the `**` operator has the highest priority, then `*`, then `+`
# Meaning we first do 4 ** 4, then 3 * 64, then 2 + 192
>>> 2 + 3 * 4 ** 4
770
```

## Precision & Representation

Integers in Python have [arbitrary precision][arbitrary-precision] -- the amount of digits is limited only by the available memory of the host system.

Floating point numbers are usually implemented using a `double` in C (_15 decimal places of precision_), but will vary in representation based on the host system.
Complex numbers have a `real` and an `imaginary` part, both of which are represented by floating point numbers.

For a more detailed discussions of the issues and limitations of floating point arithmetic across programming languages, take a look at [0.30000000000000004.com][0.30000000000000004.com] and [The Python Tutorial][floating point math].

[0.30000000000000004.com]: https://0.30000000000000004.com/
[arbitrary-precision]: https://en.wikipedia.org/wiki/Arbitrary-precision_arithmetic
[bin]: https://docs.python.org/3/library/functions.html#bin
[complex]: https://docs.python.org/3/library/functions.html#complex
[decimals]: https://docs.python.org/3/library/decimal.html#module-decimal
[float]: https://docs.python.org/3/library/functions.html#float
[floating point math]: https://docs.python.org/3.9/tutorial/floatingpoint.html
[fractions]: https://docs.python.org/3/library/fractions.html
[hex]: https://docs.python.org/3/library/functions.html#hex
[int]: https://docs.python.org/3/library/functions.html#int
[oct]: https://docs.python.org/3/library/functions.html#oct
[pemdas]: https://mathworld.wolfram.com/PEMDAS.html
[round]: https://docs.python.org/3/library/functions.html#round
