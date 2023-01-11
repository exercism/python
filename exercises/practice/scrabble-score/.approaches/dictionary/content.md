# Dictionary

```python
LETTER_SCORES = {
    'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1,
    'L': 1, 'N': 1, 'R': 1, 'S': 1, 'T': 1,
    'D': 2, 'G': 2, 'B': 3, 'C': 3, 'M': 3,
    'P': 3, 'F': 4, 'H': 4, 'V': 4, 'W': 4,
    'Y': 4, 'K': 5, 'J': 8, 'X': 8, 'Q': 10, 'Z': 10
}
def score(word):
    return sum(LETTER_SCORES[letter] for letter in word.upper())
```

This code starts with defining a constant LETTER_SCORES as a dictionary ([concept:python/dicts](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict)) where each letter is a key and the corresponding score is a value.
Then the `score` function is defined, which takes a `<word>` as an argument.

The function returns the total score for the word using the built-in function [`sum`][sum].
Sum is passed a [generator expression][generator-expression] that iterates over the letters in the word, looking up each score in LETTER_SCORES.
The generator expression produces the score values on the fly.
This means that it doesn't use memory to store all the values from LETTER_SCORES.
Instead, each value is looked up as needed by `sum`.

Within the generator expression, the word is converted from lower to uppercase.
Each letter of the word is looked up in LETTER_SCORES, and the score value is yielded to `sum` as `sum` iterates over the expression.
This is almost exactly the same process as using a `list comprehension`.
However, a `list comprehension` would look up the values and save them into a `list` in memory.
`sum` would then "unpack" or iterate over the `list`.

A variation on this dictionary approach is to use a dictionary transposition.

```python
LETTER_SCORES = {
    1: {'A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'},
    2: {'D', 'G'},
    3: {'B', 'C', 'M', 'P'},
    4: {'F', 'H', 'V', 'W', 'Y'},
    5: {'K'},
    8: {'J', 'X'},
    10: {'Q', 'Z'}
}

def score(word):
    return sum(next(score for score, letters in LETTER_SCORES.items() if character in letters) for character in word.upper())
```

However, transposing the dictionary so that the keys are the score and the values are the letters requires more computational calculation (_a loop within a loop_) and is harder to read.
Therefore, arranging the dictionary by letter is both more efficient and easier to understand.

[dictionary]: https://docs.python.org/3/library/stdtypes.html#mapping-types-dict
[generator-expression]: https://peps.python.org/pep-0289/
[sum]: https://docs.python.org/3/library/functions.html#sum
