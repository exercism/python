# Instructions append

## Exception messages

Sometimes it is necessary to [raise an exception](https://docs.python.org/3/tutorial/errors.html#raising-exceptions). When you do this, you should always include a **meaningful error message** to indicate what the source of the error is. This makes your code more readable and helps significantly with debugging. For situations where you know that the error source will be a certain type, you can choose to raise one of the [built in error types](https://docs.python.org/3/library/exceptions.html#base-classes), but should still include a meaningful message.

The Collatz Conjecture is only concerned with **strictly positive integers**, so this exercise expects you to use the [raise statement](https://docs.python.org/3/reference/simple_stmts.html#the-raise-statement) and "throw" a `ValueError` in your solution if the given value is zero or a negative integer. The tests will only pass if you both `raise` the `exception` and include a message with it.

To raise a `ValueError` with a message, write the message as an argument to the `exception` type:

```python
# example when argument is zero or a negative integer
raise ValueError("Only positive integers are allowed")
```
