# Recursion with Pattern Matching

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

[Recursion][recursion] is possible in Python, but it is much less commonly used than in some other languages.

A limitation is the lack of tail-recursion optimization, which can easily trigger stack overflow if the recursion goes too deep.
The maximum recursion depth for Python defaults to 1000 to avoid this overflow.

However, Roman numerals are so limited in scale that they could be an ideal use case for playing with recursion.
In practice, there is no obvious advantage to recursion over using a loop (_everything you can do with recursion you can do with a loop and vice-versa_) .

Note the use of [structural pattern matching][pep-636], available in Python since version 3.10.
There is also an [official tutorial][structural-pattern-matching] for this new feature.

The code above is adapted from a Scala approach, where it may be more appropriate.

Once we get past the unfamiliar-in-Python syntax, this code is doing essentially the same as other [`loop-over-romans`][loop-over-romans] approaches.

Without the pattern matching, a recursive approach might look something like this:

```python
LOOKUP = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"), (50, "L"),
    (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]

def convert (number, idx, output):
    if idx > 12:
        return output
    val, ltr = LOOKUP[idx]
    if number >= val:
        return convert(number - val, idx, output + ltr)
    return convert(number, idx + 1, output)

def roman(number):
    return convert(number, 0, "")
```


[recursion]: https://diveintopython.org/learn/functions/recursion
[pep-636]: https://peps.python.org/pep-0636/
[structural-pattern-matching]: https://docs.python.org/3/tutorial/controlflow.html#match-statements
[loop-over-romans]: https://exercism.org/tracks/python/exercises/roman-numerals/approaches/loop-over-roman
