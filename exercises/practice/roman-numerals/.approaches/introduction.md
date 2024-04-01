# Introduction

There is no single, obvious solution to this exercise, but a diverse array of working solutions have been used.

## General guidance

Roman numerals are limited to positive integers from 1 to 3999 (MMMCMXCIX).
In the version used for this exercise, the longest string needed to represent a Roman numeral is 15 characters (MMMDCCCLXXXVIII).
Minor variants of the system have been used which represent 4 as IIII rather than IV, allowing for longer strings, but those are not relevant here.

The system is inherently decimal: the number of human fingers has not changed since ancient Rome, nor the habit of using them for counting.
However, there is no zero value available, so Roman numerals represent powers of 10 with different letters (I, X, C, M), not by position (1, 10, 100, 1000).

The approaches to this exercise break down into two groups, with many variants in each:
1. Split the input number into digits, and translate each separately.
2. Iterate through the Roman numbers, from large to small, and convert the largest valid number at each step.

## Digit-by-digit approaches

The concept behind this class of approaches:
1.  Split the input number into decimal digits.
2.  For each digit, get the Roman equivalent and append to a list.
3.  Join the list into a string and return it.
Depending on the implementation, there may need to be a list-reverse step.

### With `if` conditions

```python
def roman(number: int) -> str:
    assert isinstance(number, int)

    def translate_digit(digit: int, translations: iter) -> str:
        assert isinstance(digit, int) and 0 <= digit <= 9

        units, four, five, nine = translations
        if digit < 4:
            return digit * units
        if digit == 4:
            return four
        if digit < 9:
            return five + (digit - 5) * units
        return nine

    m, c, x, i = ([0, 0, 0, 0] + [int(d) for d in str(number)])[-4:]
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

See [`if-else`][if-else] for details.

### With table lookup

```python
def roman(number):
    assert (number > 0)

    # define lookup table (as a tuple of tuples, in this case)
    table = (
        ("I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"),
        ("X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"),
        ("C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"),
        ("M", "MM", "MMM"))

    # convert the input integer to a list of single digits
    digits = [int(d) for d in str(number)]
    
    # we need the row in the lookup table for our most-significant decimal digit
    inverter = len(digits) - 1 

    # translate decimal digits list to Roman numerals list
    roman_digits = [table[inverter - i][d - 1] for (i, d) in enumerate(digits) if d != 0]

    # convert the list of Roman numerals to a single string
    return ''.join(roman_digits)
```

See [`table-lookup`][table-lookup] for details.


## Loop over Romans approaches

In this class of approaches we:
1.  Create a mapping from Roman to Arabic numbers, in some suitable format. (_`dicts` or `tuples` work well_)
2.  Iterate nested loops, a `for` and a `while`, in either order.
3.  At each step, append the largest possible Roman number to a list and subtract the corresponding value from the number being converted.
4.  When the number being converted drops to zero, join the list into a string and return it.
Depending on the implementation, there may need to be a list-reverse step.

This is one example using a dictionary:

```python
ROMAN = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
         100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
         10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}

def roman(number: int) -> str:
    result = ''
    while number:
        for arabic in ROMAN.keys():
            if number >= arabic: 
                result += ROMAN[arabic]
                number -= arabic
                break
    return result
```

There are a number of variants.
See [`loop-over-romans`][loop-over-romans] for details.

## Other approaches

### Built-in methods

Python has a package for pretty much everything, and Roman numerals are [no exception][roman-module].

```python
>>> import roman
>>> roman.toRoman(23)
'XXIII'
>>> roman.fromRoman('MMDCCCLXXXVIII')
2888
```

First it is necessary to install the package with `pip` or `conda`.
Like most external packages, `roman` is not available in the Exercism test runner.

This is the key part of the implementation on GitHub, which may look familiar:

```python
def toRoman(n):
    result = ""
    for numeral, integer in romanNumeralMap:
        while n >= integer:
            result += numeral
            n -= integer
    return result
```

The library function is a wrapper around a `loop-over-romans` approach!

### Recursion

This is a recursive version of the `loop-over-romans` approach, which only works in Python 3.10 and later:

```python
ARABIC_NUM = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
ROMAN_NUM = ("M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I")

def roman(number: int) -> str:
    return roman_recur(number, 0, [])

def roman_recur(num: int, idx: int, digits: list[str]):
    match (num, idx, digits):
        case [_, 13, digits]:
            return ''.join(digits[::-1])
        case [num, idx, digits] if num >= ARABIC_NUM[idx]:
            return roman_recur(num - ARABIC_NUM[idx], idx, [ROMAN_NUM[idx],] + digits)
        case [num, idx, digits]:
            return roman_recur(num, idx + 1, digits)
```

See  [`recurse-match`][recurse-match] for details.


### Over-use a functional approach

```python
def roman(number):
    return ''.join(one*digit if digit<4 else one+five if digit==4 else five+one*(digit-5) if digit<9 else one+ten
        for digit, (one,five,ten)
        in zip([int(d) for d in str(number)], ["--MDCLXVI"[-i*2-1:-i*2-4:-1] for i in range(len(str(number))-1,-1,-1)]))
```

*This is Python, but not as we know it*.

As the textbooks say, further analysis of this approach is left as an exercise for the reader.

## Which approach to use?

In production, it would make sense to use the `roman` package.
It is debugged and supports Roman-to-Arabic conversions in addtion to the Arabic-to-Roman approaches discussed here.

Most submissions, like the `roman` package implementation, use some variant of [`loop-over-romans`][loop-over-romans].

Using a [2-D lookup table][table-lookup] takes a bit more initialization, but then everthing can be done in a list comprehension instead of nested loops.
Python is relatively unusual in supporting both tuples-of-tuples and relatively fast list comprehensions, so the approach seems a good fit for this language.

No performance article is currently included for this exercise.
The problem is inherently limited in scope by the design of Roman numerals, so any of the approaches is likely to be "fast enough".



[if-else]: https://exercism.org/tracks/python/exercises/roman-numerals/approaches/if-else
[table-lookup]: https://exercism.org/tracks/python/exercises/roman-numerals/approaches/table-lookup
[loop-over-romans]: https://exercism.org/tracks/python/exercises/roman-numerals/approaches/loop-over-roman
[recurse-match]: https://exercism.org/tracks/python/exercises/roman-numerals/approaches/recurse-match
[roman-module]: https://github.com/zopefoundation/roman
