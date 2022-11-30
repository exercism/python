# `set` with `len()`

```python
def is_pangram(sentence):
    return len([ltr for ltr in set(sentence.lower()) if ltr.isalpha()]) \
        == 26

```

- This approach first makes a [set][set] from the [`lower`][lower]cased characters of the `sentence`.
- The characters in the `set`are then iterated in a [list comprehension][list-comprehension].
- The characters are filtered by an `if` [`isalpha()`][isalpha] statement, so that only alphabetic characters make it into the list.
- The function returns whether the [`len()`][len] of the [`list`][list] is `26`.
If the number of unique letters in the `set` is equal to the `26` letters in the alphabet, then the function will return `True`.

[lower]: https://docs.python.org/3/library/stdtypes.html?#str.lower
[set]: https://docs.python.org/3/library/stdtypes.html?#set
[list-comprehension]: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
[isalpha]: https://docs.python.org/3/library/stdtypes.html?highlight=isalpha#str.isalpha
[len]: https://docs.python.org/3/library/functions.html?#len
[list]: https://docs.python.org/3/library/stdtypes.html?#list
