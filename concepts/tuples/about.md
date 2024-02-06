# About

A [tuple][tuple] is an _immutable_ collection of items in _sequence_.


Like most collections (_see the built-ins [`list`][list], [`dict`][dict] and [`set`][set]_), `tuples` can hold any (or multiple) data type(s) -- including other `tuples`.
The elements of a tuple can be iterated over using the `for item in <tuple>` construct.
If both element index and value are needed, `for index, item in enumerate(<tuple>)` can be used.


Like any [sequence][sequence], elements within `tuples` can be accessed via _bracket notation_ using a `0-based index` number from the left or a `-1-based index` number from the right.
Tuples can be copied in whole or in part via _slice notation_ or `<tuple>.copy()`, and support all [common sequence operations][common sequence operations].
Being _immutable_, `tuples` **do not** support [mutable sequence operations][mutable sequence operations].


Tuples take up very little memory space compared to other collection types and have constant (_O(1)_) access time when using an index.
However, they cannot be resized, sorted, or altered once created, so are less flexible when frequent changes or updates to data are needed.
If frequent updates or expansions are required, a `list`, `collections.deque`, or `array.array` might be a better data structure.

<br>

## Tuple Construction

Tuples can be formed in multiple ways, using either the `tuple` class constructor or the `(<element_1>, <element_2>)` (_`tuple` literal_) declaration.

### Using the `tuple()` constructor empty or with an _iterable_:

```python
>>> no_elements = tuple()
()

# The constructor *requires* an iterable, so single elements must be passed in a list or another tuple.
>>> one_element = tuple([16])
(16,)
```

Strings are iterable, so using a single `str` as an argument to the `tuple()` constructor can have surprising results:

```python
# String elements (characters) are iterated through and added to the tuple
>>> multiple_elements_string = tuple("Timbuktu")
('T', 'i', 'm', 'b', 'u', 'k', 't', 'u')
```

Other iterables also have their elements added one by one:

```python
>>> multiple_elements_list = tuple(["Parrot", "Bird", 334782])
("Parrot", "Bird", 334782)

>>> multiple_elements_set = tuple({2, 3, 5, 7, 11})
(2,3,5,7,11)
```

The iteration default for `dict` is over the **keys**.
To include both keys and values in a tuple made from a dictionary, use `<dict>.items()`,
which will return an iterator of (`key`, `value`) `tuples`.

```python
source_data = {"fish": "gold", 
               "monkey": "brown"}

>>> multiple_elements_dict_1 = tuple(source_data)
('fish', 'monkey')

>>> multiple_elements_dict_2 = tuple(source_data.items())
(('fish', 'gold'), ('monkey', 'brown'))
```

#### Declaring a tuple as a _literal_ :

Because the `tuple()` constructor only takes _iterables_ (or nothing) as arguments, it is much easier to create
 a one-tuple via the literal method.

```python
>>> no_elements = ()
()

>>> one_element = ("Guava",)
("Guava",)
```

Note that generally parentheses are **not** required to create a `tuple` literal - only commas.
However, using `(<element)1>, <element_2>)` is considered more readable in most circumstances.
Parentheses are also required in cases of ambiguity, such as an empty or one-item tuple or where a function takes a tuple as an argument.

```python
>>> elements_separated_with_commas = "Parrot", "Bird", 334782
("Parrot", "Bird", 334782)

>>> elements_with_commas_and_parentheses = ("Triangle", 60, 60, 60)
("Triangle", 60, 60, 60)
```

Other data structures can be included as `tuple` elements, including other `tuples`.

```python
>>> nested_data_structures = ({"fish": "gold", "monkey": "brown", "parrot" : "grey"}, ("fish", "mammal", "bird"))
({"fish": "gold", "monkey": "brown", "parrot" : "grey"}, ("fish", "mammal", "bird"))

>>> nested_data_structures_1 = (["fish", "gold", "monkey", "brown", "parrot", "grey"], ("fish", "mammal", "bird"))
(["fish", "gold", "monkey", "brown", "parrot", "grey"], ("fish", "mammal", "bird"))
```

