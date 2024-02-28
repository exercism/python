# Scrub with `replace()` and join via `for` loop


```python
def abbreviate(to_abbreviate):
    phrase = to_abbreviate.replace('-', ' ').replace('_', ' ').upper().split()
    acronym = ''
    
    for word in phrase:
        acronym += word[0]

    return acronym
```


-  This approach begins by using  [`str.replace()`][str-replace] to "scrub" (_remove_) non-letter characters such as `'`,`-`,`_`, and white space from `to_abbreviate`.
- The phrase is then upper-cased by calling [`str.upper()`][str-upper],
- Finally, the phrase is turned into a `list` of words by calling [`str.split()`][str-split].

The three methods above are all [chained][chaining] together, with the output of one method serving as the input to the next method in the "chain".
This works because both `replace()` and `upper()` return strings, and both `upper()` and `split()` take strings as arguments.
However, if `split()` were called first, `replace()` and `upper()` would fail, since neither method will take a `list` as input.

After the phrase is cleaned and split into a word list, we declare an empty `acronym` string to hold our final acronym.
The phrase `list` is then looped over via `for word in phrase`.
The first letter of each word is selected via [`bracket notation`][subscript notation], and concatenated via `+` to the `acronym` string.
When the loop is complete, `acronym` is returned from the function.


~~~~exercism/note
`re.findall()` or `re.finditer()` can also be used to "scrub" `to_abbreviate`.
These two methods from the `re` module will return a `list` or a lazy `iterator` of results, respectively.
As of this writing, both of these methods benchmark slower than using `str.replace()` for scrubbing.
~~~~

[chaining]: https://pyneng.readthedocs.io/en/latest/book/04_data_structures/method_chaining.html
[str-replace]: https://docs.python.org/3/library/stdtypes.html#str.replace
[str-split]: https://docs.python.org/3/library/stdtypes.html#str.split
[str-upper]: https://docs.python.org/3/library/stdtypes.html#str.upper
[subscript notation]: https://docs.python.org/3/glossary.html#term-slice
