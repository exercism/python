# Introduction

The functools module is for higher-order functions: functions that act on or return other ***[functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)***. It provides functions for working with other functions and callable objects to use or extend them without completely rewriting them.

## Decorators

A ***[decorator](https://www.programiz.com/python-programming/decorator)*** takes in a function, adds some functionality and returns it. Decorators are example of higher order functions. We can decorate our function by writing `@decorator_function_name` just before defing function.

## Generic functions

***[Generic functions](https://pymotw.com/3/functools/#generic-functions)*** are those which preform the operation based on the argument given to them. In statically typed languages it can be done by function overloading. In python functools provides the `singledispatch()` decorator to register a set of generic functions for automatic switching based on the type of the first argument to a function.

## Partial

`functools.partial(func, /, *args, **keywords)` return a new ***[partial object](https://docs.python.org/3/library/functools.html#partial-objects)*** which when called will behave like func called with the positional arguments args and keyword arguments keywords. If more arguments are supplied to the call, they are appended to args.The ***[partial](https://docs.python.org/3/library/functools.html#functools.partial)*** is used for partial function application which “freezes” some portion of a function’s arguments and/or keywords resulting in a new object with a simplified signature.

