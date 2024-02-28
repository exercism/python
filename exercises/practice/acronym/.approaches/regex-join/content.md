# Approach: filter with `re.findall()` and join via `str.join()`


```python
import re

###re.findall###

def abbreviate(to_abbreviate):
    #Capitalize the input before cleaning.
    removed = re.findall(r"[a-zA-Z']+", to_abbreviate.upper())
    
    return ''.join(word[0] for word in removed)

#OR#

def abbreviate(to_abbreviate):
    #Capitalize the result after joining.
    return ''.join(word[0] for word in
                   re.findall(r"[a-zA-Z']+", to_abbreviate)).upper()
                   
###re.finditer###

def abbreviate(to_abbreviate):
    #Capitalize the input before cleaning.
    removed = re.finditer(r"[a-zA-Z']+", to_abbreviate.upper())

    #word.group(0)[0] (first letter of Matched word) can also be written as
    #word[0][0], with the first bracketed number referring to Match group 0.
    return ''.join(word.group(0)[0] for word in removed)

#OR#

def abbreviate(to_abbreviate):
    #Capitalize the output after joining.
    #Use bracket notation for Match group.
    return ''.join(word[0][0] for word in
                   re.finditer(r"[a-zA-Z']+", to_abbreviate)).upper()                          
```


This approach begins by using  [`re.findall()`][re-findall] method from the [re][re] module to "scrub" (_remove_) non-letter characters such as `'`,`-`,`_`, and white space from `to_abbreviate`.
Python's `re` module provides support for [regular expressions][regular expressions] within the language, and has many useful methods for searching, parsing, and modifying text.
Regular expression matching starts at the left-hand side of the input and travels toward the right.


`re.findall()` searches text for all matching patterns, returning results (_including 'empty' matches_) in a `list` of strings.


The [`re.finditer()`][re-finditer] method works in the same fashion as `re.findall()`, but returns results as a _[lazy iterator][lazy iterator]_ over [Match objects][match objects].
 This means that `re.finditer()` produces matches _on demand_ instead of saving them to memory, but needs to have both the iterator and the Match objects _unpacked_.


The regular expression `r[a-zA-Z']+` in the code example looks for any single character in the range `a-z` lowercase and `A-Z` uppercase, plus the `'` (_apostrophe_) character.
The `+` operator is a 'greedy' modifier that matches the previous range one to unlimited times.
This means that the expression will match any collection or repeat of letters (_word_), but will omit matching on any sort of space or 'non-letter' character, such as `\t`, `\n`, ` `, `_`, or `-`.

For example, in `Complementary metal-oxide semiconductor`, the regex will match `Complementary`, `metal`, `oxide`, and `semiconductor`.
The regex will not match on ` ` or `-`.
The result returned by `findall()` will then be `['Complementary', 'metal', 'oxide', 'semiconductor']`.


~~~~exercism/note
`to_abbreviate.replace("_", " ").replace("-", " ").upper().split()` can also be used to 'scrub' `to_abbreviate` and turn the results into a `list`.
The `.replace()` approach benchmarked faster than using `re.findall()`/`re.finditer()` to 'scrub', most likely due to overhead in importing the `re` module and in the [backtracking][backtracking] behavior of regex searching and matching.

[backtracking]: https://stackoverflow.com/questions/9011592/in-regular-expressions-what-is-a-backtracking-back-referencing
~~~~


Once `findall()` or `finditer()` completes, a [`generator-expression`][generator-expression] is used to iterate through the results and select the first letters of each word via [`bracket notation`][subscript notation].
Note that when using `finditer()`, the `Match object` has to be unpacked via `match.group(0)`/`match[0]` before the first letter can be selected.


Generator expressions are short-form [generators][generators] - lazy iterators that produce their values _on demand_, instead of saving them to memory.
This generator expression is consumed by [`str.join()`][str-join], which joins the generated letters together using an empty string.
Other "seperator" strings can be used with `str.join()` - see [concept:python/string-methods]() for some additional examples.


Finally, the result of `.join()` is capitalized using the [chained][chaining] [`.upper()`][str-upper].
Alternatively, `.upper()` can be used on `to_abbreviate` within `findall()`/`finditer()`, to uppercase the input before cleaning.
Since the generator expression + join + upper is fairly succinct, they can be placed directly on the `return` line rather than assigning and returning an intermediate variable for the acronym.


This approach was less performant in benchmarks than those using `loop`, `map`,  `list-comprehension`, and `reduce`.

[chaining]: https://pyneng.readthedocs.io/en/latest/book/04_data_structures/method_chaining.html
[generator-expression]: https://dbader.org/blog/python-generator-expressions
[generators]: https://dbader.org/blog/python-generators
[lazy iterator]: https://www.pythonmorsels.com/what-is-an-iterator/
[re-findall]: https://docs.python.org/3/library/re.html#re.findall
[re-finditer]: https://docs.python.org/3/library/re.html#re.finditer
[re]: https://docs.python.org/3/library/re.html
[regular expressions]: https://en.wikipedia.org/wiki/Regular_expression
[str-join]: https://docs.python.org/3/library/stdtypes.html#str.join
[str-upper]: https://docs.python.org/3/library/stdtypes.html#str.upper
[subscript notation]: https://docs.python.org/3/glossary.html#term-slice
[match objects]: https://docs.python.org/3/library/re.html#re.Match
