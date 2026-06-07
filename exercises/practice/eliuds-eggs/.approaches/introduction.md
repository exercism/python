# Introduction

There are many different approaches to solving the Eliud's Eggs exercise:

- Using a `while-loop`, modifying the parameter on each iteration
- Looping over every binary digit _without_ modifying the parameter
- Converting the `int` to a binary string and counting the ones

There are also some approaches that aren't recommended:

- Using the bit-count functionality from the Python standard library, as the instructions forbid it
- Breaking up the proccess into many functions, overcomplicating the solution


## General guidance

The goal of the Eliud's Eggs exercise is to count the number of ones in the binary representation of a [number][concept-numbers].
In essence, this requires you to loop over each bit (binary digit) of the number in some way.

The approaches below represent categories of the most common ways of accomplishing this.


## Approach: Modifying the Parameter in a `while-loop`

```python
def egg_count(display_value):
    eggs = 0
    while display_value:
        eggs += display_value % 2
        display_value //= 2
    return eggs
```

This approach uses a `while-loop` to count up all of the ones.
In the loop, we increment `eggs` by `display_value % 2`.
This adds the least significant bit (the rightmost digit in the binary representation) of `display_value` to `eggs`.

Next, we divide `display_value` by `2`, discarding any remainder.
This essentially removes the least significant bit of `display_value`, setting up `display_value` for processing the next bit.

The loop repeats until `display_value` reaches `0` (which indicates that we have no more bits to check), and then we return `eggs`.

To see more variations of this solution, see the [modify the parameter in a loop][approach-parameter-modification] approach.


## Approach: Looping Without Modifying the Parameter

```python
from math import ceil, log2

def egg_count(display_value):
    eggs = 0
    for bit_position in range(ceil(log2(display_value + 1))):
        eggs += (display_value >> bit_position) & 1
    return eggs
```

This solution uses a `for-loop` with `range()` to iterate over all of the bits in `display_value`.
To determine how many bits `display_value` has, this solution imports `ceil` and `log2` from the `math` module.
It then feeds this number into `range()` to make the `for-loop` iterate over all the `bit_position`s.

For each `bit_position`, we determine the value of the bit at that position by using the [right-shift operator][right-shift-operator] and the bitwise AND operator.
Once we determine the bit's value, we increment `eggs` by that number.

After the loop ends, we know that we have checked all of the bits in `display_value`, thus we return `eggs`.

For more details and variations, read the [loop without modifying the parameter][approach-no-parameter-modification] approach.


## Approach: Converting the Parameter to a Binary String

```python
def egg_count(display_value):
    binary_value = bin(display_value)[2:]
    eggs = 0
    for digit in binary_value:
        eggs += int(digit)
    return eggs
```

This approach uses [`bin()`][bin-built-in] (or some other means, such as an [`f-string`][f-string]) to convert `display_value` to a binary string.
Then, the first two characters of the binary string are removed, as the string has "0b" prefixed before the binary digits.

After the binary digits are obtained, this solution loops across all of them, turning each one into an integer and adding it to `eggs`.
This effectively counts up all of the instances of "1" in the binary string, as 0 and 1 are the only valid binary digits.

Many variations of this approach use a built-in function like `sum()` to make the iteration more concise.
For more details, check out the [convert to a binary string][approach-convert-to-binary-string] approach.


[approach-parameter-modification]: https://exercism.org/tracks/python/exercises/eliuds-eggs/approaches/parameter-modification
[approach-no-parameter-modification]: https://exercism.org/tracks/python/exercises/eliuds-eggs/approaches/no-parameter-modification
[approach-convert-to-binary-string]: https://exercism.org/tracks/python/exercises/eliuds-eggs/approaches/convert-to-binary-string
[bin-built-in]: https://docs.python.org/3/library/functions.html#bin
[concept-numbers]: https://exercism.org/tracks/python/concepts/numbers
[right-shift-operator]: https://www.geeksforgeeks.org/software-engineering/right-shift-operator-in-programming/
[f-string]: https://docs.python.org/3/reference/lexical_analysis.html#f-strings
