# Scrub with `re.sub()`

```python
import re


def is_isogram(phrase):
    scrubbed = re.compile('[^a-zA-Z]').sub('', phrase).lower()
    return len(set(scrubbed)) == len(scrubbed)

```

For this approach, [regular expression][regex], also known as a [regex][regex-how-to], is used to scrub the input phrase [str][str]ing.
- In the pattern of `[^a-zA-Z]` the brackets are used to define a character set that looks for characters which are _not_ `a` through `z` and `A` through `Z`.
```exercism/note
If the first character of a character set is `^`, all the characters that are _not_ in the rest of the character set will be matched.
```
This essentially matches any characters which are not in the English alphabet.
 The pattern is passed to the [`compile()`][compile] method to construct a [regular expression object][regex-object].
- The [`sub()`][sub] method is then called on the regex object.
The `sub()` method replaces all non-alphabetic characters in the input phrase with an empty string.
- The output of `sub()` is then [chained][method-chaining] as the input for [`lower()`][lower].
All of the letters are lowercased so that letters of different cases will become the same letter for comparison purposes,
since `A` and `a` are considered to be the same letter.
When the replacing and lowercasing is done, the `scrubbed` variable will be a string having all alphabetic letters lowercased.
- A [`set`][set] is constructed from the `scrubbed` string and its [`len`][len] is compared with the `len` of the the `scrubbed` string.
Since a `set` holds only unique values, the phrase will be an isogram if its number of unique letters is the same as its total number of letters.
The function returns whether the number of unique letters equals the total number of letters.
- For `Alpha` it would return `False`, because `a` is considered to repeat `A`, so the number of unique letters in `Alpha` is `4`,
and the total number of letters in `Alpha` is `5`.
- For `Bravo` it would return `True`, since the number of unique letters in `Bravo` is `5`, and the total number of letters in `Bravo` is `5`.


[regex]: https://docs.python.org/3/library/re.html
[regex-how-to]: https://docs.python.org/3/howto/regex.html
[str]: https://docs.python.org/3/library/stdtypes.html#textseq
[compile]: https://docs.python.org/3/library/re.html?#re.compile
[regex-object]: https://docs.python.org/3/library/re.html?#re-objects
[sub]: https://docs.python.org/3/library/re.html?#re.sub
[method-chaining]: https://www.tutorialspoint.com/Explain-Python-class-method-chaining
[lower]: https://docs.python.org/3/library/stdtypes.html?highlight=lower#str.lower
[set]: https://docs.python.org/3/library/stdtypes.html?highlight=set#set
[len]: https://docs.python.org/3/library/functions.html?highlight=len#len

