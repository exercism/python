# Instructions append

## Exception messages

Sometimes it is necessary to [raise an exception](https://docs.python.org/3/tutorial/errors.html#raising-exceptions). When you do this, you should always include a **meaningful error message** to indicate what the source of the error is. This makes your code more readable and helps significantly with debugging. For situations where you know that the error source will be a certain type, you can choose to raise one of the [built in error types](https://docs.python.org/3/library/exceptions.html#base-classes), but should still include a meaningful message.

This particular exercise requires that you use the [raise statement](https://docs.python.org/3/reference/simple_stmts.html#the-raise-statement) to "throw" `ValueErrors` if the `Queen` constructor is passed numbers that are negative, or numbers that are not a valid row or column.  The tests will only pass if you both `raise` the `exception` and include a message with it. You also should `raise` a `ValueError` if both the queens passed to the `can_attack()` method are on the same location.

To raise a `ValueError` with a message, write the message as an argument to the `exception` type:

```python
# if the row parameter is negative
raise ValueError("row not positive")

# if the row parameter is not on the defined board
raise ValueError("row not on board")

# if the column parameter is negative
raise ValueError("column not positive")

# if the column parameter is not on the defined board
raise ValueError("column not on board")

# if both the queens are on the same location
raise ValueError("Invalid queen position: both queens in the same square")
```
