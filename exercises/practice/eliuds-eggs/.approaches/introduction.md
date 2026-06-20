# Introduction

There are many different approaches to solving the Eliud's Eggs exercise.
Among them are:

- Using a `while-loop` and modifying the function argument on each iteration
- Looping over every binary digit _without_ modifying the function argument
- Converting the `int` argument into a binary string and counting the ones in it

There are also some approaches that aren't recommended:

- Using the bit-count functionality from the Python standard library, as the instructions ask that this challenge be solved "manually".
- Breaking up the counting process into many small functions, which can overcomplicate or slow the solution.


## General guidance

The goal of the Eliud's Eggs exercise is to count the number of ones in a [binary representation of a number][concept-numbers] (_e.g. the "filled egg slots" of a chicken coop_).
In essence, this requires you to iterate through each "slot" or bit (binary digit) of the binary number in some way.

The approaches below represent categories of the most common ways of accomplishing this.


## Approach: Modifying the Argument in a `while-loop`

```python
def egg_count(display_value):
    eggs = 0
    while display_value:
        eggs += display_value % 2
        display_value //= 2
    return eggs
```

This approach uses a `while-loop` to count up the ones in the calculated binary equivalent of `display_value`.
In the loop, we increment `eggs` by `display_value % 2`.
This adds the least significant bit (_the rightmost digit in the binary representation_) of `display_value` to `eggs`.

Next, `display_value` is divided by `2`, discarding any remainder.
This removes the least significant bit of the current `display_value`, setting up the next iteration of `display_value` for processing.

The loop repeats until `display_value` reaches `0` (_which indicates that there are no more bits to process_), at which point `eggs` is returned.

To see more variations of this solution, read the [modify the argument in a loop][approach-argument-modification] approach.


## Approach: Looping Without Modifying the Argument

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

For each `bit_position`, we determine the value of the bit at that position by using the [right-shift operator][right-shift-operator] and the [bitwise AND][bitwise-operations] operator.
Once we determine the bit's value, we increment `eggs` by that number.

After the loop ends, we know that we have processed all bits in `display_value`, so we return `eggs`.

For more details and variations, read the [loop without modifying the argument][approach-no-argument-modification] approach.


## Approach: Converting the Argument to a Binary String

```python
def egg_count(display_value):
    binary_value = bin(display_value)[2:]
    eggs = 0
    for digit in binary_value:
        eggs += int(digit)
    return eggs
```

This approach uses [`bin()`][bin-built-in] (or some other means, such as an [`f-string`][f-string]) to convert `display_value` to a binary string.
The first two characters of the binary string are removed, as "0b" is used as a prefix to the binary digits.

After the binary digits are obtained, this solution loops through them, turning each one into an integer and adding it to `eggs`.
This effectively counts up all of the instances of "1" in the binary string, as 0 and 1 are the only valid binary digits.

Many variations of this approach use a built-in function like `sum()` to make the iteration more concise.
For more details, check out the [convert to a binary string][approach-convert-to-binary-string] approach.


## Approach: Using the Built-In Bit-Count Functionality

~~~~exercism/caution
This approach does _not_ follow the instructions, as it uses the bit-count functionality from the standard library.
It is only described here to show what an idiomatic way of counting bits in a _different context_ would be.
~~~~

```python
def egg_count(display_value):
    return display_value.bit_count()
```

This solution uses [`int.bit_count()`][int-bit_count] from the Python standard library to count the number of ones in the binary representation of `display_value`.

For more details and variations, read the [built-in bit-count][approach-built-in-bit-count] approach.


## Approach: Using Helper Functions

```python
def egg_count(display_value):
    return count_ones(convert_to_binary(display_value))


def convert_to_binary(decimal_value):
    binary_value = ""

    while decimal_value > 0:
        binary_value += str(decimal_value % 2)
        decimal_value //= 2

    return binary_value[::-1] if binary_value else "0"


def count_ones(binary_value):
    count = 0

    for digit in binary_value:
        count += int(digit)

    return count
```

This approach breaks the problem down into multiple helper functions that are called from `egg_count()`.
First, `convert_to_binary()` is used to convert `display_value` to a binary string.
Then, `count_ones()` is called to count the number of ones in that string.

The actual implementations of `convert_to_binary()` and `count_ones()` could use almost any of the techniques mentioned in earlier approaches.

Though breaking the problem up into helper functions may facilitate code reuse, it also adds unnecessary overhead to the solution.
It can also overcomplicate things, as you may need to consider additional edge cases, such as making `convert_to_binary()` return "0" instead of an empty string when given the number `0`.
If you do not handle all of these cases, when your future self (_or someone else_) tries to reuse the function, they may get unexpected results, such as "0" being returned when a negative number is input.

For more details, check out the [helper functions][approach-helper-functions] approach.


[approach-built-in-bit-count]: https://exercism.org/tracks/python/exercises/eliuds-eggs/approaches/built-in-bit-count
[approach-convert-to-binary-string]: https://exercism.org/tracks/python/exercises/eliuds-eggs/approaches/convert-to-binary-string
[approach-helper-functions]: https://exercism.org/tracks/python/exercises/eliuds-eggs/approaches/helper-functions
[approach-no-argument-modification]: https://exercism.org/tracks/python/exercises/eliuds-eggs/approaches/no-argument-modification
[approach-argument-modification]: https://exercism.org/tracks/python/exercises/eliuds-eggs/approaches/argument-modification
[bin-built-in]: https://docs.python.org/3/library/functions.html#bin
[bitwise-operations]: https://docs.python.org/3/library/stdtypes.html#bitwise-operations-on-integer-types
[concept-numbers]: https://exercism.org/tracks/python/concepts/numbers
[f-string]: https://docs.python.org/3/reference/lexical_analysis.html#f-strings
[int-bit_count]: https://docs.python.org/3/library/stdtypes.html#int.bit_count
[right-shift-operator]: https://www.geeksforgeeks.org/software-engineering/right-shift-operator-in-programming/
