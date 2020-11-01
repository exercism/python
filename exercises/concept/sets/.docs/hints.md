## General

- [Tuples](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences) are immutable.
  [Sequence Types](https://docs.python.org/3/library/stdtypes.html#typesseq) that can contain any data type.
- Tuples are [iterable](https://docs.python.org/3/glossary.html#term-iterable).
- Elements within tuples can be accessed via [bracket notation](https://stackoverflow.com/questions/30250282/whats-the-difference-between-the-square-bracket-and-dot-notations-in-python), using a zero-based index.
- Other [Common Sequence Operations](https://docs.python.org/3/library/stdtypes.html#common-sequence-operations) can also be used when working with tuples.

## 1. Extract coordinates

- Remember: tuples allow access via _index_, using _brackets_. Indexes start from the left at zero.

## 2. Format coordinates

- Check [`class tuple`](https://docs.python.org/3/library/stdtypes.html#tuple) for more details on tuples.
- Check [`class str`](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str) for more details on strings.

## 3. Match coordinates

- What methods could be used here for for [testing membership](https://docs.python.org/3/reference/expressions.html#membership-test-operations)?.
- Check [`class tuple`](https://docs.python.org/3/library/stdtypes.html#tuple) for more details on tuples.
- Could you re-use your `convert_coordinate()` function?

## 4. Combine matched records

- Remember that tuples support all [common sequence operations](https://docs.python.org/3/library/stdtypes.html#common-sequence-operations).
- Could you re-use your `compare_records()` function here?

## 5. "Clean up" & format a report of all records

- Remember: tuples are _immutable_, but the contents can be accessed via _index_ using _bracket notation_.
- Tuples don't have to use parentheses unless there is _ambiguity_.
- Python has multiple methods of string formatting. [`str.format()`](https://docs.python.org/3/library/stdtypes.html#str.format) and [`f-strings`](https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals) are two very common ones.
- There are multiple textual formatting options available via Pythons [`format specification mini-language`](https://docs.python.org/3/library/string.html#format-specification-mini-language).
