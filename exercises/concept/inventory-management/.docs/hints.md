# Hints

## General

- [The Python Dictionary Tutorial](https://docs.python.org/3/tutorial/datastructures.html#dictionaries) can be a great introduction.

## 1. Create an inventory based on a list

- You need a [for loop](https://docs.python.org/3/tutorial/controlflow.html#for-statements) to iterate the list of items, then insert each item in the dictionary if missing and increment the item count using the dictionary accessor.
- You can use [`setdefault`](https://www.w3schools.com/python/ref_dictionary_setdefault.asp) to make sure the value is set before incrementing the count of the item.
- This function should [return a dict](https://www.w3schools.com/python/ref_keyword_return.asp).

## 2. Add items from a list to an existing dictionary

- You need a [for loop](https://docs.python.org/3/tutorial/controlflow.html#for-statements) to iterate the list of items, then insert each item if not already in the dictionary and [increment](https://www.w3schools.com/python/gloss_python_assignment_operators.asp) the item count using the dictionary accessor.
- You can use [`setdefault`](https://www.w3schools.com/python/ref_dictionary_setdefault.asp) to make sure the value is set before incrementing the count of the item.
- The function `add_items` can be used by the `create_inventory` function with an empty dictionary in parameter.
- This function should [return a dict](https://www.w3schools.com/python/ref_keyword_return.asp).

## 3. Decrement items from the inventory

- You need [for loop](https://docs.python.org/3/tutorial/controlflow.html#for-statements) to iterate the list of items, if the number of items is not `0` then [decrement](https://www.w3schools.com/python/gloss_python_assignment_operators.asp) the current number of items.
- You can use the `key in dict` that returns `True` if the key exists to make sure the value is in the dictionary before decrementing the number of items.
- This function should [return a dict](https://www.w3schools.com/python/ref_keyword_return.asp).

## 4. Remove an item entirely from the inventory

- If item is in the dictionary, [remove it](https://www.w3schools.com/python/ref_dictionary_pop.asp).
- If item is not in the dictionary, do nothing.
- This function should [return a dict](https://www.w3schools.com/python/ref_keyword_return.asp).

## 5. Return the inventory content

- You need [for loop](https://docs.python.org/3/tutorial/controlflow.html#for-statements) on the inventory and if the number of item is greater of `0` then append the tuple to a list.
- You can use `dict.items()` to iterate on both the item and the value at the same time, `items()` returns a tuple that you can use as it is or deconstruct.
- This function should [return](https://www.w3schools.com/python/ref_keyword_return.asp) a [list](https://docs.python.org/3/tutorial/introduction.html#lists) of [tuples](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences).
