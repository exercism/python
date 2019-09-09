# D&D Character

For a game of [Dungeons & Dragons][DND], each player starts by generating a
character they can play with. This character has, among other things, six
abilities; strength, dexterity, constitution, intelligence, wisdom and
charisma. These six abilities have scores that are determined randomly. You
do this by rolling four 6-sided dice and record the sum of the largest three
dice. You do this six times, once for each ability.

Your character's initial hitpoints are 10 + your character's constitution
modifier. You find your character's constitution modifier by subtracting 10
from your character's constitution, divide by 2 and round down.

Write a random character generator that follows the rules above.

For example, the six throws of four dice may look like:

* 5, 3, 1, 6: You discard the 1 and sum 5 + 3 + 6 = 14, which you assign to strength.
* 3, 2, 5, 3: You discard the 2 and sum 3 + 5 + 3 = 11, which you assign to dexterity.
* 1, 1, 1, 1: You discard the 1 and sum 1 + 1 + 1 = 3, which you assign to constitution.
* 2, 1, 6, 6: You discard the 1 and sum 2 + 6 + 6 = 14, which you assign to intelligence.
* 3, 5, 3, 4: You discard the 3 and sum 5 + 3 + 4 = 12, which you assign to wisdom.
* 6, 6, 6, 6: You discard the 6 and sum 6 + 6 + 6 = 18, which you assign to charisma.

Because constitution is 3, the constitution modifier is -4 and the hitpoints are 6.

## Notes

Most programming languages feature (pseudo-)random generators, but few
programming languages are designed to roll dice. One such language is [Troll].

[DND]: https://en.wikipedia.org/wiki/Dungeons_%26_Dragons
[Troll]: http://hjemmesider.diku.dk/~torbenm/Troll/

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

- Python 2.7: `py.test dnd_character_test.py`
- Python 3.4+: `pytest dnd_character_test.py`

Alternatively, you can tell Python to run the pytest module (allowing the same command to be used regardless of Python version):
`python -m pytest dnd_character_test.py`

### Common `pytest` options

- `-v` : enable verbose output
- `-x` : stop running tests on first failure
- `--ff` : run failures from previous test before running other test cases

For other options, see `python -m pytest -h`

## Submitting Exercises

Note that, when trying to submit an exercise, make sure the solution is in the `$EXERCISM_WORKSPACE/python/dnd-character` directory.

You can find your Exercism workspace by running `exercism debug` and looking for the line that starts with `Workspace`.

For more detailed information about running tests, code style and linting,
please see [Running the Tests](http://exercism.io/tracks/python/tests).

## Source

Simon Shine, Erik Schierboom [https://github.com/exercism/problem-specifications/issues/616#issuecomment-437358945](https://github.com/exercism/problem-specifications/issues/616#issuecomment-437358945)

## Submitting Incomplete Solutions

It's possible to submit an incomplete solution so you can see how others have completed the exercise.
