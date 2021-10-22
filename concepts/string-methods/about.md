# String Methods

A `str` is an [immutable sequence][text sequence] of [Unicode code points][unicode code points].
This may include letters, diacritical marks, positioning characters, numbers, currency symbols, emoji, punctuation, space and line breaks, and more.

Strings implement all [common sequence operations][common sequence operations] and can be iterated through using `for item in <str>` or `for index, item in enumerate(<str>)` syntax.
 Individual code points (_strings of length 1_) can be referenced by `0-based index` number from the left, or `-1-based index` number from the right.
  Strings can be concatenated with `+`, or via `<str>.join(<iterable>)`, split via `<str>.split(<separator>)`, and offer multiple formatting and assembly options.

 To further work with strings, Python provides a rich set of [string methods][str-methods] for searching, cleaning, transforming, translating, and many other operations.

Some of the more commonly used `str` methods include:

- Checking for prefixes/suffixes with `startswith(<substr>)` and `endswith(<substr>)`
- Altering string casing with methods like `<str>.title()`, `<str>.upper()`/`<str>.lower()`, and `<str>.swapcase()`
- Removing leading or trailing characters from a string using `<str>.strip(<chars>)`, `<str>.lstrip(<chars>)`, or `<str>.rstrip(<chars>)`
- Replacing substrings with the `<str>.replace(<old>, <new>)` method

Being _immutable_, a `str` object's value in memory cannot change; methods that appear to modify a string return a new copy or instance of that `str` object.

[`<str>.endswith(<suffix>)`][str-endswith] returns `True` if the string ends with `<suffix>`, `False` otherwise.

```python
>>> 'My heart breaks. 💔'.endswith('💔')
True

>>> 'cheerfulness'.endswith('ness')
True

# Punctuation is part of the string, so needs to be included in any endswith match.
>>> 'Do you want to 💃?'.endswith('💃')
False

>> 'The quick brown fox jumped over the lazy dog.'.endswith('dog')
False
```

[`<str>.title()`][str-title] parses a string and capitalizes the first "character" of each "word" found.
In Python, this is very dependent on the [language codec][codecs] used and how the particular language represents words and characters.
There may also be [locale][locale] rules in place for a language or character set.


```python
>>> man_in_hat_th = 'ู้ชายในหมวก'
>>> man_in_hat_ru = 'mужчина в шляпе'
>>> man_in_hat_ko = '모자를 쓴 남자'
>>> main_in_hat_en = 'the man in the hat.'

>>> man_in_hat_th.title()
'ผู้ชายในหมวก'

>>> man_in_hat_ru.title()
'Мужчина В Шляпе'

>>> man_in_hat_ko.title()
'모자를 쓴 남자'

>> main_in_hat_en.title()
'The Man In The Hat.'
```


[`<str>.strip(<chars>)`][str-strip] returns a copy of the `str` with leading and trailing `<chars>` removed.
The code points specified in `<chars>` are not a prefix or suffix - **all combinations** of the code points will be removed starting from **both ends** of the string.
 If nothing is specified for `<chars>`, all combinations of whitespace code points will be removed.
 If only left-side or right-side removal is wanted, `<str>.lstrip(<chars>)` and `<str>.rstrip(<chars>)` can be used.


 ```python
# This will remove "https://", because it can be formed from "/stph:". 
>>> 'https://unicode.org/emoji/'.strip('/stph:')
'unicode.org/emoji'

# Removal of all whitespace from both ends of the str.
>>> '   🐪🐪🐪🌟🐪🐪🐪   '.strip()
'🐪🐪🐪🌟🐪🐪🐪'

>>> justification = 'оправдание'
>>> justification.strip('еина')
'оправд'

# Prefix and suffix in one step.
>>> 'unaddressed'.strip('dnue')
'address'

>>> '  unaddressed  '.strip('dnue ')
'address'
 ```


[`<str>.replace(<substring>, <replacement substring>)`][str-replace] returns a copy of the string with all occurrences of `<substring>` replaced with `<replacement substring>`.


The quote used below is from [The Hunting of the Snark][The Hunting of the Snark] by [Lewis Carroll][Lewis Carroll]

```python
# The Hunting of the Snark, by Lewis Carroll
>>> quote = '''
"Just the place for a Snark!" the Bellman cried,
   As he landed his crew with care;
Supporting each man on the top of the tide
   By a finger entwined in his hair.

"Just the place for a Snark! I have said it twice:
   That alone should encourage the crew.
Just the place for a Snark! I have said it thrice:
   What I tell you three times is true."
'''

>>> quote.replace('Snark', '🐲')
...
'\n"Just the place for a 🐲!" the Bellman cried,\n   As he landed his crew with care;\nSupporting each man on the top of the tide\n   By a finger entwined in his hair.\n\n"Just the place for a 🐲! I have said it twice:\n   That alone should encourage the crew.\nJust the place for a 🐲! I have said it thrice:\n   What I tell you three times is true."\n'

>>> 'bookkeeper'.replace('kk', 'k k')
'book keeper'
```

:star:**Newly added in Python `3.9`**

Python `3.9` introduces two new string methods that make removing prefixes and suffixes much easier.

[`<str>.removeprefix(<substring>)`][removeprefix] returns the string without the prefix (`string[len(<substring>):]`). If the `<substring>` isn't present, a copy of the original string will be returned.

```python
# removing a prefix
>>> 'TestHook'.removeprefix('Test')
'Hook'
>>> 'bookkeeper'.removeprefix('book')
'keeper'
```

[`<str>.removesuffix(<substring>)`][removesuffix] returns the string without the suffix (`string[:-len(substring)]`). If the `<substring>` isn't present, a copy of the original string will be returned.

```python
# removing a suffix
>>> 'TestHook'.removesuffix('Hook')
'Test'
>>> 'bookkeeper'.removesuffix('keeper')
'book'
```

For more examples and methods the [informal tutorial][informal tutorial] is a nice jumping-off point.
[How to Unicode][howto unicode] in the Python docs offers great detail on Unicode, encoding, bytes, and other technical considerations for working with strings in Python.

Python also supports regular expressions via the `re` module, which will be covered in a future exercise.


[Lewis Carroll]: https://www.poetryfoundation.org/poets/lewis-carroll
[The Hunting of the Snark]: https://www.poetryfoundation.org/poems/43909/the-hunting-of-the-snark
[codecs]: https://docs.python.org/3/library/codecs.html
[common sequence operations]: https://docs.python.org/3/library/stdtypes.html#common-sequence-operations
[howto unicode]: https://docs.python.org/3/howto/unicode.html
[informal tutorial]: https://docs.python.org/3/tutorial/introduction.html#strings
[locale]: https://docs.python.org/3/library/locale.html#module-locale
[removeprefix]: https://docs.python.org/3.9/library/stdtypes.html#str.removeprefix
[removesuffix]: https://docs.python.org/3.9/library/stdtypes.html#str.removesuffix
[str-endswith]: https://docs.python.org/3/library/stdtypes.html#str.endswith
[str-methods]: https://docs.python.org/3/library/stdtypes.html#string-methods
[str-replace]: https://docs.python.org/3/library/stdtypes.html#str.replace
[str-strip]: https://docs.python.org/3/library/stdtypes.html#str.strip
[str-title]: https://docs.python.org/3/library/stdtypes.html#str.title
[text sequence]: https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
[unicode code points]: https://stackoverflow.com/questions/27331819/whats-the-difference-between-a-character-a-code-point-a-glyph-and-a-grapheme
