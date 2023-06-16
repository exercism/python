# Introduction
There are two broad ways to solve Sublist. 

## General guidance
To write the code, you need to branch out (probably with `if`) into the four different possible conditions, and return the appropriate name of the category. 

## Approach: list manipulation
The direct approach would be to manipulate and check the given lists to solve this.
This solution uses a helper function, which simplifies things, but the approach can be implemented without it.

```python
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4

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

## Approach: using strings
Another seemingly clever approach is to convert the lists to strings and then 
use the `in` operator to check for sub-sequences.
**However, this does not work.**
```python
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4

def sublist(list_one, list_two):
    list_one_check = (str(list_one).strip("[]") + ",")
    list_two_check = (str(list_two).strip("[]") + ",")

    if list_one_check == list_two_check:
        return EQUAL
    elif list_one_check in list_two_check:
        return SUBLIST
    elif list_two_check in list_one_check:
        return SUPERLIST
    return UNEQUAL
```
To understand more about this approach and **why it fails**, [read here][approach-using-strings].

[approach-list-manipulation]: https://exercism.org/tracks/python/exercises/sublist/approaches/list-manipulation
[approach-using-strings]: https://exercism.org/tracks/python/exercises/sublist/approaches/using-strings
