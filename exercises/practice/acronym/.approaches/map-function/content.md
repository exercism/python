# Scrub with `replace()` and join via `map()`


```python
def abbreviate(to_abbreviate):
    phrase = to_abbreviate.replace("_", " ").replace("-", " ").upper().split()
    
    return ''.join(map(lambda word: word[0], phrase))
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


Once the phrase is scrubbed and turned into a word `list`, the acronym is created via the [built-in][python-builtins] [`map()`][map] function.
`map()` applies an anonymous function (_the [lambda][python lambdas] in the code example_) to all the items of an iterable (_'mapping' the function 'onto' each item_), returning a [lazy iterator][lazy iterator] of results.
The application of the function travels from left to right, and function results are produced as needed.


Using code from the example above, `map(lambda word: word[0], ['GNU', 'IMAGE', 'MANIPULATION', 'PROGRAM'])` would calculate `'GNU'[0], 'IMAGE'[0], 'MANIPULATION'[0]), 'PROGRAM'[0]` in order as a stream of data.
 `word[0]` is the function, which extracts the letter at index zero for every word in the phrase list.
This stream of data can then be 'consumed' - either in a `loop`, or by being 'unpacked' by another function or process.
Here, the `iterator` from `map()` is immediately consumed/unpacked by [`join()`][str-join], which glues the results together with an empty string to produce the acronym.


Since using `join()` with `map()` is fairly succinct, the combination is put directly on the `return` line to produce the acronym rather than assigning and returning an intermediate variable.

In benchmarks, this solution performed about as well as  the `loops`, `reduce` and `list-comprehension` solutions.

[chaining]: https://pyneng.readthedocs.io/en/latest/book/04_data_structures/method_chaining.html
[lazy iterator]: https://www.pythonmorsels.com/what-is-an-iterator/
[map]: https://docs.python.org/3/library/functions.html#map
[python lambdas]: https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions
[python-builtins]: https://docs.python.org/3/library/functions.html
[str-join]: https://docs.python.org/3/library/stdtypes.html#str.join
[str-replace]: https://docs.python.org/3/library/stdtypes.html#str.replace
[str-split]: https://docs.python.org/3/library/stdtypes.html#str.split
[str-upper]: https://docs.python.org/3/library/stdtypes.html#str.upper
