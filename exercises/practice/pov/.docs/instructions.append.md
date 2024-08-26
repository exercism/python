# Instructions append

## Exception messages

Sometimes it is necessary to [raise an exception](https://docs.python.org/3/tutorial/errors.html#raising-exceptions). When you do this, you should always include a **meaningful error message** to indicate what the source of the error is. This makes your code more readable and helps significantly with debugging. For situations where you know that the error source will be a certain type, you can choose to raise one of the [built in error types](https://docs.python.org/3/library/exceptions.html#base-classes), but should still include a meaningful message.

This particular exercise requires that you use the [raise statement](https://docs.python.org/3/reference/simple_stmts.html#the-raise-statement) to "throw" multiple `ValueErrors` if the `Tree()` class is passed a tree that cannot be reoriented, or a path cannot be found between a `start node` and an `end node`. 
The tests will only pass if you both `raise` the expected `exception` type and include the expected message with it.

Please check the tests and their expected results carefully.
