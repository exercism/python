## Approach: use `re.sub`


```python
import re


def abbreviate_regex_sub(to_abbreviate):
    pattern = re.compile(r"\B[a-z',]+|-| |[A-Z]{2}\b|[^A-Z'](?<=_)")
    
    return  re.sub(pattern, "", to_abbreviate).upper()
```

This approach begins by using the [`re.sub()`][re-sub] method from the [re][re] module to "scrub" (_remove_) non-letter characters such as `'`,`-`,`_`, and white space from `to_abbreviate`.
Python's `re` module provides support for [regular expressions][regular expressions] within the language, and has many useful methods for searching, parsing, and modifying text.


`sub()` searches text for all matching patterns, **sub**stituting a replacement string (_in our case, an empty string_).
Regular expression matching starts at the left-hand side of the input and travels toward the right.

~~~~exercism/caution
While it is a fun experiment to see if the entire problem can be more or less solved with a single regex, the excessive [backtracking][backtracking] used in this solution slows down performance considerably.
This solution tested the slowest of all solutions during benchmarking.  


A more performant method of cleaning would be to use [`re.findall()`][re-findall] or [`re.finditer()`][re-finditer] to scrub the phrase of unwanted characters, and then process the results with a `list-comprehension` or `loop` to extract the first letters of words.
`to_abbreviate.replace("_", " ").replace("-", " ").upper().split()` can also be used, and is even more performant here for cleaning test inputs. 


However, if nothing but a regular expression will do, the third-party [regex][regex] module provides more tools for lookarounds, recursion, partial matches, and nested sets.
Experimenting with that third-party library on your local environment (_the exercism Python track does not support third-party libraries_) could aid in optimizing this complicated regular expression and help with extracting first letters to form acronyms.  

[backtracking]: https://stackoverflow.com/questions/9011592/in-regular-expressions-what-is-a-backtracking-back-referencing
[re-findall]: https://docs.python.org/3/library/re.html#re.findall
[re-finditer]: https://docs.python.org/3/library/re.html#re.finditer
[regex]: https://github.com/mrabarnett/mrab-regex
~~~~

The regular expression `\B[a-z',]+|-| |[A-Z]{2}\b|[^A-Z'](?<=_)` in the code example above has five alternatives for matching.
For convenience and reuse, the regex is compiled using [`re.compile()`][re-compile].
Alternatives are seperated with the pipe (`|`) symbol:


1.  `\B[a-z',]+`, which starts searching at a [non-word boundary][re-non-word boundary], looks for any character in the group `abcdefghijklmnopqrstuvwxyz',`.
The `+` operator is a 'greedy' modifier that matches a character in the previous group one to unlimited times.
This means that this expression will match any collection or repeat of the letters (_plus `'` and `,`_), but will omit matching on anything else.
2. `|-|` matches the character `-`, with no leading or trailing space.
3. `| |` matches one **single** space character.
4. `[A-Z]{2}\b` matches any character in `ABCDEFGHIJKLMNOPQRSTUVWXYZ` exactly twice (_that's the `{2}` part_) - but only right before a [word boundary][re-non-word boundary].
5. `[^A-Z'](?<=_)` matches a single character that is **not** in `ABCDEFGHIJKLMNOPQRSTUVWXYZ`, and then asserts a [positive lookbehind][positive lookbehind] to match `_`.

Because these matches are used in the `re.sub()` method, an empty string is _substituted_  - so the matches are _removed_ from the result.


As an example, for the input phrase `The Road _Not_ Taken`, the regex will match `he`, ` `, `oad`, ` `, `-`, `ot`, `-`, ` `, and `aken`, replacing each match with ''.
The result is the string `TRNT`.


To ensure that all results are capitalized for any input, the approach then [chains][chaining] [`.upper()`][str-upper] to `re.sub()` on the `return` line to produce the final acronym.

[chaining]: https://pyneng.readthedocs.io/en/latest/book/04_data_structures/method_chaining.html
[positive lookbehind]: https://www.regular-expressions.info/lookaround.html
[re-compile]: https://docs.python.org/3/library/re.html#re.compile
[re-non-word boundary]: https://stackoverflow.com/questions/4541573/what-are-non-word-boundary-in-regex-b-compared-to-word-boundary
[re-sub]: https://docs.python.org/3/library/re.html#re.sub
[re]: https://docs.python.org/3/library/re.html
[regular expressions]: https://en.wikipedia.org/wiki/Regular_expression
[str-upper]: https://docs.python.org/3/library/stdtypes.html#str.upper
