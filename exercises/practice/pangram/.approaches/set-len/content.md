# `set` with `len()`

```python
def is_pangram(sentence):
    return len(set(ltr for ltr in sentence.lower() if ltr.isalpha())) == 26
```

- This approach first makes a [set][set] from the [`lower`][lower]cased characters of the `sentence`.
- The characters are filtered using a [set comprehension][set-comprehension] with an `if` [`isalpha()`][isalpha] statement, so that only alphabetic characters make it into the set.
- The function returns whether the [`len()`][len] of the [`set`][set] is `26`.
  If the number of unique ASCII letters in the `set` is equal to the `26` letters in the ASCII alphabet, then the function will return `True`.
- This approach is efficient because it uses a set to eliminate duplicates and directly checks the length, which is a constant time operation.

[lower]: https://docs.python.org/3/library/stdtypes.html?#str.lower
[set]: https://docs.python.org/3/library/stdtypes.html?#set
[set-comprehension]: https://realpython.com/python-set-comprehension/#introducing-set-comprehensions
[isalpha]: https://docs.python.org/3/library/stdtypes.html?highlight=isalpha#str.isalpha
[len]: https://docs.python.org/3/library/functions.html?#len
