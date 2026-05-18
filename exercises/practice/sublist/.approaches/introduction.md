# Introduction

There are four broad ways to solve Sublist, though one of them ("using strings") is not recommended.

## General guidance

To write the code, you need to branch out (probably with `if`) into the four different possible conditions, and return the appropriate category (`SUBLIST`, `SUPERLIST`, `EQUAL`, or `UNEQUAL`).

Note that you shouldn't return the category's value directly, as that would introduce [magic values][magic-values] into your code.

## Approach: List manipulation

The direct approach would be to manipulate and check the given lists to solve this.
This solution uses a helper function, which simplifies things, but the approach can be implemented without it.

```python
def check_sub_sequences(list_a, list_b):
    len_a = len(list_a)
    len_b = len(list_b)
    return any(list_b[i : i + len_a] == list_a for i in range(len_b - len_a + 1))

def sublist(list_one, list_two):
    if list_one == list_two:
        return EQUAL
    if check_sub_sequences(list_one, list_two):
        return SUBLIST
    if check_sub_sequences(list_two, list_one):
        return SUPERLIST
    return UNEQUAL
```

Read more on the [detail of this approach][approach-list-manipulation].

## Approach: Manual looping

This approach uses a helper function that manually loops through the lists to determine if the first list is a sublist of the second one.
This approach is the longest one by far, though it may be more comprehensible to some.

```python
def check_sub_sequences(list_a, list_b):
    len_a, len_b = len(list_a), len(list_b)
    index_a, index_b = 0, 0
    next_index_b = 1

    while index_a < len_a and index_b < len_b:
        if list_a[index_a] == list_b[index_b]:
            index_a += 1
        else:
            index_a, index_b = 0, next_index_b
            next_index_b += 1
        index_b += 1

    if index_a == len_a:
        if len_a == len_b:
            return EQUAL
        return SUBLIST
    return UNEQUAL

def sublist(list_one, list_two):
    result = check_sub_sequences(list_one, list_two)

    if result == UNEQUAL and check_sub_sequences(list_two, list_one) == SUBLIST:
        result = SUPERLIST
    return result
```

Learn more about the [details of this approach here][approach-manual-loop].

## Approach: Sorting lists

This approach uses the `sorted()` function to determine which list is shorter and which is longer.
Knowing this information, one can implement a simplified version of the list manipulation approach.

```python
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

Read more on the [detail of this approach][approach-sort-lists].

## Approach: Using strings

Another seemingly clever approach is to convert the lists to strings and then use the `in` operator to check for sub-sequences.
**However, this does not work.**

```python
def sublist(list_one, list_two):
    list_one_check = str(list_one).strip("[]") + ","
    list_two_check = str(list_two).strip("[]") + ","

    if list_one_check == list_two_check:
        return EQUAL
    if list_one_check in list_two_check:
        return SUBLIST
    if list_two_check in list_one_check:
        return SUPERLIST
    return UNEQUAL
```

To understand more about this approach and **why it fails**, [read here][approach-using-strings].

[magic-values]: https://stackoverflow.com/questions/47882/what-is-a-magic-number-and-why-is-it-bad
[approach-list-manipulation]: https://exercism.org/tracks/python/exercises/sublist/approaches/list-manipulation
[approach-manual-loop]: https://exercism.org/tracks/python/exercises/sublist/approaches/manual-loop
[approach-sort-lists]: https://exercism.org/tracks/python/exercises/sublist/approaches/sort-lists
[approach-using-strings]: https://exercism.org/tracks/python/exercises/sublist/approaches/using-strings
