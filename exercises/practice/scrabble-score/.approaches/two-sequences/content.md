# Two sequences

```python
KEYS = "AEIOULNRSTDGBCMPFHVWYKJXQZ"
SCORES = [1] * 10 + [2] * 2 + [3] * 4 + [4] * 5 + [5] * 1 + [8] * 2 + [10] * 2

def score(word):
    return sum(SCORES[KEYS.index(letter)] for letter in word.upper())
```

This approach uses a string and a [list][list], both of which are [sequence][sequence] types.
The code begins by defining a string constant with letters.
Then another constant is defined as a list with the corresponding letter score at the same index as the letter in the string.

The `score` function takes a word as an argument.
And uses the same [generator expression][generator-expression] as the [dictionary approach][dictionary-approach] with some slight modifications.

Instead of using a [dictionary][dictionary] and looking up the score, this approach looks up the index of the letter in the KEYS constant and then then looks up the value for that index in SCORES list within the generator expression.
These values are then added up by `sum`.

[dictionary]: https://docs.python.org/3/library/stdtypes.html#mapping-types-dict
[dictionary-approach]: https://exercism.org/tracks/python/exercises/scrabble-score/approaches/dictionary
[list]: https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
[sequence]: https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range
[generator-expersion]: https://peps.python.org/pep-0289/
