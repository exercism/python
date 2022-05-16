# About

Recursion is a way to repeatedly execute code inside a function through the function calling itself.
It can be viewed as another way to loop/iterate. 
Like looping, a Boolean expression or `True/False` test is used to know when to stop the recursive execution.
_Unlike_ looping, recursion without termination in Python cannot not run infinitely.
Values used in each function call are placed in their own frames on the Python interpreter stack.
If the total amount of function calls takes up more space than the stack has room for, it will result in an error.

Python's interpreter stack is backed up by a C stack that is connected to the underlying operating system.
Function calls that take up more memory space than the C stack has will cause a stack overflow.
A stack overflow can crash Python or even the host operating system, if it is severe enough.
To avoid this situation, the Python interpreter has a maximum stack depth that limits the number of frames that can be placed on its stack.
The default is typically 999 frames, but varies by system.
The recursion limit for a given version of Python can be found by calling [`sys.getrecursionlimit()`][getrecursionlimit]

```python
def print_increment(step, max_value):
    if step > max_value:
        return
    print(f'The step is {step}')
    print_increment(step + 1, max_value)


def main():
    print_increment(1, 2)
    print("After recursion")

if __name__ == "__main__":
    main()

```

This will print

```
The step is 1
The step is 2
After recursion
```

There may be some situations that are more readable and/or easier to reason through when expressed through recursion than when expressed through looping.

## Tail Call

A tail call is when the last statement of a function only calls itself and nothing more.
This example is not a tail call, as the function adds 1 to the result of calling itself

```python
def print_increment(step, max_value):
    if step > max_value:
        return 1
    print(f'The step is {step}')
    return 1 + print_increment(step + 1, max_value)


def main():
    retval = print_increment(1, 2)
    print(f'retval is {retval} after recursion')

if __name__ == "__main__":
    main()

```

This will print

```
The step is 1
The step is 2
retval is 3 after recursion
```

To refactor it to a tail call, make `j` a parameter of `printIncrement`

```python
def print_increment(step, max_value, retval):
    if step > max_value:
        return retval
    print(f'The step is {step}')
    return print_increment(step + 1, max_value, retval + 1)


def main():
    retval = print_increment(1, 2, 1)
    print(f'retval is {retval} after recursion')

if __name__ == "__main__":
    main()

```

You may find that a tail call may be easier to reason through than a recursive call that is not a tail call.
However, it is always important when using recursion to know that there will not be so many iterations that the stack will overflow.

## Recursion Limit

Some languages are able to optimize tail calls so that each recursive call reuses the stack frame of the first call to the function, instead of adding another stack frame.
Python is not one of those languages.
To guard against stack overflow, Python has a recursion limit, which by default is set to one thousand.
Python will raise a [RecursionError][RecursionError] exception when the interpretor detects that the recursion limit has been exceeded.
It is possible to use the [sys.setrecursionlimit][setrecursionlimit] method to increase the recursion limit, but doing so runs the risk of having a runtime segmentation fault that will crash the program.


## Resources

To learn more about using recursion in Python you can start with 
- [python-programming: recursion][python-programming: recursion]
- [Real Python: python-recursion][Real Python: python-recursion]
- [Real Python: python-thinking-recursively][Real Python: python-thinking-recursively]

[python-programming: recursion]: https://www.programiz.com/python-programming/recursion
[Real Python: python-recursion]: https://realpython.com/python-recursion/
[Real Python: python-thinking-recursively]: https://realpython.com/python-thinking-recursively/
[RecursionError]: https://docs.python.org/3.8/library/exceptions.html#RecursionError
[setrecursionlimit]: https://docs.python.org/3.8/library/sys.html#sys.setrecursionlimit
