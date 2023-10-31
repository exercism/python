# Generators

A `generator` is a function or expression that returns a special type of [iterator][iterator] called [generator iterator][generator-iterator].
`Generator-iterators` are [lazy][lazy iterator]: they do not store their `values` in memory, but _generate_ their values when needed.

A generator function looks like any other function, but contains one or more [yield expressions][yield expression].
Each `yield` will suspend code execution, saving the current execution state (_including all local variables and try-statements_).
When the generator resumes, it picks up state from the suspension - unlike regular functions which reset with every call.


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

The rationale behind this is that you use a generator when you do not need to produce all the values _at once_.
This saves memory and processing power, since only the value you are _currently working on_ is calculated.


## Using a generator

Generators may be used in place of most `iterables` in Python.
This includes _functions_ or _objects_ that require an `iterable`/`iterator` as an argument.

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

Values within a `generator` can also be produced/accessed via the `next()` function.
`next()` calls the `__next__()` method of a generator-iterator object, "advancing" or evaluating the code up to its `yield` expression, which then "yields" or returns a value:

```python
>>> squared_numbers = squares_generator([1, 2])

>>> next(squared_numbers)
1
>>> next(squared_numbers)
4
```

When a `generator-iterator` is fully consumed and has no more values to return, it throws a `StopIteration` error.

```python
>>> next(squared_numbers)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```


~~~~exercism/note

Generator-iterators are a special sub-set of [iterators][iterator].
`Iterators` are the mechanism/protocol that enables looping over _iterables_.
Generator-iterators and the iterators returned by common Python [`iterables`][iterables] act very similarly, but there are some important differences to note:

- They are _[lazily evaluated][lazy evaluation]_; iteration is _one-way_ and there is no "backing up" to a previous value.
- They are _consumed_ by iterating over the returned values; there is no resetting or saving in memory.
- They are not sortable and cannot be reversed.
- They are not sequence types, and _do not_ have `indexes`. 
  You cannot reference a previous or future value using addition or subtraction and you cannot use bracket (`[]`) notation or slicing.
- They cannot be used with the `len()` function, as they have no length.
- They can be _finite_ or _infinite_ - be careful when collecting all values from an _infinite_ `generator-iterator`!

[iterator]: https://docs.python.org/3.11/glossary.html#term-iterator
[iterables]: https://wiki.python.org/moin/Iterator
[lazy evaluation]: https://en.wikipedia.org/wiki/Lazy_evaluation
~~~~


## The yield expression

The [yield expression][yield expression] is very similar to the `return` expression.
_Unlike_ the `return` expression, `yield` gives up values to the caller at a _specific point_, suspending evaluation/return of any additional values until they are requested.
When `yield` is evaluated, it pauses the execution of the enclosing function and returns any values of the function _at that point in time_.
The function then _stays in scope_, and when `__next__()` is called, execution resumes until `yield` is encountered again.


~~~~exercism/note
Using `yield` expressions is prohibited outside of functions.
~~~~

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


## Why Create a Generator?

Generators are useful in a lot of applications.

When working with a potentially large collection of values, you might not want to put all of them into memory.
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


[generator-iterator]: https://docs.python.org/3.11/glossary.html#term-generator-iterator
[iterables]: https://wiki.python.org/moin/Iterator
[iterator]: https://docs.python.org/3.11/glossary.html#term-iterator
[lazy evaluation]: https://en.wikipedia.org/wiki/Lazy_evaluation
[lazy iterator]: https://en.wikipedia.org/wiki/Lazy_evaluation
[yield expression]: https://docs.python.org/3.11/reference/expressions.html#yield-expressions
