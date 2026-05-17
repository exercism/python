# Introduction

There are four broad ways to solve Sublist, though one of them ("using strings") is not recommended.

## General guidance

To write the code, you need to branch out (probably with `if`) into the four different possible conditions, and return the appropriate category (`SUBLIST`, `SUPERLIST`, `EQUAL`, or `UNEQUAL`).

Note that you shouldn't return the category's value directly, as that would introduce [magic values][magic-values] into your code.

## Approach: List manipulation

The direct approach would be to manipulate and check the given lists to solve this.
This solution uses a helper function, which simplifies things, but the approach can be implemented without it.

```python
def check_sub_sequences(list_one, list_two):
    n1 = len(list_one)
    n2 = len(list_two)
    return any(list_two[i:i+n1] == list_one for i in range(n2 - n1 + 1))

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

Learn more about the [details of this approach here][approach-manual-loop].

## Approach: Sorting lists

This approach uses the `sorted()` function to determine which list is shorter and which is longer.
Knowing this information, one can implement a simplified version of the list manipulation approach.

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
