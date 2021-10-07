# Instructions

A generator in Python is a _callable function_ that returns a [lazy iterator](https://en.wikipedia.org/wiki/Lazy_evaluation).

_Lazy iterators_ are similar to `lists`, and other `iterators`, but with one key difference: They do not store their `values` in memory, but _generate_ their values when needed.

## Constructing a generator

Constructing a `generator` is a bit different than a normal `function`. You will need the `yield` expression, which we will go into depth with [later](#the-yield-expression).

Lets say you want to construct a `generator` that generates all the _squares_ from a list of numbers. You would construct that function like this:

```python
>>> def squares(list_of_numbers):
>>>     for number in list_of_numbers:
>>>         yield number ** 2
```

## Using a generator

It is possible to use any Python _function_ or _object_ that requires an `iterator` as an argument.

For example, if you want to use the `squares()` generator we just constructed, we simply use:

```python
>>> list_of_numbers = [1, 2, 3, 4]

>>> for square in squares(list_of_numbers):
>>>     print(square)
 1
4
9
16
```

You can also get access to the values of a `generator` by using the `next()` function. The `next()` function calls the `__next__()` attribute of a generator.

```python
square_generator = squares([1, 2])

>>> next(square_generator)
1
>>> next(square_generator)
4
```

When the `generator` has no more values to return it throws a `StopIteration` error.

```python
>>> next(square_generator)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```

## The yield expression

The [yield expression](https://docs.python.org/3.8/reference/expressions.html#yield-expressions) is very similar to the `return` expression. Unlike the `return` expression, `yield` returns a _generator object_ to the caller.

When `yield` is called, it pauses the execution of the function it is in and returns a value. When `__next__()` is called, it resumes the execution of the function.

`yield` expressions are _prohibited_ to be used outside of functions.

## Why generators?

Generators are useful in a lot of applications.

When working with a large collection, you might not want to put all of that into `memory`. You can use generators to work on data piece-by-piece, this saves memory and improves performance.

You can also use it to generate complicated or infinite sequences, like this:

```python
>>> def infinite_sequence():
>>>     current_number = 0
>>>     while True:
>>>         yield current_number
>>>         current_number += 1
```

Now whenever `__next__()` is called on the `infinite_sequence` object, it will return the _previous number_ + 1.
