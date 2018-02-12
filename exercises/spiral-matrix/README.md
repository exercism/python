# Spiral Matrix

Given the size, return a square matrix of numbers in spiral order.

The matrix should be filled with natural numbers, starting from 1
in the top-left corner, increasing in an inward, clockwise spiral order,
like these examples:

###### Spiral matrix of size 3

```text
1 2 3
8 9 4
7 6 5
```

###### Spiral matrix of size 4

```text
 1  2  3 4
12 13 14 5
11 16 15 6
10  9  8 7
```

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

Note that, when trying to submit an exercise, make sure the solution is in the `$EXERCISM_WORKSPACE/python/spiral-matrix` directory.

You can find your Exercism workspace by running `exercism debug` and looking for the line that starts with `Workspace`.

For more detailed information about running tests, code style and linting,
please see the [help page](http://exercism.io/languages/python).

## Source

Reddit r/dailyprogrammer challenge #320 [Easy] Spiral Ascension. [https://www.reddit.com/r/dailyprogrammer/comments/6i60lr/20170619_challenge_320_easy_spiral_ascension/](https://www.reddit.com/r/dailyprogrammer/comments/6i60lr/20170619_challenge_320_easy_spiral_ascension/)

## Submitting Incomplete Solutions
It's possible to submit an incomplete solution so you can see how others have completed the exercise.
