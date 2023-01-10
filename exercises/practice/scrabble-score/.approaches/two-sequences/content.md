# Two sequences

```python
KEYS = "AEIOULNRSTDGBCMPFHVWYKJXQZ"
SCORES = [1] * 10 + [2] * 2 + [3] * 4 + [4] * 5 + [5] * 1 + [8] * 2 + [10] * 2

def score(word):
    return sum(SCORES[KEYS.index(letter.upper())] for letter in word)
```

This approach uses a string and a [list][list], both of these data types belongs to the parent data type [sequences][sequence].
The code starts with defining a string constant with letters.
Then another constant is definded which is a list with corresponding score for the same index as the string.

The `score` function takes a word as a parameter.
And uses the same [generator expression][generator-expersion] as the [dictionary approach][dictionary-approach] with some slight modifications.

The difference is that instead of using a [dictionary][dictionary] and looking up the score inside of a dictonary.
This approach gets the index of the letter in the KEYS constant and then then looks up the value for that index in SCORES list.
Then takes that value and return that to the generator expression.

[dictionary]: https://docs.python.org/3/library/stdtypes.html#mapping-types-dict
[dictionary-approach]: https://exercism.org/tracks/python/exercises/scrabble-score/approaches/dictionary
[list]: https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
[sequence]: https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range
[generator-expersion]: https://peps.python.org/pep-0289/
