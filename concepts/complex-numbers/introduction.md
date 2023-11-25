# Introduction

`Complex numbers` are not complicated.
They just need a less alarming name.

They are so useful, especially in engineering and science, that Python includes [`complex`][complex] as a standard type alongside integers and floating-point numbers.

## Basics

A `complex` value in Python is essentially a pair of floating-point numbers.
These are called the "real" and "imaginary" parts.

There are two common ways to create them.
The `complex(real, imag)` constructor takes two `float` parameters:

```python
>>> z1 = complex(1.5, 2.0)
>>> z1
(1.5+2j)
```

There are two rules for an imaginary part:
- It is designated with `j` (not `i`, which you may see in textbooks).
- The `j` must immediately follow a number, to prevent Python seeing it as a variable name. If necessary, use `1j`.

```python
>>> j
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'j' is not defined

>>> 1j
1j

>>> type(1j)
<class 'complex'>
```

With this, we have a second way to create a complex number:
```python
>>> z2 = 2.0 + 1.5j
>>> z2
(2+1.5j)
```
The end result is identical to using a constructor.

To access the parts individually:
```python
>>> z2.real
2.0
>>> z2.imag
1.5
```

## Arithmetic

Most of the [`operators`][operators] used with `float` also work with `complex`:

```python
>>> z1, z2
((1.5+2j), (2+1.5j))

>>> z1 + z2  # addition
(3.5+3.5j)

>>> z1 - z2  # subtraction
(-0.5+0.5j)

>>> z1 * z2  # multiplication
6.25j

>>> z1 / z2  # division
(0.96+0.28j)

>>> z1 ** 2  # exponentiation
(-1.75+6j)

>>> 2 ** z1  # another exponentiation
(0.5188946835878313+2.7804223253571183j)

>>> 1j ** 2 # j is the square root of -1
(-1+0j)
```

Explaining the rules for complex multiplication and division is out of scope here.
Any introduction to complex numbers will cover this.
Alternatively, Exercism has a `Complex Numbers` practice exercise where you can implement this from first principles.

There are two functions that are useful with complex numbers:
- `conjugate()` simply flips the sign of the complex part.
- `abs()` is guaranteed to return a real number with no imaginary part.

```python
>>> z1
(1.5+2j)

>>> z1.conjugate() # flip the z1.imag sign
(1.5-2j)

>>> abs(z1) # sqrt(z1.real ** 2 + z1.imag ** 2)
2.5
```

## The `cmath` module

The Python standard library has a `math` module full of useful functionality for working with real numbers.
It also has an equivalent `cmath` module for complex numbers.

Details are available in the [`cmath`][cmath] module documents, but the main categories are:
- conversion between Cartesian and polar coordinates
- exponential and log functions
- trig functions
- hyperbolic functions
- classification functions
- useful constants

```python
>>> import cmath

>>> euler = cmath.exp(1j * cmath.pi) # Euler's equation

>>> euler.real
-1.0
>>> round(euler.imag, 15) # round to 15 decimal places
0.0
```

[complex]: https://docs.python.org/3/library/functions.html#complex
[cmath]: https://docs.python.org/3/library/cmath.html
[operators]: https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex
