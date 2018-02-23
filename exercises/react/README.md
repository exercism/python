# React

Implement a basic reactive system.

Reactive programming is a programming paradigm that focuses on how values
are computed in terms of each other to allow a change to one value to
automatically propagate to other values, like in a spreadsheet.

Implement a basic reactive system with cells with settable values ("input"
cells) and cells with values computed in terms of other cells ("compute"
cells). Implement updates so that when an input value is changed, values
propagate to reach a new stable system state.

In addition, compute cells should allow for registering change notification
callbacks.  Call a cell’s callbacks when the cell’s value in a new stable
state has changed from the previous stable state.

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

To run the tests, run the appropriate command below:

| Python Version | Command |
| --- | --- |
| 2.7 | `py.test react_test.py` |
| 3.3+ | `pytest react_test.py` |
| 2.7, 3.3+ | `python -m pytest react_test.py` |

<table>
    <tr>
        <td colspan="2"><strong>Common pytest options</strong></td>
    </tr>
    <tr>
        <td>-v</td>
        <td>enable verbose output</td>
    </tr>
    <tr>
        <td>-x</td>
        <td>stop running tests on first failure</td>
    </tr>
    <tr>
        <td>--ff</td>
        <td>run failures from previous test before running other tests</td>
    </tr>
</table>

For other options, see `python -m pytest -h`

## Submitting Exercises

Note that, when trying to submit an exercise, make sure the solution is in the `$EXERCISM_WORKSPACE/python/react` directory.

You can find your Exercism workspace by running `exercism debug` and looking for the line that starts with `Workspace`.

For more detailed information about running tests, code style and linting,
please see the [help page](http://exercism.io/languages/python).

## Submitting Incomplete Solutions
It's possible to submit an incomplete solution so you can see how others have completed the exercise.
