# Introduction

There are various ways to solve `scrabble-score`.
This approaches document shows different strategies to solve this exercise

## General guidance

The goal of this exercise is to write a function that calculates the scrabble score for a given word.
The problem is that

## Approach: Using a single dictionary

Using a single dictionary is an approach, it is simple and fast.
It is also very pythonic.

```python
LETTER_SCORES = {
    'A': 1,
    'E': 1,
    'I': 1,
    'O': 1,
    'U': 1,
    'L': 1,
    'N': 1,
    'R': 1,
    'S': 1,
    'T': 1,
    'D': 2,
    'G': 2,
    'B': 3,
    'C': 3,
    'M': 3,
    'P': 3,
    'F': 4,
    'H': 4,
    'V': 4,
    'W': 4,
    'Y': 4,
    'K': 5,
    'J': 8,
    'X': 8,
    'Q': 10,
    'Z': 10
}

def score(word):
    return sum(LETTER_SCORES[letter.upper()] for letter in word)
```

For more information, check the [Dictionary Approach][dictionary-approach].

## Approach: Using two sequences

Using two sequences is an approach, it is fast.
Although the reason you might not want to do this is that it is hard to read.

```python
KEYS = "AEIOULNRSTDGBCMPFHVWYKJXQZ"
SCORES = [1] * 10 + [2] * 2 + [3] * 4 + [4] * 5 + [5] * 1 + [8] * 2 +[10] * 2

def score(word):
    return sum(SCORES[KEYS.index(letter.upper())] for letter in word)
```

For more information, check the [Two Sequences Approach][two-sequences-approach].

## Approach: Enum

Using an `enum` is an approach, it is short and easy to read.
Although it is more complicated since it uses a class.

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
    return sum(Scrabble[char.upper()] for char in word)
```

You can read more about how to achieve this optimization in: [Enum Approach][enum-approach].

## Approach: Using a nested tuple

Tuples in python is more memory efficent than using a dictonary in python.
Although this solution since it is iterating over a tuple for every letter so is it slower.

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
    return sum(for character in word for letters, score in LETTERS_OF_SCORE if character in letters)
```

For more information, check the [Nested Tuple Approach][nested-tuple-approach].

[dictionary-approach]: https://exercism.org/tracks/python/exercises/scrabble-score/approaches/dictionary
[enum-approach]: https://exercism.org/tracks/python/exercises/scrabble-score/approaches/enum
[nested-tuple-approach]: https://exercism.org/tracks/python/exercises/scrabble-score/approaches/nested-tuple
[two-sequences-approach]: https://exercism.org/tracks/python/exercises/scrabble-score/approaches/two-sequences
