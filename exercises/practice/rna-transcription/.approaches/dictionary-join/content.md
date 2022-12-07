# dictionary look-up with `join`

```python
LOOKUP = {"G": "C", "C": "G", "T": "A", "A": "U"}


def to_rna(dna_strand):
    return ''.join(LOOKUP[chr] for chr in dna_strand)

```

This approach starts by defining a [dictionary][dictionaries] to map the DNA values to RNA values.

Python doesn't _enforce_ having real constant values,
but the `LOOKUP` dictionary is defined with all uppercase letters, which is the naming convention for a Python [constant][const].
It indicates that the value is not intended to be changed.

In the `to_rna()` function, the [`join()`][join] method is called on an empty string,
and is passed the list created from a [list comprehension][list-comprehension].

The list comprehension iterates each character in the input,
looks up the DNA character in the look-up dictionary, and outputs its matching RNA character as an element in the list.

The `join()` method collects the list of RNA characters back into a string.
Since an empty string is the separator for the `join()`, there are no spaces between the RNA characters in the string.

[dictionaries]: https://docs.python.org/3/tutorial/datastructures.html?#dictionaries
[const]: https://realpython.com/python-constants/
[join]: https://docs.python.org/3/library/stdtypes.html?#str.join
[list-comprehension]: https://realpython.com/list-comprehension-python/#using-list-comprehensions
