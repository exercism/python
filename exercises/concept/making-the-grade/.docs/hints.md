# Hints

## General

- `while` loops are used for _indefinite_ (uncounted) iteration
- `for` loops are used for _definite_, (counted) iteration.
- The keywords `break` and `continue` help customize loop behavior.
- `range(<start>, stop, <step>)` can be used to generate a sequence for a loop counter.
- The built-in `enumerate()` will return (`<value>`, `<index>`) pairs to iterate over.

Also being familiar with the following can help with completing the tasks:

- [`lists`][list]: indexing, nested lists, [`<list>.append`][append and pop], [`<list>.pop()`][append and pop].
- [`str`][str]: `str()` constructor, using the `+` to concatenate strings, optionally, [`f-strings`][f-strings].

## 1. Rounding Scores

- `While` loops will continue to execute until their test condition evaluates to `False`.
- `<list>.pop()` will remove and return the last item in a `list`.
- Empty lists evaluate to `False` (most empty objects in Python are "Falsy")

## 2. Non-Passing Students

- There's no need to declare `loop` counters or `index` counters when iterating through an object using a `for` loop.
- A results counter does need to be set up and _incremented_ -- you'll want to `return` the count of non-passing students when the loop terminates. 

## 3. The "Best"

- There's no need to declare `loop` counters or `index` counters when iterating through an object using a `for` loop.
- Having an empty `list` to add the "best" marks to is helpful here.
- `<list>.append()` can help add things to the results `list`.

## 4. Calculating Letter Grades

- These are _lower thresholds_.  The _lower threshold_ for a "D" is a score of **41**, since an "F" is **<= 40**.
- [`range()`][range] can be helpful here to generate a sequence with the proper "F" -> "A" increments.
- [`round()`][round] without parameters should round off increments nicely.
- As with "the best" task, `<list>.append()` could be useful here to append items from `range()` into a results `list`.

## 5. Matching Names to Scores

- [`enumerate()`][enumerate] could be helpful here.
- If both lists are the same length and sorted the same way, could you use the `index` from one to retrieve a `value` from the other?

## 6. A "Perfect" Score

- There may be or may not be a student with a score of 100, and you can't return `[]` without checking **all** scores.
- The [`control flow`][control flow] statements `continue` and `break` may be useful here to move past unwanted values.

[list]: https://docs.python.org/3/library/stdtypes.html#list
[str]: https://docs.python.org/3/library/stdtypes.html#str
[f-strings]: https://docs.python.org/3/reference/lexical_analysis.html#formatted-string-literals
[append and pop]: https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
[enumerate]: https://docs.python.org/3/library/functions.html#enumerate
[control flow]: https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops
[range]: https://docs.python.org/3/tutorial/controlflow.html#the-range-function
[round]: https://docs.python.org/3/library/functions.html#round
