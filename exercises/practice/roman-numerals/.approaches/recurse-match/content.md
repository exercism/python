# Recursion with Pattern Matching

```python
ARABIC_NUM = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
ROMAN_NUM = ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')

def roman(number):
    return roman_recur(number, 0, [])

def roman_recur(num, idx, digits):
    match (num, idx, digits):
        case [_, 13, digits]:
            return ''.join(digits)
        case [num, idx, digits] if num >= ARABIC_NUM[idx]:
            return roman_recur(num - ARABIC_NUM[idx], idx, digits + [ROMAN_NUM[idx]])
        case _:
            return roman_recur(num, idx + 1, digits)
```

Similar to the [loop over roman numerals][loop-over-romans] approach, this solution uses a mapping from Arabic numbers to Roman numbers.
Here, `roman()` calls the helper function `roman_recur()`, which has arguments for the number being converted (`num`), the index of the mapping to check (`idx`), and list of the currently computed digits (`digits`).

The code then uses [structural pattern matching][pep-636] (added in Python 3.10) to branch into three different cases depending on the input.
(See the [official pattern matching tutorial][structural-pattern-matching] for detail on how this works.)

The first case occurs when there are no more entries of the mapping to check, and it uses [`''.join()`][str-join] to join the list of digits into the final Roman numeral and return it.

The second case checks if the Arabic number at `idx` can be subtracted from the number being converted. If it can, `roman_recur()` is called [recursively][recursion] with the subtracted number, and the list of Roman digits updated with the corresponding Roman number at `idx`.

The final case uses a wildcard (`_`), so it always runs if the previous cases do not. This case also returns the result from calling `roman_recur()` again, but this time it increments `idx` so the next entry in the mapping is checked.

Though [recursion][recursion] is possible in Python, it is much less commonly used than in some other languages.

A major limitation is the lack of tail-call optimization, which can easily trigger stack overflow if the recursion goes too deep.
The maximum recursion depth for Python defaults to 1000 to avoid this overflow.

However, Roman numerals are so limited in scale that they could be an ideal use case for playing with recursion.
In practice, there is no obvious advantage to recursion over using a loop (_everything you can do with recursion you can do with a loop and vice-versa_).

The code above is adapted from a Scala approach, where it may be more appropriate.


## Variation #1

Without the pattern matching, a recursive approach might look something like this:

```python
LOOKUP = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'),
          (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]

def convert(number, idx, output):
    if idx > 12:
        return output
    val, roman_val = LOOKUP[idx]
    if number >= val:
        return convert(number - val, idx, output + roman_val)
    return convert(number, idx + 1, output)

def roman(number):
    return convert(number, 0, '')
```


[recursion]: https://diveintopython.org/learn/functions/recursion
[pep-636]: https://peps.python.org/pep-0636/
[structural-pattern-matching]: https://docs.python.org/3/tutorial/controlflow.html#match-statements
[str-join]: https://docs.python.org/3/builtins/stdtypes.html#str.join
[loop-over-romans]: https://exercism.org/tracks/python/exercises/roman-numerals/approaches/loop-over-romans
