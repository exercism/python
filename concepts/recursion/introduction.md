# Introduction

Recursion is a way to repeat code in a function by the function calling itself.
It can be viewed as another way to loop/iterate. 
Like looping, a Boolean expression or `True/False` test is used to know when to stop the recursive execution.
_Unlike_ looping, recursion without termination in Python cannot not run infinitely.
Values used in each function call are placed in their own frame on the Python interpreter stack.
If the total number of function calls takes up more space than the stack has room for, it will result in an error.

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
