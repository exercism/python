# Design

## TODO: Add introduction for this concept.
## Goal

This concept exercise is meant to teach an understanding/use of `unpacking` and the `*` (splat) and `**` (double splat) operators  in Python.

<br>

## Learning objectives

- Understand/use `unpacking` through the use of `*` and `**` _prefix_ operators in various scenarios
  - `*` and `**` as _prefixes_ ..... not to be confused with `*` (_multiply_) and `**` (_exponentiation_) as _infix_, or mathematical operators (**consider a link in the links doc or a mention in dig deeper.**)
  - ~~what happens in the process of "unpacking" - form, ordering, & iteration~~ (this will go in a **dig deeper** or the link docs.)
  - use in arguments to `functions`
  - use in argument _capture_ for `functions` (_aka passing an arbitrary number of arguments -- *args * & **kwargs_)
  - ~~use in defining `keyword only arguments`~~ (_topic moved to arguments exercise_).
  - use in iterable (_mainly `tuple` and `list`_) unpacking & packing
  - use in `dict` unpacking & packing
- Understand/use `unpacking` via `multiple assignment`
  - using `multiple assignment ` in place of `indexing`
  - using `multiple assigment` + `*`  in place of `slicing`
  - ~~using "list-like" syntax & "tuple-like" syntax~~
  - unpacking plus "leftovers" via `*`
- Differences between straight  `multiple assignment` and `*` & `**`
- Deep unpacking


## Concepts

- `unpacking`
- `unpacking generalizations`
- `multiple assignment`


## Topics that are Out of scope

- `classes`
- `comprehensions`
- `comprehensions` in `lambdas`
- `map()`, `filter()` or `functools.reduce()` in a `comprehension`
-  `function-arguments` beyond explaining briefly how `*`, `**` work in function arguments.
- `functools` beyond `functools.reduce()`(_this will get its own exercise_)
- `generators`
- using an `assignment expression` or "walrus" operator (`:=`) alone or in a `lambda`


## Prerequisites

- `basics`
- `bools`
- `comparisons`
- `dicts`
- `lists`
- `numbers`
- `strings`
- `tuples`


## Representer

This exercise does not require any specific logic to be added to the [representer][representer]

## Analyzer

This exercise does not require any specific logic to be added to the [analyzer][analyzer].

[analyzer]: https://github.com/exercism/python-analyzer
[representer]: https://github.com/exercism/python-representer