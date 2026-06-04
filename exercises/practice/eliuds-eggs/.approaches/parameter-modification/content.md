# Modify the Parameter in a Loop

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


## Variation #1: Using Boolean Operators

```python
def egg_count(display_value):
    eggs = 0
    while display_value > 0:
        if display_value % 2 == 1:
            eggs += 1
        display_value //= 2
    return eggs
```

This is essentially just a more verbose formulation of the previous version.
Instead of relying on Python converting `int`s to `bool`s, this solution manually compares `display_value` to `0`.
It also uses an `if` statement to check if `eggs` should be incremented by `1`, instead of directly using the result of `display_value % 2`.

Even though this variant is more verbose than the others, some may consider it to be more readable.


## Variation #2: Using Bitwise Operators

```python
def egg_count(display_value):
    eggs = 0
    while display_value > 0:
        eggs += display_value & 1
        display_value >>= 1
    return eggs
```

This variant replaces the modulo (`%`) and floor division (`//`) with [bitwise operators][bitwise-operators].
`&` is the bitwise AND operator, which results in a number whose binary representation only has ones where _both_ of its arguments has ones.
(All other bits are zeros.)

For example, if we used the numbers `3` (`11` in binary) and `1` (`1` in binary), we get `1`:

```python
0b011 & 0b001
#=> 0b001
```

This is because the only bit in both numbers that is `1` is least significant bit.
This property lets us extract the least significant bit of `display_value` by using `display_value & 1`.

For the next step, we use `>>`, the [right-shift operator][right-shift-operator].
The expression `a >> b` shifts all of `a`'s bits to the right by `b` places, and returns the resulting number.

For example, if we used the numbers `5` (`101` in binary) and `1`, we get `2` (`10` in binary):

```python
0b101 >> 1
#=> 0b010
```

You can see how `& 1` and `>>= 1` perform the same function as the `% 2` and `//= 2` used in earier variants.


[bitwise-operators]: https://www.w3schools.com/programming/prog_operators_bitwise.php
[right-shift-operator]: https://www.geeksforgeeks.org/software-engineering/right-shift-operator-in-programming/
