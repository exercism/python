# Reverse String

Reverse a string

For example:
input: "cool"
output: "looc"

## Exception messages

Sometimes it is necessary to raise an exception. When you do this, you should include a meaningful error message to
indicate what the source of the error is. This makes your code more readable and helps significantly with debugging. Not
every exercise will require you to raise an exception, but for those that do, the tests will only pass if you include
a message.

To raise a message with an exception, just write it as an argument to the exception type. For example, instead of
`raise Exception`, you shold write:

```python
raise Exception("Meaningful message indicating the source of the error")
```

## Running the tests

To run the tests run the command `python -m pytest reverse_string_test.py`
(`py.test reverse_string_test.py` for Python 2; `pytest <exercise>_test.py` for Python 3). Or run it with
`-v` to be more verbose like this: `pytest reverse_string_test.py`. Using the
`-x` flag will cause the test to fail at the first failure instead of it
trying all cases before exiting.

To run this exercises's tests for example, run this command:
```
python -m pytest reverse_string_test.py -v
```

## Submitting Exercises

Note that, when trying to submit an exercise, make sure the solution is in the `$EXERCISM_WORKSPACE/python/reverse-string` directory.

You can find your Exercism workspace by running `exercism debug` and looking for the line that starts with `Workspace`.

For more detailed information about running tests, code style and linting,
please see the [help page](http://exercism.io/languages/python).

## Source

Introductory challenge to reverse an input string [https://medium.freecodecamp.org/how-to-reverse-a-string-in-javascript-in-3-different-ways-75e4763c68cb](https://medium.freecodecamp.org/how-to-reverse-a-string-in-javascript-in-3-different-ways-75e4763c68cb)

## Submitting Incomplete Solutions
It's possible to submit an incomplete solution so you can see how others have completed the exercise.
