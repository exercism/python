# Ledger

Refactor a ledger printer.

The ledger exercise is a refactoring exercise. There is code that prints a
nicely formatted ledger, given a locale (American or Dutch) and a currency (US
dollar or euro). The code however is rather badly written, though (somewhat
surprisingly) it consistently passes the test suite.

Rewrite this code. Remember that in refactoring the trick is to make small steps
that keep the tests passing. That way you can always quickly go back to a
working version.  Version control tools like git can help here as well.

Please keep a log of what changes you've made and make a comment on the exercise
containing that log, this will help reviewers.

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

- Python 2.7: `py.test ledger_test.py`
- Python 3.4+: `pytest ledger_test.py`

Alternatively, you can tell Python to run the pytest module (allowing the same command to be used regardless of Python version):
`python -m pytest ledger_test.py`

### Common `pytest` options

- `-v` : enable verbose output
- `-x` : stop running tests on first failure
- `--ff` : run failures from previous test before running other test cases

For other options, see `python -m pytest -h`

## Submitting Exercises

Note that, when trying to submit an exercise, make sure the solution is in the `$EXERCISM_WORKSPACE/python/ledger` directory.

You can find your Exercism workspace by running `exercism debug` and looking for the line that starts with `Workspace`.

For more detailed information about running tests, code style and linting,
please see [Running the Tests](http://exercism.io/tracks/python/tests).

## Submitting Incomplete Solutions

It's possible to submit an incomplete solution so you can see how others have completed the exercise.
