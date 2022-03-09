# Introduction

A [`list`][list] is a mutable collection of items in _sequence_.
Like most collections (_see the built-ins [`tuple`][tuple], [`dict`][dict] and [`set`][set]_), lists can hold reference to any (or multiple) data type(s) - including other lists.
Like any [sequence][sequence type], items can be accessed via `0-based index` number from the left and `-1-base index` from the right.
Lists can be copied in whole or in part via [slice notation][slice notation] or `<list>.copy()`

Lists support both [common][common sequence operations] and [mutable][mutable sequence operations] sequence operations such as `min()`/`max()`, `<list>.index()`, `<list>.append()` and `<list>.reverse()`.
List elements can be iterated over using the `for item in <list>` construct.
 `for index, item in enumerate(<list>)` can be used when both the element index and the element value are needed.

Under the hood, `lists` are implemented as [dynamic arrays][dynamic array] -- similar to Java's [`ArrayList`][arraylist] type, and are most often used to store groups of similar data (_strings, numbers, sets etc._) of unknown length.
Lists are an extremely flexible and useful data structure and many built-in methods and operations in Python produce lists as their output.


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

For readability, line breaks can be used when there are many elements or nested data structures within a `list`:


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
 Elements in the iterable are cycled through by the constructor and added to the `list` in order:


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

Results when using a `list` constructor with a `string` or a `dict` may be surprising:


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

>>> multiple_elements_dict_1 = list(source_data)
['fish', 'monkey']
```

Because the `list` constructor will only take _iterables_ (or nothing) as arguments, objects that are _not_ iterable will throw a type error.
 Consequently, it is much easier to create a one-item `list` via the literal method.

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

Items inside lists (_as well as items in other sequence types `str` & `tuple`_) can be accessed via `0-based index` and _bracket notation_.
 Indexes can be from **`left`** --> **`right`** (_starting at zero_) or **`right`** --> **`left`** (_starting at -1_).


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

A section of the elements inside a `list` can be accessed via _slice notation_ (`<list>[start:stop]`).
 A _slice_ is defined as an element sequence at position `index`, such that `start <= index < stop`.
 _Slicing_ returns a copy of the "sliced" items and does not modify the original `list`.


A `step` parameter can also be used `[start:stop:step]` to "skip over" or filter the `list` elements (_for example, a `step` of 2 will select every other element in the range_):


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

The usage of the built-in `sum()` function on a list will return the sum of all the numbers in the list:

```python
>>> number_list = [1, 2, 3, 4]
>>> sum(number_list)
10
```

You can also get the _length_ of a list by using the `len()` function:

```python
>>> long_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
>>> len(long_list)
10
```

Lists can be also combined in various ways:

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
```

Lists supply an _iterator_, and can be looped through/over in the same manner as other _sequence types_.

```python
#  Looping through the list and printing out each element.
>>> colors = ["Orange", "Green", "Grey", "Blue"]

>>> for item in colors:
...     print(item)
...
Orange
Green
Grey
Blue
```

_For a more in-depth explanation, of `loops` and `iterators`, complete the `loops` concept._

[arraylist]: https://beginnersbook.com/2013/12/java-arraylist/
[common sequence operations]: https://docs.python.org/3/library/stdtypes.html#common-sequence-operations
[dict]: https://docs.python.org/3/library/stdtypes.html#dict
[dynamic array]: https://en.wikipedia.org/wiki/Dynamic_array
[list]: https://docs.python.org/3/library/stdtypes.html#list
[mutable sequence operations]: https://docs.python.org/3/library/stdtypes.html#typesseq-mutable
[sequence type]: https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range
[set]: https://docs.python.org/3/library/stdtypes.html#set
[slice notation]: https://docs.python.org/3/reference/expressions.html#slicings
[tuple]: https://docs.python.org/3/library/stdtypes.html#tuple
