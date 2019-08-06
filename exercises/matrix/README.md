# Matrix

Given a string representing a matrix of numbers, return the rows and columns of
that matrix.

So given a string with embedded newlines like:

```text
9 8 7
5 3 2
6 6 7
```

representing this matrix:

```text
    1  2  3
  |---------
1 | 9  8  7
2 | 5  3  2
3 | 6  6  7
```

your code should be able to spit out:

- A list of the rows, reading each row left-to-right while moving
  top-to-bottom across the rows,
- A list of the columns, reading each column top-to-bottom while moving
  from left-to-right.

The rows for our example matrix:

- 9, 8, 7
- 5, 3, 2
- 6, 6, 7

And its columns:

- 9, 5, 6
- 8, 3, 6
- 7, 2, 7

In this exercise you're going to create a **class**.  _Don't worry, it's not as complicated as you think!_ 

-   [**A First Look at Classes**](https://docs.python.org/3/tutorial/classes.html#a-first-look-at-classes) from the Python 3 documentation. 
-   [**How to Define a Class in Python**](https://realpython.com/python3-object-oriented-programming/#how-to-define-a-class-in-python) from the Real Python website.  
-   [**Data Structures in Python**](https://docs.python.org/3/tutorial/datastructures.html) from the Python 3 documentation.


## Exception messages

Sometimes it is necessary to raise an exception. When you do this, you should include a meaningful error message to
indicate what the source of the error is. This makes your code more readable and helps significantly with debugging. Not
every exercise will require you to raise an exception, but for those that do, the tests will only pass if you include
a message.

To raise a message with an exception, just write it as an argument to the exception type. For example, instead of
`raise Exception`, you should write:

```python
raise Exception("Meaningful message indicating the source of the error")
```

## Running the tests

To run the tests, run the appropriate command below ([why they are different](https://github.com/pytest-dev/pytest/issues/1629#issue-161422224)):

- Python 2.7: `py.test matrix_test.py`
- Python 3.4+: `pytest matrix_test.py`

Alternatively, you can tell Python to run the pytest module (allowing the same command to be used regardless of Python version):
`python -m pytest matrix_test.py`

### Common `pytest` options

- `-v` : enable verbose output
- `-x` : stop running tests on first failure
- `--ff` : run failures from previous test before running other test cases

For other options, see `python -m pytest -h`

## Submitting Exercises

Note that, when trying to submit an exercise, make sure the solution is in the `$EXERCISM_WORKSPACE/python/matrix` directory.

You can find your Exercism workspace by running `exercism debug` and looking for the line that starts with `Workspace`.

For more detailed information about running tests, code style and linting,
please see [Running the Tests](http://exercism.io/tracks/python/tests).

## Source

Warmup to the `saddle-points` warmup. [http://jumpstartlab.com](http://jumpstartlab.com)

## Submitting Incomplete Solutions

It's possible to submit an incomplete solution so you can see how others have completed the exercise.
