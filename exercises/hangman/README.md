# Need edit
Implement the logic of the hangman game using functional reactive programming.

Hangman is a simple word guessing game.

Functional Reactive Programming is a way to write interactive programs. It differs from the usual perspective in that instead of saying "when the button is pressed increment the counter", you write "the value of the counter is the sum of the number of times the button is pressed."

Implement the basic logic behind hangman using functional reactive programming. You'll need to install an FRP library for this, this will be described in the language/track specific files of the exercise.

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

Note that, when trying to submit an exercise, make sure the solution is in the `exercism/python/<exerciseName>` directory.

For example, if you're submitting `bob.py` for the Bob exercise, the submit command would be something like `exercism submit <path_to_exercism_dir>/python/bob/bob.py`.

For more detailed information about running tests, code style and linting,
please see the [help page](http://exercism.io/languages/python).
