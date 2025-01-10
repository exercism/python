
# Introduction

This exercise tests iteration, logic and error handling.

## General considerations

It is possible to break the exercise down into a series of sub-tasks, with plenty of scope to mix and match approaches within these.

- Is the board valid?
- Is the current square a mine?
- what are the valid neighboring cells, and how many of them are mines?

Core Python does not support matrices, or N-dimensional arrays more generally, though these are at the heart of many third-party packes such as NumPy.

Thus, the input board and the final result are implemented as lists of strings, though intermediate processing is likely to use lists of lists plus a final `''.join()` for each row in the `return` statement.

Helpfully, Python can iterate over strings exactly like lists.

## Valid boards

The board must be rectangular: essentially, all rows must be the same length as the first row.

Perhaps surprisingly, the row and column lengths can be zero, so an apparently non-existent board is valid and needs special handling.

```python
    rows = len(minefield)
    if rows > 0:
        cols = len(minefield[0])
    else:
        return []
    if any([len(row) != cols for row in minefield]):
        raise ValueError('The board is invalid with current input.')
```

Additionally, the only valid entries are a space `' '` or an asterisk `'*'`. All other characters should raise an error.

Some solutions use regular expressions for this test, but there are simpler options:

```python
    if minefield[row][col] not in (' ', '*'):
        # raise error
```

Depending how the code is structured, it may be possible to combine the tests.

More commonly, the board dimensions are checked at the beginning, then invalid characters are detected while iterating through the board.

## Processing squares

Squares containg a mine are easy: just copy `'*'` to the corresponding square in the result.

For empty squares, the challenge is to count how many mines are in the adjacent squares.

*How many squares are adjacent?* In the middle of a reasonably large board there will be 8, but this is reduced for squares at the edges or corners.

### 1. Nested `if..elif` statements

This can be made to work, but quickly becomes very verbose.

### 2. Explicit coordinates

```python
    def count_adjacent(r, c):
        adj_squares = (
            (r-1, c-1), (r-1, c), (r-1, c+1),
            (r,   c-1),           (r,   c+1),
            (r+1, c-1), (r+1, c), (r+1, c+1),
        )

        # which are on the board?
        neighbors = [minefield[r][c] for r, c in adj_squares
                     if 0 <= r < rows and 0 <= c < cols]
        # how many contain mines?
        return len([adj for adj in neighbors if adj == '*'])
```

Slightly better, this lists all the possibilities then filters out any that fall outside the board.

Note that we only want a count of nearby mines, their precise location is irrelevant.

### 3. Use a comprehension or generator

A key insight is that we can work on a 3x3 block of cells, because we already ensured that the central cell does *not* contain a mine that would affect our count.

```python
        squares = ((row + row_diff, col + col_diff) 
                    for row_diff in (-1, 0, 1) 
                    for col_diff in (-1, 0, 1))
```

We can then filter and count as in the previous code.

### 4. Use complex numbers

A particularly elegant solution is to treat the board as a portion of the complex plane.

In Python, [complex numbers][complex-numbers] are a standard numeric type, alongside integers and floats.

*This is less widely known than it deserves to be.*

```python
def neighbors(cell: complex) -> Generator[complex, None, None]:
    """Yield all eight neighboring cells."""
    for x in (-1, 0, 1):
        for y in (-1, 0, 1):
            if offset := x + y * 1j:
                yield cell + offset
```

The constructor for a complex number is `complex(x, y)` or (as here) `x + y * 1j`, where `x` and `y` are the real and imaginary parts, respectively.

There are two properties of complex numbers that help us in this case:

- The real and imaginary parts act independently under addition.
- The value `complex(0, 0)` is the complex zero, which like integer zero is treated as False in Python conditionals.

A tuple of integers would not work as a substitute, because `+` behaves as the concatenation operator for tuples:

```python
>>> complex(1, 2) + complex(3, 4)
(4+6j)
>>> (1, 2) + (3, 4)
(1, 2, 3, 4)
```

Note also the use of the ["walrus" operator][walrus-operator] `:=` in the definition of `offset` above.

This relatively recent addition to Python simplifies variable assignment within the limited scope of an if statement or a comprehension.

***Bethany - any chance we could finish and merge PR #3585 so that I can reference it here?***

## Putting it all together

The example below is an object-oriented approach using complex numbers, included because it is a particularly clear illustration of the various topics discussed above:

```python
"""Minesweeper."""

from typing import Generator


def neighbors(cell: complex) -> Generator[complex, None, None]:
    """Yield all eight neighboring cells."""
    for x in (-1, 0, 1):
        for y in (-1, 0, 1):
            if offset := x + y * 1j:
                yield cell + offset


class Minefield:
    """Minefield helper."""

    def __init__(self, data: list[str]):
        """Initialize."""
        self.height = len(data)
        self.width = len(data[0]) if data else 0

        if not all(len(row) == self.width for row in data):
            raise ValueError("The board is invalid with current input.")

        self.data = {}
        for y, line in enumerate(data):
            for x, val in enumerate(line):
                self.data[x + y * 1j] = val
        if not all(v in (" ", "*") for v in self.data.values()):
            raise ValueError("The board is invalid with current input.")

    def val(self, x: int, y: int) -> str:
        """Return the value for one square."""
        cur = x + y * 1j
        if self.data[cur] == "*":
            return "*"
        count = sum(self.data.get(neighbor, "") == "*" for neighbor in neighbors(cur))
        return str(count) if count else " "

    def convert(self) -> list[str]:
        """Convert the minefield."""
        return [
            "".join(self.val(x, y) for x in range(self.width))
            for y in range(self.height)
        ]


def annotate(minefield: list[str]) -> list[str]:
    """Annotate a minefield."""
    return Minefield(minefield).convert()
```

The import is only needed for type annotation, so can be considered optional.

All validation is done in the object constructor.

[complex-numbers]: https://exercism.org/tracks/python/concepts/complex-numbers
[walrus-operator]: 
