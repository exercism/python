# `all()` on lowercased letters

```python
from string import ascii_lowercase


def is_pangram(sentence):
    return all(letter in sentence.lower() for letter in ascii_lowercase)

```

- This begins by importing all of the [ascii_lowercase][ascii-lowercase] letters.
- It lowercases the input by using the [lower()][lower] method.
- It then checks if all letters in the lowercase alphabet are contained in the lowercased `sentence`,
using the [`all()`][all] function.
- If all of the letters in the alphabet are contained in the `sentence`, then the function will return `True`.

```exercism/note
Instead of `lower()`, the [`casefold`](https://docs.python.org/3/library/stdtypes.html#str.casefold)
method could be used to lowercase the letters.
`casefold()` differs from `lower()` in lowercasing certain Unicode characters.
At the time of writing, those differences are not of concern to this exercise.
Also, `casefold()` benched slower than `lower()`.
```

[ascii-lowercase]: https://docs.python.org/3/library/string.html#string.ascii_lowercase
[lower]: https://docs.python.org/3/library/stdtypes.html?#str.lower
[all]: https://docs.python.org/3/library/functions.html#all
