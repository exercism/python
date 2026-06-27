# Clean with `replace()` and join via `generator-expression`


```python
def abbreviate(to_abbreviate):
    phrase = to_abbreviate.replace("-", " ").replace("_", " ").upper().split()
    
    # Note the lack of square brackets around the comprehension.
    return "".join(word[0] for word in phrase)
```

- This approach begins by using [`str.replace()`][str-replace] on `to_abbreviate` to convert non-letter characters such as `-` and `_` into spaces.
- The phrase is then upper-cased by calling [`str.upper()`][str-upper].
- Finally, the phrase is turned into a `list` of words by calling [`str.split()`][str-split].

The three methods above are all [chained][chaining] together, with each method operating on the output of the method before it in the "chain".
This works because both `replace()` and `upper()` _operate on_ strings (as they are `str` methods) and _return_ strings.
If `split()` was called first, `replace()` and `upper()` would fail, since they cannot operate on the `list` returned by `split()`.

~~~~exercism/note
`re.findall()` or `re.finditer()` can also be used to clean `to_abbreviate`.
These two methods from the [`re` module][re-module] will return a `list` or a lazy `iterator` of results, respectively.
As of this writing, both of these methods benchmark slower than using `str.replace()` for cleaning.

[re-module]: https://docs.python.org/3/library/re.html
~~~~


A [`generator-expression`][generator-expression] is then used to iterate through the phrase and select the first letters of each word via [`bracket notation`][subscript notation].


Generator expressions are short-form [generators][generators] — lazy iterators that produce their values _on demand_, instead of saving them to memory.
This generator expression is consumed by [`str.join()`][str-join], which joins the generated letters together using an empty string.
Other "separator" strings can be used with `str.join()` — see [concept:python/string-methods]() for some additional examples.
Since the generator expression and `join()` are fairly succinct, they are put directly on the `return` line, rather than assigning and returning an intermediate variable for the acronym.


In benchmarks, this solution was surprisingly slower than the `list comprehension` version.
[This article][Oscar-Alsing-article] from Oscar Alsing briefly explains why.

[Oscar-Alsing-article]: https://www.oscaralsing.com/list-comprehension-vs-generator-expression/#:~:text=List%20comprehensions%20are%20usually%20faster,difference%20is%20often%20quite%20small.
[chaining]: https://pyneng.readthedocs.io/en/latest/book/04_data_structures/method_chaining.html
[generator-expression]: https://dbader.org/blog/python-generator-expressions
[generators]: https://dbader.org/blog/python-generators
[str-join]: https://docs.python.org/3/library/stdtypes.html#str.join
[str-replace]: https://docs.python.org/3/library/stdtypes.html#str.replace
[str-split]: https://docs.python.org/3/library/stdtypes.html#str.split
[str-upper]: https://docs.python.org/3/library/stdtypes.html#str.upper
[subscript notation]: https://docs.python.org/3/glossary.html#term-slice
