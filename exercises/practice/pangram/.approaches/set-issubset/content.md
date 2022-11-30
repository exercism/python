# `set` with `is_subset`

```python
from string import ascii_lowercase

ALPHABET = set(ascii_lowercase)


def is_pangram(sentence):
    return ALPHABET.issubset(sentence.lower())

```

In this approach a [set][set] is made from the [ascii_lowercase][ascii-lowercase] letters,
and another `set` is made from the [`lower`][lower]cased letters in the `sentence`.

The function returns if the alphabet `set` [issubset()][issubset] of the `sentence` `set`.
If all of the letters in the alphabet are a subset of the letters in the `sentence`,
then the function will return `True`.

[set]: https://docs.python.org/3/library/stdtypes.html?#set
[ascii-lowercase]: https://docs.python.org/3/library/string.html#string.ascii_lowercase
[lower]: https://docs.python.org/3/library/stdtypes.html?#str.lower
[issubset]: https://docs.python.org/3/library/stdtypes.html?highlight=issubset#frozenset.issubset
