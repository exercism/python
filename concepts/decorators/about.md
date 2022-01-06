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

## How to write them

As said before, decorators can modify or register a function.
The simplest decorator however, does absolutely nothing.  

Decorators are functions which return functions.
They take one argument - the function which they have been added to.
They also return one thing - the function which will be run by the program.
This is usually either the function they were added to or a slightly modified version of that function, but it does not have to be - it can be any function whatsoever.

The simplest decorator - one that does nothing - can be written as follows:
```python
def do_nothing(function):
    return function
```
```python
def function4a():
    return 4

@do_nothing
def function4b():
    return 4
```
```python
>>>function4a()
4
>>>function4b()
4
```
As you can see, both functions do the same thing, and when the decorator is added nothing changes.
