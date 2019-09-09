# Knapsack

In this exercise, let's try to solve a classic problem.

Bob is a thief. After months of careful planning, he finally manages to
crack the security systems of a high-class apartment.

In front of him are many items, each with a value (v) and weight (w). Bob,
of course, wants to maximize the total value he can get; he would gladly
take all of the items if he could. However, to his horror, he realizes that
the knapsack he carries with him can only hold so much weight (W).

Given a knapsack with a specific carrying capacity (W), help Bob determine
the maximum value he can get from the items in the house. Note that Bob can
take only one of each item.

All values given will be strictly positive. Items will be represented as a
list of pairs, `wi` and `vi`, where the first element `wi` is the weight of
the *i*th item and `vi` is the value for that item.

For example:

Items: [
  { "weight": 5, "value": 10 },
  { "weight": 4, "value": 40 },
  { "weight": 6, "value": 30 },
  { "weight": 4, "value": 50 }
]

Knapsack Limit: 10

For the above, the first item has weight 5 and value 10, the second item has
weight 4 and value 40, and so on.

In this example, Bob should take the second and fourth item to maximize his
value, which, in this case, is 90. He cannot get more than 90 as his
knapsack has a weight limit of 10.

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

- Python 2.7: `py.test knapsack_test.py`
- Python 3.4+: `pytest knapsack_test.py`

Alternatively, you can tell Python to run the pytest module (allowing the same command to be used regardless of Python version):
`python -m pytest knapsack_test.py`

### Common `pytest` options

- `-v` : enable verbose output
- `-x` : stop running tests on first failure
- `--ff` : run failures from previous test before running other test cases

For other options, see `python -m pytest -h`

## Submitting Exercises

Note that, when trying to submit an exercise, make sure the solution is in the `$EXERCISM_WORKSPACE/python/knapsack` directory.

You can find your Exercism workspace by running `exercism debug` and looking for the line that starts with `Workspace`.

For more detailed information about running tests, code style and linting,
please see [Running the Tests](http://exercism.io/tracks/python/tests).

## Source

Wikipedia [https://en.wikipedia.org/wiki/Knapsack_problem](https://en.wikipedia.org/wiki/Knapsack_problem)

## Submitting Incomplete Solutions

It's possible to submit an incomplete solution so you can see how others have completed the exercise.
