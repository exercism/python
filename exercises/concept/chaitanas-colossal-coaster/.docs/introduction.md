In Python, a [`list`][list std type] is a mutable collection of items in _sequence_. Like most collections (see the built-ins tuple, dict and set), lists can hold reference to any (or multiple) data type(s) - including other lists.

Like any [sequence type][sequence type], items are referenced by 0-based index number and can be copied in whole or in part via _slice notation_. Lists support all [common sequence operations][common sequence operations], as well as [mutable sequence operations][mutable sequence operations]. They can be iterated over in a loop by using the for `item in <list>` construct.

Python also provides some additional [methods][list-methods] for working with lists. Let's take a look at some of them.

Keep in mind that when you manipulate a list with a list-method, **you alter the list** object that has been passed. If you do not wish to mutate your original `list`, you will need to make a copy of it via slice or `.copy()`.

### Adding Items

If you want to add an item to the end of an existing list, use `list.append()`:

```python
>>> numbers = [1, 2, 3]
>>> numbers.append(9)
>>> numbers
[1, 2, 3, 9]
```

Rather than _appending_, `list.insert()` gives you the ability to add the item to a _specific index_ in the list.

`list.insert()` takes 2 parameters:

1. the index of the item _before which_ you want the new item to appear
2. the item to be inserted

**Note**: If the given index is 0, the item will be added to the start of the list. If the supplied index is greater than the last index on the list, the item will be added in the final position -- the equivalent of using `list.append()`.

```python
>>> numbers = [1, 2, 3]
>>> numbers.insert(0, -2)
>>> numbers
[-2, 1, 2, 3]
>>> numbers.insert(1, 0)
>>> numbers
[-2, 0, 1, 2, 3]
```

If you have an iterable that you would like to _combine_ with your current list (concatenating the two), `list.extend()` can be used. `list.extend()` will _unpack_ the supplied iterable, adding its elements in the same order to the end of your list (_using `.append()` in this circumstance would add the entire iterable as a **single item**._).

```python
>>> numbers = [1, 2, 3]
>>> other_numbers = [5, 6, 7]

>>> numbers.extend(other_numbers)
>>> numbers
[1, 2, 3, 5, 6, 7]

>>> numbers.extend([8, 9])
>>> numbers
[1, 2, 3, 5, 6, 7, 8, 9]
```

### Removing Items

To delete an item from a list use `list.remove()`, passing the item to be removed as an argument. `list.remove()` will throw a `ValueError` if the item is not present in the list.

```python
>>> numbers = [1, 2, 3]
>>> numbers.remove(2)
>>> numbers
[1, 3]

# Trying to remove a value that is not in the list throws a ValueError
>>> numbers.remove(0)
ValueError: list.remove(x): x not in list
```

Alternatively, using the `list.pop()` method will both remove **and** `return` an element for use.

`list.pop()` takes one optional parameter: the index of the item you need to remove and receive. If the optional index argument is not specified, the last element of the list will be removed and returned to you. If you specify an index number higher than the length of the list, you will get an `IndexError`.

```python
>>> numbers = [1, 2, 3]
>>> numbers.pop(0)
1
>>> numbers
[2, 3]
>>> numbers.pop()
3
>>> numbers
[2]
>>> numbers.pop(1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: pop index out of range
```

If you want to remove all items from a `list`, use `list.clear()`. It does not take any parameters.

```python
>>> numbers = [1, 2, 3]
>>> numbers.clear()
>>> numbers
[]
```

### Reversing and reordering

You can reverse the order of a list with the `list.reverse()` method.

```python
>>> numbers = [1, 2, 3]
>>> numbers.reverse()
>>> numbers
[3, 2, 1]
```

A list can be re-ordered _**in place**_ with the help of `list.sort()`. Internally, Python uses [`Timsort`][timsort] to arrange the list. The default order is _ascending_. Take a look at the Python docs for some [additional tips and techniques for sorting][sorting how to] lists effectively.

```python
>>> names = ["Tony", "Natasha", "Thor", "Bruce"]

# The default sort order is *ascending*.
>>> names.sort()
>>> names
["Bruce", "Natasha", "Thor", "Tony"]
```

If you want the sort to be in descending order, pass the `reverse=True` argument:

```python
>>> names = ["Tony", "Natasha", "Thor", "Bruce"]
>>> names.sort(reverse=True)
>>> names
["Tony", "Thor", "Natasha", "Bruce"]
```

For cases where sorting the original list is undesirable, the built-in [`sorted()`][sorted] can be used to return a new, sorted copy of your original list.

### Occurrences of an item in a list

You can find the number of occurrences of an element in a list with the help of `list.count()`. It takes the item you need to tally as its argument and returns the total number of times it appears on the list.

```python
>>> items = [1, 4, 7, 8, 2, 9, 2, 1, 1, 0, 4, 3]
>>> items.count(1)
3
```

### Finding the index of items

`list.index()` will return the index number of the _first occurrence_ of an item passed in. If there are no occurrences, a `ValueError` is raised. If you don't need the exact position of an item and are only checking that it is present inside the list, the built-in `in` operator is more efficient.

Indexing is zero-based, meaning the position of the first item is `0`.

```python
>>> items = [7, 4, 1, 0, 2, 5]
>>> items.index(4)
1
>>> items.index(10)
ValueError: 10 is not in list
```

You can also provide `start` and `end` indices to search within a specific section of the list:

```python
>>> names = ["Tina", "Leo", "Thomas", "Tina", "Emily", "Justin"]
>>> names.index("Tina")
0
>>> names.index("Tina", 2, 5)
3
```

### Making Copies

Remember that variables in Python are labels that point to underlying objects.

If you assign a list object to a new variable name, any change you make to the items in the list using the new variable name will also _impact the original_, because both variable names point to the **same list object** and all of its underlying items.

To avoid this complicaton, you must make a copy via `list.copy()` or slice.

```python
>>> actual_names = ["Tony", "Natasha", "Thor", "Bruce"]

# Assinging a new variable name does not make a copy of the container or its data.
>>> same_list = actual_names

#  Altering the list via the new name is the same as altering the list via the old name.
>>> same_list.append("Clarke")
>>> same_list
["Tony", "Natasha", "Thor", "Bruce", "Clarke"]
>>> actual_names
["Tony", "Natasha", "Thor", "Bruce", "Clarke"]

#  Likewise, altering the data in the list via the original nane will also alter the data under the new name.
>>> actual_names[0] = "Wanda"
>>> same_list
['Wanda', 'Natasha', 'Thor', 'Bruce', 'Clarke']

# If you copy the list, there will be two seperate list objects which can be changed independantly.
>>> copied_list = actual_names.copy()
>>> copied_list[0] = "Tony"
>>> actual_names
['Wanda', 'Natasha', 'Thor', 'Bruce', 'Clarke']
>>> copied_list
["Tony", "Natasha", "Thor", "Bruce", "Clarke"]
```

[list-methods]: https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
[list std type]: https://docs.python.org/3.9/library/stdtypes.html#list
[timsort]: https://en.wikipedia.org/wiki/Timsort
[sorted]: https://docs.python.org/3/library/functions.html#sorted
[sorting how to]: https://docs.python.org/3/howto/sorting.html
[sequence type]: https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range
[common sequence operations]: https://docs.python.org/3/library/stdtypes.html#common-sequence-operations
[mutable sequence operations]: https://docs.python.org/3/library/stdtypes.html#typesseq-mutable
