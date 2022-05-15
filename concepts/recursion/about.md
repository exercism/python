# About

Recursion is a way to repeat code in a function by the function calling itself.
It is another way to loop/iterate. Like looping, the function should test a Boolean expression to know when to end.
Unlike looping, recursion that never ends will not run infinitely.
The values used in each function call will be placed in their own frame on the stack.
If the amount of function calls takes up more space than the stack has, it will result in a stack overflow error.

```python
def printIncrement(i, maxValue):
    if i > maxValue:
        return
    print(f'The number is {i}')
    printIncrement(i + 1, maxValue)


def main():
    printIncrement(1, 2)
    print("After recursion")

if __name__ == "__main__":
    main()

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
This example is not a tail call, as the function adds 1 to the result of calling itself

```python
def printIncrement(i, maxValue):
    if i > maxValue:
        return 1
    print(f'The number is {i}')
    return 1 + printIncrement(i + 1, maxValue)


def main():
    j = printIncrement(1, 2)
    print(f'j is {j} after recursion')

if __name__ == "__main__":
    main()

```

This will print

```
The number is 1
The number is 2
j is 3 after recursion
```

To refactor it to a tail call, make `j` a parameter of `printIncrement`

```python
def printIncrement(i, maxValue, j):
    if i > maxValue:
        return j
    print(f'The number is {i}')
    return printIncrement(i + 1, maxValue, j + 1)


def main():
    j = printIncrement(1, 2, 1)
    print(f'j is {j} after recursion')

if __name__ == "__main__":
    main()

```

You may find that a tail call may be easier to reason through than a recursive call that is not a tail call.
However, it is always important when using recursion to know that there will not be so many iterations that the stack will overflow.

## Resources

To learn more about using recursion in Python you can start with 
- [python-programming: recursion][python-programming: recursion]
- [Real Python: python-recursion][Real Python: python-recursion]
- [Real Python: python-thinking-recursively][Real Python: python-thinking-recursively]

[python-programming: recursion]: https://www.programiz.com/python-programming/recursion
[Real Python: python-recursion]: https://realpython.com/python-recursion/
[Real Python: python-thinking-recursively]: https://realpython.com/python-thinking-recursively/
