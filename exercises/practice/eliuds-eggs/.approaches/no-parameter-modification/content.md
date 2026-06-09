# Loop Without Modifying the Parameter

```python
from math import ceil, log2

def egg_count(display_value):
    eggs = 0
    for bit_position in range(ceil(log2(display_value + 1))):
        eggs += (display_value >> bit_position) & 1
    return eggs
```

This approach uses a loop with `range()` to iterate over all of the bits in `display_value`.

To determine how many bits `display_value` has, this solution imports `ceil` and `log2` from the `math` module.
We then calculate the base 2 logarithm of `display_value` (plus 1) and round it up.
(Rounding up is neccessary because `range(<stop>)` excludes the value of `<stop>` from its returned values.)

Once we have the bit length of `display_value`, we feed this number into `range()` to make the `for-loop` iterate over all of `display_value`'s `bit_position`s.

For each `bit_position`, we determine the value of the bit at that position by using the [right-shift operator][right-shift-operator] and the bitwise AND operator.
We do this by right-shifting `display_value` by `bit_position`, making the bit at `bit_position` become the least significant bit.
Then we use the bitwise AND operator with `1` to remove all bits that are not the least significant bit.

~~~~exercism/note
You could also calculate the bit's value by using arithmetic operators instead of bitwise ones:

```python
eggs += (display_value // (2 ** bit_position)) % 2
```
~~~~

Once we determine the bit's value, we increment `eggs` by that number.

After the loop ends, we know that we have checked all of the bits in `display_value`, thus we return `eggs`.


## Variation #1: Using an `if` Statement

```python
from math import ceil, log2

def egg_count(display_value):
    eggs = 0
    for bit_position in range(ceil(log2(display_value + 1))):
        if display_value & (1 << bit_position):
            eggs += 1
    return eggs
```

In this variant, the loop uses an `if` statement to check if the digit at `display_value` is `1`.


## Variation #2: Using `sum()` with a Generator Expression

```python
from math import ceil, log2

def egg_count(display_value):
    return sum(
        (display_value >> bit_position) & 1
        for bit_position in range(ceil(log2(display_value + 1)))
    )
```

This variant is actually a one-liner, it is just split up here for readability.
Here, we replace the `for-loop` with a [generator expression][generator-expression] and use [`sum()`][sum-built-in] to collect the values into the result.


## Variation #3: Manually Tracking the Place Value

```python
def egg_count(display_value):
    eggs = 0
    place_value = 1
    while place_value <= display_value:
        if display_value & place_value:
            eggs += 1
        place_value <<= 1
    return eggs
```

This variant avoids `import`s by manually tracking the `place_value` of the current bit position.
This way, the `while-loop` can end when `place_value` becomes greater than `display_value`.

The operations in the loop are rather similar to the "using an `if` statement" variant.
The main differences are not having to calculate the `place_value` from the bit position, and having to manually progress the iteration by left-shifting `place_value` by `1` (which is the same as multiplying `place_value` by `2`).


[generator-expression]: https://dbader.org/blog/python-generator-expressions
[right-shift-operator]: https://www.geeksforgeeks.org/software-engineering/right-shift-operator-in-programming/
[sum-built-in]: https://docs.python.org/3/library/functions.html#sum
