# Complex Numbers

A complex number is a number in the form `a + b * i` where `a` and `b` are real and `i` satisfies `i^2 = -1`.

`a` is called the real part and `b` is called the imaginary part of `z`.
The conjugate of the number `a + b * i` is the number `a - b * i`.
The absolute value of a complex number `z = a + b * i` is a real number `|z| = sqrt(a^2 + b^2)`. The square of the absolute value `|z|^2` is the result of multiplication of `z` by its complex conjugate.

The sum/difference of two complex numbers involves adding/subtracting their real and imaginary parts separately:
`(a + i * b) + (c + i * d) = (a + c) + (b + d) * i`,
`(a + i * b) - (c + i * d) = (a - c) + (b - d) * i`.

Multiplication result is by definition
`(a + i * b) * (c + i * d) = (a * c - b * d) + (b * c + a * d) * i`.

The reciprocal of a non-zero complex number is
`1 / (a + i * b) = a/(a^2 + b^2) - b/(a^2 + b^2) * i`.

Dividing a complex number `a + i * b` by another `c + i * d` gives:
`(a + i * b) / (c + i * d) = (a * c + b * d)/(c^2 + d^2) + (b * c - a * d)/(c^2 + d^2) * i`.

Exponent of a complex number can be expressed as
`exp(a + i * b) = exp(a) * exp(i * b)`,
and the last term is given by Euler's formula `exp(i * b) = cos(b) + i * sin(b)`.


Implement the following operations:
 - addition, subtraction, multiplication and division of two complex numbers,
 - conjugate, absolute value, exponent of a given complex number.


Assume the programming language you are using does not have an implementation of complex numbers.

## Hints

See [Emulating numeric types](https://docs.python.org/2/reference/datamodel.html#emulating-numeric-types) for help on operator overloading.


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

- Python 2.7: `py.test complex_numbers_test.py`
- Python 3.4+: `pytest complex_numbers_test.py`

Alternatively, you can tell Python to run the pytest module (allowing the same command to be used regardless of Python version):
`python -m pytest complex_numbers_test.py`

### Common `pytest` options

- `-v` : enable verbose output
- `-x` : stop running tests on first failure
- `--ff` : run failures from previous test before running other test cases

For other options, see `python -m pytest -h`

## Submitting Exercises

Note that, when trying to submit an exercise, make sure the solution is in the `$EXERCISM_WORKSPACE/python/complex-numbers` directory.

You can find your Exercism workspace by running `exercism debug` and looking for the line that starts with `Workspace`.

For more detailed information about running tests, code style and linting,
please see [Running the Tests](http://exercism.io/tracks/python/tests).

## Source

Wikipedia [https://en.wikipedia.org/wiki/Complex_number](https://en.wikipedia.org/wiki/Complex_number)

## Submitting Incomplete Solutions

It's possible to submit an incomplete solution so you can see how others have completed the exercise.
