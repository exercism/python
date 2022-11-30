# Filter with `re.findall()`

```python
import re


def is_isogram(phrase):
    scrubbed = "".join(re.findall("[a-zA-Z]", phrase)).lower()
    return len(set(scrubbed)) == len(scrubbed)

```

For this approach, [regular expression pattern][regex], also known as a [regex][regex-how-to], is used to filter the input phrase [str][str]ing.
- In the pattern of `[a-zA-Z]` the brackets are used to define a character set that looks for characters which are `a` through `z` or `A` through `Z`.
This essentially matches any characters which are in the English alphabet.
The pattern is passed to the [`findall()`][findall] method to return a list of matched characters.
- The result of `findall()` is passed as an argument to the [`join()`][join] method, which is called on an empty string.
This makes a string out of the list of matched characters.
- The output of `join()` is then [chained][method-chaining] as the input for [`lower()`][lower].
All of the letters are lowercased so that letters of different cases will become the same letter for comparison purposes,
since `A` and `a` are considered to be the same letter.
When the filtering and lowercasing is done, the scrubbed variable will be a string having all alphabetic letters lowercased.
- A [`set`][set] is constructed from the scrubbed string and its [`len`][len] is compared with the `len` of the the scrubbed string.
Since a `set` holds only unique values, the phrase will be an isogram if its number of unique letters is the same as its total number of letters.
The function returns whether the number of unique letters equals the total number of letters.
- For `Alpha` it would return `False`, because `a` is considered to repeat `A`, so the number of unique letters in `Alpha` is `4`,
and the total number of letters in `Alpha` is `5`.
- For `Bravo` it would return `True`, since the number of unique letters in `Bravo` is `5`, and the total number of letters in `Bravo` is `5`.


[regex]: https://docs.python.org/3/library/re.html
[regex-how-to]: https://docs.python.org/3/howto/regex.html
[str]: https://docs.python.org/3/library/stdtypes.html#textseq
[findall]: https://docs.python.org/3/library/re.html?#re.findall
[join]: https://docs.python.org/3/library/stdtypes.html?#str.join
[method-chaining]: https://www.tutorialspoint.com/Explain-Python-class-method-chaining
[lower]: https://docs.python.org/3/library/stdtypes.html?highlight=lower#str.lower
[set]: https://docs.python.org/3/library/stdtypes.html?highlight=set#set
[len]: https://docs.python.org/3/library/functions.html?highlight=len#len

