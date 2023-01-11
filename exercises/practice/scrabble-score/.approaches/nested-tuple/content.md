# Nested Tuple

```python
LETTERS_OF_SCORE = (
    ("AEIOULNRST", 1),
    ("DG", 2),
    ("BCMP", 3),
    ("FHVWY", 4),
    ("K", 5),
    ("JX", 8),
    ("QZ", 10),
)

def score(word):
    return sum(score for character in word.upper() for
    letters, score in LETTERS_OF_SCORE if character in letters)
```

The code starts with defining a constant, `LETTERS_OF_SCORE` as a [`tuple`][tuple] of tuples (_also known as a nested tuple_).
Inside of the inner tuples are 2 values, the first value is a string of letters and the second value is the score for those letters.

Next, the `score` function is defined, taking a word as an argument.
The `score` function uses a [generator expression][generator-expression] similar to the [dictionary approach][dictionary-approach] with some slight modifications.

This particular approach uses a _nested_ [for loop][for-loop] to iterate over the letters and the tuples.
We first iterate over the characters in the word and then the tuples.
Which means that for **_each letter_** we iterate over **all** of the tuples.
Each iteration, the tuple is unpacked into the letters and their corresponding score.
You can read more about unpacking in the [concept:python/unpacking-and-multiple-assignment]().

Then the code checks if the character is in the unpacked letters and if it is we return its score.

[generator-expression]: https://peps.python.org/pep-0289/
[for-loop]: https://realpython.com/python-for-loop/
[tuple]: https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences
