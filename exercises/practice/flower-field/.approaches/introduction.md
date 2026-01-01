
# Introduction

The Flower Field exercise is designed to practice iteration, boolean logic and raising errors with error messages.
It also provides ample opportunities for working with `lists`, `list-indexing`, `comprehensions`, `tuples`, and `generator-expressions`.


## General considerations and guidance for the exercise

It is possible (_and potentially easier_) to break the problem down into a series of sub-tasks, with plenty of scope to mix and match strategies within these sections:

- Is the board valid?
- Is the current square a flower?
- What are the valid neighboring squares, and how many of them contain flowers?

Core Python does not support matrices nor N-dimensional arrays, though these are at the heart of many third-party packages such as NumPy.
Due to this limitation, the input board and final result for this exercise are implemented in the tests as a `list` of strings; one string per "row" of the board.


Intermediate processing for the problem is likely to use lists of lists with a final `''.join()` for each "row" in the returned single `list`, although other strategies could be employed.
Helpfully, Python considers both [lists][ordered-sequences] and [strings][text-sequences] as [sequence types][common-sequence-operations], and can iterate over/index into both in the same fashion.


## Validating boards

The "board" or "field" must be rectangular: essentially, all rows must be the same length as the first row.
This means that any board can be invalidated using the built-ins `all()` or `any()` to check for equal lengths of the strings in the `list` (_see an example below_).

Perhaps surprisingly, both row and column lengths **can be zero/empty**, so an apparently "non-existent board or field" is considered valid and needs special handling:


```python
    rows = len(garden)
    if rows > 0:
        cols = len(garden[0])
    else:
        return []
        
    if any([len(row) != cols for row in garden]):
        raise ValueError('The board is invalid with current input.')
```

Additionally, the only valid entries for the board/field are a space `' '` (_position empty_) or an asterisk `'*'` (_flower in position_).
 All other characters are _invalid_ and should `raise` an error with an appropriate error message.
 The exercise [tests][flower-field-tests] check for specific error messages including punctuation, so should be read or copied carefully.

Some solutions use regular expressions for these checks, but there are simpler (_and more performant_) options:


```python
    if garden[row][col] not in (' ', '*'):
        # raise error
```

Depending on how the code is structured, it may be possible to combine the checks for row length with the checks for valid characters.
More commonly, board/field dimensions are checked at the beginning.
Invalid characters are then detected while iterating through the rows of the board/field.


## Processing squares and finding occupied neighbors

Squares containing a flower are straightforward: you can copy `'*'` to the corresponding square in the results `list`.

Empty squares present a challenge: count how many flowers are in all the squares _adjacent_ to it.
But *How many squares are adjacent to the current position?*
In the middle of a reasonably large board there will be 8 adjacent squares, but this is reduced for squares at edges or corners.


### Some square processing methods

Note that we only want a _count_ of nearby flowers.
Their precise _location_ is irrelevant.


1. Nested `if..elif` statements

   This can be made to work, but can quickly become very verbose or confusing if not thought out carefully:

   ```python
       for index_i, _ in enumerate(flowerfield):
        temp_row = ""
        for index_j in range(column_count):
            if flowerfield[index_i][index_j].isspace():
                temp_row += count_flowers(flowerfield, index_i, index_j)
            elif flowerfield[index_i][index_j] == "*":
                temp_row += "*"
            else:
                raise ValueError("The board is invalid with current input.")
        flowerfield[index_i] = temp_row
    ```

2. Explicit coordinates

   List all the possibilities then filter out any squares that fall outside the board:

    ```python
        def count_adjacent(row, col):
            adj_squares = (
                (row-1, col-1), (row-1, col), (row-1, col+1),
                (row,   col-1),           (row,   col+1),
                (row+1, col-1), (row+1, col), (row+1, col+1),
            )
    
            # which are on the board?
            neighbors = [garden[row][col] for row, col in adj_squares
                         if 0 <= row < rows and 0 <= col < cols]
            # how many contain flowers?
            return len([adj for adj in neighbors if adj == '*'])
    ```

3. Using a comprehension or generator expression

    ```python
     # Using a list comprehension
     squares = [(row + row_diff, col + col_diff) 
                 for row_diff in (-1, 0, 1) 
                 for col_diff in (-1, 0, 1)]
      
     # Using a generator expression       
     squares = ((row + row_diff, col + col_diff) 
                 for row_diff in (-1, 0, 1) 
                 for col_diff in (-1, 0, 1))
    ```

     A key insight here is that we can work on a 3x3 block of cells: we already ensured that the central cell does *not* contain a flower that would affect our count.
    We can then filter and count as in the `count_adjacent` function in the previous code.

4.  Using complex numbers

    ```python
    def neighbors(cell):
            """Yield all eight neighboring cells."""
            for x in (-1, 0, 1):
                for y in (-1, 0, 1):
                    if offset := x + y * 1j:
                        yield cell + offset
    ```

    A particularly elegant solution is to treat the board/field as a portion of the complex plane.
    In Python, [complex numbers][complex-numbers] are a standard numeric type, alongside integers and floats.
    *This is less widely known than it deserves to be.*

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


## Ways of putting it all together

The example below takes an object-oriented approach using complex numbers, included because it is a particularly clear illustration of the various topics discussed above.

All validation checks are done in the object constructor.

```python
"""Flower Field."""

def neighbors(cell):
    """Yield all eight neighboring cells."""
    for x in (-1, 0, 1):
        for y in (-1, 0, 1):
            if offset := x + y * 1j:
                yield cell + offset


class Garden:
    """garden helper."""

    def __init__(self, data):
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

    def val(self, x, y):
        """Return the value for one square."""
        cur = x + y * 1j
        if self.data[cur] == "*":
            return "*"
        count = sum(self.data.get(neighbor, "") == "*" for neighbor in neighbors(cur))
        return str(count) if count else " "

    def convert(self):
        """Convert the garden."""
        return ["".join(self.val(x, y) 
                for x in range(self.width))
                for y in range(self.height)]


def annotate(garden):
    """Annotate a garden."""
    return Garden(garden).convert()
```

The example below takes an opposite strategy, using a single function, `list comprehensions`, and nested `if-elif` statements":

```python
def annotate(garden):
    grid = [[0 for _ in row] for row in garden]
    positions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    for col, row in enumerate(garden):
        # Checking that the board/field is rectangular up front.
        if len(row) != len(grid[0]):
            raise ValueError("The board is invalid with current input.")
        
        # Validating square content.
        for index, square in enumerate(row):
            if square == " ": 
                continue
            elif square != "*":
                raise ValueError("The board is invalid with current input.")
            grid[col][index] = "*"
            
            for dr, dc in positions:
                dr += col
                if dr < 0 or dr >= len(grid):
                    continue
                
                dc += index
                if dc < 0 or dc >= len(grid[dr]):
                    continue
                
                if grid[dr][dc] != "*":
                    grid[dr][dc] += 1
                
    return ["".join(" " if square == 0 else str(square) for square in row) for row in grid]
```

[common-sequence-operations]: https://docs.python.org/3.13/library/stdtypes.html#common-sequence-operations
[complex-numbers]: https://exercism.org/tracks/python/concepts/complex-numbers
[flower-field-tests]: https://github.com/exercism/python/blob/main/exercises/practice/flower-field/flower_field_test.py
[ordered-sequences]: https://docs.python.org/3.13/library/stdtypes.html#sequence-types-list-tuple-range
[text-sequences]: https://docs.python.org/3.13/library/stdtypes.html#text-sequence-type-str
[walrus-operator]: https://peps.python.org/pep-0572/
