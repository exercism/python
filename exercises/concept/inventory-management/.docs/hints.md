# Hints

## General

- [The Python Dictionary Tutorial][dict-tutorial] can be a great place to start.
- The Python docs on [Mapping Types - dicts][dict docs] is also pretty helpful.

## 1. Create an inventory based on a list

- You need a [for loop][for-loop] to iterate the list of items, then insert each item in the dictionary if missing and increment the item count using the dictionary accessor.
- You can use [`dict.setdefault`][dict setdefault] to make sure the value is set before incrementing the count of the item.
- This function should [return][return-keyword] a dict].

## 2. Add items from a list to an existing dictionary

- You need a [for loop][for-loop] to iterate the list of items, then insert each item if not already in the dictionary and [increment][increment] the item count using the dictionary accessor.
- You can use [`dict.setdefault`][dict setdefault] to make sure the value is set before incrementing the count of the item.
- The function `add_items` can be used by the `create_inventory` function with an empty dictionary in parameter.
- This function should [return][return-keyword] a dict.

## 3. Decrement items from the inventory

- You need [for loop][for-loop] to iterate the list of items, if the number of items is not `0` then [decrement][decrement] the current number of items.
- You can use the check `key in dict` that returns `True` if the key exists to make sure the value is in the dictionary before decrementing the number of items.
- This function should [return][return-keyword] a dict.

## 4. Remove an item entirely from the inventory

- If item is in the dictionary, [remove it][dict-pop].
- If item is not in the dictionary, do nothing.
- This function should [return][return-keyword] a dict.

## 5. Return the inventory content

- You need to use a [for loop][for-loop] on the inventory and if the number of item is greater of `0` then append the `tuple` to a `list`.
- You can use [`dict.items()`][dict items] to iterate on both the item and the value at the same time, `items()` returns a `tuple` that you can use or deconstruct, if needed.
- This function should [return][return-keyword] a [list][list] of [tuples][tuples].

[decrement]: https://www.w3schools.com/python/gloss_python_assignment_operators.asp
[dict docs]: https://docs.python.org/3/library/stdtypes.html#mapping-types-dict
[dict items]: https://docs.python.org/3/library/stdtypes.html#dict.items
[dict setdefault]: https://www.w3schools.com/python/ref_dictionary_setdefault.asp
[dict-pop]: https://www.w3schools.com/python/ref_dictionary_pop.asp
[dict-tutorial]: https://docs.python.org/3/tutorial/datastructures.html#dictionaries
[for-loop]: https://docs.python.org/3/tutorial/controlflow.html#for-statements
[increment]: https://www.w3schools.com/python/gloss_python_assignment_operators.asp
[list]: https://docs.python.org/3/tutorial/introduction.html#lists
[return-keyword]: https://www.w3schools.com/python/ref_keyword_return.asp
[tuples]: https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences
