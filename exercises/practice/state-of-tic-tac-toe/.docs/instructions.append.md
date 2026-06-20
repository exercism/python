# Instructions append

## Exception messages

Sometimes it is necessary to [raise an exception][raising-exceptions].
When you do this, you should always include a **meaningful error message** to indicate what the source of the error is.
This makes your code more readable and helps significantly with debugging.
For situations where you know that the error source will be a certain type, you can choose to raise one of the [built in error types][error-base-classes], but should still include a meaningful message.


A valid game of `Tic Tac Toe` ends when one player wins.
If both players are in a winning state, this exercise expects you to use the [raise statement][raise] and "throw" a `ValueError` in your solution.
Your code is also expected to throw a `ValueError` if one player is assessed as playing two turns in a row, or playing the first move when they were assigned to play the second move.


To raise a `ValueError` with a message, write the message as an argument to the `exception` type:

```python
# Example when player X goes before player O.
raise ValueError("Wrong turn order: O started")

# Example when player X goes twice.
raise ValueError("Wrong turn order: X went twice")

# Example when player X wins AND player O wins.
raise ValueError("Impossible board: game should have ended after the game was won")
```

The tests will check for an exact error message match, so please read the expected results carefully.

[raising-exceptions]: https://docs.python.org/3/tutorial/errors.html#raising-exceptions
[error-base-classes]: https://docs.python.org/3/library/exceptions.html#base-classes
[raise]: https://docs.python.org/3/reference/simple_stmts.html#the-raise-statement
