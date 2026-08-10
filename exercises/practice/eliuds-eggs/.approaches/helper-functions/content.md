# Use Helper Functions


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

In this specific version of the approach, `convert_to_binary()` is implemented similarly to the [modify the argument in a loop][approach-argument-modification] approach.
The main differences are that the bits are converted to strings and concatenated (_rather than being added together_), and that a [conditional expression][conditional-expression] (_also called a ternary operator_) is used to handle the edge case of a `0`.


~~~~exercism/note
Here, the [`or` operator][boolean-operations-default-or] could be used instead of a conditional expression:

```python
return binary_value[::-1] or "0"
```

Which one to use is mostly a matter of preference and readability.

[boolean-operations-default-or]: https://docs.python.org/3/reference/expressions.html#boolean-operations:~:text=if%20s%20is%20a%20string%20that%20should%20be%20replaced%20by%20a%20default%20value%20if%20it%20is%20empty,%20the%20expression%20s%20or%20'foo'%20yields%20the%20desired%20value.
~~~~


The `count_ones()` helper function is implemented very similarly to the [convert to a binary string][approach-convert-to-binary-string] approach.
The only difference is that it takes the binary string as an argument rather than calculating it.

Though breaking a problem up into helper functions may facilitate code reuse, here it adds unnecessary overhead to the solution.
This approach is also complicated by additional edge cases, such as making `convert_to_binary()` return "0" instead of an empty string when given the number `0`.
Additionally, the edge case of negative numbers is not handled, and doing so would complicate the solution even further:

```python
def convert_to_binary(decimal_value):
    if decimal_value < 0:
        return "-" + convert_to_binary(-decimal_value)

    binary_value = ""

    while decimal_value > 0:
        binary_value += str(decimal_value % 2)
        decimal_value //= 2

    return binary_value[::-1] or "0"
```

Due to these scenarios, one may decide to forego handling all the edge cases.
However, when your future self (_or someone else_) tries to reuse the function, edge cases could produce errors or unexpected results.


[approach-argument-modification]: https://exercism.org/tracks/python/exercises/eliuds-eggs/approaches/argument-modification
[approach-convert-to-binary-string]: https://exercism.org/tracks/python/exercises/eliuds-eggs/approaches/convert-to-binary-string
[conditional-expression]: https://docs.python.org/3/reference/expressions.html#conditional-expressions
