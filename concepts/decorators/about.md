# About

Decorators are functions that take another function as an argument for the purpose of extending or replacing the behavior of the passed-in function.
If function `A` is a decorator, and function `B` is its argument, then function `A` modifies, extends or replaces function `B`'s **behavior** _without modifying_ function `B`'s code.
We say that the decorator function `A` _wraps_ function `B`.
While we talk about "modifying"  behavior, the wrapped function is _not actually changed_.
Behavior is either added _around_ the wrapped function (_and what it returns_), or the wrapped function's behavior is _substituted_ for some other behavior.

## A Decorator is a Higher-Order Function

A [higher-order function][higher-order functions] is a function that accepts one or more functions as arguments and/or returns one or more functions.
A function, used as an argument or returned from another function, is a [first-class function][first-class functions].
A Python function, as a [callable object][callable objects], is a first-class function which can be stored in a variable or used as an argument, much like any other value or object.
Higher-order functions and first-class functions work together to make decorators possible.

## What Using Decorator Looks Like

The `@` symbol is prepended to the name of the decorator function and placed just above the function to be decorated, like so:

```python
@decorator
def decorated_function():
    pass
```

Some decorators take arguments:

```python
@decorator_with_arg(name="Bob")
def function2():
    pass
```

If a decorator takes a default argument, you must still call it with parentheses for the decorator to work:

```python
@decorator_with_default_arg()
def function3():
    pass
```

If a decorator takes a positional argument, using empty parentheses will result in an error which will look something like:

```
TypeError: decorator_with_pos_arg() missing 1 required positional argument: 'name'
```

The `@decorator` syntax is just syntactic sugar.
Following are examples of alternative ways for setting a decorator:

```python
def function():
    pass

function = decorator(function)


def function2():
    pass

function2 = decorator_with_arg(name="Bob")(function2)


def function3():
    pass

function3 = decorator_with_default_arg()(function3)
```

## How to write a simple Decorator

Decorators are intended to extend or replace the behavior of another function, but a decorator may do nothing but return the function it is wrapping.

Decorators are functions which take at least one argument - the function which they are wrapping.
They usually return either the wrapped function or the result of an expression that uses the wrapped function.

A simple decorator - one that simply returns its wrapped function - can be written as follows:
```python
>>> def do_nothing(func):
...     return func
... 
... @do_nothing
... def function4():
...     return 4
... 
>>> print(function4())
4

```

A decorator may only add side effects, such as for logging:

```python
>>> def my_logger(func):
...     print(f"Entering {func.__name__}")
...     return func
... 
... @my_logger
... def my_func():
...     print("Hello")
... 
>>> my_func()
Entering my_func
Hello

```

A decorator does not return itself.
It may return its function argument, another function, or a value that replaces the return value from the function argument.
If a decorator returns another function, it will usually return an [inner function][inner functions].

## Inner Functions

A function can be defined within a function.
Such a nested function is called an [inner function][inner functions].
A decorator may use an inner function to wrap its function argument.
The decorator returns its inner function.
The inner function may return the original function argument.

### How to write a validating Decorator using an inner function

Following is an example of a decorator being used for validation:

```python
>>> def my_validator(func):
...     def my_wrapper(planet):
...         print(f"Entering {func.__name__} with {planet} argument")
...         if ("Pluto" == planet):
...             print("Pluto is not a planet!")
...         else:
...             return func(planet)
...     return my_wrapper
... 
... @my_validator
... def my_func(planet):
...     print(f"Hello, {planet}!")
... 
>>> my_func("World")
Entering my_func with World argument
Hello, World!
>>> my_func(Pluto")
Entering my_func with Pluto argument
Pluto is not a planet!

```

On the first line, we have the definition for the decorator with its `func` argument.
On the next line is the definition for the decorators inner function, which wraps the `func` argument.
Since the inner function wraps the decorator's `func` argument, it is passed the same argument of `planet`.
It doesn't have to have the same name of `planet`.
If `planet` was replaced with `world` throughout the decorator, the decorater would still work.

The inner function returns either `func` or, if `planet` equals `Pluto`, it will print that Pluto is not a planet.
It could be coded to raise a `ValueError` instead.
So, the inner function wraps `func`, and returns either `func` or does something that substitutes what `func` would do.
The decorator returns the inner function.
It does not _directly_ return the original function.
Depending on what happens in the wrapper function, `func` may or may not be returned.

### How to write a Decorator for a function that takes an arbitrary number of arguments

Decorators can be written for functions that take an arbitrary number of arguments by using the `*args` and `**kwargs` syntax.

Following is an example of a decorator for a function that takes an arbitrary number of arguments:

```python
>>> def double(func):
...     def wrapper(*args, **kwargs):
...         return func(*args, **kwargs) * 2
...     return wrapper
... 
... @double
... def add(*args):
...     return sum(args)
... 
>>> print(add(2, 3, 4))
18
>>> print(add(2, 3, 4, 5, 6))
40

```

This works for doubling the return value from the function argument.
If we want to triple, quadruple, etc. the return value, we can add a parameter to the decorator itself.

### How to write a Decorator which has its own parameters

Following is an example of a decorator that can be configured to multiply the decorated function's return value by an arbitrary amount:

```python
>>> def multi(factor=1):
...     if (factor == 0):
...         raise ValueError("factor must not be 0")
... 
...     def outer_wrapper(func):
...         def inner_wrapper(*args, **kwargs):
...             return func(*args, **kwargs) * factor
...         return inner_wrapper
...     return outer_wrapper
... 
... @multi(factor=3)
... def add(*args):
...     return sum(args)
... 
>>> print(add(2, 3, 4))
27
>>> print(add(2, 3, 4, 5, 6))
60

```

The first lines validate that `factor` is not `0`.
Then the outer wrapper is defined.
This has the same signature we expect for an unparameterized decorator.
The outer wrapper has an inner function with the same signature as the original function.
The inner wrapper does the work of multiplying the returned value from the original function by the argument passed to the decorator.
The outer wrapper returns the inner wrapper, and the decorator returns the outer wrapper.

Following is an example of a parameterized decorator that controls whether it validates the argument passed to the original function:

```python
>>> def check_for_pluto(check=True):
...     def my_validator(func):
...         def my_wrapper(world):
...             print(f"Entering {func.__name__} with {world} argument")
...             if (check and "Pluto" == world):
...                 print("Pluto is not a planet!")
...             else:
...                 return func(world)
...         return my_wrapper
...     return my_validator
... 
... @check_for_pluto(check=False)
... def my_func(planet):
...     print(f"Hello, {planet}!")
... 
>>> my_func("World")
Entering my_func with World argument
Hello, World!
>>> my_func("Pluto")
Entering my_func with Pluto argument
Hello, Pluto!

```

This allows for easy toggling between checking for `Pluto` or not, and is done without having to modify `my_func`.

[callable objects]: https://www.pythonmorsels.com/callables/
[first-class functions]: https://www.geeksforgeeks.org/first-class-functions-python/
[higher-order functions]: https://www.geeksforgeeks.org/higher-order-functions-in-python/
[inner functions]: https://www.geeksforgeeks.org/python-inner-functions/
