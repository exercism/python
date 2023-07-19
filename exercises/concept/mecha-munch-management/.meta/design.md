## Learning objectives

Cover useful `dict` methods and a few techniques for operating on/manipulating `dicts`.

- `dict.setdefault()` for automatically adding keys when needed.
- `dict.fromkeys(iterable, <default value>)` for creating a new `dict` from any number of iterables.
- `dict.keys()`, `dict.values()`, and `dict.items()` for convenient iterators.
- `reversed(dict.keys())`, `reversed(dict.values())`, or `reversed(dict.items())` for reversed views.
- `sorted()` with `dict.items()`. for re-ordering entries in a `dict`.
- `dict_one.update(<dict_two>)` for updating one `dict` with overlapping values from another `dict`.
- `dict | other_dict` and `dict |= other_dict` for merging or updating two `dict`s via operators.
- `dict.popitem()` for removing and returning a key, value pair.

- Working more with  the `dict` views `items()` , `keys()` or `values()`.  (e.g, by sorting information using `sorted()` or by swapping `keys` and `values`, etc.)
- Knowing that Dictionaries can be _nested_, _-- e.g._ ' a dictionary of dictionaries'.
- Considerations when `updating()` or using `union` with dictionaries.

## Out of scope

Please take a look at the `dicts` concept exercise [design.md file](https://github.com/exercism/python/edit/main/exercises/concept/inventory-management/.meta/design.md) for `dict` features  taught thus far.
While those methods can be used for solutions to this exercise, it  isn't necessary to cover them again in detail.  Additionally, the following is out of scope:

- Dictionary comprehensions
- Built-in functions as they relate to this data structure (*e.g.* `len()`, or `enumerate()`
- Considerations of Mutability
- `copy()` vs `deepcopy()`
- Memory and performance characteristics.
- Related `collections` module with `Counter()` and `defaultdict()`

## Concepts

- `dicts`
- `dict-methods`

## Prerequisites

These are the concepts/concept exercises the student needs to complete/understand before solving this concept exercise.

- `basics`
- `bools`
- `conditionals`
- `comparisons`
- `dicts`
- `lists`
- `loops`
- `numbers`
- `strings`
- `tuples`


## Resources to refer to

- [Python docs:  Tutorial - Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
- [Python docs:  Mapping Type `dict`](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict)
- [Real Python:  Dicts](https://realpython.com/python-dicts/)
- [Digital Ocean:  Understanding dictionaries in python 3](https://www.digitalocean.com/community/tutorials/understanding-dictionaries-in-python-3)
- [Stack Overflow: exchanging keys with values in a `dict` in Python](https://stackoverflow.com/questions/1031851/how-do-i-exchange-keys-with-values-in-a-dictionary)
- [kite:  how to sort a dictionary by key in python](https://www.kite.com/python/answers/how-to-sort-a-dictionary-by-key-in-python)
- [medium:  16 Python Dictionary Tips](https://medium.com/python-in-plain-english/16-intermediate-level-python-dictionary-tips-tricks-and-shortcuts-1376859e1adc)  _**note:** this is a good resource for ideas and writing this exericse, but is a subscription-based service, so not the best for linking to_