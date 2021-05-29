# Hints

## General

- The [Python Docs Tutorial for strings][python-str-doc] has an overview of the Python `str` type.
- String methods [<str>.join()][str-join] and [<str>.split()][str-split] ar very helpful when processing strings.
- The [Python Docs on Sequence Types][common sequence operations] has a rundown of operations common to all sequences, including `strings`, `lists`, `tuples`, and `ranges`.

There's four activities in the assignment, each with a set of text or words to work with.

## 1. Add a prefix to a word

- Small strings can be concatenated with the `+` operator.

## 2. Add prefixes to word groups

- Believe it or not, `<str>.join()` is all you need.
- Like `<str>.split()`, `<str>.join()` can take an arbitrary-length string, made up of any unicode code points.

## 3. Remove a suffix from a word

- Strings can be both indexed and sliced from either the left (starting at 0) or the right (starting at -1).
- If you want the last code point of an arbitrary-length string, you can use [-1].
- The last three letters in a string can be "sliced off" using a negative index. e.g. 'beautiful'[:-3] == 'beauti'

## 4. Extract and transform a word

- Using `<str>.split()` returns a list of strings broken on white space.
- `lists` are sequences, and can be indexed.
- `<str>.split()` can be direcly indexed. e.g. `'Exercism rocks!'.split()[0] == 'Exercism'`
- Be careful of punctuation! Periods can be removed via slice: `'dark.'[:-1] == 'dark'`

[python-str-doc]: https://docs.python.org/3/tutorial/introduction.html#strings

[common sequence operations]: https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
[str-join]: https://docs.python.org/3/library/stdtypes.html#str.join
[str-split]: https://docs.python.org/3/library/stdtypes.html#str.split
