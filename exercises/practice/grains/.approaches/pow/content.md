## `pow`

```python
def square(number):
    if number < 1 or number > 64:
        raise ValueError('square must be between 1 and 64')

    return pow(2, number - 1)


def total():
    return pow(2, 64) - 1

```

[`pow`][pow] is nicely suited to the problem, since we start with one grain and keep doubling the number of grains on each successive square.
`1` grain is `pow(2, 0)`, `2` grains is `pow(2, 1)`, `4` is `pow(2, 2)`, and so on.

So, to get the right exponent, we subtract `1` from the square `number`.

The easiest way to get `total` is to use `pow` to get the value for an imaginary 65th square,
and then subtract `1` from it.
To understand how that works, consider a board that has only two squares.
If we could grow the board to three squares, then we could get the number of grains on the imaginary third square,
which would be `4.`
You could then subtract `4` by `1` to get `3`, which is the number of grains on the first square (`1`) and the second square (`2`).
Remembering that the exponent must be one less than the square you want,
you can call `pow(2, 64)` to get the number of grains on the imaginary 65th square.
Subtracting that value by `1` gives the values on all `64` squares.

[pow]: https://docs.python.org/3/library/functions.html#pow
