Python allows you to manipulate a [`list`][list] in a lot of ways. A `list` is simple a collection of objects of [type `List`][list std type]. They are mutable, ordered and indexed. Let's look at the methods that are available to manipulate a `list` object.

When you manipulate a list with a list-method, you are changing the properties of the list you pass. That is, **you will alter the list** object that is being used with the list-method. If you do not want to change the original list, you need to copy the list and then work on the copied list.

To begin, you first need a `list` object to apply the methods to.

```python
>>> empty_list = list() # (or) empty_list = []
>>> empty_list
[]
```

# Add Items to a list

Methods to add items:

1. `list.append()`
2. `list.insert()`
3. `list.extend()`

If you want to add an item after all the items of an existing list, you use the list-method `append()` for it. As the name indicates, `append()` attaches the item at the **end** of the list.

```python
>>> numbers = [1, 2, 3]
>>> numbers.append(9)
>>> numbers
[1, 2, 3, 9]
```

Rather than appending, the `insert()` method gives you the ability to add the item to a _specific index_ in the list.

`.insert()` takes 2 parameters:

1. the index of the item before which you want the new item to appear
2. the item to be inserted

Note: If the given index is 0, the item will be added to the start of the list. If the supplied index is greater than the last index of the list, the item will be added in the last position, this is the equivalent of using the `append()` method.

```python
>>> numbers = [1, 2, 3]
>>> numbers.insert(0, -2)
>>> numbers
[-2, 1, 2, 3]
>>> numbers.insert(1, 0)
>>> numbers
[-2, 0, 1, 2, 3]
```

If you have an iterable that you would like to _combine_ with your current list (concatenating the two), you can use the `list.extend()` method. `extend()` will unpack the supplied iterable and add its elements, in the same order, to your list (_using `.append()` in this circumstance would add the entire iterable as a **single item**._).

The extend method takes an iterable as its parameter:

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

# Remove Items from a list

Methods to remove items:

1. `list.remove()`
2. `list.pop()`
3. `list.clear()`

If you want to delete an item from a list, you can use the `list.remove()` method, passing the item to be removed as an argument. `remove()` will throw a `ValueError` if the item is not present in the list.

```python
>>> numbers = [1, 2, 3]
>>> numbers.remove(2)
>>> numbers
[1, 3]
>>> numbers.remove(0)
ValueError: list.remove(x): x not in list
```

Alternatively, using the `list.pop()` method will both remove **and** `return` an element for use. `pop()` takes one optional parameter: the index of the item you need to remove and receive. If you specify an index number higher than the length of the list, you will get an `IndexError`. If the optional index argument is not specified, the last element of the list will be removed and returned to you.

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
```

If you want to remove all the items from a `list` you can use the `list.clear()` method. It does not take any parameters.

```python
>>> numbers = [1, 2, 3]
>>> numbers.clear()
>>> numbers
[]
```

# Reverse and reorder a list

You can reverse the order of a list with the `list.reverse()` method.

```python
>>> numbers = [1, 2, 3, 0]
>>> numbers.reverse()
>>> numbers
[0, 3, 2, 1]
```

A list can be re-ordered _**in place**_ with the help of the `list.sort()` method. Internally, Python uses [`Timsort`][timsort] to arrange the list. The default order is _ascending_. The Python docs offer some [additional tips and techniques for sorting][sorting how to] lists effectively.

If you have a list of names and you want to sort them:

```python
>>> names = ["Tony", "Natasha", "Thor", "Bruce"]
>>> names.sort()
>>> names
["Bruce", "Natasha", "Thor", "Tony"]
```

If you want the sort to be in descending order, you can pass the reverse argument:

```python
>>> names = ["Tony", "Natasha", "Thor", "Bruce"]
>>> names.sort(reverse=True)
>>> names
["Tony", "Thor", "Natasha", "Bruce"]
```

For cases where changing your original list is undesirable, the built-in [`sorted()`][sorted] can be used to return a new, sorted copy of your original list.

# Occurrences of an item in a list

You can find the occurrences of an element in a list with the help of `list.count()`. It takes the item you need to tally as its argument and returns the total number of times it appears on the list.

```python
>>> items = [1, 4, 7, 8, 2, 9, 2, 1, 1, 0, 4, 3]
>>> items.count(1)
3
```

# Find the index of an item

The `list.index()` method will give you the index number of the _first occurrence_ of an item you pass in. If there are no occurrences of the item, a `ValueError` is raised. If you do not need the exact position of an item and are only checking that it is present inside the list, the built-in `in` operator is more efficient.

Indexing is zero-based, meaning the position of the first item is `0`.

```python
>>> items = [7, 4, 1, 0, 2, 5]
>>> items.index(4)
1
>>> items.index(10)
ValueError: 10 is not in list
```

You can provide start and end indices to search within a specific section of the list.

```python
>>> names = ["Tina", "Leo", "Thomas", "Tina", "Emily", "Justin"]
>>> names.index("Tina")
0
>>> names.index("Tina", 2, 5)
3
```

# Make a copy of a list

Remember that variables in Python are labels that point to underlying objects.

Lists are _collections_ of object references ordered by an index. If you assign a list object to a new variable name, any change you make to the list using the new variable name will also _impact_ the original variable. Both variable names point to the **same list object** which is modified.

```python
>>> actual_names = ["Tony", "Natasha", "Thor", "Bruce"]

