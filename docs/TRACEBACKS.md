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

TODO: examples of some common errors, their tracebacks, and how to read them...
