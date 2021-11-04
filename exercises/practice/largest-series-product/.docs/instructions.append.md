# Instructions append

## Exception messages

Sometimes it is necessary to [raise an exception](https://docs.python.org/3/tutorial/errors.html#raising-exceptions). When you do this, you should always include a **meaningful error message** to indicate what the source of the error is. This makes your code more readable and helps significantly with debugging. For situations where you know that the error source will be a certain type, you can choose to raise one of the [built in error types](https://docs.python.org/3/library/exceptions.html#base-classes), but should still include a meaningful message.

This particular exercise requires that you use the [raise statement](https://docs.python.org/3/reference/simple_stmts.html#the-raise-statement) to "throw" a `ValueError` when your `largest_product()` function receives invalid input. The tests will only pass if you both `raise` the `exception` and include a message with it.  Feel free to reuse your code from the `series` exercise!

To raise a `ValueError` with a message, write the message as an argument to the `exception` type:

```python
# span of numbers is longer than number series
raise ValueError("span must be smaller than string length")

# span of number is zero or negative
raise ValueError("span must be greater than zero")

# series includes non-number input
raise ValueError("digits input must only contain digits")
```
