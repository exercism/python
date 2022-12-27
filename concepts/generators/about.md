# About

## Constructing a generator

Generators are constructed much like other looping or recursive functions, but require a [`yield` expression](#the-yield-expression), which we will explore in depth a bit later.

An example is a function that returns the _squares_ from a given list of numbers.  
As currently written, all input must be processed before any values can be returned:

```python
>>> def squares(list_of_numbers):
...     squares = []
...     for number in list_of_numbers:
...         squares.append(number ** 2)
...     return squares
```

You can convert that function into a generator like this:

```python
>>> def squares_generator(list_of_numbers):
...     for number in list_of_numbers:
...         yield number ** 2
```

The rationale behind this is that you use a generator when you do not need all the values _at once_.

This saves memory and processing power, since only the value you are _currently working on_ is calculated.

## Using a generator

Generators may be used in place of most `iterables` in Python. This includes _functions_ or _objects_ that require an `iterable`/`iterator` as an argument.

To use the `squares_generator()` generator:

```python
>>> squared_numbers = squares_generator([1, 2, 3, 4])

>>> for square in squared_numbers:
...     print(square)
...
1
4
9
16
```

Values within a generator can also be produced/accessed via the `next()` function.
`next()` calls the `__next__()` method of a generator object, "advancing" or evaluating the generator code up to its `yield` expression, which then "yields" or returns the value.

```python
>>> squared_numbers = squares_generator([1, 2])

>>> next(squared_numbers)
1
>>> next(squared_numbers)
4
```

When a `generator` is fully consumed and has no more values to return, it throws a `StopIteration` error.

```python
>>> next(squared_numbers)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```

### Difference between iterables and generators

Generators are a special sub-set of _iterators_.
`Iterators` are the mechanism/protocol that enables looping over _iterables_.
Generators and the iterators returned by common Python [`iterables`][iterables] act very similarly, but there are some important differences to note:

- Generators are _one-way_; there is no "backing up" to a previous value.

- Iterating over generators consume the returned values; no resetting.

- Generators (_being lazily evaluated_) are not sortable and can not be reversed.

- Generators do _not_ have `indexes`, so you can't reference a previous or future value using addition or subtraction.

- Generators cannot be used with the `len()` function.

- Generators can be _finite_ or _infinite_, be careful when collecting all values from an _infinite_ generator.

## The yield expression

The [yield expression][yield expression] is very similar to the `return` expression.

_Unlike_ the `return` expression, `yield` gives up values to the caller at a _specific point_, suspending evaluation/return of any additional values until they are requested.

When `yield` is evaluated, it pauses the execution of the enclosing function and returns any values of the function _at that point in time_.

The function then _stays in scope_, and when `__next__()` is called, execution resumes until `yield` is encountered again.

Note: _Using `yield` expressions is prohibited outside of functions._

```python
>>> def infinite_sequence():
...     current_number = 0
...     while True:
...         yield current_number
...         current_number += 1

>>> lets_try = infinite_sequence()
>>> lets_try.__next__()
0
>>> lets_try.__next__()
1
```

## Why generators?

Generators are useful in a lot of applications.

When working with a large collection, you might not want to put all of its values into `memory`.
A generator can be used to work on larger data piece-by-piece, saving memory and improving performance.

Generators are also very helpful when a process or calculation is _complex_, _expensive_, or _infinite_:

```python
>>> def infinite_sequence():
...     current_number = 0
...     while True:
...         yield current_number
...         current_number += 1
```

Now whenever `__next__()` is called on the `infinite_sequence` object, it will return the _previous number_ + 1.

[iterables]: https://wiki.python.org/moin/Iterator
[yield expression]: https://docs.python.org/3.11/reference/expressions.html#yield-expressions
