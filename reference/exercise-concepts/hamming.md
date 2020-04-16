# Concepts of `hamming`

## Example implementation

From the current [example.py](https://github.com/exercism/python/blob/master/exercises/hamming/example.py):

```python
def distance(s1, s2):
    if len(s1) != len(s2):
        raise ValueError("Sequences not of equal length.")

    return sum(a != b for a, b in zip(s1, s2))
```

## Concepts

- [Function definition][function-definition]: functions are defined and named using the `def` keyword
- [Function signature][function-signature]: functions take named arguments which are accessible within the body of the function; this one requires the student to make a function that accepts 2
- [Return value][return-value]: the function must return a number (int)
- [Strings][strings]: strings are used generally
- [Builtin functions][builtin-functions]: strings have a length, accessible by calling `len()`, a builtin python function
- [Iterable][iterable]: strings are iterable, which provides a lot of opportunity to leverage Python functions against them
- [Immutable][immutable]: strings are immutable (_immutability_)
- [Booleans][booleans]: this solution uses Boolean values (`True` / `False`)
- [Inequality][inequality]: this solution checks if `a` is not equal to `b`.
- [Booleans are integers][booleans-are-integers]: Booleans values are just named aliases for the integers 1 (`True`) and 0 (`False`)
- [Zip][zip]: builtin that joins multiple iterables into a single one
- [Enumeration][enumeration]: `zip()` in this solution creates an iterable, which is iterated over by using the `for ... in` syntax
- [Sum][sum]: another builtin that operates on iterables
- [Tuple unpacking][tuple-unpacking]: the values in an iterable can be unpacked into variables and used, i.e. `for a, b in zip(s1, s2)`
- [Exception handling][exception-handling]: the exercise requires Exception handling
- [Raise][raise]: the student is required to raise an `Exception` for incorrect input
- [Exception hierarchy][exception-hierarchy]: the idiomatic `Exception` type is a `ValueError`, meaning the input is incorrect
- [Exception catching][exception-catching]: `Exceptions` can be caught from outside the scope where they are raised, using the `try/except` syntax. All `Exceptions` types inherit from the base class, `Exception` and thus can be caught by either checking specifically for the type of Exception, or for any Exception
- [Exception message][exception-message]: Custom error messages can (and should) be supplied to an Exception when raised
- [Operators][operators]: `!=` is "not equal", which is not the same thing as `is`, or an identity check, but is the inverse of `==`, which is equality
- [Loops][loops]: the `for ... in` syntax is useful for looping through a list or other iterable object
- [Generators][generators]: generators calculate then `yield` a value one at a time, as opposed to lists which calculate and return all values in memory at once. A generator will pick up where it leaves off, and generate one item at a time, on demand
- [Generator comprehension][generator-comprehension]: a generator comprehension is passed to `sum()` to drive summation without storing all the values in a list first
- [Tuple unpacking][tuple-unpacking]: iterating through a list of tuples, i.e. [(1, 2), (2,3)], each piece of each tuple can be unpacked into a separate variable (syntax: `a, b = (1, 2)`); this works for any sort of iterable (lists, for example, and even strings!) but is commonly used with tuples because they are typically of a known size/length, and so can be safely unpacked into N variables, with names.
- [Dunder Methods][dunder-methods]: "dunder" -> "double under", referring to the names of these methods being prefixed with two underscores, e.g. `__init__`. There is no formal privacy in Python, but conventionally a single underscore indicates a private method, or one that the programmer should assume may change at any time; methods without an underscore are considered part of an object's public API. Double underscores are even more special - they are used by Python's builtin functions like `len()`, for example, to allow objects to implement various interfaces and functionality. They can also be used for operator overloading. If you have a custom class that you would like to be able to compare to other instances of the same class, implementing `__lt__`, `__gt__`, `__eq__` etc. allow programmers to use the `>`, `<`, `=` operators. Dunder methods allow programmers to build useful objects with simple interfaces, i.e. you can add two instances together using `+` instead of writing something like `instance1.add(instance2)`.
- [Builtin Function][builtin-functions]: Python has several handy builtin functions in the stdlib that can operate on many types of data, e.g. `len()`, `max()`, `min()`. Under the hood these are implemented via dunder methods - if an object (and everything in Python is an object) implements the correct dunder methods (see that topic for more information), it can support use in these functions. (For example, if an object implements `__len__`, the len(<object>) will return that value.) Because these functions are not strictly tied to any data type, they can be used almost anywhere, and will crop up again and again as we learn Python. Docs: https://docs.python.org/3/library/functions.html
- [Polymorphism][polymorphism]: Python is "dynamically typed," meaning that variable names are bound to objects only, not to a particular type. You can assign `foo` to a string, and then reassign it to an `int` with no issues. "Polymorphism" formally means that different types respond to the same function - so the ability to add custom class instances together using `+`, for example, shows how Python can define the same function against different types.
- [Duck Typing][duck-typing]: Python is also a good example of "Duck typing," to wit, "if it walks like a duck, talks like a duck, it's a duck.". This is accomplished partly with "magic" or "dunder" methods (double-under) that provide various interfaces to an object. If an object implements `__iter__` and `__next__`, it can be iterated through; it doesn't matter what type the object actually is.
