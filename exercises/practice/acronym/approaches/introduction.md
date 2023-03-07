# Introduction

There are multiple Pythonic ways to solve the Acronym exercise.
Among them are:

- Using `str.replace()` to scrub, and a `for loop` with string concatenation via the `+` operator.
- Using `str.replace()` to scrub, and joining via `str.join()`passing a `list-comprehension` or `generator-expression`.
- Using `str.replace()` to scrub, and joining via `map()` or `functools.reduce()`.
- Using `re.findall`/`re.finditer` to scrub, and `str.join` with a `generator-expression` or `list-comprehension`.
- Using only `re.sub` (aka "only" regex)`


## General Guidance

The goal of the Acronym exercise is to collect the first letters of each word in the input phrase and return them as a single capitalized string (_the acronym_) .

Strings are _immutable_, so any method to produce an acronym will be creating a new `str`.


Forming an acronym is most easily done with a direct or indirect loops, although some regex methods can avoid looping constructs altogether.

The challenge is to efficiently identify and capitalize the first letters while removing or ignoring non-letter characters such as `'`,`-`,`_`, and white space.



## Approach: scrub with `replace()` and join via `for` loop

```python
def abbreviate(to_abbreviate):
    phrase = to_abbreviate.replace('-' , ' ').replace("_", " ").upper().split()
    acronym = ""
    
    for word in phrase:
        acronym += word[0]

    return acronym

```

This approach uses the `str.replace()` method to remove non-letter characters, capitalizes all the words via `.upper()`, and creates a word list via `.split()`.
The resulting `list` is looped over to select the first letter of each word, which is then concatenated via `+` to the acronym string.

For more information, check the [loop approach][approach-loop].


## Approach: scrub with `replace()` and join via `list comprehension`

```python
def abbreviate(to_abbreviate):
    phrase = to_abbreviate.replace("_", " ").replace("-", " ").upper().split()
    words = [word[0] for word in phrase]
    acronym = ''.join(words)
    
    return acronym
```

This approach uses the `str.replace()` method to remove non-letter characters, capitalizes all the words via `.upper()`, and creates a word list via `.split()`.
A list comprehension is used to select the first letters of each word.
The list of first letters is then concatenated via `str.join()` to form the acronym.

For more information, check the [list-comprehension][approach-list-comprehension]  approach.


## Approach: scrub with `replace()` and join via `map()`

```python
def abbreviate(to_abbreviate):
    phrase = to_abbreviate.replace("_", " ").replace("-", " ").upper().split()
    acronym = ''.join(map(lambda word: word[0], phrase))
    
    return acronym
```

This approach uses the `str.replace()` method to remove non-letter characters, capitalizes all the words via `.upper()`, and creates a word list via `.split()`.
The first letters of each word are extracted via the built-in `map()` function, which is passed to `str.join()` to form the acronym.

For more information, check the [map][approach-map-function] approach.


## Approach: scrub with `replace()` and join via `functools.reduce()`

```python
from functools import reduce

def abbreviate(to_abbreviate):
    phrase = to_abbreviate.replace("_", " ").replace("-", " ").upper().split()
    acronym = reduce(lambda start, word: start + word[0], phrase, "")
    
    return acronym
```

This approach uses the `str.replace()` method to remove non-letter characters, capitalizes all the words via `.upper()`, and creates a word list via `.split()`.
 The acronym is created via `functools.reduce()`, isolating the first letters of each word, and joining them together in a new string.

For more information, take a look at the [functools.reduce()][approach-functools-reduce] approach.


## Approach: scrub with `replace()` & join via `generator expression`

```python
def abbreviate(to_abbreviate):
    phrase = to_abbreviate.replace("_", " ").replace("-", " ").upper().split()
    words = (word[0] for word in phrase) # note the parenthesis instead of square brackets.
    acronym = ''.join(words)
    
    return acronym

```

This approach uses the `str.replace()` method to remove non-letter characters, capitalizes all the words via `.upper()`, and creates a word list via `.split()`.
A `generator-expression` is used to select the first letters of each word.
The generator-expression is then consumed by `str.join()` to create the acronym.

For more information, check the [generator-expression][approach-generator-expression] approach.


## Approach: filter with `re.findall()` and join via `str.join()`

```python
import re


def abbreviate(phrase):
    removed = re.findall(r"[a-zA-Z']+", phrase)
    acronym = ''.join(word[0] for word in removed)
    
    return acronym.upper()

```

This approach uses a `regex` to remove non-letter characters, then uses a `generator-expression` passed to  `str.join()` to isolate the first letters of each word.

The resulting string is capitalized using `.upper()`.

For more information, check the [regex-join][approach-regex-join] approach.


## Approach: use `re.sub`

```python
import re

def abbreviate_regex_sub(to_abbreviate):
    acronym = re.sub("\B[a-z',]+|-| |[A-Z]{2}\b|[^A-Z'](?<=_)", "", to_abbreviate)
    
    return  acronym.upper()
```

This approach uses the regular expression module `re` to clean the string and identify the first letters of each word without the use of loops.

`.upper()` is then called on the result to capitalize all the characters.

For more information, read the [regex-sub][approach-regex-sub] approach.



## Other approaches

Besides these seven idiomatic approaches, there are a multitude of possible variations using different string cleaning and joining methods.

However, these listed approaches cover the majority of 'mainstream' strategies.



## Which approach to use?

All seven approaches are idiomatic, and show multiple paradigms and possiblities.

The `list-comprehension` approach is the fastest, although `loop`, `map`,  and`reduce`near identical in performance.

The least performant for the input data was using a `generator-expression` , `re.findall` and  `re.sub` (least performant).

To compare performance of the approaches, take a look at the [Performance article][article-performance].


[approach-functools-reduce]: https://exercism.org/tracks/python/exercises/acronym/approaches/functools-reduce
[approach-generator-expression]: https://exercism.org/tracks/python/exercises/acronym/approaches/generator-expression
[approach-list-comprehension]: https://exercism.org/tracks/python/exercises/acronym/approaches/list-comprehension
[approach-loop]: https://exercism.org/tracks/python/exercises/acronym/approaches/loop
[approach-map-function]: https://exercism.org/tracks/python/exercises/acronym/approaches/map-function
[approach-regex-join]: https://exercism.org/tracks/python/exercises/acronym/approaches/regex-join
[approach-regex-sub]: https://exercism.org/tracks/python/exercises/acronym/approaches/regex-sub
[article-performance]: https://exercism.org/tracks/python/exercises/isogram/articles/performance
