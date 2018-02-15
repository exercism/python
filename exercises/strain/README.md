# Strain

Implement the `keep` and `discard` operation on collections. Given a collection
and a predicate on the collection's elements, `keep` returns a new collection
containing those elements where the predicate is true, while `discard` returns
a new collection containing those elements where the predicate is false.

For example, given the collection of numbers:

- 1, 2, 3, 4, 5

And the predicate:

- is the number even?

Then your keep operation should produce:

- 2, 4

While your discard operation should produce:

- 1, 3, 5

Note that the union of keep and discard is all the elements.

The functions may be called `keep` and `discard`, or they may need different
names in order to not clash with existing functions or concepts in your
language.

## Restrictions

Keep your hands off that filter/reject/whatchamacallit functionality
provided by your standard library!  Solve this one yourself using other
basic tools instead.

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

To run the tests run the command `python -m pytest strain_test.py`
(`py.test strain_test.py` for Python 2; `pytest <exercise>_test.py` for Python 3). Or run it with
`-v` to be more verbose like this: `pytest strain_test.py`. Using the
`-x` flag will cause the test to fail at the first failure instead of it
trying all cases before exiting.

To run this exercises's tests for example, run this command:
```
python -m pytest strain_test.py -v
```

## Submitting Exercises

Note that, when trying to submit an exercise, make sure the solution is in the `$EXERCISM_WORKSPACE/python/strain` directory.

You can find your Exercism workspace by running `exercism debug` and looking for the line that starts with `Workspace`.

For more detailed information about running tests, code style and linting,
please see the [help page](http://exercism.io/languages/python).

## Source

Conversation with James Edward Gray II [https://twitter.com/jeg2](https://twitter.com/jeg2)

## Submitting Incomplete Solutions
It's possible to submit an incomplete solution so you can see how others have completed the exercise.
