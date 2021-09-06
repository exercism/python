# Implementation notes: exceptions

This exercise expects the code to raise exceptions in certain circumstances.
Exceptions are usually raised when an operation cannot be completed for some reason.
If the operation cannot be completed, a return value cannot be computed and any value would be incorrect.
Since any return value would be incorrect, we cannot use a normal return.
Therefore, an exception is raised instead of returning a value.
When raising an exception, the tests expect that the exception class in instantiated and contains a message.

```python
# Avoid this. There is no message and the tests will fail:
raise ValueError
# Do this. Provide a clear and actionable message:
raise ValueError(f"Number must be greater than zero. {num} is too small.")
```
