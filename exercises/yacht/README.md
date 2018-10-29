# Yacht

# Score a single throw of dice in *Yacht*

The dice game [Yacht](https://en.wikipedia.org/wiki/Yacht_(dice_game)) is from
the same family as Poker Dice, Generala and particularly Yahtzee, of which it
is a precursor. In the game, five dice are rolled and the result can be entered
in any of twelve categories. The score of a throw of the dice depends on
category chosen.

## Scores in Yacht

    Category    Score                   Example
    Ones            1 × number of ones      1 1 1 4 5 scores 3
    Twos            2 × number of twos      2 2 3 4 5 scores 4
    Threes          3 × number of threes    3 3 3 3 3 scores 15
    Fours           4 × number of fours     1 2 3 3 5 scores 0
    Fives           5 × number of fives     5 1 5 2 5 scores 15
    Sixes           6 × number of sixes     2 3 4 5 6 scores 6
    Full House      Total of the dice       3 3 3 5 5 scores 19
    Four of a Kind  Total of the four dice  4 4 4 4 6 scores 16
    Little Straight 30 points               1 2 3 4 5 scores 30
    Big Straight    30 points               2 3 4 5 6 scores 30
    Choice          Sum of the dice         2 3 3 4 6 scores 18
    Yacht           50 points               4 4 4 4 4 scores 50

If the dice do not satisfy the requirements of a category, the score is zero.
If, for example, *Four Of A Kind* is entered in the *Yacht* category, zero
points are scored. A *Yacht* scores zero if entered in the *Full House* category.

## Task
Given a list of values for five dice and a category, your solution should return
the score of the dice for that category. If the dice do not satisfy the requirements
of the category your solution should return 0. You can assume that five values
will always be presented, and the value of each will be between one and six
inclusively. You should not assume that the dice are ordered.

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

- Python 2.7: `py.test yacht_test.py`
- Python 3.4+: `pytest yacht_test.py`

Alternatively, you can tell Python to run the pytest module (allowing the same command to be used regardless of Python version):
`python -m pytest yacht_test.py`

### Common `pytest` options

- `-v` : enable verbose output
- `-x` : stop running tests on first failure
- `--ff` : run failures from previous test before running other test cases

For other options, see `python -m pytest -h`

## Submitting Exercises

Note that, when trying to submit an exercise, make sure the solution is in the `$EXERCISM_WORKSPACE/python/yacht` directory.

You can find your Exercism workspace by running `exercism debug` and looking for the line that starts with `Workspace`.

For more detailed information about running tests, code style and linting,
please see [Running the Tests](http://exercism.io/tracks/python/tests).

## Source

James Kilfiger, using wikipedia [https://en.wikipedia.org/wiki/Yacht_(dice_game)](https://en.wikipedia.org/wiki/Yacht_(dice_game))

## Submitting Incomplete Solutions

It's possible to submit an incomplete solution so you can see how others have completed the exercise.
