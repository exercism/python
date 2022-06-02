# Hints

## General


[Tuples][tuples] are immutable [sequence Types][sequence types] that can contain any data type.
Tuples are [iterable][iterable], and elements within tuples can be accessed via [bracket notation][bracket notation], using a zero-based index from the left, or -1 from the right.
Other [Common Sequence Operations][common sequence operations] can also be used when working with tuples.

## 1. Extract coordinates

- Remember: tuples allow access via _index_, using _brackets_. Indexes start from the left at zero.

## 2. Format coordinates

- Check [`class tuple`][class tuple] for more details on tuples.
- Check [`class str`][class str] for more details on strings.

## 3. Match coordinates

- What methods could be used here for for [testing membership][testing membership]?.
- Check [`class tuple`][class tuple] for more details on tuples.
- Could you re-use your `convert_coordinate()` function?

## 4. Combine matched records

- Remember that tuples support all [common sequence operations][common sequence operations].
- Could you re-use your `compare_records()` function here?

## 5. "Clean up" & make a report of all records

- Remember: tuples are _immutable_, but the contents can be accessed via _index_ using _bracket notation_.
- Tuples don't have to use parentheses unless there is _ambiguity_.
- Python has multiple methods of string formatting. [`str.format()`][str.format] and [`f-strings`][f-strings] are two very common ones.
- There are multiple textual formatting options available via Pythons [`format specification mini-language`][format specification mini-language].


[tuples]: https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences
[sequence types]: https://docs.python.org/3/library/stdtypes.html#typesseq
[iterable]: https://docs.python.org/3/glossary.html#term-iterable
[bracket notation]: https://stackoverflow.com/questions/30250282/whats-the-difference-between-the-square-bracket-and-dot-notations-in-python
[common sequence operations]: https://docs.python.org/3/library/stdtypes.html#common-sequence-operations
[class tuple]: https://docs.python.org/3/library/stdtypes.html#tuple
[class str]: https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
[str.format]: https://docs.python.org/3/library/stdtypes.html#str.format
[f-strings]: https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals
[format specification mini-language]: https://docs.python.org/3/library/string.html#format-specification-mini-language
[testing membership]: https://docs.python.org/3/reference/expressions.html#membership-test-operations