Tuples can be concatenated using plus `+` operator, which unpacks each `tuple` creating a new, combined `tuple`.

```python
>>> new_via_concatenate = ("George", 5) + ("cat", "Tabby")
("George", 5, "cat", "Tabby")

#likewise, using the multiplication operator * is the equivalent of using + n times
>>> first_group = ("cat", "dog", "elephant")

>>> multiplied_group = first_group * 3
('cat', 'dog', 'elephant', 'cat', 'dog', 'elephant', 'cat', 'dog', 'elephant')
```

## Accessing Data

Elements inside tuples (_like the other sequence types `str` and `list`_), can be accessed via _bracket notation_.
Indexes can be from **`left`** --> **`right`** (_starting at zero_) or **`right`** --> **`left`** (_starting at -1_).
Tuples can also be copied in whole or in part via _slice notation_ or using `<tuple>.copy()`.

```python

>>> student_info = ("Alyssa", "grade 3", "female", 8 )

#name is at index 0 or index -4
>>> student_name = student_info[0]
Alyssa

>>> student_name = student_info[-4]
Alyssa

#age is at index 3 or index -1
>>> student_age_1 = student_info[3]
8

>>> student_age_2 = student_info[-1]
8
```

## Iteration Over Elements

Elements inside tuples can be _iterated over_ in a loop using `for item in <tuple>` syntax.
If both indexes and values are needed, `for index, item in enumerate(<tuple>)` can be used.

```python
>>> student_info = ("Alyssa", "grade 3", "female", 8 )
>>> for item in student_info:
...   print(item)

...
Alyssa
grade 3
female
8

>>> for index, item in enumerate(student_info):
...  print("Index is: " + str(index) + ", value is: " + str(item) +".")

...
Index is: 0, value is: Alyssa.
Index is: 1, value is: grade 3.
Index is: 2, value is: female.
Index is: 3, value is: 8.
```


## Tuples as Homogeneous Information

Tuples are often used as _records_ containing data that is _organizationally_ or _conceptually_ homogeneous and treated as a single unit of information -- even if individual elements are of  _heterogeneous_ data types.

```python

>>> student_info = ("Alyssa", "grade 3", "female", 8 )

```

Tuples are also used when homogeneous immutable sequences of data are needed for [`hashability`][hashability], storage in a `set`, or creation of keys in a dictionary.

Note that while `tuples` are in most cases _immutable_, because they can contain _any_ data structure or object they can _become mutable_ if any of their elements is a _mutable type_.
Using a mutable data type within a `tuple` will make the enclosing `tuple` **un-hashable**.

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

## Extended tuples and related data types

Tuples are often used as _records_, but the data inside them can only be accessed via _position_/_index_.
The [`namedtuple()`][namedtuple] class in the [`collections`][collections] module extends basic tuple functionality to allow access of elements by _name_.
Additionally, users can adapt a [`dataclass`][dataclass] to provide similar named attribute functionality, with a some [pros and cons][dataclass pros and cons].


[collections]: https://docs.python.org/3/library/collections.html#module-collections
[common sequence operations]: https://docs.python.org/3/library/stdtypes.html#common-sequence-operations
[dataclass pros and cons]: https://stackoverflow.com/questions/51671699/data-classes-vs-typing-namedtuple-primary-use-cases
[dataclass]: https://docs.python.org/3/library/dataclasses.html
[dict]: https://docs.python.org/3/library/stdtypes.html#mapping-types-dict
[hashability]: https://docs.python.org/3/glossary.html#hashable
[list]: https://docs.python.org/3/library/stdtypes.html#list
[mutable sequence operations]: https://docs.python.org/3/library/stdtypes.html#mutable-sequence-types
[namedtuple]: https://docs.python.org/3/library/collections.html#collections.namedtuple
[sequence]: https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range
[set]: https://docs.python.org/3/library/stdtypes.html#set
[tuple]: https://docs.python.org/3/library/stdtypes.html#tuple
