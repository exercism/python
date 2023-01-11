# Introduction

There are various ways to solve `scrabble-score`.
This approaches document shows different strategies to solve this exercise.

## General guidance

The goal of this exercise is to write a function that calculates the scrabble score for a given word.
The challenge is that the scrabble score is calculated by summing the scores of individual letters in a word.
The student needs to find an efficient and easily accessed way to store individual letter scores for lookup when processing different words.

## Approach: Using a single dictionary

Using a single dictionary for letter lookup is simple and fast.
It is also very pythonic, and could be considered the canonical approach to this exercise.

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

For more information, check the [Dictionary Approach][dictionary-approach].

## Approach: Using two sequences

Using two sequences removes the need to use a nested data structure or a dictionary.
Although you might not want to use this approach because it is hard to read and maintain.

```python
KEYS = "AEIOULNRSTDGBCMPFHVWYKJXQZ"
SCORES = [1] * 10 + [2] * 2 + [3] * 4 + [4] * 5 + [5] * 1 + [8] * 2 +[10] * 2

def score(word):
    return sum(SCORES[KEYS.index(letter)] for letter in word.upper())
```

For more information, check the [Two Sequences Approach][two-sequences-approach].

## Approach: Enum

Using an `Enum` is is short and easy to read.
Although creating an `Enum` can be more complicated since it uses OOP (object oriented programming).

```python
from enum import IntEnum

class Scrabble(IntEnum):
    A = E = I = O = U = L = N = R = S = T = 1
    D = G = 2
    B = C = M = P = 3
    F = H = V = W = Y = 4
    K = 5
    J = X = 8
    Q = Z = 10

def score(word):
    return sum(Scrabble[letter] for letter in word.upper())
```

For more information, check the [Enum Approach][enum-approach].

## Approach: Using a nested tuple

Using a tuple in Python is generally more memory efficient than using a dictionary.
However, this solution requires iterating over the entire `tuple` for every letter in order to score a full word.
This makes the solution slower than the dictionary approach.

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

For more information, check the [Nested Tuple Approach][nested-tuple-approach].

[dictionary-approach]: https://exercism.org/tracks/python/exercises/scrabble-score/approaches/dictionary
[enum-approach]: https://exercism.org/tracks/python/exercises/scrabble-score/approaches/enum
[nested-tuple-approach]: https://exercism.org/tracks/python/exercises/scrabble-score/approaches/nested-tuple
[two-sequences-approach]: https://exercism.org/tracks/python/exercises/scrabble-score/approaches/two-sequences
