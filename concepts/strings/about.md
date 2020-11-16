Pythons `str` (_string_) type can be very powerful. At its core, a `str` is an immutable [text sequence][text sequence] of [Unicode code points][unicode code points]. There is no separate "character" or "rune" type in Python.

Like any [sequence type][sequence type], code points within a `str` can be referenced by 0-based index number and can be copied in whole or in part via _slice notation_. Since there is no separate “character” type, indexing a string produces a new `str` of length 1:

```python

>>> website = "exercism"
>>> type(website[0])
<class 'str'>

>>> len(website[0])
1

>>> website[0] == website[0:1] == 'e'
True
```

Strings support all [common sequence operations][common sequence operations]. Individual code points can be iterated through in a loop via **`for item in`**.

```python

>>> exercise = 'လေ့ကျင့်'

#note that there are more code points than percieved glyphs or characters
>>> for code_point in exercise:
...    print(code_point)
...
လ
ေ
့
က
ျ
င
်
့
```

For a deep dive on what information a string encodes (or, _"how does the computer know how to translate zeroes and ones into letters?"_), [this blog post is enduringly helpful][joel-on-text]. Additionally, the docs provide a [unicode HOWTO][unicode how-to] that discusses Pythons support for the Unicode specification in the `str`, `bytes` and `re` modules, and some common issues.

Strings can be transformed by [various methods][str-methods], split into code points via [`.split()`][str-split], or joined together into larger strings via [`.join()`][str-join] or `+`. Due to their _immutability_, any transformations applied to strings return new `str` objects.

### Construction

The simplest way to create a `str` literal is by delimiting it with `"` or `'`. Strings can also be written across multiple lines by using triple quotes (`"""` or `'''`) .

```python

>>> single_quoted = 'Single quotes allow "double quoting" without "escape" characters.'

>>> double_quoted = "Double quotes allow embedded 'single quoting' without 'escape' characters".

>>> triple_quoted =  '''Three single quotes or double quotes in a row allow for multi-line string literals.  You will most often encounter these as "doc strings" or "doc tests" written just below the first line of a function or class definition.  They are often used with auto documentation tools.'''
String literals that are part of a single expression and are separated only by white space are _implicitly concatenated_ into a single string literal:


#if you put seperate strings within parenthesis, they will be *implicitly concatenated* by the interpreter
>>> ("I do not "
"like "
"green eggs and ham.") == "I do not like green eggs and ham."
True
```

Additionally, [interpolated][f-strings] strings (`f-strings`) can be formed:

```python
my_name = "Praveen"

intro_string = f"Hi! My name is {my_name}, and I'm happy to be here!"

>>>print(intro_string)
Hi! My name is Praveen, and I'm happy to be here!
```

Finally, the [`str()` constructor][str-constructor] can be used to create/coerce strings from other objects/types. However, the `str` constructor _**will not iterate**_ through an object , so if something like a `list` of individual elements needs to be connected, `.join()` is a better option:

```python
>>> my_number = 675
>>> str(my_number)
'675'

#this is a bit surprising, as it will make the entire data structure, complete with the brackets, into a str
>>> my_list = ["hen", "egg", "rooster"]
>>> str(my_list)
"['hen', 'egg', 'rooster']"


#however, using .join() will iterate and form a string from individual elements
>>> ' '.join(my_list)
'hen egg rooster'
```

### Formatting

Python provides a rich set of tools for [formatting][str-formatting] and [templating][template-strings] strings, as well as more sophisticated text processing through the [re (_regular expressions_)][re], [difflib (_sequence comparison_)][difflib], and [textwrap][textwrap] modules. For a great introduction to string formatting in Python, see [this post at Real Python][real python string formatting]. For more details on string methods, see [Strings and Character Data in Python][strings and characters] at the same site.

### Related types and encodings

In addition to `str` (a _text_ sequence), Python has corresponding [binary sequence types][binary sequence types] summarized under [binary data services][binary data services] -- `bytes` (a _binary_ sequence), `bytearray`, and `memoryview` for the efficient storage and handling of binary data. Additionally, [Streams][streams] allow sending and receiving binary data over a network connection without using callbacks.

[text sequence]: https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
[unicode code points]: https://stackoverflow.com/questions/27331819/whats-the-difference-between-a-character-a-code-point-a-glyph-and-a-grapheme
[sequence type]: https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range
[common sequence operations]: https://docs.python.org/3/library/stdtypes.html#common-sequence-operations
[joel-on-text]: https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses/
[str-methods]: https://docs.python.org/3/library/stdtypes.html#string-methods
[str-join]: https://docs.python.org/3/library/stdtypes.html#str.join
[f-strings]: https://en.wikipedia.org/wiki/String_interpolation
[str-constructor]: https://docs.python.org/3/library/stdtypes.html#str
[str-formatting]: https://docs.python.org/3/library/string.html#custom-string-formatting
[template-strings]: https://docs.python.org/3/library/string.html#template-strings
[re]: https://docs.python.org/3/library/re.html
[difflib]: https://docs.python.org/3/library/difflib.html
[textwrap]: https://docs.python.org/3/library/textwrap.html
[real python string formatting]: https://realpython.com/python-string-formatting/
[strings and characters]: https://realpython.com/python-strings/
[binary sequence types]: https://docs.python.org/3/library/stdtypes.html#binaryseq
[streams]: https://docs.python.org/3/library/asyncio-stream.html#streams
[unicode how-to]: https://docs.python.org/3/howto/unicode.html
[str-split]: https://docs.python.org/3/library/stdtypes.html#str.split
[binary data services]: https://docs.python.org/3/library/binary.html#binaryservices
