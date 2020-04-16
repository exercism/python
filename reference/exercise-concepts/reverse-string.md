# Concepts of `reverse-string`

## Example implementation:

From the current [example.py](https://github.com/exercism/python/blob/master/exercises/reverse-string/example.py):

```python
def reverse(text: str = "") -> str:
    """Reverse a given string"""
    return text[::-1]
```

## Concepts

- [Function][function]: `def` to create a function in Python
- [Immutability][immutability]: `text` str in Python is [immutable](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str).
  In this exercise, you return a new string, the old string `text` is not changed.
- [Return Value][return-value]: this function return a string by this line: `return text[::-1]`
- [Slicing][slicing]: becase `str` in Python is a sequence type, [slicing](https://docs.python.org/3/reference/expressions.html#slicings) syntax can be used here. Specifically: for syntax `string[start:stop:stride]`:

  - `start`: 0-index of the start position, `start=0` by default (i.e., not specified) (start from the beginning)
  - `stop`: 0-index of the stop position, `stop=-1` by default (i.e., not specified) (stop at the end)
  - `stride`: number of skip step. For example,
    ```python
    >>> string = 'ABCDEF'[::2]
    >>> print(string)
    'ACE'
    ```
  - In this exercise, `stride = -1` means start from the end
    Together effectively, slicing of `[::-1]` gives the reversed string
    [Extra material for string slicing.](https://www.digitalocean.com/community/tutorials/how-to-index-and-slice-strings-in-python-3)

- [Docstrings][docstrings]: used to document the function, normally situated right below `def func():`
- [Type hinting][type-hinting]: In modern Python it's possibly to type hint annotations to parameters and variables, see [typing](https://docs.python.org/3/library/typing.html#module-typing). While not neccessary in Python such annotations can help your code be easier to read, understand, and check automatically using tools like `mypy`.
