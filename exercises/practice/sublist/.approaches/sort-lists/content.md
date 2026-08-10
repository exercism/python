# Sorting lists

This approach uses the `sorted()` function to determine which list is shorter and which is longer.
Knowing this information, one can implement a simplified version of the [list manipulation approach][approach-list-manipulation].

```python
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4

def sublist(list_one, list_two):
    if list_one == list_two:
        return EQUAL
    if not list_one:
        return SUBLIST
    if not list_two:
        return SUPERLIST

    shorter, longer = sorted((list_one, list_two), key=len)

    for index in range(len(longer) - len(shorter) + 1):
        if longer[index : index + len(shorter)] == shorter:
            return SUPERLIST if longer is list_one else SUBLIST

    return UNEQUAL
```

Here, the case of the lists being equal is checked first.
Then the special cases of empty lists are handled, returning `SUBLIST` or `SUPERLIST` as necessary.

Once those simple cases are out of the way, the `sorted()` function is used with the keyword argument `key` set to the `len()` function.
This makes `sorted()` sort the items according to their length.

Once `sorted()` does its work, we use multiple assignment to unpack the results into the `shorter` and `longer` variables.
Then, for each slice of length `len(shorter)` in `longer`, we test if that slice is equal to `shorter`.

If we find such a slice, that means `shorter` is a sublist of `longer`.
Then we use a [conditional expression][conditional-expression] along with the `is` operator to return `SUBLIST` or `SUPERLIST` depending on which of the original lists is `longer`.

If we do not find such a slice, we can eliminate `SUBLIST` and `SUPERLIST` from the possible categories, thus the two lists must be `UNEQUAL`.

[approach-list-manipulation]: https://exercism.org/tracks/python/exercises/sublist/approaches/list-manipulation
[conditional-expression]: https://docs.python.org/3/reference/expressions.html#conditional-expressions