# Both variable names point to the same list
>>> same_list = actual_names

>>> same_list.append("Clarke")
>>> same_list
["Tony", "Natasha", "Thor", "Bruce", "Clarke"]
>>> actual_names
["Tony", "Natasha", "Thor", "Bruce", "Clarke"]
```

If you need to use a new list, use the `list.copy()` method or a _slice_ to make a `shallow_copy` of the list. Using `copy()` or slicing will create a new list _object_, but will not create new objects for the list items. (More about the differences between a `shallow_copy` and a `deep_copy` later).

```python
>>> names = ["Tony", "Natasha", "Thor", "Bruce"]

# The two list objects are independents, but they contain of the same items.
>>> new_list = names.copy()

>>> new_list.append("Clarke")
>>> new_list
["Tony", "Natasha", "Thor", "Bruce", "Clarke"]
>>> names
["Tony", "Natasha", "Thor", "Bruce"]
```

_Slicing_ will also make a second set of references that can then be changed without the danger of unintentional mutation of elements:

```python
>>> names = ["Tony", "Natasha", "Thor", "Bruce"]

# This is equivalent to using names.copy()
>>> new_list = names[:]

>>> new_list.append("Clarke")
>>> new_list
["Tony", "Natasha", "Thor", "Bruce", "Clarke"]
>>> names
["Tony", "Natasha", "Thor", "Bruce"]
```

This reference constraint becomes exacerbated when working with nested/multiplied lists:

```python
from pprint import pprint

# This will produce a game grid that is 8x8, pre-populated with zeros
>>> game_grid = [[0]*8] *8

>>> pprint(game_grid)
[[0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0]]

# An attempt to put a "X" in the bottom right corner
>>> game_grid[7][7] = "X"

# This doesn't work because all the rows are referencing the same underlying list object.
>>> pprint(game_grid)
[[0, 0, 0, 0, 0, 0, 0, 'X'],
 [0, 0, 0, 0, 0, 0, 0, 'X'],
 [0, 0, 0, 0, 0, 0, 0, 'X'],
 [0, 0, 0, 0, 0, 0, 0, 'X'],
 [0, 0, 0, 0, 0, 0, 0, 'X'],
 [0, 0, 0, 0, 0, 0, 0, 'X'],
 [0, 0, 0, 0, 0, 0, 0, 'X'],
 [0, 0, 0, 0, 0, 0, 0, 'X']]
```

As mentioned earlier, if your list contains _variables_ or nested data structures, those second-level references will **not be copied** via `copy()` or slice. To copy an entire tree of containers, references, and objects, you need to use `list.deep_copy()` or a `list comprehension`. For a detailed explanation of list behaviors, see this excellent [making a game board][making a game board] article.

```python
from pprint import pprint

# This loop will safely produce a game grid that is 8x8, pre-populated with zeros
>>> game_grid = []
>>> filled_row = [0] * 8
>>> for row in range(8):
...    game_grid.append(filled_row.copy())

>>> pprint(game_grid)
[[0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0]]

# An attempt to put a "X" in the bottom right corner
>>> game_grid[7][7] = "X"

# The game grid now works the way we expect it to
>>> pprint(game_grid)
[[0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 'X']]
```

[list]: https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
[list std type]: https://docs.python.org/3.9/library/stdtypes.html#list
[timsort]: https://en.wikipedia.org/wiki/Timsort
[sorted]: https://docs.python.org/3/library/functions.html#sorted
[making a game board]: https://nedbatchelder.com/blog/201308/names_and_values_making_a_game_board.html
[sorting how to]: https://docs.python.org/3/howto/sorting.html
