TODO: the content below is copied from the exercise introduction and probably needs rewriting to a proper concept introduction

In Python, a [list][list] is a mutable collection of items in _sequence_. Like most collections (_see the built-ins [`tuple`][tuple], [`dict`][dict] and [`set`][set]_), lists can hold reference to any (or multiple) data type(s) - including other lists. Like any [sequence][sequence type], items are referenced by 0-based index number, and can be copied in whole or in part via _slice notation_. Lists support all [common sequence operations][common sequence operations], as well as [mutable sequence operations][mutable sequence operations] like `.append()` and `.reverse()`. They can be iterated over in a loop by using the `for item in <list>` construct.

Under the hood, `lists` are implemented as [dynamic arrays][dynamic array] -- similar to Java's [`Arraylist`][arraylist] type. Lists are most often used to store groups of similar data (_strings, numbers, sets etc._) of unknown length. Accessing items, checking for membership via `in`, or appending items to the "right-hand" side of a list are all very efficient. Appending to the "left-hand" side or inserting into the middle of a list is much _less_ efficient because it requires shifting items to keep them in sequence.

Because lists are mutable and can contain references to arbitrary objects, they take up more memory space than a fixed-size `array.array` type of the same apparent length. Despite this, lists are an extremely flexible and useful data structure and many built-in methods and operations in Python produce lists as their output.

## Construction

A list can be declared as a _literal_ with square `[]` brackets and commas between elements:

```python
>>> no_elements = []
[]

>>> one_element = ["Guava"]
["Guava"]

>>> elements_separated_with_commas = ["Parrot", "Bird", 334782]
["Parrot", "Bird", 334782]
```

For readability, line breaks can be used when there are many elements or nested data structures within a list:

```python
>>> lots_of_entries =[
                        "Rose",
                        "Sunflower",
                        "Poppy",
                        "Pansy",
                        "Tulip",
                        "Fuchsia",
                        "Cyclamen",
                        "Lavender"
                      ]
['Rose', 'Sunflower', 'Poppy', 'Pansy', 'Tulip', 'Fuchsia', 'Cyclamen', 'Lavender']


# Each data structure is on its own line to help clarify what they are.
>>> nested_data_structures = [
                                 {"fish": "gold", "monkey": "brown", "parrot" : "grey"},
                                 ("fish", "mammal", "bird"),
                                 ['water', 'jungle', 'sky']
                             ]
[{"fish": "gold", "monkey": "brown", "parrot" : "grey"}, ("fish", "mammal", "bird"), ['water', 'jungle', 'sky']]
```

The `list()` constructor can be used empty or with an _iterable_ as an argument. Elements in the iterable are cycled through by the constructor and added to the list in order:

```python
>>> no_elements = list()
[]

# The tuple is unpacked and each element is added.
>>> multiple_elements_tuple = list(("Parrot", "Bird", 334782))
["Parrot", "Bird", 334782]

# The set is unpacked and each element is added.
>>> multiple_elements_set = list({2, 3, 5, 7, 11})
[2,3,5,7,11]
```

Results when using a list constructor with a string or a dict may be surprising:

```python

# String elements (Unicode code points) are iterated through and added *individually*.
>>> multiple_elements_string = list("Timbuktu")
['T', 'i', 'm', 'b', 'u', 'k', 't', 'u']


# Unicode separators and positioning code points are also added *individually*.
>>> multiple_code_points_string = list('अभ्यास')
['अ', 'भ', '्', 'य', 'ा', 'स']
```

Because the `list` constructor will only take _iterables_ (or nothing) as arguments, objects that are _not_ iterable will throw a type error. Consequently, it is much easier to create a one-item list via the literal method.

```python

# Numbers are not iterable, and so attempting to create a list with a number passed to the constructor fails.
>>> one_element = list(16)
Traceback (most recent call last):
   File "<stdin>", line 1, in <module>
   TypeError: 'int' object is not iterable

# Tuples *are* iterable, so passing a one-element tuple to the constructor does work, but it's awkward
>>> one_element_from_iterable = list((16,))
[16]
```

## Accessing elements

Items inside lists (_like the sequence types `string` and `tuple`_), can be accessed via 0-based index and _bracket notation_. Indexes can be from **`left`** --> **`right`** (_starting at zero_) or **`right`** --> **`left`** (_starting at -1_).

| **0** | **1** | **2** | **3** | **4** | **5** |\
 -------------------------\
 | P | y | t | h | o | n |\
 -------------------------\
 |_**-6**_ |_**-5**_ |_**-4**_ |_**-3**_ |_**-2**_ |_**-1**_ | <----

```python

>>> breakfast_foods = ["Oatmeal", "Fruit Salad", "Eggs", "Toast"]

# Oatmeal is at index 0 or index -4.
>>> first_breakfast_food = breakfast_foods[0]
'Oatmeal'

>>> first_breakfast_food = breakfast_foods[-4]
'Oatmeal'
```

You can access a portion of a list with _slice notation_ (`[start:stop]`). A _slice_ is defined as the sequence of items in a list at position `index` such that `start <= index < stop`. _Slicing_ does not modify the original `list`. Instead, you get a new list with copies of all the elements you asked for.

You can also slice a list using a `step` parameter with the notation `[start:stop:step]`. Using a `step` will "skip over" or filter the list elements (_for example, a `step` of 2 will be every other element in the range_):

```python
>>> colors = ["Red", "Purple", "Green", "Yellow", "Orange", "Pink", "Blue", "Grey"]

# If there is no step parameter, the step is assumed to be 1.
>>> middle_colors = colors[2:6]
["Green", "Yellow", "Orange", "Pink"]

# If the start or stop parameters are omitted, the slice will
# start at index zero, and will stop at the end of the list.
>>> primary_colors = colors[::3]
["Red", "Yellow", "Blue"]
```

## Working with lists

Lists supply an _iterator_, and can be looped through/over in the same manner as other _sequence types_:

```python
>>> colors = ["Orange", "Green", "Grey", "Blue"]

#  Looping through the list and printing out each element.
>>> for item in colors:
...     print(item)
...
Orange
Green
Grey
Blue

>>> numbers_to_cube = [5, 13, 12, 16]

# Looping through the list and printing out the cube of each element.
>>> for number in numbers_to_cube:
...     print(number*3)
...
15
39
36
48

```

Lists can be combined via various techniques:

```python
# Using the plus + operator unpacks each list and creates a new list, but it is not efficent.
>>> new_via_concatenate = ["George", 5] + ["cat", "Tabby"]
["George", 5, "cat", "Tabby"]

# Likewise, using the multiplication operator * is the equivalent of using + n times.
>>> first_group = ["cat", "dog", "elephant"]

>>> multiplied_group = first_group * 3
['cat', 'dog', 'elephant', 'cat', 'dog', 'elephant', 'cat', 'dog', 'elephant']
```

[list]: https://docs.python.org/3/library/stdtypes.html#list
[tuple]: https://docs.python.org/3/library/stdtypes.html#tuple
[dict]: https://docs.python.org/3/library/stdtypes.html#dict
[set]: https://docs.python.org/3/library/stdtypes.html#set
[sequence type]: https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range
[common sequence operations]: https://docs.python.org/3/library/stdtypes.html#common-sequence-operations
[mutable sequence operations]: https://docs.python.org/3/library/stdtypes.html#typesseq-mutable
[dynamic array]: https://en.wikipedia.org/wiki/Dynamic_array
[arraylist]: https://beginnersbook.com/2013/12/java-arraylist/
