# Using a `generator-expression` for both cleaning and joining

```python
from string import ascii_letters


VALID_CHARS = {' ', '-'} | set(ascii_letters)


def abbreviate(to_abbreviate):
    to_abbreviate = ''.join(' ' if char == '-' else char
                            for char in to_abbreviate
                            if char in VALID_CHARS)

    return ''.join(word[0] for word in to_abbreviate.split()).upper()
```

One way someone might try to increase performce is to use a single [generator expression][generator-expression] to clean the input, rather than using multiple calls to [`str.replace()`][str-replace].
However, this approach is actually amongst the slower ones.
(See the [performance article][article-performance] for more detail.)

In this approach, the `VALID_CHARS` constant is first defined using `string.ascii_letters`, a space, and a hyphen.
In `abbreviate()`, the first generator expression iterates over `to_abbreviate`, excluding any code points that are not a member of the `VALID_CHARS` set.
For each code point that is not excluded, the expression passes it into [`str.join()`][str-join] (unless it is a hyphen, in which case it replaces the hyphen with a space).
`to_abbreviate` is then set to the result of the `str.join()`, preparing it for the next step.

Next, [`to_abbreviate.split()`][str-split] is used to split `to_abbreviate` into words separated by whitespace — we can ignore the case of hyphens as we already replaced all of them with spaces.
Now the second generator expression iterates over the list returned by `to_abbreviate.split()`, yeilding the first code point in each word.
These code points are passed to another `str.join()`, which is then [chained][chaining] to [`str.upper()`][str-upper].
Now that both steps are complete, we return the result of `str.upper()` directly on the same line.

[article-performance]: https://exercism.org/tracks/python/exercises/acronym/articles/performance
[chaining]: https://pyneng.readthedocs.io/en/latest/book/04_data_structures/method_chaining.html
[generator-expression]: https://dbader.org/blog/python-generator-expressions
[str-join]: https://docs.python.org/3/library/stdtypes.html#str.join
[str-replace]: https://docs.python.org/3/library/stdtypes.html#str.replace
[str-split]: https://docs.python.org/3/library/stdtypes.html#str.split
[str-upper]: https://docs.python.org/3/library/stdtypes.html#str.upper
