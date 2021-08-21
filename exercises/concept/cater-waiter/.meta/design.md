## Goal

The goal of this exercise is to teach the basics of [`sets`][set type] (_set type_) in Python.


## Learning objectives

*  understand that a set is an **unordered collection of distinct hashable objects**
*  create a `set` via constructor (`set()`) and  literal (`{}`)
*  de-dupe a list of elements by converting a sequence type such as a `list` to a `set` type
*  check for a membership of an element in a given set via `in`
*  set comparison functions and set comparison operators (`=<`, `>=`, `issubset()`, `issuperset()`, etc.)
*  additional set operators (`union`, `intersection`, `difference`, and `symmetric_difference`)
*  add values to a given set via `add()`
*  remove values from a given set via `discard()`
*  iterate through a given set by using `for item in <set>` and `for index, item in enumerate(<set>)`
*  understand that iterating through a set twince may result in a different iteration order (_sets are unordered_)

## Out of scope

*  `frozenset()`
*  `clear()` to delete all elements of a set
*  check the length of a given set via `len()`
*  `remove` as opposed to `discard` (_`remove` tosses a `keyerror` if the element is not present_)
*   all forms/variants of `update()`
*  remove (and use) a value from a given set via `pop()`
*  make shallow copy(s) of a given set via `copy()`
*  using additional builtins such as `sorted()`, `min()`, or `map()` with a set
*  set comprehensions

## Concepts

*  `sets`
*  [`hashable`][term-hashable] objects
* `set` comparisons
* `set` operations

## Prerequisites

* `basics`
* `booleans`
* `comparisons`
* `dicts`
* `lists`
* `loops`

## Resources to refer to

*  [Set Types (Python Official Docs)][set types](https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset)
*   [Hashable (Python Official Docs Glossary)][term-hashable]
*  [immutable (Python Official Docs Glossary)][term-immutable]

### Hints

Hints should link to the `Sets` section of the Python docs tutorial: [Sets][sets-tutorial], or equivelent resources.


### After

After, the student can explore comprehension syntax, although it will be taught in separate exercises. This would also be a good time to explore set comparisons via function &/or operator, or experimenting with the `issuperset()` & `issubset()` functions.



[set type]: https://github.com/exercism/v3/blob/master/languages/python/reference/concepts/builtin_types/set.md
[set types]: https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset
[sets-tutorial]: https://docs.python.org/3/tutorial/datastructures.html#sets
[term-hashable]: https://docs.python.org/3/glossary.html#term-hashable
[term-immutable]: https://docs.python.org/3/glossary.html#term-immutable