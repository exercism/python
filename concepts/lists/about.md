# About

A [`list`][list] is a mutable collection of items in _sequence_.
 Like most collections (_see the built-ins [`tuple`][tuple], [`dict`][dict] and [`set`][set]_), lists can hold reference to any (or multiple) data type(s) - including other lists.
 Like any [sequence][sequence type], items can be accessed via `0-based index` number from the left and `-1-based index` from the right.
 Lists can be copied in whole or in part via [slice notation][slice notation] or `<list>.copy()`.


Lists support both [common][common sequence operations] and [mutable][mutable sequence operations] sequence operations such as `min()`/`max()`, `<list>.index()`, `.append()` and `.reverse()`.
 List elements can be iterated over using the `for item in <list>` construct. `for index, item in enumerate(<list)` can be used when both the element index and the element value are needed.


Lists are implemented as [dynamic arrays][dynamic array] -- similar to Java's [`Arraylist`][arraylist] type, and are most often used to store groups of similar data (_strings, numbers, sets etc._) of unknown length (_the number of entries may arbitrarily expand or shrink_).


Accessing elements, checking for membership via `in`, or appending items to the "right-hand" side of a list are all very efficient.
 Prepending (_appending to the "left-hand" side_) or inserting into the middle of a list are much _less_ efficient because those operations require shifting elements to keep them in sequence.
 For a similar data structure that supports memory efficient `appends`/`pops` from both sides, see [`collections.deque`][deque], which has approximately the same O(1) performance in either direction.


Because lists are mutable and can contain references to arbitrary objects, they also take up more space in memory than a fixed-size [`array.array`][array.array] type of the same apparent length.
 Despite this, lists are an extremely flexible and useful data structure and many built-in methods and operations in Python produce lists as their output.


## Construction

A `list` can be declared as a _literal_ with square `[]` brackets and commas between elements:


```python
>>> no_elements = []

>>> no_elements
[]

>>> one_element = ["Guava"]

>>> one_element
['Guava']

>>> elements_separated_with_commas = ["Parrot", "Bird", 334782]

>>> elements_separated_with_commas
['Parrot', 'Bird', 334782]
```

For readability, line breaks can be used when there are many elements or nested data structures within a list:


```python
>>> lots_of_entries = [
      "Rose",
      "Sunflower",
      "Poppy",
      "Pansy",
      "Tulip",
      "Fuchsia",
      "Cyclamen",
      "Lavender"
   ]

>>> lots_of_entries
['Rose', 'Sunflower', 'Poppy', 'Pansy', 'Tulip', 'Fuchsia', 'Cyclamen', 'Lavender']


# Each data structure is on its own line to help clarify what they are.
>>> nested_data_structures = [
      {"fish": "gold", "monkey": "brown", "parrot": "grey"},
      ("fish", "mammal", "bird"),
      ['water', 'jungle', 'sky']
   ]

>>> nested_data_structures
[{'fish': 'gold', 'monkey': 'brown', 'parrot': 'grey'}, ('fish', 'mammal', 'bird'), ['water', 'jungle', 'sky']]
```

The `list()` constructor can be used empty or with an _iterable_ as an argument.
 Elements in the iterable are cycled through by the constructor and added to the list in order:


```python
>>> no_elements = list()
>>> no_elements
[]

# The tuple is unpacked and each element is added.
>>> multiple_elements_from_tuple = list(("Parrot", "Bird", 334782))

>>> multiple_elements_from_tuple
['Parrot', 'Bird', 334782]

# The set is unpacked and each element is added.
>>> multiple_elements_from_set = list({2, 3, 5, 7, 11})

>>> multiple_elements_from_set
[2, 3, 5, 7, 11]
```

Results when using a list constructor with a string or a dict may be surprising:

```python
# String elements (Unicode code points) are iterated through and added *individually*.
>>> multiple_elements_string = list("Timbuktu")

>>> multiple_elements_string
['T', 'i', 'm', 'b', 'u', 'k', 't', 'u']

# Unicode separators and positioning code points are also added *individually*.
>>> multiple_code_points_string = list('अभ्यास')

>>> multiple_code_points_string
['अ', 'भ', '्', 'य', 'ा', 'स']

# The iteration default for dictionaries is over the keys, so only key data is inserted into the list.
>>> source_data = {"fish": "gold", "monkey": "brown"}
>>> list(source_data)
['fish', 'monkey']
```

Because the `list()` constructor will only take iterables (or nothing) as arguments, objects that are **not** iterable will raise a `TypeError`. Consequently, it is much easier to create a one-item list via the literal method.

```python
# Numbers are not iterable, and so attempting to create a list with a number passed to the constructor fails.
>>> one_element = list(16)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'int' object is not iterable

# Tuples *are* iterable, so passing a one-element tuple to the constructor does work, but it's awkward
>>> one_element_from_iterable = list((16,))

>>> one_element_from_iterable
[16]
```

## Accessing elements

Items inside lists (_as well as elements in other sequence types such as [`str`][string] & [`tuple`][tuple]_), can be accessed using  _bracket notation_. Indexes can be from **`left`** --> **`right`** (_starting at zero_) or **`right`** --> **`left`** (_starting at -1_).


