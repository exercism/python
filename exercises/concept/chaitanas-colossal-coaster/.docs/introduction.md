# Introduction

A [`list`][list] is a mutable collection of items in _sequence_.
 Like most collections (_see the built-ins [`tuple`][tuple], [`dict`][dict] and [`set`][set]_), lists can hold reference to any (or multiple) data type(s) - including other lists.
 Lists can be copied in whole or in part via [slice notation][slice notation] or through the use of `<list>.copy()`.
 Like any [sequence][sequence type], elements within `lists` are referenced by `0-based index` number from the left, or `-1-based index` number from the right.

Lists support both [common][common sequence operations] and [mutable][mutable sequence operations] sequence operations such as `min(<list>)`/`max(<list>)`, `<list>.index()`, `<list>.append()` and `<list>.reverse()`.
 Elements inside a `list`  can be iterated over using the `for item in <list>` construct.
 `for index, item in enumerate(<list>)` can be used when both the element index and element value are needed.

Python also provides many useful [list-methods][list-methods] for working with lists.
 A selection of these `list methods` is covered below.


Note that when you manipulate a `list` with a `list-method`, **you alter the list** object that has been passed.
 If you do not wish to mutate the original `list`, you will need to at least make a `shallow copy` of it via slice or `<list>.copy()`.


## Adding Items

To add an item to the end or "right-hand side" of an existing list, use `<list>.append(<item>)`:

```python
>>> numbers = [1, 2, 3]
>>> numbers.append(9)

>>> numbers
[1, 2, 3, 9]
```

Rather than _appending_, `<list>.insert()` gives you the ability to add the item to a _specific index_ in the list.
It takes 2 parameters:

1. the `<index>` at which you want the item to be inserted.
2. the `<item>` to be inserted.

**Note**: If the given `index` is 0, the item will be added to the start ("left-hand side") of the `list`.
 If the supplied `index` is greater than the final `index` on the `list`, the item will be added in the final position -- the equivalent of using `<list>.append(<item>)`.


```python
>>> numbers = [1, 2, 3]
>>> numbers.insert(0, -2)

>>> numbers
[-2, 1, 2, 3]

>>> numbers.insert(1, 0)

>>> numbers
[-2, 0, 1, 2, 3]
```


`<list>.extend(<item>)` can be used to combine an existing list with the elements from another iterable (for example, a `set`, `tuple`, `str`, or `list`).
  The iterable is _unpacked_ and elements are appended in order (_Using `<list>.append(<item>)` in this circumstance would add the entire iterable as a **single item**._).


```python
>>> numbers = [1, 2, 3]
>>> other_numbers = [5, 6, 7]

>>> numbers.extend(other_numbers)

>>> numbers
[1, 2, 3, 5, 6, 7]

>>> numbers.extend([8, 9])

>>> numbers
[1, 2, 3, 5, 6, 7, 8, 9]

>>> numbers.append([8,9])

>>> numbers
[1, 2, 3, 5, 6, 7, 8, 9, [8, 9]]
```


## Removing Items

To delete an item from a list use `<list>.remove(<item>)`, passing the item to be removed as an argument.
 `<list>.remove(<item>)` will throw a `ValueError` if the item is not present in the `list`.


```python
>>> numbers = [1, 2, 3]
>>> numbers.remove(2)

>>> numbers
[1, 3]

# Trying to remove a value that is not in the list throws a ValueError
>>> numbers.remove(0)
ValueError: list.remove(x): x not in list
```


Alternatively, using the `<list>.pop(<index>)` method will both remove **and** `return` an element for use.


`<list>.pop(<index>)` takes one optional parameter: the `index` of the item to be removed and returned.
 If the (optional) `index` argument is not specified, the final element of the `list` will be removed and returned.
 If the `index` specified is higher than the final item `index`, an `IndexError` is raised.


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

All elements can be removed from a `list` with `list.clear()`. It doesn't take any parameters.

```python
>>> numbers = [1, 2, 3]
>>> numbers.clear()

>>> numbers
[]
```

## Reversing and reordering

The `<list>.reverse()` method will reverse the order of elements **in-place**.


```python
>>> numbers = [1, 2, 3]
>>> numbers.reverse()

>>> numbers
[3, 2, 1]
```


A list can be re-ordered _**in place**_ with the help of `<list>.sort()`.
 Internally, Python uses [`Timsort`][timsort] to arrange the list.
 Default order is _ascending_ from the left.
 The Python docs offer [additional tips and techniques for sorting][sorting how to] lists effectively.


```python
>>> names = ["Tony", "Natasha", "Thor", "Bruce"]

# The default sort order is *ascending*.
>>> names.sort()

>>> names
["Bruce", "Natasha", "Thor", "Tony"]
```

If a _descending_ order is desired, pass the `reverse=True` argument:

```python
>>> names = ["Tony", "Natasha", "Thor", "Bruce"]
>>> names.sort(reverse=True)

>>> names
["Tony", "Thor", "Natasha", "Bruce"]
```

For cases where mutating the original list is undesirable, the built-in [`sorted(<iterable>)`][sorted] function can be used to return a sorted **copy**.


```python
>>> names = ["Tony", "Natasha", "Thor", "Bruce"]

>>> sorted(names)
['Bruce', 'Natasha', 'Thor', 'Tony']
```


## Occurrences of an item in a list

The number of occurrences of an element in a list can be calculated with the help of `list.count(<item>)`.
 It takes the `item` to be counted as its argument and returns the total number of times that element appears in the `list`.


```python
>>> items = [1, 4, 7, 8, 2, 9, 2, 1, 1, 0, 4, 3]

>>> items.count(1)
3
```

## Finding the index of items

`<list>.index(<item>)` will return the `index` number of the _first occurrence_ of an item passed in.
 If there are no occurrences, a `ValueError` is raised.
 If the exact position of an item isn't needed, the built-in `in` operator is more efficient for checking if a list contains a given value.


Indexing is zero-based from the left, so the position of the "first" item is `0`.
Indexing will also work from the right, beginning with `-1`.


```python
>>> items = [7, 4, 1, 0, 2, 5]

>>> items.index(4)
1

>>> items.index(10)
ValueError: 10 is not in list
```

`start` and `end` indices can also be provided to narrow the search to a specific section of the `list`:

```python
>>> names = ["Tina", "Leo", "Thomas", "Tina", "Emily", "Justin"]

>>> names.index("Tina")
0

>>> names.index("Tina", 2, 5)
3
```


[common sequence operations]: https://docs.python.org/3/library/stdtypes.html#common-sequence-operations
[dict]: https://docs.python.org/3/library/stdtypes.html#dict
[list-methods]: https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
[list]: https://docs.python.org/3/library/stdtypes.html#list
[mutable sequence operations]: https://docs.python.org/3/library/stdtypes.html#typesseq-mutable
[sequence type]: https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range
[set]: https://docs.python.org/3/library/stdtypes.html#set
[slice notation]: https://docs.python.org/3/reference/expressions.html#slicings
[sorted]: https://docs.python.org/3/library/functions.html#sorted
[sorting how to]: https://docs.python.org/3/howto/sorting.html
[timsort]: https://en.wikipedia.org/wiki/Timsort
[tuple]: https://docs.python.org/3/library/stdtypes.html#tuple
