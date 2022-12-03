# Instructions append

## How this Exercise is Structured in Python

While linked lists can be implemented in a variety of ways with a variety of underlying data structures, we ask here that you implement your linked list in an OOP fashion.

In the stub file, you will see a `Node` class and a `LinkedList` class.
Your `Node` class should keep track of its value, as well as which other nodes preceed or follow.
Your `push`, `pop`, `shift`, `unshift`, and the special method for `len` should be implemented in the `LinkedList` class.


In addition to the methods outlined above, we also ask that you implement `delete`.
`delete` will take one argument, which is the vaule to be removed from the linked list.
If the value appears more than once, the **first** occurance should be removed.

<br>

## Exception messages

Sometimes it is necessary to [raise an exception](https://docs.python.org/3/tutorial/errors.html#raising-exceptions). When you do this, you should always include a **meaningful error message** to indicate what the source of the error is. This makes your code more readable and helps significantly with debugging. For situations where you know that the error source will be a certain type, you can choose to raise one of the [built in error types](https://docs.python.org/3/library/exceptions.html#base-classes), but should still include a meaningful message.

This particular exercise requires that you use the [raise statement](https://docs.python.org/3/reference/simple_stmts.html#the-raise-statement) to "throw" a `ValueError` when a node value being `delet()`-ed is not found in the linked list.  Additionally, an `IndexError` should be thrown if there are no nodes left to `pop()`. The tests will only pass if you both `raise` these `exceptions` and include messages with them.

To raise a `ValueError` with a message, write the message as an argument to the `exception` type:

```python
# When the value passed to `delete()` is not found.


# When pop() is called and there are no nodes left in the linked list


```

## Special Methods in Python

The tests for this exercise will also be calling `len()` on your `LinkedList`.
In order for `len()` to work, you will need to create a `__len__` special method.
For details on implementing special or "dunder" methods in Python, see [Python Docs: Basic Object Customization][basic customization] and [Python Docs: object.__len__(self)][__len__].

<br>

