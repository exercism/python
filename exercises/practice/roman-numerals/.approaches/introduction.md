# Introduction

There is no single, obvious solution to this exercise, but a diverse array of working solutions have been used.

## General guidance

Roman numerals are limited to positive integers from 1 to 3999 (MMMCMXCIX).
In the version used for this exercise, the longest string needed to represent a Roman numeral is 15 characters (MMMDCCCLXXXVIII).
Minor variants of the system have been used which represent 4 as IIII rather than IV, allowing for longer strings, but those are not relevant here.

The system is inherently decimal: the number of human fingers has not changed since ancient Rome, nor the habit of using them for counting.
However, there is no zero value available, so Roman numerals represent powers of 10 with different letters (I, X, C, and M), not by position (1, 10, 100, 1000, etc).

The approaches to this exercise break down into two groups, with many variants in each:

1. Split the input number into digits, and translate each separately.
2. Iterate through the Roman numbers, from large to small, and convert the largest valid number at each step.

## Digit-by-digit approaches

The process behind this class of approaches begins by splitting the input number into decimal digits.
Then for each digit, the Roman equivalent is determined, and the results are collected into a string and returned.

Depending on the implementation, the resulting string (or an intermediate representation) may need to be reversed.

### With `if` conditions

```python
def roman(number):
    def translate_digit(digit, translations):
        units, four, five, nine = translations
        if digit < 4:
            return digit * units
        if digit == 4:
            return four
        if digit < 9:
            return five + (digit - 5) * units
        return nine

    m, c, x, i = ([0, 0, 0, 0] + [int(digit) for digit in str(number)])[-4:]
    res = ''
    if m > 0:
        res += m * 'M'
    if c > 0:
        res += translate_digit(c, ('C', 'CD', 'D', 'CM'))
    if x > 0:
        res += translate_digit(x, ('X', 'XL', 'L', 'XC'))
    if i > 0:
        res += translate_digit(i, ('I', 'IV', 'V', 'IX'))
    return res
```

See the [if else][if-else] approach for details.

### With table lookup

```python
def roman(number):
    # define lookup table (as a tuple of tuples, in this case)
    table = (
        ('I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'),
        ('X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'),
        ('C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'),
        ('M', 'MM', 'MMM'))

    # convert the input integer to a list of single digits
    digits = [int(digit) for digit in str(number)]
    
    # get the row in the lookup table for the most-significant decimal digit
    inverter = len(digits) - 1

    # translate decimal digits list to Roman numerals list
    roman_digits = [table[inverter - idx][digit - 1] for idx, digit in enumerate(digits) if digit != 0]

    # convert the list of Roman numerals to a single string
    return ''.join(roman_digits)
```

See the [table lookup][table-lookup] approach for details.


## Loop over Roman Numerals approaches

In this class of approaches, we begin by creating a mapping from Roman to Arabic numbers, in some suitable format (_`dicts` or `tuples` work well_).
Then, we use nested loops to repeatedly append the largest possible Roman number to a sequence and subtract the corresponding value from the number being converted.
When the number being converted drops to zero, we return the resulting sequence (converting to a string if necessary).

Depending on the implementation, the resulting string (or an intermediate representation) may need to be reversed.

This is one example using a dictionary:

```python
ROMANS = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
          100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
          10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}

def roman(number):
    result = ''
    while number:
        for arabic in ROMANS.keys():
            if number >= arabic:
                result += ROMANS[arabic]
                number -= arabic
                break
    return result
```

There are a number of variants.
See the [loop over roman numerals][loop-over-romans] approach for details.

## Other approaches

### Built-in methods

Python has a package for pretty much everything, and Roman numerals are no exception:

```python
>>> import roman
>>> roman.toRoman(23)
'XXIII'
>>> roman.fromRoman('MMDCCCLXXXVIII')
2888
```

First it is necessary to install the package with `pip`, `conda`, or another tool.
Like most external packages, the [`roman` module][roman-module] is not available in the Exercism test runner.

The [key part of `toRoman()`'s implementation][roman-module-implementation] can be viewed on GitHub, which may look familiar.
This is because the library function is a wrapper around a "loop over roman numerals" approach!

### Recursion

This is a recursive version of the "loop over roman numerals" approach, which only works in Python 3.10 and later:

```python
ARABIC_NUM = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
ROMAN_NUM = ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')

def roman(number):
    return roman_recur(number, 0, [])

def roman_recur(num, idx, digits):
    match (num, idx, digits):
        case [_, 13, digits]:
            return ''.join(digits[::-1])
        case [num, idx, digits] if num >= ARABIC_NUM[idx]:
            return roman_recur(num - ARABIC_NUM[idx], idx, [ROMAN_NUM[idx]] + digits)
        case _:
            return roman_recur(num, idx + 1, digits)
```

See the [recurse match][recurse-match] approach for details.


### With `itertools.starmap()`

```python
from itertools import starmap


def roman(number):
    def options(i, v, x):
        return ['', i, i * 2, i * 3, i + v, v, v + i, v + i * 2, v + i * 3, i + x]

    def compute(val, chars):
        return options(*chars)[number % (val * 10) // val]

    orders = [(1000, 'M  '), (100, 'CDM'), (10, 'XLC'), (1, 'IVX')]
    return ''.join(starmap(compute, orders))
```

See the [`itertools.starmap()`][itertools-starmap] approach for details.


### Over-use a functional approach

```python
def roman(number):
    return ''.join(
        one*digit if digit<4 else one+five if digit==4 else five+one*(digit-5) if digit<9 else one+ten
        for digit, (one, five, ten) in zip(
            [int(digit) for digit in str(number)],
            ['--MDCLXVI'[-idx*2-1 : -idx*2-4 : -1] for idx in range(len(str(number)) - 1, -1, -1)]
        )
    )
```

*This is Python, but not as we know it*.

As the textbooks say, further analysis of this approach is left as an exercise for the reader.

## Which approach to use?

In production, it would make sense to use the `roman` package.
It is debugged and supports Roman-to-Arabic conversions in addition to the Arabic-to-Roman approaches discussed here.

Most submissions, like the `roman` package implementation, use some variant of the [loop over roman numerals][loop-over-romans] approach.

Using a [2-D lookup table][table-lookup] takes a bit more initialization, but then everything can be done in a list comprehension instead of nested loops.
Python is relatively unusual in supporting both tuples-of-tuples and relatively fast list comprehensions, so the approach seems a good fit for this language.

No performance article is currently included for this exercise.
The problem is inherently limited in scope by the design of Roman numerals, so any of the approaches is likely to be "fast enough".



[if-else]: https://exercism.org/tracks/python/exercises/roman-numerals/approaches/if-else
[table-lookup]: https://exercism.org/tracks/python/exercises/roman-numerals/approaches/table-lookup
[loop-over-romans]: https://exercism.org/tracks/python/exercises/roman-numerals/approaches/loop-over-romans
[recurse-match]: https://exercism.org/tracks/python/exercises/roman-numerals/approaches/recurse-match
[itertools-starmap]: https://exercism.org/tracks/python/exercises/roman-numerals/approaches/itertools-starmap
[roman-module]: https://github.com/zopefoundation/roman
[roman-module-implementation]: https://github.com/zopefoundation/roman/blob/6c0a134c091df4b63fc60c7e720fe1fb645f521d/src/roman/__init__.py#L73-L78
