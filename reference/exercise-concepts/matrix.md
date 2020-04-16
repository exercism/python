# Concepts of `matrix`

## Example implementation:

From the existing [example.py](https://github.com/exercism/python/blob/master/exercises/matrix/example.py):

```python
class Matrix:
    def __init__(self, s):
        self.rows = [[int(n) for n in row.split()]
                     for row in s.split('\n')]
        self.columns = [list(tup) for tup in zip(*self.rows)]

    def row(self, index):
        return self.rows[index - 1]

    def column(self, index):
        return self.columns[index - 1]
```

An alternate implementation [processing columns in a method rather than an instance property](https://exercism.io/tracks/python/exercises/matrix/solutions/e5004e990ddc4582a50ecc1f660c31df):

```python
class Matrix(object):

    def __init__(self, matrix_string):
        self.matrix = [[int(ele) for ele in row.split(' ') ] for row in matrix_string.split('\n')]

    def row(self, index):
        return self.matrix[index - 1]

    def column(self, index):
        return [row[index - 1] for row in self.matrix]
```

An extended implementation [using `.copy()` to protect against accidental data mutation](https://exercism.io/tracks/python/exercises/matrix/solutions/b6a3486a35c14372b64fdc35e7c6f98f):

```python
class Matrix(object):
    def __init__(self, matrix_string):
        # have to use "List Comprehension" to make lists in a list
        self.matrix = [[int(num) for num in tmp.split()] for tmp in matrix_string.splitlines()]

    def row(self, index): # grab which ever row requested
        return self.matrix[index - 1].copy() # use .copy() to protect accidental data issues

    def column(self, index): # grab the first number in each array
        return [row[index - 1] for row in self.matrix]

```

## Concepts

- [Classes][classes]: the exercise objective is to define a `matrix` type. Tested methods are linked to a `matrix` class
- [Objects][objects]: creating different instances with different data representing different `matrices` is tested
- [Constructor][constructor]: customizing object initalization with actions and persisting data. The example uses a constructor to process the passed in data into a list of lists assigned to an instance property
- [Dunder Methods][dunder-methods]: the example uses the `__init__` magic method as its constructor for the class
- [Return Values][return-value]: "row" and "column" list values are expected from defined instance method(s)
- [Implicit Argument][implicit-argument]: the example uses the `self` implicit argument for methods and properties linked to a specific instance of the class
- [Namespaces][namespaces]: knowing to use `self`.`<propertyname>` for instance properties and `self` as first argument to instance methods in a class
- [Instance Methods][instance-methods]: tests for this exercises require one or more instance methods that will return a specified row or column list of the `matrix`.
- [Instance Properties][instance-properties]: this exercise rquires one or more instance properties to persist passed in data.
- [Mutability][mutability]: in the extended example, knowing there are no protected or private properties in python and adjusting coding patterns
- [Assignment][assignment]: instance properties need to be assigned passed in data
- [Method Arguments][method-arguments]: the methods returning "row" and "column" need to take both `self` and an integer as arguments
- [Lists][lists]: this exercise requires "row" or "column" be returnd as a `list`. A `list` of `lists` is also the reccommended way to process and store the passed-in data.
- [Indexing][indexing]: the "rows" and "columns" of this exercise need to be retrieved from a list of lists via index
- [Bracket Notation][bracket-notation]: knowing that `[]` should be used to refer to a value at a specific index in a list
- [Slicing][slicing]: the extended solution to this exercise can employ a slice (returns a copy) instead of calling `.copy()`.
- [Iteration][iteration]: the passed-in string is iterated over, and split into rows. The row lists are iterated over and split into elements
- [Iterables][iterables]: understanding that strings, lists, and other data structures can be iterated over in the same fashion
- [Iterators][iterators]: the example solution for this exercise uses `zip()`, which returns an _iterator_.
- [For Loop][for-loop]: iterating over the passed in `matrix` string using a `for` loop to extract "rows" and "columns" that are appended to a list
- [Comprehension Syntax][comprehension-syntax]: knowing that this is equivelent to a `for loop` - putting the row or column creation code _inside_ the list literal instead of using loop + append.
- [Zip][zip]: the example solution for this exercise uses this function to aggregage the column-wise elements of each rown list to form the matrix "columns".
- [Argument Unpacking][argument unpacking]: the example solution for this exercise uses `splat` (`*`) to unpack rows for the `zip()` function.
- [String Splitting][string-splitting]: the example uses `str.split` with and without seperators to break the passed in string into "rows" and then "elements"
- [Type Conversion][type-conversion]: the passed in data is in `str` format but the output is expected as a list of type `int`.
- [Int][int]: the example converts the parsed `str` elements into `int`
