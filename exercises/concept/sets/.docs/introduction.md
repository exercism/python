In Python, a [set](https://docs.python.org/3/library/stdtypes.html#set) is an _unordered_ collection of distinct _hashable_ objects. Like most collections, sets can hold any (or multiple) data type(s) -- as long as those types can be [hashed](https://docs.python.org/3.7/glossary.html#term-hashable). Sets come in two flavors: _mutable_ (`set`) and _immutable_ (`frozenset`).

Sets are most commonly used to remove duplicates from sequences, test for membership (_finding supersets & subsets_), and performing "set math" (_union, intersection, difference & symmetric difference_).

Like other collection types such as `dict`, `list`, & `tuple`, `sets` support membership testing through `in`, length calculation through `len()` & _iteration_ via `for item in set`. Unlike the `sequence types` `string`, `list` & `tuple`, `sets` are neither ordered nor indexed, and **do not support** indexing, slicing, sorting, or other sequence behavior.

## Set Construction

Sets can be formed multiple ways, using either the `set` class constructor or the `set` literal declaration.

#### Using the `set()` constructor:

```python
#elements are iterated through and added to the set.  Sets are unordered, duplicates are not allowed.
>>> multiple_elements_string = set("Timbuktu")
{'m', 't', 'u', 'b', 'k', 'T', 'i'}

>>> multiple_elements = set(["Parrot", "Seagull", "Kingfisher", "Pelican", "Seagull", "Kingfisher", "Kingfisher"])
{'Seagull', 'Kingfisher', 'Pelican', 'Parrot'}
```

#### Declaring a set _literal_ via `{}``:

```python
#Because sets use the same {} as dictionaries, you cannot declare an empty set with {}

>>>empty_set = set()
set()

>>> multiple_items = {"Triangle", "Square", "Circle"}
{'Square', 'Triangle', 'Circle'}

>>> multiple_data_structures = {1, (3,5,9), "numbers"}
{(3, 5, 9), 1, 'numbers'}
```

## Concatenation

Tuples can be _concatenated_ via the plus `+` operator, which returns a new tuple.

```python
>>> new_via_concatenate = ("George", 5) + ("cat", "Tabby")
("George", 5, "cat", "Tabby")
```

## Accessing data

Items inside tuples can be accessed via 0-based index and _bracket notation_.

```python
student_info = ("Alyssa", "grade 3", "female", 8 )

#gender is at index 2
>>> student_gender = student_info[2]
female
```

## Iterating through a tuple

Items inside tuples can be _iterated over_ in a loop using `for item in` syntax.

## Checking membership

The `in` operator can be used to check membership in a tuple.
