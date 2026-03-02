# List Comprehension

```python
def is_armstrong_number(number):
    digits = str(number)
    power = len(digits)
    return sum(int(d) ** power for d in digits) == number
```

## How it works

1. Convert `number` to a string to iterate over individual digits.
2. The `power` is the count of digits (length of the string).
3. A generator expression computes `int(d) ** power` for each digit.
4. `sum()` adds all the powered digits together.
5. Compare the sum to the original number.

## When to use this approach

This is the most readable and Pythonic solution. It handles all cases including single-digit numbers (which are always Armstrong numbers) and zero.

## Performance

For typical Armstrong number checks (numbers up to 9 digits), this approach is efficient. String conversion has O(n) complexity where n is the number of digits.
