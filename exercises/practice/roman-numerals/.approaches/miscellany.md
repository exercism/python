# Other stuff


```python
"""Convert an int to a Roman numeral."""


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

```python
# @bobahop
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

```python
# @meatball
def roman(number):
    roman_hash = { 1000: 'M', 900: 'CM', 500 : 'D', 400: 'CD',
                     100 : 'C', 90  : 'XC', 50  : 'L', 40  : 'XL',
                     10   : 'X', 9   : 'IX', 5  : 'V', 4   : 'IV',
                     1    : 'I' }
    result = ""
    for x, y in roman_hash.items():
        while x <= number:
            number -= x
            result += y
    return result
```


```python
# @pranasas
def roman(number: int) -> str:
    result = ''
    divisor_map = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC',
                   50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
    for divisor, symbol in divisor_map.items():
        major, number = divmod(number, divisor)
        result += symbol * major
    return result
```
