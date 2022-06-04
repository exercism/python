# Reading and Troubleshooting Stack Traces in Python

## Frame Object

A frame object holds the local variables and arguments passed to a function.
A frame object is created when a function is called and is destroyed when that function returns.
When function `B` is called within function `A`, function `B`'s values are put into a frame object, which is then placed on top of function `A`'s frame object on the call stack.

## Call Stack

The call stack is a collection of frame objects for the currently active functions.
If function `A` has called function `B` and function `B` has called function `C`, then the frame objects for all three functions will be on the call stack.
Once function `C` returns, then its frame object will be popped off the stack and only the frame objects for functions `A` and `B` will remain on the call stack.

## Traceback

A Traceback is a report of all the frame objects on the stack for a specific time.
When a Python program encounters an unhandled exception, it will print the exception message and a Traceback.
The Traceback will show where the exception was raised and what functions were called leading up to it.

## How to Read a Traceback

`ValueError` is a common exception.

Following is an example of `ValueError` resulting from trying to assign two variables on the left from only one value on the right:

```python
>>> first, second = [1]
Traceback (most recent call last):
File <stdin>, line 1, in <module>
    first, second = [1]
ValueError: not enough values to unpack (expected 2, got 1)

```

It says that the most recent call is last, so the place to start is with the exception at the bottom of the trace.
From there it can be traced back to the start.
If we place the offending line in a function and then call the function we see a longer trace:

```python
>>> def my_func():
...     first, second = [1]
... 
>>> my_func()
Traceback (most recent call last):
  File <stdin>, line 5, in <module>
    my_func()
  File <stdin>, line 2, in my_func
    first, second = [1]
ValueError: not enough values to unpack (expected 2, got 1)
```

Working backwards from the bottom, we see that the call where the exception happened is on line 2 in `my_func`.
We got there by calling `my_func` on line 5.

## Using the `print` function

Sometimes an error is not being raised, but a value is not what is expected.
This can be especially perplexing if the value is the result of a chain of calculations.
In such a situation it can be helpful to look at the value at each step to see which step is the one that isn't behaving as expected.
The [print][print] function can be used for printing the value to the console.
Following is an example of a function that doesn't return the value expected

```python
# the intent is to only pass an int to this function and get an int back
def halve_and_quadruple(num):
    return (num / 2) * 4
```

When the function is passed `5`, the expected value is `8`, but it it returns `10.0`.
To troubleshoot, the calculating is broken up so that the value can be inspected at every step.


```python
# the intent is to only pass an int to this function and get an int back
def halve_and_quadruple(num):
    # verify the number in is what is expected
    # prints 5
    print(num)
    # we want the int divided by an int to be an int
    # but this prints 2.5! We've found our mistake.
    print(num / 2)
    # this makes sense, since 2.5 x 4 = 10.0
    print((num / 2) * 4)
    return (num / 2) * 4
```

What the `print` calls revealed is that we used `/` when we should have used `//`, the [floor divison operator][floor divison operator].

TODO: assert, logging and debugging tools

[floor divison operator]: https://www.codingem.com/python-floor-division
[print]: https://www.w3schools.com/python/ref_func_print.asp
