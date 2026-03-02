# Math Approach (no string conversion)

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

## How it works

1. Handle the edge case of `0` (which is an Armstrong number).
2. Calculate the number of digits using `math.log10`.
3. Use a while loop to extract each digit via modulo `% 10`.
4. Raise each digit to the power and accumulate the sum.
5. Integer-divide `n` by 10 to move to the next digit.

## When to use this approach

When you want to avoid string conversion entirely and work purely with integers. This can be slightly more efficient for very large numbers since it avoids creating string objects.
