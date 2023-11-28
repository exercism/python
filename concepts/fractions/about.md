# About

The [`Fractions`][fractions] module allows us to handle [`rational numbers`][rational]: fractions with an integer numerator divided by an integer denominator.
For example, we can store `2/3` as an exact fraction instead of the approximate `float` value `0.6666...`

## Creating Fractions


Unlike `int`, `float`, and `complex` numbers, fractions do not have a literal form.
However, the fractions constructor is quite flexible.

Most obviously, it can take take two integers.
Common factors are removed, to convert the fraction to its "lowest form": the smallest integers that accurately represent the fraction.

```python
>>> from fractions import Fraction

>>> f1 = Fraction(2, 3) # 2/3
>>> f1
Fraction(2, 3)

>>> f2 = Fraction(6, 9)
>>> f2
Fraction(2, 3)  # automatically simplified

>>> f1 == f2
True
```

It can also parse a string representation of the fraction:

```python
>>> f3 = Fraction('2/3')
>>> f3
Fraction(2, 3)
```

It can work with `float` parameters, but this may run into problems with the approximate nature of representing the decimal value interally as binary. 
For a more reliable result, there is the `<fraction>.limit_denominator()` method.

[`.limit_denominator()`][limit_denominator] can take an integer parameter if you have specific requirements, but even the default (`max_denominator=1000000`) can work well and give an acceptable, simple approximation.

```python
>>> Fraction(1.2)
Fraction(5404319552844595, 4503599627370496)

>>> Fraction(1.2).limit_denominator()
Fraction(6, 5)
```

## Arithmetic

The usual [`arithmetic operators`][operators] `+ - * / **` work with fractions, as with other numeric types.

Integers and other `Fraction`s can be included and give a `Fraction` result.
Including a `float` in the expression results in `float` output.

```python
>>> Fraction(2, 3) + Fraction(1, 4) # addition
Fraction(11, 12)

>>> Fraction(2, 3) * Fraction(6, 5) # multiply fractions
Fraction(4, 5)

>>> Fraction(2, 3) * 6 / 5 # fraction with integers
Fraction(4, 5)

>>> Fraction(2, 3) * 1.2  # fraction with float -> float
0.7999999999999999

>>> Fraction(2, 3) ** 2  # exponentiation with integer
Fraction(4, 9)
```

## Conversions

Fractions are great for preserving precision during intermediate calculations, but may not be what you want for the final output.

It is possible to get the numerator and denominator individually or as a tuple ([`tuples`][tuple] will be discussed in a later Concept):

```python
>>> Fraction(2, 3).numerator
2
>>> Fraction(2, 3).denominator
3
>>> Fraction(2, 3).as_integer_ratio()
(2, 3)
```

Various standard Python numeric functions also give the result you might expect from working with `int` and `float` types:

```python
>>> round(Fraction(11, 3))
4

>>> from math import floor, ceil
>>> floor(Fraction(11, 3))
3
>>> ceil(Fraction(11, 3))
4

>>> float(Fraction(11, 3))
3.6666666666666665
```

[fractions]: https://docs.python.org/3/library/fractions.html
[tuple]: https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences
[operators]: https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex
[rational]: https://en.wikipedia.org/wiki/Rational_number
[limit_denominator]: https://docs.python.org/3/library/fractions.html
