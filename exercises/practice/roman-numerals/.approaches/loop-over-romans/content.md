# Loop Over Roman Numerals

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

This approach is one of a family, using some mapping from Arabic (decimal) to Roman numbers.

The code above uses a dictionary.
With minor changes, we could also use nested tuples:

```python
ROMANS = ((1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"),
          (90, "XC"), (50, "L"), (40, "XL"), (10, "X"),
          (9, "IX"), (5, "V"), (4, "IV"), (1, "I"))

def roman(number: int) -> str:
    assert(number > 0)

    roman_num = ""
    for (k, v) in ROMANS:
        while k <= number:
            roman_num += v
            number -= k
    return roman_num
```

Using a pair of lists is also possible, with a shared index from the `enumerate()`. 

```python
# Use a translation 
numbers = [1000, 900, 500, 400, 100,  90, 50,  40,  10,  9,  5,    4,   1]
names   = [  'M', 'CM','D','CD', 'C','XC','L','XL', 'X','IX','V','IV', 'I']

def roman(number: int) -> str:
    "Take a decimal number and return Roman Numeral Representation"

    # List of Roman symbols
    res = []

    while (number > 0):
        # Find the largest amount we can chip off
        for i, val in enumerate(numbers):
            if (number >= val):
                res.append(names[i])
                number -= val
                break

    return ''.join(res)
```

However, for a read-only lookup it may be better to use (immutable) tuples for `numbers` and `names`.

As Roman numerals are built up from letters for 1, 5, 10 times powers of 10, it is possible to shorten the lookup and build up most of the digits programmatically:

```python
# The 10's, 5's and 1's position chars for 1, 10, 100, 1000.
DIGIT_CHARS = ["XVI", "CLX", "MDC", "??M"]


def roman(number: int) -> str:
    """Return the Roman numeral for a number."""
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

    out = ""
    for num, numerals in mapping:
        while number >= num:
            out += numerals
            number -= num
    return out
```

The code below is doing something similar to the dictionary approach at the top of this page, but more concisely:

```python
def roman(number: int) -> str:
    result = ''
    divisor_map = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC',
                   50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
    for divisor, symbol in divisor_map.items():
        major, number = divmod(number, divisor)
        result += symbol * major
    return result
```


These five solutions all share some common features:
- Some sort of translation lookup.
- Nested loops, a `while`and a `for`, in either order.
- At each step, find the largest number that can be subtracted from the decimal input and appended to the Roman representation.

When building a string gradually, it is often better to build an intermediate list, then do a `join()` at the end, as in the third example.
This is because strings are immutable, so need to be copied at each step, and the old strings need to be garbage-collected.

However, Roman numerals are always so short that the difference is minimal in this case.

Incidentally, notice the use of type hints: `def roman(number: int) -> str`.
This is optional in Python and (currently) ignored by the interpreter, but is useful for documentation purposes.

Increasingly, IDE's such as VSCode and PyCharm understand the type hints, using them to flag problems and provide advice.

