# Manual looping

This approach uses a helper function that manually loops through the lists to determine if the first list is a sublist of the second one.
This approach is significantly longer than the [list manipulation approach][approach-list-manipulation], though it may be more comprehensible to some.

```python
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4

def check_sub_sequences(list_one, list_two):
    index_one = 0
    index_two = 0
    next_index_two = 1

    while index_one < len(list_one) and index_two < len(list_two):
        if list_one[index_one] == list_two[index_two]:
            index_one += 1
        else:
            index_one = 0
            index_two = next_index_two
            next_index_two += 1
        index_two += 1

    if index_one == len(list_one):
        if len(list_one) == len(list_two):
            return EQUAL
        return SUBLIST
    return UNEQUAL

def sublist(list_one, list_two):
    result = check_sub_sequences(list_one, list_two)
    if result == UNEQUAL and check_sub_sequences(list_two, list_one) == SUBLIST:
        result = SUPERLIST
    return result
```

In this approach, the first thing `sublist()` does is call the helper function.
That function then loops through the lists, keeping track of an index for both lists so it can test all necessary combinations to determine if `list_one` is a sublist of `list_two`.

However, the helper function only determines if `list_one` is equal to or a sublist of `list_two`, not if `list_one` is a superlist of `list_two`.
That is why if the helper function returns `UNEQUAL`, `sublist()` needs to make sure that it isn't acutally a superlist.

`sublist()` does this by calling the helper function with its arguments reversed: `check_sub_sequences(list_two, list_one)`.
If the result is `SUBLIST`, that means `list_two` is a sublist of `list_one`, thus `list_one` must be a superlist of `list_two`.

Thus all possibilities are covered, and `sublist()` returns the result.

[approach-list-manipulation]: https://exercism.org/tracks/python/exercises/sublist/approaches/list-manipulation
