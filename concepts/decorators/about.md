# About

Decorators are a feature of the Python language that can modify or register a function.

## How to use them

Decorators are placed just above a function in the code like so:

```python
@decorator
def function():
    pass
```

Some decorators take arguments:

```python
@decorator2(name="Bob")
def function2():
    pass
```

If a decorator takes any arguments, but you don't wish to pass any, you must still call it with parentheses for the decorator to work:

```python
@decorator3()
def function3():
    pass
```

Decorators are just syntactic sugar.
An alternative way of doing the same as the above three examples is using higher-order functions:
```python
def function():
    pass

function = decorator(function)


def function2():
    pass

function2 = decorator2(name="Bob")(function2)


def function3():
    pass

function3 = decorator3()(function3)
```
