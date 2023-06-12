# Using strings

Another clever solution is to convert the lists to strings and then use the `in` operator to check for sub-sequences.
Note that this approach is not as performant as the previous one.
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
Note that we can't use `.join` as it only accepts strings inside the iterable, while there the test cases have integers.

In this approach, we convert the lists to strings, so `[1, 2, 3]` becomes `"[1, 2, 3]"`, remove the brackets `"1, 2, 3"`, and add a comma `"1, 2, 3,"` so that there's a consistent pattern of number + comma while using the `in` operator.

We check equality and then use the `in` operator to check for `SUBLIST` or `SUPERLIST`, and finally return `UNEQUAL`.