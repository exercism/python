# `translate()` with `maketrans()`

```python
LOOKUP = str.maketrans("GCTA", "CGAU")


def to_rna(dna_strand):
    return dna_strand.translate(LOOKUP)

```

This approach starts by defining a [dictionary][dictionaries] (also called a translation table in this context) by calling the [`maketrans()`][maketrans] method.

Python doesn't _enforce_ having real constant values,
but the `LOOKUP` translation table is defined with all uppercase letters, which is the naming convention for a Python [constant][const].
It indicates that the value is not intended to be changed.

The translation table that is created uses the [ASCII][ASCII] values (also called the ordinal values) for each letter in the two strings.
The ASCII value for "G" in the first string is the key for the ASCII value of "C" in the second string, and so on.

In the `to_rna()` function, the [`translate()`][translate] method is called on the input,
and is passed the translation table.
The output of `translate()` is a string where all of the input DNA characters have been replaced by their RNA complement in the translation table.


```exercism/note
As of this writing, no invalid DNA characters are in the argument to `to_rna()`, so there is no error handling required for invalid input.
```

[dictionaries]: https://docs.python.org/3/tutorial/datastructures.html?#dictionaries
[maketrans]: https://docs.python.org/3/library/stdtypes.html?#str.maketrans
[const]: https://realpython.com/python-constants/
[translate]: https://docs.python.org/3/library/stdtypes.html?#str.translate
[ASCII]: https://www.asciitable.com/
