# Scrub with `replace()` and join via `functools.reduce()`


```python
from functools import reduce


def abbreviate(to_abbreviate):
    phrase = to_abbreviate.replace("_", " ").replace("-", " ").upper().split()
    
    return reduce(lambda start, word: start + word[0], phrase, "")
```


-  This approach begins by using  [`str.replace()`][str-replace] to "scrub" (_remove_) non-letter characters such as `'`,`-`,`_`, and white space from `to_abbreviate`.
- The phrase is then upper-cased by calling [`str.upper()`][str-upper],
- Finally, the phrase is turned into a `list` of words by calling [`str.split()`][str-split].

The three methods above are all [chained][chaining] together, with the output of one method serving as the input to the next method in the "chain".
This works because both `replace()` and `upper()` return strings, and both `upper()` and `split()` take strings as arguments.
However, if `split()` were called first, `replace()` and `upper()` would fail, since neither method will take a `list` as input.

~~~~exercism/note
`re.findall()` or `re.finditer()` can also be used to "scrub" `to_abbreviate`.
These two methods from the `re` module will return a `list` or a lazy `iterator` of results, respectively.
As of this writing, both of these methods benchmark slower than using `str.replace()` for scrubbing.
~~~~


Once the phrase is scrubbed and turned into a word `list`, the acronym is created via `reduce()`.
`reduce()` is a method from the [`functools`][functools] module, which provides support for higher-order functions and functional programming in Python.


[`functools.reduce()`][reduce] applies an anonymous two-argument function (_the [lambda][python lambdas] in the code example_) to the items of an iterable.
 The application of the function travels from left to right, so that the iterable becomes a single value (_it is "reduced" to a single value_).


 Using code from the example above, `reduce(lambda start, word: start + word[0], ['GNU', 'IMAGE', 'MANIPULATION', 'PROGRAM'])` would calculate `((('GNU'[0] + 'IMAGE'[0])+'MANIPULATION'[0])+'PROGRAM'[0])`, or `GIMP`.
  The left argument, `start`, is the _accumulated value_ and the right argument, `word`, is the value from the iterable that is used to update the accumulated 'total'.
  The optional 'initializer' value '' is used here, and is placed ahead/before the items of the iterable in the calculation, and serves as a default if the iterable that is passed is empty.


Since using `reduce()` is fairly succinct, it is put directly on the `return` line to produce the acronym rather than assigning and returning an intermediate variable.


In benchmarks, this solution performed about as well as both the `loops` and the `list-comprehension` solutions.

[chaining]: https://pyneng.readthedocs.io/en/latest/book/04_data_structures/method_chaining.html
[functools]: https://docs.python.org/3/library/functools.html
[reduce]: https://docs.python.org/3/library/functools.html#functools.reduce
[str-replace]: https://docs.python.org/3/library/stdtypes.html#str.replace
[str-split]: https://docs.python.org/3/library/stdtypes.html#str.split
[str-upper]: https://docs.python.org/3/library/stdtypes.html#str.upper
[python lambdas]: https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions
