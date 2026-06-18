# Modify the Argument in a Loop

```python
def egg_count(display_value):
    eggs = 0
    while display_value:
        eggs += display_value % 2
        display_value //= 2
    return eggs
```

This approach uses a `while-loop` to count up the ones in the binary representation.
In the loop, we increment `eggs` by `display_value % 2`.
This adds the least significant bit (_the rightmost digit in the binary representation_) of `display_value` to `eggs`.

Next, we divide `display_value` by `2`, discarding any remainder.
This essentially removes the least significant bit of the current `display_value`, setting up the next iteration's `display_value` for processing the next bit.

This loop repeats until `display_value` reaches `0` (_which indicates that we have no more bits to process_), and then we return `eggs`.


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

This variant replaces the modulo (`%`) and floor division (`//`) operators with [bitwise operators][bitwise-operators].
`&` is the bitwise AND operator, which results in a number whose binary representation only has ones where _both_ of its arguments have ones (_all other bits become zeros_).

For example, if we use the numbers `3` (`11` in binary) and `1` (`1` in binary), we get `1`:

```python
0b011 & 0b001
#=> 0b001
```

This is because the only bit in both numbers that is `1` is their least significant bit.
This property lets us extract the least significant bit of `display_value` by using `display_value & 1`.

For the next step we use `>>`, the [right-shift operator][right-shift-operator].
The expression `a >> b` shifts all of `a`'s bits to the right by `b` places, and returns the resulting number.

For example, if we use the numbers `5` (`101` in binary) and `1`, we get `2` (`10` in binary):

```python
0b101 >> 1
#=> 0b010
```

You can see how `& 1` and `>>= 1` perform the same function as the `% 2` and `//= 2` used in earlier variants.


## Variation #3: Using a `list`

```python
def egg_count(display_value):
    egg_positions = []

    while display_value:
        egg_positions.append(display_value % 2)
        display_value //= 2

    return egg_positions.count(1)
```

Here, we append the binary digits to a `list` and then count the number of ones using [`list.count()`][sequence-count].
This solution would make sense if the positions of the eggs mattered, but since we only need the amount here, tracking the positions just adds unnecessary overhead.
Further overhead is added when `list.count()` iterates through the `list` to obtain the total.


## Variation #4: Using `divmod()`

```python
def egg_count(display_value):
    eggs = 0
    while display_value:
        display_value, remainder = divmod(display_value, 2)
        eggs += remainder
    return eggs
```

This variant uses the [`divmod()`][divmod-built-in] built-in instead of `%` and `//`.
(_For `int` arguments, `divmod(a, b)` returns a [`tuple`][concept-tuples] of `(a // b, a % b)`._)

Within the loop, `divmod(display_value, 2)` is used to get both the quotient and the remainder of the division.
The `tuple` returned by `divmod()` is [unpacked][concept-unpacking-and-multiple-assignment] into `display_value` and `remainder` using [multiple assignment][concept-unpacking-and-multiple-assignment].
`eggs` is then incremented by `remainder`.

As `display_value` is updated in the multiple assignment expression, we don't need to do anything else inside the loop.
Just like the previous variations, the loop will continue until `display_value` reaches 0, and then we return `eggs`.

[bitwise-operators]: https://www.w3schools.com/programming/prog_operators_bitwise.php
[concept-tuples]: https://exercism.org/tracks/python/concepts/tuples
[concept-unpacking-and-multiple-assignment]: https://exercism.org/tracks/python/concepts/unpacking-and-multiple-assignment
[divmod-built-in]: https://docs.python.org/3/library/functions.html#divmod
[right-shift-operator]: https://www.geeksforgeeks.org/software-engineering/right-shift-operator-in-programming/
[sequence-count]: https://docs.python.org/3/library/stdtypes.html#sequence.count
