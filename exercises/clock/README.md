# Clock

Implement a clock that handles times without dates.

You should be able to add and subtract minutes to it.

Two clocks that represent the same time should be equal to each other.

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

## Submitting Exercises

Note that, when trying to submit an exercise, make sure the solution is in the `$EXERCISM_WORKSPACE/python/clock` directory.

You can find your Exercism workspace by running `exercism debug` and looking for the line that starts with `Workspace`.

For more detailed information about running tests, code style and linting,
please see the [help page](http://exercism.io/languages/python).

## Source

Pairing session with Erin Drummond [https://twitter.com/ebdrummond](https://twitter.com/ebdrummond)

## Submitting Incomplete Solutions
It's possible to submit an incomplete solution so you can see how others have completed the exercise.
