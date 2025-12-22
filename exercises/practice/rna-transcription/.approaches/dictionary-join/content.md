# dictionary look-up with `join`

```python
LOOKUP = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}


def to_rna(dna_strand):
    return ''.join(LOOKUP[nucleotide] for nucleotide in dna_strand)

```

This approach starts by defining a [dictionary][dictionaries] to map the DNA values to RNA values.

Python doesn't _enforce_ having real constant values,
but the `LOOKUP` dictionary is defined with all uppercase letters, which is the naming convention for a Python [constant][const].
It indicates that the value is not intended to be changed.

In the `to_rna()` function, the [`join()`][join] method is called on an empty string,
and is passed the list created from a [generator expression][generator-expression].

The generator expression iterates each character in the input,
looks up the DNA character in the look-up dictionary, and outputs its matching RNA character as an element in the list.

The `join()` method collects the RNA characters back into a string.
Since an empty string is the separator for the `join()`, there are no spaces between the RNA characters in the string.

A generator expression is similar to a [list comprehension][list-comprehension], but instead of creating a list, it returns a generator, and iterating that generator yields the elements on the fly.

A variant that uses a list comprehension is almost identical, but note the additional square brackets inside the `join()`:

```python
LOOKUP = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}


def to_rna(dna_strand):
    return ''.join([LOOKUP[nucleotide] for nucleotide in dna_strand])
```


For a relatively small number of elements, using lists is fine and may be faster, but as the number of elements increases, the memory consumption increases and performance decreases.
You can read more about [when to choose generators over list comprehensions][list-comprehension-choose-generator-expression] to dig deeper into the topic.


~~~~exercism/note
As of this writing, no invalid DNA characters are in the argument to `to_rna()`, so there is no error handling required for invalid input.
~~~~


[dictionaries]: https://docs.python.org/3/tutorial/datastructures.html?#dictionaries
[const]: https://realpython.com/python-constants/
[join]: https://docs.python.org/3/library/stdtypes.html?#str.join
[list-comprehension]: https://realpython.com/list-comprehension-python/#using-list-comprehensions
[list-comprehension-choose-generator-expression]: https://realpython.com/list-comprehension-python/#choose-generators-for-large-datasets
[generator-expression]: https://realpython.com/introduction-to-python-generators/#building-generators-with-generator-expressions
