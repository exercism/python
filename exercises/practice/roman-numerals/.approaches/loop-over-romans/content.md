# Loop Over Roman Numerals

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

This approach is one of a family, using some mapping from Arabic (decimal) numbers to Roman numbers.
This specific solution uses a dictionary to hold the mappings, though other data structures can work as well.

Here, the `roman()` function iterates over the mapping and finds the biggest Roman numeral that can be subtracted from the number being converted.
Next, that numeral is appended to the resulting string, and its corresponding decimal value is subtracted from the number being converted.
This process then repeats until the number being converted drops to zero, and then the accumulated string is returned.


## Variation #1

```python
ROMANS = ((1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'),
          (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'),
          (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I'))

def roman(number):
    roman_num = ''
    for arabic, roman in ROMANS:
        while arabic <= number:
            roman_num += roman
            number -= arabic
    return roman_num
```

This variant uses nested tuples instead of a dictionary to hold the mappings.
It also finds the largest Roman numeral slightly differently: It iterates over the mapping first, repeating the appending and subtraction of each number as many times as necessary.


## Variation #2

```python
NUMBERS = [1000, 900, 500, 400, 100,  90, 50,  40,  10,  9,  5,    4,   1]
NAMES   = [ 'M', 'CM','D','CD', 'C','XC','L','XL', 'X','IX','V','IV', 'I']

def roman(number):
    res = []

    while number > 0:
        for idx, val in enumerate(NUMBERS):
            if number >= val:
                res.append(NAMES[idx])
                number -= val
                break

    return ''.join(res)
```

This solution uses a pair of lists, with a shared index from `enumerate()`.
It also accumulates the numerals using a list instead of a string, and uses a [`str.join()`][str-join] at the end get the final result.

However, for a read-only lookup it may be better to use (immutable) tuples for `NUMBERS` and `NAMES`.


## Variation #3

```python
# The 10's, 5's, and 1's position chars for 1, 10, 100, and 1000.
DIGIT_CHARS = ['XVI', 'CLX', 'MDC', '??M']


def roman(number):
    # Generate a mapping from numeric value to Roman numeral.
    mapping = []
    for position in range(len(DIGIT_CHARS) - 1, -1, -1):
        # Values: 1000, 100, 10, 1
        scale = 10 ** position
        chars = DIGIT_CHARS[position]
        # This might be: (9, IX) or (90, XC)
        mapping.append((9 * scale, chars[2] + chars[0]))
        # This might be: (5, V) or (50, D)
        mapping.append((5 * scale, chars[1]))
        # This might be: (4, IV) or (40, XD)
        mapping.append((4 * scale, chars[2] + chars[1]))
        mapping.append((1 * scale, chars[2]))

    out = ''
    for num, numerals in mapping:
        while number >= num:
            out += numerals
            number -= num
    return out
```

This variant takes advantage of the fact that Roman numerals are built up from letters for 1, 5, and 10 times powers of 10 to build up the mapping programmatically.


## Variation #4

```python
DIVISOR_MAP = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC',
               50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}

def roman(number: int) -> str:
    result = ''
    for divisor, symbol in DIVISOR_MAP.items():
        major, number = divmod(number, divisor)
        result += symbol * major
    return result
```

This solution removes a level of looping by replacing the inner loop with calculations to determine how many of each number can be subtracted from the number being converted.
Here the built-in [`divmod()`][divmod] function is used to get the number of times the numeral can be subtracted (`major`), and what remains of the number being converted after the subtraction (`number`) in one step.

Incidentally, notice the use of [type hints][type-hints]: `def roman(number: int) -> str`.
This is optional in Python and is (currently) ignored by the interpreter, but is useful for documentation purposes.

Increasingly, code editors and IDEs such as VSCode and PyCharm understand the type hints, using them to flag problems and provide advice.


## Conclusions

These five solutions all share some common features:

- Some sort of translation lookup.
- Nested loops, a `while` and a `for`, in either order (except the last one).
- At each step, find the largest number that can be subtracted from the decimal input and appended to the Roman representation.

When building a string gradually, it is often better to build an intermediate list, then do a `join()` at the end, as in the third example.
This is because strings are immutable, so they need to be copied at each step, and the old strings need to be garbage-collected.

However, Roman numerals are always so short that the difference is minimal in this case.


[divmod]: https://docs.python.org/3/builtins/functions.html#divmod
[str-join]: https://docs.python.org/3/builtins/stdtypes.html#str.join
[type-hints]: https://docs.python.org/3/library/typing.html
