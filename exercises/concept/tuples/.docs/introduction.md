In Python, a [tuple](https://docs.python.org/3/library/stdtypes.html#tuple) is an immutable collection of items in _sequence_. Like most collections, tuples can hold any (or multiple) data type(s) -- including other tuples. Like any sequence, items are referenced by 0-based index number. Tuples support all [common sequence operations](https://docs.python.org/3/library/stdtypes.html#common-sequence-operations).

## Tuple Construction

Tuples can be formed in multiple ways, using either the `tuple` class constructor or the `tuple` literal declaration.

#### Using the `tuple()` constructor:

```python
#elements are iterated through and added to the tuple in order
>>> multiple_elements_string = tuple("Timbuktu")
('T', 'i', 'm', 'b', 'u', 'k', 't', 'u')

>>> multiple_elements = tuple(("Parrot", "Bird", 334782))
("Parrot", "Bird", 334782)
```

#### Declaring a tuple _literal_ :

```python
>>> elements_separated_with_commas = "Parrot", "Bird", 334782
("Parrot", "Bird", 334782)

>>> elements_with_commas_and_parentheses = ("Triangle", (60, 60, 60))
("Triangle", (60, 60, 60))
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
