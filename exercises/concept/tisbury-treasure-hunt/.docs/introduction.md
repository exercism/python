# Introduction

In Python, a [tuple][tuple] is an _immutable_ collection of items in _sequence_.
Like most collections, `tuples` can hold any (or multiple) data type(s) -- including other `tuples`.
Tuples support all [common sequence operations][common sequence operations], but **do not** support [mutable sequence operations][mutable sequence operations].
The elements of a tuple can be iterated over using the `for item in <tuple>` construct.
If both element index and value are needed, `for index, item in enumerate(<tuple>)` can be used.
Like any sequence, elements within `tuples` can be accessed via _bracket notation_ using a `0-based index` number from the left or a `-1-based index` number from the right.


## Tuple Construction

Tuples can be formed in multiple ways, using either the `tuple(<iterable>)` class constructor or the `tuple` literal declaration.

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

Single iterables have their elements added one by one:

```python
>>> multiple_elements_list = tuple(["Parrot", "Bird", 334782])
("Parrot", "Bird", 334782)

>>> multiple_elements_set = tuple({2, 3, 5, 7, 11})
(2,3,5,7,11)
```

#### Declaring a tuple as a _literal_ :

Because the `tuple(<iterable>)` constructor only takes _iterables_ (or nothing) as arguments, it is much easier to create
 a one-tuple via the literal method.

```python
>>> no_elements = ()
()

>>> one_element = ("Guava",)
("Guava",)
```

Nested data structures can be included as `tuple` elements, including other `tuples`:

```python
>>> nested_data_structures = ({"fish": "gold", "monkey": "brown", "parrot" : "grey"}, ("fish", "mammal", "bird"))
({"fish": "gold", "monkey": "brown", "parrot" : "grey"}, ("fish", "mammal", "bird"))

>>> nested_data_structures_1 : (["fish", "gold", "monkey", "brown", "parrot", "grey"], ("fish", "mammal", "bird"))
(["fish", "gold", "monkey", "brown", "parrot", "grey"], ("fish", "mammal", "bird"))
```

## Tuple Concatenation

Tuples can be concatenated using plus `+` operator, which unpacks each `tuple` creating a new, combined `tuple`.

```python
>>> new_via_concatenate = ("George", 5) + ("cat", "Tabby")
("George", 5, "cat", "Tabby")

#likewise, using the multiplication operator * is the equivalent of using + n times
>>> first_group = ("cat", "dog", "elephant")

>>> multiplied_group = first_group * 3
('cat', 'dog', 'elephant', 'cat', 'dog', 'elephant', 'cat', 'dog', 'elephant')
```

## Accessing Elements Inside a Tuple

Elements within a `tuple` can be accessed via _bracket notation_ using a `0-based index` number from the left or a `-1-based index` number from the right.

```python
student_info = ("Alyssa", "grade 3", "female", 8 )

#gender is at index 2 or index -2
>>> student_gender = student_info[2]
'female'

>>> student_gender = student_info[-2]
'female'

#name is at index 0 or index -4
>>> student_name = student_info[0]
Alyssa

>>> student_name = student_info[-4]
Alyssa
```

## Iterating Over a Tuples Elements

Elements inside a `tuple` can be _iterated over_ in a loop using `for item in <tuple>` syntax.
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

## Checking Membership in a Tuple

The `in` operator can be used to check membership in a `tuple`.

```python
>>> multiple_elements_list = tuple(["Parrot", "Bird", 334782])
("Parrot", "Bird", 334782)

>>> "Parrot" in multiple_elements_list
True
```

[common sequence operations]: https://docs.python.org/3/library/stdtypes.html#common-sequence-operations
[tuple]: https://docs.python.org/3/library/stdtypes.html#tuple
[mutable sequence operations]: https://docs.python.org/3/library/stdtypes.html#mutable-sequence-types