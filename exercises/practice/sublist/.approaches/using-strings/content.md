# Using strings

~~~~exercism/caution
**This approach does not work, and this document exists to explain that.**
Please do not use it in your code.
~~~~

Another seemingly clever solution is to convert the lists to strings and then use the `in` operator to check for sub-sequences.
Note that this approach, even if it worked, is not as performant as the previous one.

```python
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4

def sublist(list_one, list_two):
    list_one_check = str(list_one).strip("[]")
    list_two_check = str(list_two).strip("[]")

    if list_one_check == list_two_check:
        return EQUAL
    if list_one_check in list_two_check:
        return SUBLIST
    if list_two_check in list_one_check:
        return SUPERLIST
    return UNEQUAL
```

Let's parse the code to see what it does.
In this approach, we convert the lists to strings, so `[1, 2, 3]` becomes `"[1, 2, 3]"`, remove the brackets `"1, 2, 3"`, and add a comma `"1, 2, 3,"`.
We check equality and then use the `in` operator to check for `SUBLIST` or `SUPERLIST`, and finally return `UNEQUAL`.

We add a comma because, say, we call `sublist` with `[1, 2]` and `[1, 22]`. `"1, 2" in "1, 22"` evaluates to `True`, so the **function would wrongly mark it as `SUBLIST`**.

This case can be handled by changing the code like this:

```python
list_one_check = str(list_one).strip("[]") + ","
list_two_check = str(list_two).strip("[]") + ","
```

Yet, even though the code would pass all of the tests in the Exercism test suite, it would still fail in some cases.
For example, if we call `sublist` with `[1, 2]` and `[5, "1, 2,", 7]`, the function would return `SUBLIST` when it should actually return `UNEQUAL`.

This could be avoided by changing the code to use a separator that isn't the default one:

```python
list_one_check = "|".join(str(item) for item in list_one) + "|"
list_two_check = "|".join(str(item) for item in list_two) + "|"
```

However, this only avoids the (theoretical) test and does not fix the solution. For example, a test with the inputs `[1, 2]` and `[5, "1|2|", 7]` would now fail.

No matter what separator is chosen, there will always be at least one input for which the function will return the wrong result. **This is why no approach that converts the lists to strings can ever be correct for all possible inputs.**
