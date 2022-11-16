# Bit-shifting

```python
def square(number):
    if number < 1 or number > 64:
        raise ValueError('square must be between 1 and 64')

    return 1 << number - 1


def total():
    return (1 << 64) - 1

```

Instead of using math for calculation, you can set a bit in the correct position for the number of grains on a square.

To understand how this works, consider just two squares that are represented in binary bits as `00`.

You use the [left-shift operator][left-shift-operator] to set `1` at the position needed to make the correct decimal value.
- To set the one grain on Square One you shift `1` for `0` positions to the left.
So, if `number` is `1` for square One, you subtract `number` by `1` to get `0`, which will not move it any positions to the left.
The result is binary `01`, which is decimal `1`.
- To set the two grains on Square Two you shift `1` for `1` position to the left.
So, if `number` is `2` for square Two, you subtract `number` by `1` to get `1`, which will move it `1` position to the left.
The result is binary `10`, which is decimal `2`.

| Square  | Shift Left By | Binary Value | Decimal Value |
| ------- | ------------- | ------------ | ------------- |
|       1 |             0 |         0001 |             1 |
|       2 |             1 |         0010 |             2 |
|       3 |             2 |         0100 |             4 |
|       4 |             3 |         1000 |             8 |

For `total` we want all of the 64 bits set to `1` to get the sum of grains on all sixty-four squares.
The easy way to do this is to set the 65th bit to `1` and then subtract `1`.
To go back to our two-square example, if we can grow to three squares, then we can shift `1` two positions to the left for binary `100`,
which is decimal `4`.
By subtracting `1` we get `3`, which is the total amount of grains on the two squares.

| Square  | Binary Value | Decimal Value |
| ------- | ------------ | ------------- |
|       3 |         0100 |             4 |

| Square  | Sum Binary Value | Sum Decimal Value |
| ------- | ---------------- | ----------------- |
|       1 |             0001 |                 1 |
|       2 |             0011 |                 3 |

[left-shift-operator]: https://realpython.com/python-bitwise-operators/#left-shift
