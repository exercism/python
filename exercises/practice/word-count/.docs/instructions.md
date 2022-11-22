# Instructions

Given a phrase, count the occurrences of each _word_ in that phrase.

For the purposes of this exercise you can expect that a _word_ will always be one of:

1. A _number_ composed of one or more ASCII digits (ie "0" or "1234") OR
2. A _simple word_ composed of one or more ASCII letters (ie "a" or "they") OR
3. A _contraction_ of two _simple words_ joined by a single apostrophe (ie "it's" or "they're")

When counting words you can assume the following rules:

1. The count is _case insensitive_ (ie "You", "you", and "YOU" are 3 uses of the same word)
2. The count is _unordered_; the tests will ignore how words and counts are ordered
3. Other than the apostrophe in a _contraction_ all forms of _punctuation_ are ignored
4. The words can be separated by _any_ form of whitespace (ie "\t", "\n", " ")

For example, for the phrase `"That's the password: 'PASSWORD 123'!", cried the Special Agent.\nSo I fled.` the count would be:

```text
that's: 1
the: 2
password: 2
123: 1
cried: 1
special: 1
agent: 1
so: 1
i: 1
fled: 1
```
