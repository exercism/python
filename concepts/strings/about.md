# About

A `str` in Python is an [immutable sequence][text sequence] of [Unicode code points][unicode code points].
These could include letters, diacritical marks, positioning characters, numbers, currecy symbols, emoji, punctuation, space and line break characters, and more.
Being immutable, a `str` object's value in memory doesn't change; methods that appear to modify a string return a new copy or instance of `str`.

For a deep dive on what information a string encodes (or, _"how does the computer know how to translate zeroes and ones into letters?"_), [this blog post is enduringly helpful][joel-on-text]. Additionally, the docs provide a [unicode HOWTO][unicode how-to] that discusses Pythons support for the Unicode specification in the `str`, `bytes` and `re` modules, and some common issues.

A `str` literal can be declared via single `'` or double `"` quotes. The escape `\` character is available as needed.

```python

>>> single_quoted = 'These allow "double quoting" without "escape" characters.'

>>> double_quoted = "These allow embedded 'single quoting', so you don't have to use an 'escape' character".
```

Muliti-line strings are declared with `'''` or `"""`.

```python
>>> triple_quoted =  '''Three single quotes or "double quotes" in a row allow for multi-line string literals.
  Line break characters, tabs and other whitespace is fully supported.

  You\'ll most often encounter these as "doc strings" or "doc tests" written just below the first line of a function or class definition.
    They\'re often used with auto documentation ✍ tools.
    '''
```

The [`str()` constructor][str-constructor] can be used to create/coerce strings from other objects:

```python
>>> my_number = 42
>>> str(my_number)
...
"42"
```

While the `str()` constructor can be used to coerce strings from other objects, it _**will not iterate**_ through an object.
This lack of iteration can have surprising results.

```python
>>> number_words = ["ਤਿੰਨ", "ਪੰਜ", "ਨੌ"]
>>> str(number_words)
...
'["ਤਿੰਨ", "ਪੰਜ", "ਨੌ"]'
```

If a `list`, `tuple`, `set` or other collection of individual elements needs to be converted to a `str` type, [`<str>.join(<iterable>)`][str-join], is a better option:

```python
# To avoid surprises with iteration, str.join() the elements of an iterable.
>>> chickens = ["hen", "egg", "rooster"]
>>> ' '.join(chickens)
'hen egg rooster'

# Any string can be used as the joining element.
>>> ' :: '.join(chickens)
'hen :: egg :: rooster'

>>> ' 🌿 '.join(chickens)
'hen 🌿 egg 🌿 rooster'
```

Strings can also be concatenated using the `+` operator.
This method should be used sparingly, as it is not very performant or easily maintained.

```python
language = "Ukrainian"
number = "nine"
word = "девять"

sentence = word + " " + "means" + " " + number + " in " + language + "."

>>> print(sentence)
...
"девять means nine in Ukrainian."
```

String literals that are part of a single expression and are separated only by white space are _implicitly concatenated_ into a single string literal:

```python
# Seperate strings within parenthesis will be *implicitly concatenated* by the interpreter.
>>> ("I do not "
"like "
"green eggs and ham.") == "I do not like green eggs and ham."
True
```

Strings can be broken into smaller strings via [`<str>.split(<separator>)`][str-split], which will return a `list` of substrings.
Using `<str>.split()` without any arguments will split the string on whitespace.

```python
>>> cat_ipsum = "Destroy house in 5 seconds enslave the hooman."
>>> cat_ipsum.split()
...
['Destroy', 'house', 'in', '5', 'seconds', 'enslave', 'the', 'hooman.']
```

Code points within a `str` can be referenced by 0-based index number and can be copied in whole or in part via _slice notation_, using [`<str>[<start>:stop:<step>]`][common sequence operations].

```python
noodles = "ก๋วยเตี๋ยว"

>>> first_code_point = noodles[0]
'ก'

>> last_code_point = noodles[-1]
'ว'

>>> middle_four_points = noodels[3:7]
'ยเตี'

>> noodles_copy = noodles[:]
"ก๋วยเตี๋ยว"
```

There is no separate “character” or "rune" type in Python, so indexing a string produces a new `str` of length 1:

```python

>>> website = "exercism"
>>> type(website[0])
<class 'str'>

>>> len(website[0])
1

>>> website[0] == website[0:1] == 'e'
True
```

Strings support all [common sequence operations][common sequence operations].
Individual code points can be iterated through in a loop via `for item in <str>`.
Indexes _with_ items can be iterated through in a loop via `for index, item in enumerate(<str>)`

```python

>>> exercise = 'လေ့ကျင့်'

# Note that there are more code points than percieved glyphs or characters
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

# Using enumerate will give both the value and index position of each element.
>>> for index, code_point in enumerate(exercise):
...    print(index, ": ", code_point)
...
0 :  လ
1 :  ေ
2 :  ့
3 :  က
4 :  ျ
5 :  င
6 :  ်
7 :  ့
```

## String Methods

To manipulate strings, Python provides a rich set of [string methods][str-methods] that can assist with searching, cleaning, splitting, transforming, translating, and many other operations.

## Formatting

Python also provides a rich set of tools for [formatting][str-formatting] and [templating][template-strings] strings, as well as more sophisticated text processing through the [re (_regular expressions_)][re], [difflib (_sequence comparison_)][difflib], and [textwrap][textwrap] modules. For a great introduction to string formatting in Python, see [this post at Real Python][real python string formatting]. For more details on string methods, see [Strings and Character Data in Python][strings and characters] at the same site.

## Related types and encodings

In addition to `str` (a _text_ sequence), Python has corresponding [binary sequence types][binary sequence types] summarized under [binary data services][binary data services] -- `bytes` (a _binary_ sequence), `bytearray`, and `memoryview` for the efficient storage and handling of binary data. Additionally, [Streams][streams] allow sending and receiving binary data over a network connection without using callbacks.

[text sequence]: https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
[unicode code points]: https://stackoverflow.com/questions/27331819/whats-the-difference-between-a-character-a-code-point-a-glyph-and-a-grapheme
[common sequence operations]: https://docs.python.org/3/library/stdtypes.html#common-sequence-operations
[joel-on-text]: https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses/
[str-methods]: https://docs.python.org/3/library/stdtypes.html#string-methods
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
[str-join]: https://docs.python.org/3/library/stdtypes.html#str.join