<table>
<tr>
  <td style="vertical-align: top"> index from left ⟹<br><br><br><br><br><br><br></td><td style="vertical-align: middle">

|  0<br>👇🏾 	|  1<br>👇🏾 	|  2<br>👇🏾 	|  3<br>👇🏾 	|  4<br>👇🏾 	|  5<br>👇🏾 	|
|:--------:	|:--------:	|:--------:	|:--------:	|:--------:	|:--------:	|
|     P    	|     y    	|     t    	|     h    	|     o    	|     n    	|
| 👆🏾<br>-6 	| 👆🏾<br>-5 	| 👆🏾<br>-4 	| 👆🏾<br>-3 	| 👆🏾<br>-2 	| 👆🏾<br>-1 	|
</td><td style="vertical-align: bottom"><br><br><br><br><br>⟸ index from right</td>
</tr>
</table>


```python
>>> breakfast_foods = ["Oatmeal", "Fruit Salad", "Eggs", "Toast"]

# Oatmeal is at index 0 or index -4.
>>> breakfast_foods[0]
'Oatmeal'

>>> breakfast_foods[-4]
'Oatmeal'

# Eggs are at index -2 or 2
>>> breakfast_foods[-2]
'Eggs'

>>> breakfast_foods[2]
'Eggs'

# Toast is at -1
>>> breakfast_foods[-1]
'Toast'
```

A section of a list can be accessed via _slice notation_ (`<list>[start:stop]`). A _slice_ is defined as an element sequence at position `index`, such that `start <= index < stop`. [_Slicing_][slice notation] returns a copy of the "sliced" items and does not modify the original `list`.

A `step` parameter can also be used in the slice (`[start:stop:step]`) to "skip over" or filter the returned elements (_for example, a `step` of 2 will select every other element in the section_):

```python
>>> colors = ["Red", "Purple", "Green", "Yellow", "Orange", "Pink", "Blue", "Grey"]

# If there is no step parameter, the step is assumed to be 1.
>>> middle_colors = colors[2:6]

>>> middle_colors
['Green', 'Yellow', 'Orange', 'Pink']

# If the start or stop parameters are omitted, the slice will
# start at index zero, and will stop at the end of the list.
>>> primary_colors = colors[::3]

>>> primary_colors
['Red', 'Yellow', 'Blue']
```


## Working with lists

Lists supply an [_iterator_][iterator], and can be looped through/over in the same manner as other _sequence types_, using either `for item in <list>` or `for index, item in enumerate(<list>)`:

```python
# Make a list, and then loop through it to print out the elements
>>> colors = ["Orange", "Green", "Grey", "Blue"]
>>> for item in colors:
...     print(item)
...
Orange
Green
Grey
Blue


# Print the same list, but with the indexes of the colors included
>>> colors = ["Orange", "Green", "Grey", "Blue"]
>>> for index, item in enumerate(colors):
...     print(item, ":", index)
...
Orange : 0
Green : 1
Grey : 2
Blue : 3


# Start with a list of numbers and then loop through and print out their cubes.
>>> numbers_to_cube = [5, 13, 12, 16]
>>> for number in numbers_to_cube:
...     print(number**3)
...
125
2197
1728
4096
```

One common way to compose a list of values is to use `<list>.append()` within a loop:

```python
>>> cubes_to_1000 = []
>>> for number in range(11):
...    cubes_to_1000.append(number**3)

>>> cubes_to_1000
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
```

Lists can also be combined via various techniques:

```python
# Using the plus + operator unpacks each list and creates a new list, but it is not efficient.
>>> new_via_concatenate = ["George", 5] + ["cat", "Tabby"]

>>> new_via_concatenate
['George', 5, 'cat', 'Tabby']

# Likewise, using the multiplication operator * is the equivalent of using + n times.
>>> first_group = ["cat", "dog", "elephant"]
>>> multiplied_group = first_group * 3

>>> multiplied_group
['cat', 'dog', 'elephant', 'cat', 'dog', 'elephant', 'cat', 'dog', 'elephant']

# Another method for combining 2 lists is to use slice assignment or a loop-append.
# This assigns the second list to index 0 in the first list.
>>> first_one = ["cat", "Tabby"]
>>> second_one = ["George", 5]
>>> first_one[0:0] = second_one

>>> first_one
['George', 5, 'cat', 'Tabby']

# This loops through the first list and appends it's items to the end of the second list.
>>> first_one = ["cat", "Tabby"]
>>> second_one = ["George", 5]

>>> for item in first_one:
...      second_one.append(item)

>>> second_one
['George', 5, 'cat', 'Tabby']
```


## Some cautions

Recall that variables in Python are _labels_ that point to _underlying objects_.
`lists` add one more layer as  _container objects_ -- they hold object references for their collected items.
This can lead to multiple potential issues when working with lists, if not handled properly.


### Assigning more than one variable name
Assigning a `list` object to a new variable _name_ **does not copy the `list` object nor its elements**.
Any change made to the elements in the `list` under the _new_ name _impact the original_.


