# PaaS I/O

Report network IO statistics.

You are writing a [PaaS][], and you need a way to bill customers based
on network and filesystem usage.

Create a wrapper for network connections and files that can report IO
statistics. The wrapper must report:

- The total number of bytes read/written.
- The total number of read/write operations.

[PaaS]: http://en.wikipedia.org/wiki/Platform_as_a_service

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

To run the tests, run `pytest paasio_test.py`

Alternatively, you can tell Python to run the pytest module:
`python -m pytest paasio_test.py`

### Common `pytest` options

- `-v` : enable verbose output
- `-x` : stop running tests on first failure
- `--ff` : run failures from previous test before running other test cases

For other options, see `python -m pytest -h`

## Submitting Exercises

Note that, when trying to submit an exercise, make sure the solution is in the `$EXERCISM_WORKSPACE/python/paasio` directory.

You can find your Exercism workspace by running `exercism debug` and looking for the line that starts with `Workspace`.

For more detailed information about running tests, code style and linting,
please see [Running the Tests](http://exercism.io/tracks/python/tests).

## Source

Brian Matsuo [https://github.com/bmatsuo](https://github.com/bmatsuo)

## Submitting Incomplete Solutions

It's possible to submit an incomplete solution so you can see how others have completed the exercise.
