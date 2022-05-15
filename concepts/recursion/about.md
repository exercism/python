# About

Recursion is a way to repeat code in a function by the function calling itself.
It is another way to loop/iterate. Like looping, the function should test a Boolean expression to know when to end.
Unlike looping, recursion that never ends will not run infinitely.
The values used in each function call may be placed in their own frame on the stack.
If the amount of function calls takes up more space than the stack has, it will result in a stack overflow error.

```python
# TODO: Python example code here
```

This will print

```
The number is 1
The number is 2
After recursion
```

There may be some situations that are more readable and/or easier to reason through when expressed through recursion than when expressed through looping.


## Tail Call

A tail call is when the last statement of a function only calls itself and nothing more.

A tail call is a particular form of recursion which may allow the compiler to optimize the recursion into a loop in the compiled code.
That gives the best of both worlds: the readability of recursion with the performance of a loop.
The compiling of recursion into a loop is called `tail call elimination` or `tail call optimization.`

When a tail call is compiled into a loop, a new stack frame is not created for every function call.
The address of the function when originally called is passed the updated values, thus saving stack space and improving performance.

This example is not a tail call, as the function adds 1 to the result of calling itself

```python
# TODO: Python example code here
```

This will print

```
The number is 1
The number is 2
j is 3 after recursion
```

To refactor it to a tail call, make `j` a parameter of `printIncrement`

```python
# TODO: Python example code here
```

You may find that a tail call may be easier to reason through than a recursive call that is not a tail call.
However, compilers usually do not guarantee that all tail calls will be optimized.
It is always important when using recursion to know that there will not be so many iterations that the stack will overflow.