Making a `shallow_copy` via `list.copy()` or slice will avoid this first-leve referencing complication.
A `shallow_copy` will create a new `list` object, but **will not** create new objects for the contained list _elements_. This type of copy will usually be enough for you to add or remove items from the two `list` objects independently, and effectively have two "separate" lists.


```python
>>> actual_names = ["Tony", "Natasha", "Thor", "Bruce"]

# Assigning a new variable name does not make a copy of the container or its data.
>>> same_list = actual_names

#  Altering the list via the new name is the same as altering the list via the old name.
>>> same_list.append("Clarke")
>>> same_list
["Tony", "Natasha", "Thor", "Bruce", "Clarke"]
>>> actual_names
["Tony", "Natasha", "Thor", "Bruce", "Clarke"]

#  Likewise, altering the data in the list via the original name will also alter the data under the new name.
>>> actual_names[0] = "Wanda"
>>> same_list
['Wanda', 'Natasha', 'Thor', 'Bruce', 'Clarke']

# If you copy the list, there will be two separate list objects which can be changed independently.
>>> copied_list = actual_names.copy()
>>> copied_list[0] = "Tony"
>>> actual_names
['Wanda', 'Natasha', 'Thor', 'Bruce', 'Clarke']
>>> copied_list
["Tony", "Natasha", "Thor", "Bruce", "Clarke"]
```


This reference complication becomes exacerbated when working with nested or multiplied lists (_the following examples are from the excellent 2013 [`Ned Batchelder`][ned batchelder] blog post [Names and values: making a game board][names and values]_):

```python
from pprint import pprint

# This will produce a game grid that is 8x8, pre-populated with zeros.
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

# An attempt to put a "X" in the bottom right corner.
>>> game_grid[7][7] = "X"

# This attempt doesn't work because all the rows are referencing the same underlying list object.
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

But in this circumstance, a `shallow_copy` is enough to allow the behavior we'd like:

```python
from pprint import pprint

# This loop will safely produce a game grid that is 8x8, pre-populated with zeros
>>> game_grid = []
>>> filled_row = [0] * 8
>>> for row in range(8):
...    game_grid.append(filled_row.copy()) # This is making a new shallow copy of the inner list object each iteration.

>>> pprint(game_grid)
[[0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0]]

# An attempt to put a "X" in the bottom right corner.
>>> game_grid[7][7] = "X"

# The game grid now works the way we expect it to!
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

As mentioned earlier, lists are containers of _references_, so there is a second layer of potential complication.
If a list contains variables, objects, or nested data structures, those second-level references **will not be copied** via `shallow_copy` or slice.
Mutating the underlying objects will then affect _any and all_ copies, since each `list` object only contains _references pointing to_ the contained elements.

```python
from pprint import pprint

>>> pprint(game_grid)
[[0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 'X']]

# We'd like a new board, so we make a shallow copy.
>>> new_game_grid = game_grid.copy()

# But a shallow copy doesn't copy the contained references or objects.
>>> new_game_grid[0][0] = 'X'

# So changing the items in the copy also changes the originals items.
>>>  pprint(game_grid)
[['X', 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 'X']]
```

## Related data types

Lists are often used as _stacks_ and _queues_ -- although their underlying implementation makes prepending and inserting slow.
The [collections][collections] module offers a [deque][deque] variant optimized for fast appends and pops from either end that is implemented as a [doubly linked list][doubly linked list].
Nested lists are also used to model small _matrices_ -- although the [Numpy][numpy] and [Pandas][pandas] libraries are much more robust for efficient matrix and tabular data manipulation.
The collections module also provides a `UserList` type that can be customized to fit specialized list needs.

[array.array]: https://docs.python.org/3/library/array.html
[arraylist]: https://beginnersbook.com/2013/12/java-arraylist/
[collections]: https://docs.python.org/3/library/collections.html
[common sequence operations]: https://docs.python.org/3/library/stdtypes.html#common-sequence-operations
[deque]: https://docs.python.org/3/library/collections.html#collections.deque
[dict]: https://docs.python.org/3/library/stdtypes.html#dict
[doubly linked list]: https://en.wikipedia.org/wiki/Doubly_linked_list
[dynamic array]: https://en.wikipedia.org/wiki/Dynamic_array
[iterator]: https://docs.python.org/3/glossary.html#term-iterator
[list]: https://docs.python.org/3/library/stdtypes.html#list
[mutable sequence operations]: https://docs.python.org/3/library/stdtypes.html#typesseq-mutable
[names and values]: https://nedbatchelder.com/blog/201308/names_and_values_making_a_game_board.html
[ned batchelder]: https://nedbatchelder.com/
[numpy]: https://numpy.org/
[pandas]: https://pandas.pydata.org/
[sequence type]: https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range
[set]: https://docs.python.org/3/library/stdtypes.html#set
[slice notation]: https://docs.python.org/3/reference/expressions.html#slicings
[string]: https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
[tuple]: https://docs.python.org/3/library/stdtypes.html#tuple