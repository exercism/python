# About

The functools module is for higher-order functions: functions that act on or return other ***[functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)***. It provides functions for working with other functions and callable objects to use or extend them without completely rewriting them.

We must be comfortable with the fact that everything in Python is an object, even the functions.

```python

# Simple python function for greeting
>>> def greet():
        print("Hello, How are you?")

>>> greet()
"Hello, How are you?"

>>> g = greet

>>> g()
"Hello, How are you?"

# Here both functions g and greet give the same output because g and greet refer to the same function object.
```

## Decorators

A ***[decorator](https://www.programiz.com/python-programming/decorator)*** takes in a function, adds some functionality and returns it. Decorators are example of higher order functions. We can decorate our function by writing `@decorator_function_name` just before defing function.

Functions and methods are called callable as they can be called.

In fact, any object which implements the special ```__call__()``` method is termed callable. So, in the most basic sense, a decorator is a callable that returns a callable.

Basically, a decorator takes in a function, adds some functionality and returns it.

```python

# add_wish is a decorator which take a function and add some more functionality to  it.

>>> def add_wish(func):
        def inner():
            print("Good Morning")
            func()
        return inner

# Simple python function for greeting

>>> def greet():
        print("Hello, How are you?")

>>> greet_with_wish = add_wish(greet)

>>> greet_with_wish()
Good Morning
Hello, How are you?

# Or we Can simply use this syntax while defing the the greet function.

 >>> @add_wish
     def greet():
        print("Hello, How are you?")

>>> greet()
Good Morning
Hello, How are you?

# Now we are geting the same output.
```

### Decorating Functions with Parameters

```python

>>> def smart_divide(func):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! cannot divide")
            return

        return func(a, b)
    return inner


>>> @smart_divide
    def divide(a, b):
        print(a/b)

>>> divide(2,5)
I am going to divide 2 and 5
0.4

>>> divide(2,0)
I am going to divide 2 and 0
Whoops! cannot divide

```

A keen observer will notice that parameters of the nested ```inner()``` function inside the decorator is the same as the parameters of functions it decorates. Taking this into account, now we can make general decorators that work with any number of parameters.

## Generic functions

***[Generic functions](https://pymotw.com/3/functools/#generic-functions)*** are those which preform the operation based on the argument given to them. In statically typed languages it can be done by function overloading. In python functools provides the `singledispatch()` decorator to register a set of generic functions for automatic switching based on the type of the first argument to a function.

The ```register()``` attribute of the function serves as another decorator for registering alternative implementations.To add overloaded implementations to the function, use the ```register(type)``` attribute of the generic function.

When user is going to call the function with the integer argument, then it will be redirected  to the function decorated with ```register(int)``` decorator.

The first function wrapped with singledispatch() is the default implementation if no other type-specific function is found, default implementation will be called.

```python

>>> from functools import singledispatch

>>> @singledispatch
    def fun(arg):
        print("default argument string: ", arg)


>>> fun.register(int)
    def _(arg): 
        print("This is an integer: ", arg)

>>> fun.register(list)
    def _(arg):
        print("This is a list: ", arg)

>>> fun("Hello")
"default argument string: Hello"

>>> fun(10)
"This is an integer: 10"

>>> fun([1,2,3])
"This is a list: [1,2,3]"

# This will call the default function as we didn't registered any function with float.
>>> fun(2.45)
"default argument string: 2.45"

```

## Partial

`functools.partial(func, /, *args, **keywords)` return a new ***[partial object](https://docs.python.org/3/library/functools.html#partial-objects)*** which when called will behave like func called with the positional arguments args and keyword arguments keywords. If more arguments are supplied to the call, they are appended to args.The ***[partial](https://docs.python.org/3/library/functools.html#functools.partial)*** is used for partial function application which “freezes” some portion of a function’s arguments and/or keywords resulting in a new object with a simplified signature.

```python

>>> def add(a, b):
    print(f"got a={a}, b={b}")
    print(a+b)

>>> a = partial(add, 10)
>>> a(4)
"got a=10, b=4"
14

# 10 got assigned to a because partial start assigning arguments from the left.

>>> a = partial(add, b=10)
>>> a(4)
"got a=4, b=10"
14

# But By using the keywords we can assign the value to the arguments at right

```
