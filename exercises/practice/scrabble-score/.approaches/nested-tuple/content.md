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
    return sum(score for character in word for letters, score in LETTERS_OF_SCORE if character.upper() in letters)
```

The code starts with initializing a constant with a [tuple][tuple] of tuples (_also known as a nested tuple_).
Inside of the inner tuples there is 2 values, the first value is a string of letters and the second value is the score for the letters.

Then a function is defined that takes a word as an argument.
The function returns a [generator expression][generator-expersion] similar to the [dictionary approach][dictionary-approach] but has some slight modifcations.

The difference is that this one uses a nested [for loop][for-loop] to iterate over the letters and the tuples.
We first iterate over the characters in the word and then iterate over the tuples.
Which means that for each letter are we iterating over all of the tuples.
There the tuple is unpacked into the letters and the score.
You can read more about unpacking in the [concept:python/unpacking-and-multiple-assignment]().

Then we check if the character is in the letters and if it is we return the score.

[tuple]: https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences
[generator-expersion]: https://peps.python.org/pep-0289/
[for-loop]: https://realpython.com/python-for-loop/
