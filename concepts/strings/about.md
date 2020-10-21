Pythons string type `str` can be very powerful. At its core, a `str` is an immutable [text sequence](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str) of [Unicode code points](https://stackoverflow.com/questions/27331819/whats-the-difference-between-a-character-a-code-point-a-glyph-and-a-grapheme). There is no separate "character" or "char" type in Python.

Like any [sequence type](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range), code points or "characters" within a string can be referenced by 0-based index number, and can be copied in whole or in part via _slice notation_. Since there is no separate “character” type, indexing a string produces a new `str` of length 1 (_for example "exercism"[0] == "exercism"[0:1] == "e"_). Strings support all [common sequence operations](https://docs.python.org/3/library/stdtypes.html#common-sequence-operations), and individual code points or "characters" can be iterated through in a loop via `for item in`.

For a deep dive on what information a `str` encodes (or, _"how does the computer know how to translate zeroes and ones into letters?"_), [this blog post is enduringly helpful][joel-on-text].

Strings can be transformed by [various methods](https://docs.python.org/3/library/stdtypes.html#string-methods), split into letters/symbols, and joined together via [`.join()`](https://docs.python.org/3/library/stdtypes.html#str.join) or `+` to create larger strings . Due to their immutability, any transformations applied to a `str` return a new `str`.

### Construction

The simplest way to create a `str` literal is by delimiting it with `"` or `'`. Strings can also be written across multiple lines by using triple quotes (`"""` or `'''`) .

````python
single_quoted = 'Single quotes allow "double quoting" without "escape" characters.'

double_quoted = "Double quotes allow embedded 'single quoting' without 'escape' characters".

triple_quoted =  '''Three single quotes or double quotes in a row allow for multi-line string literals.  You will most often encounter these as "doc strings" or "doc tests" written just below the first line of a function or class definition.  They are often used with auto documentation tools.'''
String literals that are part of a single expression and are separated only by white space are _implicitly concatenated_ into a single string literal:

```python
("I do not "
"like "
"green eggs and ham.") == "I do not like green eggs and ham."```


Additionally,  [interpolated](https://en.wikipedia.org/wiki/String_interpolation) strings (`f-strings`) can be formed:

```python
my_name = "Praveen"

intro_string = f"Hi! My name is {my_name}, and I'm happy to be here!"

>>>print(intro_string)
Hi! My name is Praveen, and I'm happy to be here!```

Finally, the  [`str()` constructor](https://docs.python.org/3/library/stdtypes.html#str) can be used to create/coerce strings from other objects/types.  However, the `str` constructor _**will not iterate**_ through an object , so if something like a `list` of elements needs to be connected, `.join()` is a better option:

```python
>>> my_number = 675
>>> str(my_number)
'675'

>>> my_list = ["hen", "egg", "rooster"]
>>> str(my_list)
"['hen', 'egg', 'rooster']"

>>> ' '.join(my_list)
'hen egg rooster'```


### Formatting

Python provides a rich set of tools for [formatting](https://docs.python.org/3/library/string.html#custom-string-formatting) and [templating](https://docs.python.org/3/library/string.html#template-strings) strings, as well as more sophisticated text processing through the [re (_regular expressions_)](https://docs.python.org/3/library/re.html), [difflib (_sequence comparison_)](https://docs.python.org/3/library/difflib.html), and [textwrap](https://docs.python.org/3/library/textwrap.html) modules.   For a great introduction to string formatting in Python, see [this post at Real Python](https://realpython.com/python-string-formatting/).

For more details on string methods, see [Strings and Character Data in Python](https://realpython.com/python-strings/) at the same site.

###  Related types and encodings

In addition to `str` (a *text* sequence), Python has corresponding  [binary sequence types](https://docs.python.org/3/library/stdtypes.html#binaryseq) `bytes` (a *binary* sequence),  `bytearray` and `memoryview` for the efficient storage and handling of binary data.  Additionally, [Streams](https://docs.python.org/3/library/asyncio-stream.html#streams) allow sending and receiving binary data over a network connection without using callbacks.
````
