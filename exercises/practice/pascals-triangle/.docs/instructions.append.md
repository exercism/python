# Instructions append

## How this Exercise is Implemented in Python: Recursion

This exercise is designed to be completed using [concept:python/recursion](), rather than loops.
A recursive function is a function that calls itself, which is useful when solving problems that are defined in terms of themselves.
To avoid infinite recursion (or more specifically, to avoid overflowing the stack), something called a "base case" is used.
When the base case is reached, a non-recursive value is returned, which allows the previous function call to resolve and return its value, and so on, rippling back down the stack until the first function call returns the answer.
We could write a recursive function to find the answer to 5! (i.e. 5 * 4 * 3 * 2 * 1) like so:

````python
def factorial(number):
  if number <= 1:  # base case
    return 1

  return number * factorial(number - 1) # recursive case

print(factorial(5)) # returns 120
````

Finally, it should be noted that Python limits the number of times recursive calls can be made (1000 by default) and does not optimize for [tail recursion][tail-recursion].

## Exception messages

Sometimes it is necessary to [raise an exception][raising].
When you do this, you should always include a **meaningful error message** to indicate what the source of the error is.
This makes your code more readable and helps significantly with debugging.
For situations where you know that the error source will be a certain type, you can choose to raise one of the [built in error types][built-in-errors], but should still include a meaningful message.

This particular exercise requires that you use the [raise statement][raise-statement] to "throw" multiple `ValueErrors` if the `rows()` function is passed a negative number.
The tests will only pass if you both `raise` the `exception` and include a message with it.

To raise a `ValueError` with a message, write the message as an argument to the `exception` type:

```python
# if the rows function is passed a negative number.
raise ValueError("number of rows is negative")
```

[built-in-errors]: https://docs.python.org/3/library/exceptions.html#base-classes
[raise-statement]: https://docs.python.org/3/reference/simple_stmts.html#the-raise-statement
[raising]: https://docs.python.org/3/tutorial/errors.html#raising-exceptions
[tail-recursion]: https://www.geeksforgeeks.org/tail-recursion/
