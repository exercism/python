# Connect

Compute the result for a game of Hex / Polygon.

The abstract boardgame known as
[Hex](https://en.wikipedia.org/wiki/Hex_%28board_game%29) / Polygon /
CON-TAC-TIX is quite simple in rules, though complex in practice. Two players
place stones on a rhombus with hexagonal fields. The player to connect his/her
stones to the opposite side first wins. The four sides of the rhombus are
divided between the two players (i.e. one player gets assigned a side and the
side directly opposite it and the other player gets assigned the two other
sides).

Your goal is to build a program that given a simple representation of a board
computes the winner (or lack thereof). Note that all games need not be "fair".
(For example, players may have mismatched piece counts.)

The boards look like this (with spaces added for readability, which won't be in
the representation passed to your code):

```text
. O . X .
 . X X O .
  O O O X .
   . X O X O
    X O O O X
```

"Player `O`" plays from top to bottom, "Player `X`" plays from left to right. In
the above example `O` has made a connection from left to right but nobody has
won since `O` didn't connect top and bottom.

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

- Python 2.7: `py.test connect_test.py`
- Python 3.3+: `pytest connect_test.py`

Alternatively, you can tell Python to run the pytest module (allowing the same command to be used regardless of Python version):
`python -m pytest connect_test.py`

### Common `pytest` options

- `-v` : enable verbose output
- `-x` : stop running tests on first failure
- `--ff` : run failures from previous test before running other test cases

For other options, see `python -m pytest -h`

## Submitting Exercises

Note that, when trying to submit an exercise, make sure the solution is in the `$EXERCISM_WORKSPACE/python/connect` directory.

You can find your Exercism workspace by running `exercism debug` and looking for the line that starts with `Workspace`.

For more detailed information about running tests, code style and linting,
please see the [help page](http://exercism.io/languages/python).

## Submitting Incomplete Solutions

It's possible to submit an incomplete solution so you can see how others have completed the exercise.
