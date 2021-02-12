# After

In Python, a [tuple](https://github.com/exercism/v3/blob/master/languages/python/reference/concepts/builtin_types/tuple.md) is an immutable collection of items in _sequence_. Like most collections (_see the built-ins [`list`](https://github.com/exercism/v3/blob/master/languages/python/reference/concepts/builtin_types/list.md), [`dict`](https://github.com/exercism/v3/blob/master/languages/python/reference/concepts/builtin_types/dict.md) and [`set`](https://github.com/exercism/v3/blob/master/languages/python/reference/concepts/builtin_types/set.md)_), tuples can hold any (or multiple) data type(s) -- including other tuples. Like any [sequence](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range), items are referenced by 0-based index number, and can be copied in whole or in part via _slice notation_. Tuples support all [common sequence operations](https://docs.python.org/3/library/stdtypes.html#common-sequence-operations).

Tuples take up very little memory space compared to other collection types and have constant (_O(1)_) access time. However, they cannot be resized, sorted, or altered once created, so are less flexible when frequent changes or updates to data are needed.

## Tuple Construction

Tuples can be formed in multiple ways, using either the `tuple` class constructor or the `tuple` literal declaration.

### Using the `tuple()` constructor empty or with an _iterable_:

```python
>>> no_elements = tuple()
()

#the string elements (characters) are iterated through and added to the tuple
>>> multiple_elements_string = tuple("Timbuktu")
('T', 'i', 'm', 'b', 'u', 'k', 't', 'u')

>>> multiple_elements_list = tuple(["Parrot", "Bird", 334782])
("Parrot", "Bird", 334782)

>>> multiple_elements_set = tuple({2, 3, 5, 7, 11})
(2,3,5,7,11)


"""
The iteration default for dictionaries is over the keys.
To include both keys and values in a tuple made from a dictionary, use dict.items(),
which returns a list of (key, value) tuples.
"""
source_data = {"fish": "gold", "monkey": "brown"}
>>> multiple_elements_dict_1 = tuple(source_data)
('fish', 'monkey')

>>> multiple_elements_dict_2 = tuple(source_data.items())
(('fish', 'gold'), ('monkey', 'brown'))


"""
because the tuple constructor only takes _iterables_ (or nothing), it is much easier to create
 a one-tuple via the literal method.
"""
>>> one_element = tuple([16])
(16,)

```

#### Declaring a tuple as a _literal_ :

```python
>>> no_elements = ()
()

>>> one_element = ("Guava",)
("Guava",)

>>> elements_separated_with_commas = "Parrot", "Bird", 334782
("Parrot", "Bird", 334782)

>>> elements_with_commas_and_parentheses = ("Triangle", 60, 60, 60)
("Triangle", 60, 60, 60)

>>> nested_data_structures = ({"fish": "gold", "monkey": "brown", "parrot" : "grey"}, ("fish", "mammal", "bird"))
({"fish": "gold", "monkey": "brown", "parrot" : "grey"}, ("fish", "mammal", "bird"))

#using the plus + operator unpacks each tuple and creates a new tuple.
>>> new_via_concatenate = ("George", 5) + ("cat", "Tabby")
("George", 5, "cat", "Tabby")

#likewise, using the multiplication operator * is the equvilent of using + n times
>>> first_group = ("cat", "dog", "elephant")

>>> multiplied_group = first_group * 3
('cat', 'dog', 'elephant', 'cat', 'dog', 'elephant', 'cat', 'dog', 'elephant')

```

Note that generally parentheses are not _required_ to create a `tuple` literal - only commas. Parentheses are required in cases of ambiguity, such as an empty or one-item tuple or where a function takes a tuple as an argument.

## Tuples as related information

Tuples are often used as _records_ containing heterogeneous data that is _organizationally_ or _conceptually_ related and treated as a single unit of information.

```python

>>> student_info = ("Alyssa", "grade 3", "female", 8 )

```

Tuples are also used when homogeneous immutable sequences of data are needed for [`hashability`](https://docs.python.org/3/glossary.html#hashable), storage in a set, or creation of keys in a dictionary.

Note that while tuples are in most cases _immutable_, because they can contain _any_ data structure or object they can become mutable if any of their elements is a _mutable type_. Using a mutable data type within a tuple will make the enclosing tuple un-hashable.

```python

>>> cmyk_color_map = {
                      (.69, .3, .48, .1) : ("Teal 700", (59, 178, 146), 0x3BB292),
                      (0, .5, 1, 0) : ("Pantone 151", (247, 127, 1), 0xF77F01),
                      (.37, .89, 0, .44) : ("Pantone 267", (89, 16, 142), 0x59108E),
                      (0, 1, .46, .45) : ("Pantone 228", (140, 0, 76), 0x8C004C)
                     }

>>>> unique_rgb_colors = {
                          (59, 178, 146),
                          (247, 127, 1),
                          (89, 16, 142),
                          (140, 0, 76),
                          (76, 0, 140)
                         }

>>> teal_700 = hash((59, 178, 146))

>>> teal_700 = hash(("Pantone 228", [(140, 0, 76), 0x8C004C]))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'

```

## Accessing data inside a tuple

Items inside tuples (_like the sequence types `string` and `list`_), can be accessed via 0-based index and _bracket notation_. Indexes can be from **`left`** --> **`right`** (_starting at zero_) or **`right`** --> **`left`** (_starting at -1_).

Items inside tuples can also be _iterated over_ in a loop using `for item in` syntax.

```python

>>> student_info = ("Alyssa", "grade 3", "female", 8 )

#name is at index 0 or index -4
>>> student_name = student_info[0]
Alyssa

>>> student_name = student_info[-4]
Alyssa

#grade is at index 1 or index -3
>>> student_grade = student_info[1]
'grade 3'

>>> student_grade = student_info[-3]
'grade 3'

#age is at index 3 or index -1
>>> student_age_1 = student_info[3]
8

>>> student_age_2 = student_info[-1]
8


>>> for item in student_info:
>>>     print(item)

....
Alyssa
grade 3
female
8

```

## Extended tuples and related data types

Tuples are often used as _records_, but the data inside them can only be accessed via _position_/_index_. The [`namedtuple()`](https://docs.python.org/3/library/collections.html#collections.namedtuple) class in the [`collections`](https://docs.python.org/3/library/collections.html#module-collections) module extends basic tuple functionality to allow access of elements by _name_. Additionally, users can adapt a [`dataclass`](https://docs.python.org/3/library/dataclasses.html) to provide similar named attribute functionality, with a some [pros and cons](https://stackoverflow.com/questions/51671699/data-classes-vs-typing-namedtuple-primary-use-cases).
