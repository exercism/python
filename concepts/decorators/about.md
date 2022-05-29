# About

Decorators are functions that take another function as an argument for the purpose of extending or replacing the behavior of the function argument.
If function `A` is a decorator, and function `B` is its argument, then function `A` extends or replaces function `B`'s behavior _without modifying_ it.
We say that the decorator function `A` _wraps_ function `B`.
The wrapped function is not actually changed.
Beahvior is either added around the wrapped function, or the wrapped function's behavior is substituted.

## A Decorator is a Higher-Order Function

A [higher-order function][higher-order functions] is a function that accepts a function as an argument and/or returns a function.
A function, used as an argument or returned from another function, is a [first-class function][first-class functions].
A Python function, as a [callable object][callable object], is a first-class function which can be stored in a variable or used as an argument, much like any other value.
Higher-order functions and first-class functions work together to make decorators possible.

## What a Decorator looks like

Decorators are placed just above a function in the code like so:

```python
@decorator
def function():
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

If a decorator takes a positional argument, using empty parentheses will result in an error which will look something like

```
TypeError: decorator_with_default_arg() missing 1 required positional argument: 'name'
```

Decorators are just syntactic sugar.
Following are examples of alternative ways of setting a decorator:

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

## How to write a Decorator

Decorators are intended to extend or replace the behavior of another function, but a decorator may do nothing but return the function it is wrapping.

Decorators are functions which take at least one argument - the function which they are wrapping.
They usually either return the wrapped function or they may return the result of an expression that uses the wrapped function.

The simplest decorator - one that does nothing - can be written as follows:
```python
def do_nothing(function):
...     return function
... 
@do_nothing
def function4():
...     return 4
... 
>>>function4()
4

```

A decorator may add side effects (such as logging) and/or validation:

```python
>>> def my_logger(func):
...     def my_logger_wrapper(*args, **kwargs):
...         print(f"Entering {func.__name__} with {args} argument")
...         if any("Pluto" in text for text in args):
...             print("Pluto is not a world!")
...         else:
...             func(*args, **kwargs)
...         print(f"After {func.__name__}")
...     return my_logger_wrapper
... 
... 
>>> @my_logger
... def my_func(planet):
...     print(f"Hello, {planet}!")
... 
... 
>>> my_func("World")
Entering my_func with ('World',) argument
Hello, World!
After my_func
>>> my_func(Pluto")
Entering my_func with ('Pluto',) argument
Pluto is not a world!
After my_func

```

Many decorators you write will change what is run when the function is called.
These will need to return a different function to the one passed.
This different function is written inside the decorator's function.

This decorator doubles the result of the function:
```python
def double(function):
    def wrapper():
        function_result = function()
        doubled = function_result * 2
        return doubled
    return wrapper
```
```python
def function6a():
    return 6

@double
def function6b():
    return 6
```
```python
>>>function6a()
6
>>>function6b()
12
```
As you can see the decorator modifies the result of the function.

Now lets take a look at what is actually happening in this decorator.

On the first line, we have the normal function definition.
But, when we go inside this function and take a look at the next line, we get another function definition.
This function is what we will return at the end of the decorator.
This means we are not returning the original function.
Because of this, Python will not actually call the original function when a call is made to what looks like that function.
Instead, Python will call the function we created, `wrapper()`.

If we look inside our `wrapper()` function, we first see a call to the original function.
This call will do exactly the same as if we had called the original function without the decoration to the function.
Then we get a line that modifies this result.
Finally we return the modified result, which is what we get when calling the function.

If we apply this decorator to a function which takes a single number and triples it, then we should get a function that sextuples our number.
Lets see what happens:
```python
@double
def triple(number):
    return number * 3
```
```python
>>>triple(5)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: wrapper() takes 0 positional arguments but 1 was given
```
Unfortunately, we get an error.
This happens because, as said earlier, python does not call the original function when you appear to call it.
Python actually calls the function in the decorator, `wrapper()`, which does not have any parameters.

To rectify this, we can add a parameter to our `wrapper()` function.
An updated `@double` decorator is shown below:
```python
def double(function):
    def wrapper(value):
        function_result = function(value)
        doubled = function_result * 2
        return doubled
    return wrapper
```
```python
>>>triple(5)
30
```
However, if we now call our function which took no parameters earlier, it will fail:
```python
>>>function6b()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: wrapper() mising 1 required positional argument: 'value'
```
It would also fail for any other number of parameters too.

Fortunately we can write decorators that don't care about the number of parameters a function may take by using the `*args` and `**kwargs` syntax.
Here's an update `@double` decorator:
```python
def double(function):
    def wrapper(*args, **kwargs):
        function_result = function(*args, **kwargs)
        doubled = function_result * 2
        return doubled
    return wrapper
```
Now we should be to use this decorator on functions which accept zero, one, two or even one million (though we wouldn't recommend that many!) parameters:
```python
>>>triple(5)
30
>>>function6b()
12
```

[callable object]: https://www.pythonmorsels.com/callables/
[first-class functions]: https://www.geeksforgeeks.org/first-class-functions-python/
[higher-order functions]: https://www.geeksforgeeks.org/higher-order-functions-in-python/
