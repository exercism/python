# About

A `str` in Python is an [immutable sequence][text sequence] of [Unicode code points][unicode code points].
These may include letters, diacritical marks, positioning characters, numbers, currency symbols, emoji, punctuation, space and line break characters, and more.

For a deep dive on what information a string encodes (or, _"how does a computer know how to translate zeroes and ones into letters?"_), [this blog post is enduringly helpful][joel-on-text].
The Python docs also provide a very detailed [unicode HOWTO][unicode how-to] that discusses Pythons support for the Unicode specification in the `str`, `bytes` and `re` modules, considerations for locales, and some common issues with encoding and translation.

Strings implement all [common sequence operations][common sequence operations] and can be iterated through using `for item in <str>` or `for index, item in enumerate(<str>)` syntax.
 Individual code points (_strings of length 1_) can be referenced by `0-based index` number from the left, or `-1-based index` number from the right.

Strings can be concatenated with `+`, or via `<str>.join(<iterable>)`, split via `<str>.split(<separator>)`, and offer multiple formatting and assembly options.


A `str` literal can be declared via single `'` or double `"` quotes. The escape `\` character is available as needed.

```python

>>> single_quoted = 'These allow "double quoting" without "escape" characters.'

>>> double_quoted = "These allow embedded 'single quoting', so you don't have to use an 'escape' character".
```


Multi-line strings are declared with `'''` or `"""`.

```python
>>> triple_quoted = '''Three single quotes or "double quotes" in a row allow for multi-line string literals.
  Line break characters, tabs and other whitespace is fully supported. Remember - The escape "\" character is also available if needed (as can be seen below). 
  
  You\'ll most often encounter multi-line strings as "doc strings" or "doc tests" written just below the first line of a function or class definition.
    They\'re often used with auto documentation ✍ tools.
    '''
```

The [`str(<object>)` constructor][str-constructor] can be used to create/coerce strings from other objects:

```python
>>> my_number = 42
>>> str(my_number)
...
"42"
```

While the `str(<object>)` constructor can be used to coerce/convert strings, it _**will not iterate**_ or unpack an object.
This is different from the behavior of constructors for other data types such as `list()`, `set()`, `dict()`, or `tuple()`, and can have surprising results.


```python
>>> numbers = [1,3,5,7]
>>> str(numbers)
...
'[1,3,5,7]'
```


Code points within a `str` can be referenced by `0-based index` number from the left:

```python
creative = '창의적인'

>>> creative[0]
'창'

>>> creative[2]
'적'

>>> creative[3]
'인'

```

Indexing also works from the right, starting with a `-1-based index`:

```python
creative = '창의적인'

>>> creative[-4]
'창'

>>> creative[-2]
'적'

>>> creative[-1]
'인'

```

There is no separate “character” or "rune" type in Python, so indexing a string produces a new `str` of **length 1**:

```python

>>> website = "exercism"
>>> type(website[0])
<class 'str'>

>>> len(website[0])
1

>>> website[0] == website[0:1] == 'e'
True
```

Substrings can be selected via _slice notation_, using [`<str>[<start>:stop:<step>]`][common sequence operations] to produce a new string.
Results exclude the `stop` index.
If no `start` is given, the starting index will be 0.
If no `stop` is given, the `stop` index will be the end of the string.


```python
moon_and_stars = '🌟🌟🌙🌟🌟⭐'

>>> moon_and_stars[1:4]
'🌟🌙🌟'

>>> moon_and_stars[:3]
'🌟🌟🌙'

>>> moon_and_stars[3:]
'🌟🌟⭐'

>>> moon_and_stars[:-1]
'🌟🌟🌙🌟🌟'

>>> moon_and_stars[:-3]
'🌟🌟🌙'
```

Strings can also be broken into smaller strings via [`<str>.split(<separator>)`][str-split], which will return a `list` of substrings.
Using `<str>.split()` without any arguments will split the string on whitespace.


```python
>>> cat_ipsum = "Destroy house in 5 seconds command the hooman."
>>> cat_ipsum.split()
...
['Destroy', 'house', 'in', '5', 'seconds', 'command', 'the', 'hooman.']


>>> cat_words = "feline, four-footed, ferocious, furry"
>>> cat_words.split(',')
...
['feline', ' four-footed', ' ferocious', ' furry']


>>> colors = """red,
orange,
green,
purple,
yellow"""

>>> colors.split(',\n')
['red', 'orange', 'green', 'purple', 'yellow']
```

Strings can be concatenated using the `+` operator.
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

If a `list`, `tuple`, `set` or other collection of individual strings needs to be combined into a single `str`, [`<str>.join(<iterable>)`][str-join], is a better option:


```python
# str.join() makes a new string from the iterables elements.
>>> chickens = ["hen", "egg", "rooster"]
>>> ' '.join(chickens)
'hen egg rooster'

# Any string can be used as the joining element.
>>> ' :: '.join(chickens)
'hen :: egg :: rooster'

>>> ' 🌿 '.join(chickens)
'hen 🌿 egg 🌿 rooster'
```

Strings support all [common sequence operations][common sequence operations].
Individual code points can be iterated through in a loop via `for item in <str>`.
Indexes _with_ items can be iterated through in a loop via `for index, item in enumerate(<str>)`.


```python

>>> exercise = 'လေ့ကျင့်'

# Note that there are more code points than perceived glyphs or characters
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

Python provides a rich set of [string methods][str-methods] that can assist with searching, cleaning, splitting, transforming, translating, and many other operations.
A selection of these methods are covered in another exercise.


## Formatting

Python also provides a rich set of tools for [formatting][str-formatting] and [templating][template-strings] strings, as well as more sophisticated text processing through the [re (_regular expressions_)][re], [difflib (_sequence comparison_)][difflib], and [textwrap][textwrap] modules.
For a great introduction to string formatting in Python, see [this post at Real Python][real python string formatting].
 For an introduction to string methods, see [Strings and Character Data in Python][strings and characters] at the same site.


## Related types and encodings

In addition to `str` (a _text_ sequence), Python has corresponding [binary sequence types][binary sequence types] summarized under [binary data services][binary data services] -- `bytes` (a _binary_ sequence), `bytearray`, and `memoryview` for the efficient storage and handling of binary data.
Additionally, [Streams][streams] allow sending and receiving binary data over a network connection without using callbacks.


[binary data services]: https://docs.python.org/3/library/binary.html#binaryservices
[binary sequence types]: https://docs.python.org/3/library/stdtypes.html#binaryseq
[common sequence operations]: https://docs.python.org/3/library/stdtypes.html#common-sequence-operations
[difflib]: https://docs.python.org/3/library/difflib.html
[joel-on-text]: https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses/
[re]: https://docs.python.org/3/library/re.html
[real python string formatting]: https://realpython.com/python-string-formatting/
[str-constructor]: https://docs.python.org/3/library/stdtypes.html#str
[str-formatting]: https://docs.python.org/3/library/string.html#custom-string-formatting
[str-join]: https://docs.python.org/3/library/stdtypes.html#str.join
[str-methods]: https://docs.python.org/3/library/stdtypes.html#string-methods
[str-split]: https://docs.python.org/3/library/stdtypes.html#str.split
[streams]: https://docs.python.org/3/library/asyncio-stream.html#streams
[strings and characters]: https://realpython.com/python-strings/
[template-strings]: https://docs.python.org/3/library/string.html#template-strings
[text sequence]: https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
[textwrap]: https://docs.python.org/3/library/textwrap.html
[unicode code points]: https://stackoverflow.com/questions/27331819/whats-the-difference-between-a-character-a-code-point-a-glyph-and-a-grapheme
[unicode how-to]: https://docs.python.org/3/howto/unicode.html
