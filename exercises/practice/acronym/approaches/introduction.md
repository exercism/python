# Introduction

There are multiple Pythonic ways to solve the Acronym exercise.
Among them are:

- Using `str.replace()` to scrub the input, and:
  - joining with a `for loop` with string concatenation via the `+` operator.
  - joining via `str.join()`, passing a `list-comprehension` or `generator-expression`.
  - joining via `str.join()`,  passing `map()`.
  - joining via `functools.reduce()`.

- Using `re.findall()`/`re.finditer()` to scrub the input, and:
  - joining via `str.join()`, passing a `generator-expression`.

 - Using `re.sub()` for both cleaning and joining (_using "only" regex for almost everything_)`


## General Guidance

The goal of the Acronym exercise is to collect the first letters of each word in the input phrase and return them as a single capitalized string (_the acronym_).
The challenge is to efficiently identify and capitalize the first letters while removing or ignoring non-letter characters such as `'`,`-`,`_`, and white space.


There are two idiomatic strategies for non-letter character removal:
- Python's built-in [`str.replace()`][str-replace].
- The [`re`][re] module, (_regular expressions_).

For all but the most complex scenarios, using `str.replace()` is generally more efficient than using a regular expression.


Forming the final acronym is most easily done with a direct or indirect `loop`, after splitting the input into a word list via [`str.split()`][str-split].
The majority of these approaches demonstrate alternatives to the "classic" looping structure using various other iteration techniques.
Some `regex` methods can avoid looping altogether, although they can become very non-performant due to excessive backtracking.

Strings are _immutable_, so any method to produce an acronym will be creating and returning a new `str`.


## Approach: scrub with `replace()` and join via `for` loop

```python
def abbreviate(to_abbreviate):
    phrase = to_abbreviate.replace('-', ' ').replace('_', ' ').upper().split()
    acronym = ''
    
    for word in phrase:
        acronym += word[0]

    return acronym
```

For more information, take a look at the [loop approach][approach-loop].


## Approach: scrub with `replace()` and join via `list comprehension` or `Generator expression`


```python
def abbreviate(to_abbreviate):
    phrase = to_abbreviate.replace('-', ' ').replace('_', ' ').upper().split()
    
    return ''.join([word[0] for word in phrase])
    
###OR### 
    
def abbreviate(to_abbreviate):
    phrase = to_abbreviate.replace('-', ' ').replace('_', ' ').upper().split()
    
    # note the parenthesis instead of square brackets.    
    return ''.join((word[0] for word in phrase))
```

For more information, check out the [list-comprehension][approach-list-comprehension]  approach or the [generator-expression][approach-generator-expression] approach.


## Approach: scrub with `replace()` and join via `map()`

```python
def abbreviate(to_abbreviate):
    phrase = to_abbreviate.replace("_", " ").replace("-", " ").upper().split()
    
    return ''.join(map(lambda word: word[0], phrase))
```

For more information, read the [map][approach-map-function] approach.


## Approach: scrub with `replace()` and join via `functools.reduce()`

```python
from functools import reduce


def abbreviate(to_abbreviate):
    phrase = to_abbreviate.replace("_", " ").replace("-", " ").upper().split()
    
    return reduce(lambda start, word: start + word[0], phrase, "")
```

For more information, take a look at the [functools.reduce()][approach-functools-reduce] approach.


## Approach: filter with `re.findall()` and join via `str.join()`

```python
import re


def abbreviate(phrase):
    removed = re.findall(r"[a-zA-Z']+", phrase)
    
    return ''.join(word[0] for word in removed).upper()
```

For more information, take a look at the [regex-join][approach-regex-join] approach.


## Approach: use `re.sub()`

```python
import re


def abbreviate_regex_sub(to_abbreviate):
    pattern = re.compile(r"(?<!_)\B[\w']+|[ ,\-_]")
 
    return  re.sub(pattern, "", to_abbreviate.upper())
```

For more information, read the [regex-sub][approach-regex-sub] approach.


## Other approaches

Besides these seven idiomatic approaches, there are a multitude of possible variations using different string cleaning and joining methods.

However, these listed approaches cover the majority of 'mainstream' strategies.


## Which approach to use?

All seven approaches are idiomatic, and show multiple paradigms and possibilities.
All approaches are also `O(n)`, with `n` being the length of the input string.
No matter the removal method, the entire input string must be iterated through to be cleaned and the first letters extracted.

Of these strategies, the `loop` approach is the fastest, although `list-comprehension`, `map`,  and `reduce` have near-identical performance for the test data.
All approaches are fairly succinct and readable, although the 'classic' loop is probably the easiest understood by those coming to Python from other programming languages.


The least performant for the test data was using a `generator-expression`, `re.findall` and  `re.sub` (_least performant_).

To compare performance of the approaches, take a look at the [Performance article][article-performance].

[approach-functools-reduce]: https://exercism.org/tracks/python/exercises/acronym/approaches/functools-reduce
[approach-generator-expression]: https://exercism.org/tracks/python/exercises/acronym/approaches/generator-expression
[approach-list-comprehension]: https://exercism.org/tracks/python/exercises/acronym/approaches/list-comprehension
[approach-loop]: https://exercism.org/tracks/python/exercises/acronym/approaches/loop
[approach-map-function]: https://exercism.org/tracks/python/exercises/acronym/approaches/map-function
[approach-regex-join]: https://exercism.org/tracks/python/exercises/acronym/approaches/regex-join
[approach-regex-sub]: https://exercism.org/tracks/python/exercises/acronym/approaches/regex-sub
[article-performance]: https://exercism.org/tracks/python/exercises/isogram/articles/performance
