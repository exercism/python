# Introduction

The `str` class offers [many useful methods][str methods] for working with and composing strings.
These include searching, cleaning, splitting, transforming, translating, and many other techniques.

Strings are [immutable sequences][text sequence] of [Unicode code points][unicode code points] (_for more details, see [HOWTO Unicode][howto unicode] in the Python Docs._) -- individual "characters" or code points (_strings of length 1_) can be referenced by `0-based index` number from the left, or `-1-based index` number from the right.

Strings can be iterated through using `for item in <string>` or `for item in enumerate(<string>)` syntax.
They can be concatenated using the `+` operator or with the `<string>.join()` method, and also implement all [common sequence operations][common sequence operations].

Strings are immutable, meaning the value of a `str` object in memory cannot change.
Functions or methods that operate on a `str` (_like the ones we are learning about here_) will return a _new instance_ of that `str` instead of modifying the original `str` object.


[`<str>.title()`][str-title] parses a string and capitalizes the first "character" of each "word" found.  In Python, this is very dependant on the [language codec][codecs] used, and how the particular language represents words and characters.  There may also be [locale][locale] rules in place.

```python
man_in_hat_th = 'ู้ชายในหมวก'
man_in_hat_ru = 'mужчина в шляпе'
man_in_hat_ko = '모자를 쓴 남자'
main_in_hat_en = 'the man in the hat.'

>>> man_in_hat_th.title()
'ผู้ชายในหมวก'

>>> man_in_hat_ru.title()
'Мужчина В Шляпе'

>>> man_in_hat_ko.title()
'모자를 쓴 남자'

>> main_in_hat_en.title()
'The Man In The Hat.'
```

[`<str>`.endswith(<suffix>)][str-endswith] returns `True` if the string ends with `<suffix>`, `False` otherwise.

```python
>>> 'My heart breaks. 💔'.endswith('💔')
True

>>> 'cheerfulness'.endswith('ness')
True

>>> 'Do you want to 💃?'.endswith('💃')
False

>> 'The quick brown fox jumped over the lazy dog.'.endswith('dog')
False
```

[`<str>`.strip(<chars>)][str-strip] returns a copy of the `str` with leading and trailing `<chars>` removed.
The code points specified in `<chars>` are not a prefix or suffix - all combinations of the code points will be removed starting from both ends of the string.
 If nothing is specified for `<chars>`, all combinations of whitespace will be removed.

 ```python
 >>> 'https://unicode.org/emoji/'.strip('/stph:')
'unicode.org/emoji'

>>> '   🐪🐪🐪🌟🐪🐪🐪   '.strip()
'🐪🐪🐪🌟🐪🐪🐪'

>>> justification = 'оправдание'
>>> justification.strip('еина')
'оправд'

>>> 'unaddressed'.strip('dnue')
'address'

>>> '  unaddressed  '.strip('dnue ')
'address'
```

[`<str>.replace(<substring>, <replacement substring>)`][str-replace] returns a copy of the string with all occurences of `<substring>` replaced with `<replacement substring>`.

```python
# Quote from The Hunting of the Snark, by Lewis Carroll
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

[str methods]: https://docs.python.org/3/library/stdtypes.html#string-methods
[text sequence]: https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
[unicode code points]: https://stackoverflow.com/questions/27331819/whats-the-difference-between-a-character-a-code-point-a-glyph-and-a-grapheme
[common sequence operations]: https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
[str-title]: https://docs.python.org/3/library/stdtypes.html#str.title
[str-endswith]: https://docs.python.org/3/library/stdtypes.html#str.endswith
[str-strip]: https://docs.python.org/3/library/stdtypes.html#str.strip
[str-replace]: https://docs.python.org/3/library/stdtypes.html#str.replace
[codecs]: https://docs.python.org/3/library/codecs.html
[locale]: https://docs.python.org/3/library/locale.html#module-locale
[howto unicode]: https://docs.python.org/3/howto/unicode.html
