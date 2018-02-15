# Trinary

Convert a trinary number, represented as a string (e.g. '102012'), to its
decimal equivalent using first principles.

The program should consider strings specifying an invalid trinary as the
value 0.

Trinary numbers contain three symbols: 0, 1, and 2.

The last place in a trinary number is the 1's place. The second to last
is the 3's place, the third to last is the 9's place, etc.

```shell
# "102012"
    1       0       2       0       1       2    # the number
1*3^5 + 0*3^4 + 2*3^3 + 0*3^2 + 1*3^1 + 2*3^0    # the value
  243 +     0 +    54 +     0 +     3 +     2 =  302
```

If your language provides a method in the standard library to perform the
conversion, pretend it doesn't exist and implement it yourself.

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

To run the tests run the command `python -m pytest trinary_test.py`
(`py.test trinary_test.py` for Python 2; `pytest <exercise>_test.py` for Python 3). Or run it with
`-v` to be more verbose like this: `pytest trinary_test.py`. Using the
`-x` flag will cause the test to fail at the first failure instead of it
trying all cases before exiting.

To run this exercises's tests for example, run this command:
```
python -m pytest trinary_test.py -v
```

## Submitting Exercises

Note that, when trying to submit an exercise, make sure the solution is in the `$EXERCISM_WORKSPACE/python/trinary` directory.

You can find your Exercism workspace by running `exercism debug` and looking for the line that starts with `Workspace`.

For more detailed information about running tests, code style and linting,
please see the [help page](http://exercism.io/languages/python).

## Source

All of Computer Science [http://www.wolframalpha.com/input/?i=binary&a=*C.binary-_*MathWorld-](http://www.wolframalpha.com/input/?i=binary&a=*C.binary-_*MathWorld-)

## Submitting Incomplete Solutions
It's possible to submit an incomplete solution so you can see how others have completed the exercise.
