# About

A [`list`][list] is a mutable collection of items in _sequence_. Like most collections (_see the built-ins [`tuple`][tuple], [`dict`][dict] and [`set`][set]_), lists can hold references to any (or multiple) data type(s) - including other lists.
They're considered a [sequence][sequence type] in Python, and can be copied in whole or in part via [slice notation][slice notation].
Like any sequence, elements within `lists` can be referenced by `0-based index` number from the left, or `-1-based index` number from the right.

Lists support both [common][common sequence operations] and [mutable][mutable sequence operations] sequence opterations like `min(<list>)`/`max(<list>)`, `<list>.index()`, `<list>.append()` and `<list>.reverse()`.
Items can be iterated over using the `for item in <list>` construct, and `for index, item in enumerate(<list>)` can be used when both the element and element index are needed.

Python provides many useful [methods][list-methods] for working with lists.

Becasue `lists` are mutable, list-methods **alter the original list object** passed into the method.
If mutation is undesirable, the original `list` needs to at least be copied via `shallow copy` via `slice` or `<list>.copy()`.

## Adding Items

Adding items to the end of an existing list can be done via `<list>.append(<item>)`:

```python
>>> numbers = [1, 2, 3]
>>> numbers.append(9)
>>> numbers
[1, 2, 3, 9]
```

Rather than _appending_, `<list>.insert(<index>, <item>)` adds the item to a _specific index_ within the list.
`<index>` is the index of the item _before which_ you want the new item to appear.
`<item>` is the element to be inserted.

**Note**: If `<index>` is 0, the item will be added to the start of the list.
If `<index>` is greater than the final index on the list, the item will be added in the final position -- the equivalent of using `<list>.append(<item>)`.

```python
>>> numbers = [1, 2, 3]
>>> numbers.insert(0, -2)
>>> numbers
[-2, 1, 2, 3]

>>> numbers.insert(1, 0)
>>> numbers
[-2, 0, 1, 2, 3]
```

An `iterable` can be _combined_ with an existing list (concatenating the two) via `<list>.extend(<iterable>)`.
`<list>.extend(<iterable>)` will _unpack_ the supplied iterable, adding its elements in the same order to the end of the target list (_using `<list>.append(<item>)` in this circumstance would add the entire iterable as a **single item**._).

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

<br>

## Removing Items

`<list>.remove(<item>)` can be used to remove an element from the list.
`<list>.remove(<item>)` will throw a `ValueError` if the element is not present in the list.

```python
>>> numbers = [1, 2, 3]
>>> numbers.remove(2)
>>> numbers
[1, 3]

# Trying to remove a value that is not in the list throws a ValueError.
>>> numbers.remove(0)
ValueError: list.remove(x): x not in list
```

Alternatively, using `<list>.pop(<item>)` method will both remove **and** `return` an element for use.

`<list>.pop(<item>)` takes one optional parameter: the `index` of the element to remove and return.
If the optional `<index>` argument is not specified, the last element of the list will be removed and returned.
If `<index>` is a higher number than the final index of the list, an `IndexError` will be thrown.

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

