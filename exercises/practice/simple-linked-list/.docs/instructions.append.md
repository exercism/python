# Instructions append

## Customizing and Raising Exceptions

Sometimes it is necessary to both [customize](https://docs.python.org/3/tutorial/errors.html#user-defined-exceptions) and [`raise`](https://docs.python.org/3/tutorial/errors.html#raising-exceptions) exceptions in your code. When you do this, you should always include a **meaningful error message** to indicate what the source of the error is. This makes your code more readable and helps significantly with debugging.

Custom exceptions can be created through new exception classes (see [`classes`](https://docs.python.org/3/tutorial/classes.html#tut-classes) for more detail.) that are typically subclasses of [`Exception`](https://docs.python.org/3/library/exceptions.html#Exception).

For situations where you know the error source will be a derivative of a certain exception _type_, you can choose to inherit from one of the [`built in error types`](https://docs.python.org/3/library/exceptions.html#base-classes) under the _Exception_ class. When raising the error, you should still include a meaningful message.

This particular exercise requires that you create a _custom exception_ to be [raised](https://docs.python.org/3/reference/simple_stmts.html#the-raise-statement)/"thrown" when your linked list is **empty**. The tests will only pass if you customize appropriate exceptions, `raise` those exceptions, and include appropriate error messages.

To customize a generic _exception_, create a `class` that inherits from `Exception`. When raising the custom exception with a message, write the message as an argument to the `exception` type:

```python
# subclassing Exception to create EmptyListException
class EmptyListException(Exception):
    """Exception raised when the linked list is empty.

    message: explanation of the error.

    """
    def __init__(self, message):
        self.message = message
        
# raising an EmptyListException
raise EmptyListException("The list is empty.")
```

## Additional Hints

To support `list()`, see [implementing an iterator for a class.](https://docs.python.org/3/tutorial/classes.html#iterators)

Note that Python2's `next()` was replaced by `__next__()` in Python3. If dual compatibility is needed, `next()` can be implemented as:

```Python
def next(self):
    return self.__next__()
```
