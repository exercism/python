# Implementation notes: exceptions

This exercise expects the code to raise exceptions in certain circumstances.
Exceptions are usually raised when an operation cannot be completed for some
reason and there is no value that can be returned which would be correct.
Instead, an exception is raised. When raising an exception, the tests expect
that the exception class in instantiated and contains a message.

```python
# Avoid this. There is no message and the tests will fail:
raise ValueError
# Do this. Provide a clear message with as much detail as possible:
raise ValueError(f"Number must be greater than zero. {num} is too small.")
```
