# Introduction

There are many Pythonic approaches to solving the Eliud's Eggs exercise:

- Using a `while-loop`, modifying the parameter on each iteration
- Looping over every binary digit _without_ modifying the parameter
- Converting the `int` to a binary string and counting the ones

There are also some approaches that aren't recommended:

- Using the bit-count functionality from the Python standard library, as the instructions forbid it
- Breaking up the proccess into many functions, overcomplicating the solution


## General guidance

The goal of the Eliud's Eggs exercise is to count the number of ones in the binary representation of a number.
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

To see more variants of this solution, see the [modify the parameter in a loop][parameter-modification] approach.


[parameter-modification]: https://exercism.org/tracks/python/exercises/eliuds-eggs/approaches/parameter-modification
