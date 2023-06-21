# Using strings
~~~~exercism/caution
**This approach does not work, and this document exists to explain that.** 
Please do not use it in your code.
~~~~

Another seemingly clever solution is to convert the lists to strings and then 
use the `in` operator to check for sub-sequences.
Note that this approach, even if it worked, is not as performant as the 
previous one.
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
    elif list_one_check in list_two_check:
        return SUBLIST
    elif list_two_check in list_one_check:
        return SUPERLIST
    return UNEQUAL
```
Let's parse the code to see what it does.
In this approach, we convert the lists to strings, so `[1, 2, 3]` becomes `"[1, 2, 3]"`, remove the brackets `"1, 2, 3"`, and add a comma `"1, 2, 3,"`. 
We check equality and then use the `in` operator to check for `SUBLIST` or `SUPERLIST`, and finally return `UNEQUAL`.

We add a comma because, say, we call `sublist` with `[1, 2]` and `[1, 22]`. `"1, 2" in "1, 22"` evaluates to `True`, so 
the **function would wrongly mark it as `SUBLIST`**. 

This test can be overridden by changing the code like this:
```python
list_one_check = str(list_one).strip("[]") + ','
list_two_check = str(list_two).strip("[]") + ','
```
Yet, the test case (which doesn't exist in the Exercism test suite) `["1", "2"]` and `["5", "'1', '2',", "7"]` would 
fail.

Students can add any arbitrary string into the representation to try to "defeat" this test - `list_one_check = str
(list_one) + TOKEN`. The test suite currently test `TOKEN = ''`, but not others.

[gen-exp]: https://www.programiz.com/python-programming/generator