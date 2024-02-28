# Scrub with `replace()` and join via `list comprehension`

```python
def abbreviate(to_abbreviate):
    phrase = to_abbreviate.replace('-', ' ').replace('_', ' ').upper().split()
    
    return ''.join([word[0] for word in phrase])
```

-  This approach begins by using  [`str.replace()`][str-replace] to "scrub" (_remove_) non-letter characters such as `'`,`-`,`_`, and white space from `to_abbreviate`.
- The phrase is then upper-cased by calling [`str.upper()`][str-upper],
- Finally, the phrase is turned into a `list` of words by calling [`str.split()`][str-split].

The three methods above are all [chained][chaining] together, with the output of one method serving as the input to the next method in the "chain".
This works because both `replace()` and `upper()` return strings, and both `upper()` and `split()` _take_ strings as arguments.
However, if `split()` were called first, `replace()` and `upper()` would fail, since neither method will take a `list` as input.


~~~~exercism/note
`re.findall()` or `re.finditer()` can also be used to "scrub" `to_abbreviate`.
These two methods from the `re` module will return a `list` or a lazy `iterator` of results, respectively.
As of this writing, both of these methods benchmark slower than using `str.replace()` for scrubbing.
~~~~


A [`list comprehension`][list comprehension] is then used to iterate through the phrase and select the first letters of each word via [`bracket notation`][subscript notation].
This comprehension is passed into [`str.join()`][str-join], which unpacks the `list` of first letters and joins them together using an empty string - the acronym.
Other "seperator" strings besides an empty string can be used with `str.join()` - see [concept:python/string-methods]() for some additional examples.
Since the comprehension and `join()` are fairly succinct, they are put directly on the `return` line rather than assigning and returning an intermediate variable for the acronym.


The weakness of this solution is that it is taking up extra space with the `list comprehension`, which is creating and saving a `list` in memory - only to have that list immediately unpacked by the `str.join()` method.
While this is trivial for the inputs this problem is tested against, it could become a problem if the inputs get longer.
It could also be an issue if the code were deployed in a memory-constrained environment.
A [generator expression][generator-expression] here would be more memory-efficient, though there are speed tradeoffs.
See the [generator expression][approach-generator-expression] approach for more details.

[approach-generator-expression]: https://exercism.org/tracks/python/exercises/acronym/approaches/generator-expression
[chaining]: https://pyneng.readthedocs.io/en/latest/book/04_data_structures/method_chaining.html
[generator-expression]: https://dbader.org/blog/python-generator-expressions
[list comprehension]: https://treyhunner.com/2015/12/python-list-comprehensions-now-in-color/
[str-join]: https://docs.python.org/3/library/stdtypes.html#str.join
[str-replace]: https://docs.python.org/3/library/stdtypes.html#str.replace
[str-split]: https://docs.python.org/3/library/stdtypes.html#str.split
[str-upper]: https://docs.python.org/3/library/stdtypes.html#str.upper
[subscript notation]: https://docs.python.org/3/glossary.html#term-slice
