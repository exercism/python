# About

Decorators are functions that take another function as an argument for the purpose of extending or replacing the behavior of the passed-in function.
If function `A` is a decorator, and function `B` is its argument, then function `A` modifies, extends, or replaces function `B`'s **behavior** _without modifying_ function `B`'s code.
We say that the decorator function `A` _wraps_ function `B`.
While we talk about "modifying" behavior, the wrapped function is _not actually changed_.
Behavior is either added _around_ the wrapped function (_and what it returns_), or the wrapped function's behavior is _substituted_ for some other behavior.

## A Decorator is a Higher-Order Function

A [higher-order function][higher-order functions] is a function that accepts one or more functions as arguments and/or returns one or more functions.
A function, used as an argument or returned from another function, is a [first-class function][first-class functions].
A Python function, as a [callable object][callable objects], is a first-class function which can be stored in a variable or used as an argument, much like any other value or object.
Higher-order functions and first-class functions work together to make decorators possible.

## What Using a Decorator Looks Like

The `@` symbol is prepended to the name of the decorator function and placed just above the function to be decorated, like so:

```python
@decorator
def decorated_function():
    pass
```

Some decorators accept arguments:

```python
@decorator_with_arg(name="Bob")
def decorated_function2():
    pass
```

If a decorator has defined default arguments, you must use parenthesis in the `@decorator()` call for the decorator to work, as you would in calling any function:

```python
@decorator_with_default_arg()
def decorated_function3():
    pass
```

If a decorator takes a _positional_ arguments, not supplying the arguments will result in an error which will look something like:

```
TypeError: decorator_with_pos_arg() missing 1 required positional argument: 'name'
```

The `@decorator` syntax is syntactic sugar or a shorthand for calling the _decorating function_ and passing the _decorated function_ to it as an argument.
Following are examples of alternative ways for calling a decorator:

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

## Writing a Simple Decorator

Most decorators are intended to _extend_ or _replace_ the behavior of another function, but some decorators may do nothing but return the functions they are wrapping.

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

A decorator may only add side effects, such as additional information used for logging:

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
It may return its function arguments, another function, or one or more values that replace the return from the passed-in or decorated function.
If a decorator returns another function, it will usually return an [inner function][inner functions].

## Inner Functions

A function can be defined within a function.
Such a nested function is called an [inner function][inner functions].
A decorator may use an inner function to wrap its function argument.
The decorator then returns its inner function.
The inner function may then return the original function argument.

### A Validating Decorator Using an Inner Function

Following is an example of a decorator being used for validation:

```python
>>> def my_validator(func):
...     def my_wrapper(world):
...         print(f"Entering {func.__name__} with {world} argument")
...         if ("Pluto" == world):
...             print("Pluto is not a planet!")
...         else:
...             return func(world)
...     return my_wrapper
...
... @my_validator
... def my_func(planet):
...     print(f"Hello, {planet}!")
...
>>> my_func("World")
Entering my_func with World argument
Hello, World!
...
>>> my_func("Pluto")
Entering my_func with Pluto argument
Pluto is not a planet!
```

On the first line, we have the definition for the decorator with its `func` argument.
On the next line is the definition for the decorators _inner function_, which wraps the `func` argument.
Since the _inner function_ wraps the decorator's `func` argument, it is passed the same argument that is passed to `func`.
Note that the wrapper doesn't have to use the same name for the argument that was defined in `func`.
The original function uses `planet` and the decorator uses `world`, and the decorator still works.

The inner function returns either `func` or, if `planet` equals `Pluto`, it will print that Pluto is not a planet.
It could be coded to raise a `ValueError` instead.
So, the inner function wraps `func`, and returns either `func` or does something that substitutes what `func` would do.
The decorator returns its _inner function_.
The _inner_function_ may or may not return the original, passed-in function.
Depending on what code conditionally executes in the wrapper function or _inner_function_, `func` may be returned, an error could be raised, or a value of `func`'s return type could be returned.

### Decorating a Function that Takes an Arbitrary Number of Arguments

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
If we want to triple, quadruple, etc. the return value, we can add a parameter to the decorator itself, as we show in the next section.

### Decorators Which Have Their own Parameters

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
