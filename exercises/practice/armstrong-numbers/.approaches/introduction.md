# Introduction

There are several ways to solve Armstrong Numbers in Python.

## Approach: List Comprehension with String Conversion

```python
def is_armstrong_number(number):
    digits = str(number)
    power = len(digits)
    return sum(int(d) ** power for d in digits) == number
```

Convert the number to a string, get the count of digits, then sum each digit raised to that power. This is the most Pythonic approach.

For more detail, see the [List Comprehension approach][approach-list-comprehension].

## Approach: Math (no string conversion)

```python
import math

def is_armstrong_number(number):
    if number == 0:
        return True
    power = math.floor(math.log10(number)) + 1
    total, n = 0, number
    while n > 0:
        total += (n % 10) ** power
        n //= 10
    return total == number
```

Uses modular arithmetic to extract digits without string conversion. More efficient for very large numbers.

For more detail, see the [Math approach][approach-math].

[approach-list-comprehension]: https://exercism.org/tracks/python/exercises/armstrong-numbers/approaches/list-comprehension
[approach-math]: https://exercism.org/tracks/python/exercises/armstrong-numbers/approaches/math-approach
