# Approach: Filter with `re.findall()` and join via `str.join()`


```python
import re


def abbreviate(to_abbreviate):
    # Capitalize the input before cleaning.
    cleaned = re.findall(r"[a-zA-Z']+", to_abbreviate.upper())
    
    return "".join(word[0] for word in cleaned)

#OR#

def abbreviate(to_abbreviate):
    # Capitalize the result after joining.
    return "".join(word[0] for word in
                   re.findall(r"[a-zA-Z']+", to_abbreviate)).upper()
```


This approach begins by using the [`re.findall()`][re-findall] method from the [`re` module][re-module] to clean `to_abbreviate` and split it into words.

Python's `re` module provides support for [regular expressions][regular expressions] within the language, and has many useful methods for searching, parsing, and modifying text.
Regular expression matching starts at the left-hand side of the input and travels toward the right.


`re.findall()` searches text for all matching patterns, returning results (_including 'empty' matches_) in a `list` of strings.


The regular expression `[a-zA-Z']+` in the code example looks for any single character in the range `a-z` (_lowercase_) and `A-Z` (_uppercase_), plus the `'` (_apostrophe_) character.
The `+` operator is a 'greedy' modifier that matches the previous range one to unlimited times.
This means that the expression will match any collection or repeat of letters (_a word_), but will not match any sort of space or 'non-letter' character, such as a tab, space, hyphen, or underscore.

For example, in `Complementary metal-oxide semiconductor`, the regex will match `Complementary`, `metal`, `oxide`, and `semiconductor`.
The regex will not match any of the spaces or the hyphen (`-`).
The result returned by `findall()` will then be `["Complementary", "metal", "oxide", "semiconductor"]`.


~~~~exercism/note
`to_abbreviate.replace("-", " ").replace("_", " ").upper().split()` can also be used to clean `to_abbreviate` and turn the results into a `list`.
The `.replace()` approach benchmarked faster than using `re.findall()` to clean, most likely due to overhead in importing the `re` module and in the [backtracking][backtracking] behavior of regex searching and matching.

[backtracking]: https://stackoverflow.com/questions/9011592/in-regular-expressions-what-is-a-backtracking-back-referencing
~~~~


Once `findall()` completes, a [`generator-expression`][generator-expression] is used to iterate through the results and select the first letters of each word via [`bracket notation`][subscript notation].


Generator expressions are short-form [generators][generators] — [lazy iterators][lazy iterator] that produce their values _on demand_, instead of saving them to memory.
This generator expression is consumed by [`str.join()`][str-join], which joins the generated letters together using an empty string.
Other "separator" strings can be used with `str.join()` — see [concept:python/string-methods]() for some additional examples.


Finally, the result of `.join()` is capitalized using the [chained][chaining] [`str.upper()`][str-upper].
Alternatively, `str.upper()` can be used on `to_abbreviate` within `findall()`, to uppercase the input before cleaning.
Since the solution is fairly succinct, it can be condensed onto the `return` line, rather than assigning and returning an intermediate variable for the acronym.


This approach was less performant in benchmarks than those using `loop`, `map`, `list-comprehension`, and `reduce`.


## Variation 1: `re.finditer()`


```python
import re


def abbreviate(to_abbreviate):
    # Capitalize the input before cleaning.
    cleaned = re.finditer(r"[a-zA-Z']+", to_abbreviate.upper())

    # word.group(0)[0] (first letter of Matched word) can also be written as
    # word[0][0], with the first bracketed number referring to Match group 0.
    return "".join(word.group(0)[0] for word in cleaned)

#OR#

def abbreviate(to_abbreviate):
    # Capitalize the output after joining.
    # Use bracket notation for Match group.
    return "".join(word[0][0] for word in
                   re.finditer(r"[a-zA-Z']+", to_abbreviate)).upper()
```


This variant uses [`re.finditer()`][re-finditer] for cleaning instead of `re.findall()`.

The `re.finditer()` method works in the same fashion as `re.findall()`, but it returns results as a _[lazy iterator][lazy iterator]_ over [`Match` objects][match objects].
This means that `re.finditer()` produces matches _on demand_ instead of saving them to memory, but needs to have both the iterator and the `Match` objects _unpacked_.

Due to this, the generator expression was modified to unpack the `Match` objects via `word.group(0)` (or `word[0]`) before the first letter is selected.


[chaining]: https://pyneng.readthedocs.io/en/latest/book/04_data_structures/method_chaining.html
[generator-expression]: https://dbader.org/blog/python-generator-expressions
[generators]: https://dbader.org/blog/python-generators
[lazy iterator]: https://www.pythonmorsels.com/what-is-an-iterator/
[re-findall]: https://docs.python.org/3/library/re.html#re.findall
[re-finditer]: https://docs.python.org/3/library/re.html#re.finditer
[re-module]: https://docs.python.org/3/library/re.html
[regular expressions]: https://en.wikipedia.org/wiki/Regular_expression
[str-join]: https://docs.python.org/3/library/stdtypes.html#str.join
[str-upper]: https://docs.python.org/3/library/stdtypes.html#str.upper
[subscript notation]: https://docs.python.org/3/glossary.html#term-slice
[match objects]: https://docs.python.org/3/library/re.html#re.Match
