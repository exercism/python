# Hints

## General

- All of the problems is solvable with different methods from the `itertools` module.

## 1. ice_cream_combinations

- The `itertools.combinations(iterable, size)` method can be used to generate all combinations of a an iterable like a `tuple` or `list`.

## 2. sprinkles

- The `itertools.compress(iterable, selector)` method can be used to filter an iterable based on a boolean selector.

## 3. fill_out_ice_cream_menu

- You can use `zip()` to combine an arbitrary number of iterables into a `tuple` of `tuples`.
- The `itertools.zip_longest(iterable, fillvalue)` method can be used to combine iterables of different lengths.
- You can give a value to the `fillvalue` parameter to fill in missing values.
