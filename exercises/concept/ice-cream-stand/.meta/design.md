# Design

## Goal

The goal of the concept exercise described in this issue is to teach understanding/use of the itertools module in Python.

## Learning objectives

Learn more about iteration tools the Python Standard Library provides through the itertools module.

Build and understanding of and use the following functions from the module, as well as practicing some of the recipes included:

At least one of the infinite itertators: `count()`, `cycle()`, or `repeat()`

- `accumulate()`
- `product()`
- `chain() & chain.from_iterable()`
- `groupby()`
- `islice()`
- `zip_longest() and the zip() built-in`
- `permutations()`
- `combinations()`

## Concepts

- iteration
- iterators
- itertools

## Topics that are Out of scope

- `classes` & `class customization` beyond the use of the `itertools` methods.
- `class-inheritance` beyond what is needed to customize iteration using `itertools`
- `comprehensions` beyond what is needed to work with itertools
- `comprehensions` in `lambdas`
- coroutines
- `decorators` beyond what is needed to work with `itertools`
- functions and higher-order functions beyond what might be needed to work with itertools
- `functools` and related `map`, `filter()` and `functools.reduce()`(they have their own exercise which is a prerequisite to this one)
- `generators` beyond what might be needed to work with itertools (they have their own exercise which is a prerequisite to this one)
- `lambdas` beyond what might be needed to work with `itertools`
- using an assignment expression or "walrus" operator (:=)
- class decorators
- enums

## Prerequisites

- `basics`
- `booleans`
- `comparisons`
- `rich-comparisons`
- **dicts**
- **dict-methods**
- **functions**
- **functional tools**
- _generators_
- **higher-order functions**
- **Identity methods is and is not**
- `iteration`
- `lists`
- `list-methods`
- `loops`
- `numbers`
- `sequences`
- **sets**
- `strings`
- `string-methods`
- `tuples`

## Representer

This exercise does not require any specific logic to be added to the [representer][representer]

## Analyzer

This exercise does not require any specific logic to be added to the [analyzer][analyzer].

[analyzer]: https://github.com/exercism/python-analyzer
[representer]: https://github.com/exercism/python-representer
