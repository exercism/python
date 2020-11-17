Python has three different types of built-in numbers: integers ([`int`][int]), floating-point ([`float`][float]), and complex ([`complex`][complex]). Fractions ([`fractions.Fraction`][fractions]) and Decimals ([`decimal.Decimal`][decimals]) are also available via import from the standard library.

Whole numbers (_including hex, octals and binary numbers_) **without** decimal places are identified as `ints`:

```python
#whole number
>>> 1234
1234
>>> type(1234)
<class 'int'>

>>> -12
-12
```

Hex numbers are written/printed with `0x` prefix:

```python
#hex number
>>> 0x17
23
>>> type(0x17)
<class 'int'>
```

Octals are written with a `0o` prefix:

```python
#octal number
>>> 0o446
294
>>> type(0o446)
<class 'int'>
```

Binary numbers are prefixed with `0b`, and written with only zeros and ones:

```python
#binary number
>>> 0b1100110
102
>>> type(0b1100110)
<class 'int'>
```

Each of these `int` displays can be converted into the other via constructor:

```python

>>> starting_number = 1234

>>> hex(starting_number)
'0x4d2'

>>> oct(starting_number)
'0o2322'

>>> bin(starting_number)
'0b10011010010'

>>> hex(0b10011010010)
'0x4d2'

>>> int(0x4d2)
1234
```

Numbers containing a decimal point (_with or without any numbers following_) are identified as `floats`:

```python
>>> 3.45
3.45
>>> type(3.45)
<class 'float'>

```

Appending `j` or `J` to a number creates an _imaginary number_ -- a `complex` number with a zero real part. `ints` or `floats` can then be added to an imaginary number to create a `complex` number with both real and imaginary parts:

```python
>>> 3j
3j
>>> type(3j)
<class 'complex'>

>>> 3.5+4j
(3.5+4j)
```

### Arithmetic

Python fully supports arithmetic between these different number types, and will convert narrower numbers to match their less narrow counterparts when used with the binary arithmetic operators (`+`, `-`, `*`, `/`, `//`, and `%`).

Python considers `ints` narrower than `floats`, which are considered narrower than `complex` numbers. Comparisons between different number types behaves as as if the _exact_ values of those numbers were being compared:

```python
#the int is widened to a float here, and a float is returned
>>> 3 + 4.0
7.0

#the int is widened to a complex number, and a complex number is returned
>>> 6/(3+2j)
(2+2j)

#division always returns a float, even if integers are used
>>> 6/2
3.0

#if an int result is needed, you can use floor division to truncate the result
>>> 6//2
3

#when comparing, exact values are used
>>> 23 == 0x17
True

>>> 0b10111 == 0x17
True

>>> 6 == (6+0j)
True
```

All numbers (except complex) support all [arithmetic operations][arithmetic operations], evaluated according to [operator precedence][operator precedence]. Support for mathematical functions (beyond `+`, `-`, `/`) for complex numbers can be found in the [cmath][cmath] module.

### Precision & Representation

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
[arethmetic operations]: https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex
[operator precedence]: https://docs.python.org/3/reference/expressions.html#operator-precedence
[floating point math]: https://docs.python.org/3.9/tutorial/floatingpoint.html
