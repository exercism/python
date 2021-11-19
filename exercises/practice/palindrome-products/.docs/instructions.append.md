# Instructions append

## Notes regarding the implementation of `smallest` and `largest`:

Both functions must take two keyword arguments:
- `max_factor`: int
- `min_factor`: int, default 0

Their return value must be a `tuple -- (value, factors)` where `value` is the
palindrome itself, and `factors` is an `iterable` containing both factors of the
palindrome in arbitrary order.


## Exception messages

Sometimes it is necessary to [raise an exception](https://docs.python.org/3/tutorial/errors.html#raising-exceptions). When you do this, you should always include a **meaningful error message** to indicate what the source of the error is. This makes your code more readable and helps significantly with debugging. For situations where you know that the error source will be a certain type, you can choose to raise one of the [built in error types](https://docs.python.org/3/library/exceptions.html#base-classes), but should still include a meaningful message.

This particular exercise requires that you use the [raise statement](https://docs.python.org/3/reference/simple_stmts.html#the-raise-statement) to "throw" a `ValueError` when the `largest()` or `smallest()` function receives a pair of factors that are not in the correct range. The tests will only pass if you both `raise` the `exception` and include a message with it.

To raise a `ValueError` with a message, write the message as an argument to the `exception` type:

```python
# if the max_factor is less than the min_factor
raise ValueError("min must be <= max")
```