# This will throw an error because there is only index 0.
>>> numbers.pop(1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: pop index out of range
```

All items can be removed from a `list` via `<list>.clear()`. It does not take any parameters.

```python
>>> numbers = [1, 2, 3]
>>> numbers.clear()
>>> numbers
[]
```

<br>

## Reversing and reordering

The order of list elements can be reversed  _**in place**_ with `<list>.reverse()`. This will mutate the original list.

```python
>>> numbers = [1, 2, 3]
>>> numbers.reverse()
>>> numbers
[3, 2, 1]
```

List elements can be sorted _**in place**_ using `<list>.sort()`.
Internally, Python uses [`Timsort`][timsort] to arrange the elements.
The default order is _ascending_.
The Python docs have [additional tips and techniques for sorting][sorting how to] `lists` effectively.

```python
>>> names = ["Tony", "Natasha", "Thor", "Bruce"]

# The default sort order is *ascending*.
>>> names.sort()
>>> names
["Bruce", "Natasha", "Thor", "Tony"]
```

To sort a list in _descending_ order, pass a `reverse=True` argument to the method:

```python
>>> names = ["Tony", "Natasha", "Thor", "Bruce"]
>>> names.sort(reverse=True)
>>> names
["Tony", "Thor", "Natasha", "Bruce"]
```

For cases where mutating the original `list` is undesirable, the built-in functions [`sorted()`][sorted] and [`reversed()`][reversed] can be used.
`sorted(<list>)` will return a sorted _copy_, and takes the same parameters as `<list>.sort()`.
`reversed(<list>)` returns an _iterator_ that yields the list's items in reverse order.
`Iterators` will be covered in detail in another exercise.

<br>

## Occurrences of an item in a list

Finding the number of occurrences of an element in a list can be done with the help of `<list>.count(<item>)`.
It returns the total number of times `<item>` appears as an element in the list.

```python
>>> items = [1, 4, 7, 8, 2, 9, 2, 1, 1, 0, 4, 3]
>>> items.count(1)
3
```

<br>

## Finding the index of items

`<list>.index(<item>)` will return the index number of the _first occurrence_ of an item passed in.
If there are no occurrences, a `ValueError` is raised.
Indexing is 0-based from the left, meaning the position of the first item is index `0`.

```python
>>> items = [7, 4, 1, 0, 2, 5]
>>> items.index(4)
1
>>> items.index(10)
ValueError: 10 is not in list
```

Providing `start` and `end` indices will search within a specific section of the list:

```python
>>> names = ["Tina", "Leo", "Thomas", "Tina", "Emily", "Justin"]
>>> names.index("Tina")
0
>>> names.index("Tina", 2, 5)
3
```

If the exact position of an element is not needed, the built-in `in` operator is more efficient for verifying membership.

```python
>>> names = ["Tina", "Leo", "Thomas", "Tina", "Emily", "Justin"]
>>> "Thomas" in names
True
```

<br>

## Making Copies

Remember that variables in Python are labels that point to underlying objects and `lists` are _container_ objects that only hold references to their contained items.

Assigning a `list` object to a new variable _name_ does not copy the object or any of its referenced data. Any change made to the items in the `list` using the new variable name will also _impact the original_.

`<list>.copy()` will create a new `list` object, but **will not** create new objects for the referenced list _elements_. This is called a `shallow copy`. A `shallow copy` is usually enough when you want to add or remove items from one of the `list` objects without modifying the other. But if there is any chance that the _underlying_ elements of a `list` might be accidentally mutated (_thereby mutating all related shallow copies_), [`copy.deepcopy()`][deepcopy] in the `copy` module should be used to create a complete or "deep" copy of **all** references and objects.

For a detailed explanation of names, values, list, and nested list behavior, take a look at this excellent blog post from [Ned Batchelder][ned batchelder] -- [Names and values: making a game board][names and values].

[list-methods]: https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
[timsort]: https://en.wikipedia.org/wiki/Timsort
[sorted]: https://docs.python.org/3/library/functions.html#sorted
[reversed]: https://docs.python.org/3/library/functions.html#reversed
[sorting how to]: https://docs.python.org/3/howto/sorting.html
[list]: https://docs.python.org/3/library/stdtypes.html#list
[tuple]: https://docs.python.org/3/library/stdtypes.html#tuple
[set]: https://docs.python.org/3/library/stdtypes.html#set
[dict]: https://docs.python.org/3/library/stdtypes.html#dict
[common sequence operations]: https://docs.python.org/3/library/stdtypes.html#common-sequence-operations
[slice notation]: https://docs.python.org/3/reference/expressions.html#slicings
[sequence type]: https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range
[deepcopy]: https://docs.python.org/3/library/copy.html
[mutable sequence operations]: https://docs.python.org/3/library/stdtypes.html#typesseq-mutable
[names and values]: https://nedbatchelder.com/blog/201308/names_and_values_making_a_game_board.html
[ned batchelder]: https://nedbatchelder.com/
