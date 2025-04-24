# About

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


[generator-iterator]: https://docs.python.org/3.11/glossary.html#term-generator-iterator
[iterables]: https://wiki.python.org/moin/Iterator
[iterator]: https://docs.python.org/3.11/glossary.html#term-iterator
[lazy iterator]: https://en.wikipedia.org/wiki/Lazy_evaluation
[yield expression]: https://docs.python.org/3.11/reference/expressions.html#yield-expressions



## ZIP function

The zip() function in python is built in function. it pairs the two or more  iteratbles and combines them one by one in into a single data structure, only  done when needed (lazy evaluation)

Example:
l1= ["AA","BB","CC"]
l2=[1,2,3]
l3= zip(l1, l2)
print(list(l3))

output
[('AA', 1), ('BB', 2), ('CC', 3)]


## map function 

the map() function in the Python takes 2 arguments that is : 1. A function, 2. list or any iterable 
then the map() function applies the function to each of the item in iterable 
Example:
l1=[1,2,3]
result = map(lambda x:x**2, l1)
print(list (result) )

output:
[1, 4, 9]

In short map() map() helps you apply a rule to each and every item in the list (or iterable) does by without using any extra memory 

## filter

filter() function in python helps you to filter the items based on the specified condition.
it filters only those items or iterables which are True
Example: l2=[1,2,3]
result = filter (lambda x:x%2==0 , l2)
print(list (result) )

output:
[2]
In short filter() helps you pick only the items that match a rule






zip() Function
The zip() function in Python is a built-in that pairs elements from two or more iterables together. It combines them element-by-element into a single iterable — and does this lazily (only when needed).

Example:

python
Copy
Edit
l1 = ["AA", "BB", "CC"]
l2 = [1, 2, 3]
l3 = zip(l1, l2)
print(list(l3))
Output:

css
Copy
Edit
[('AA', 1), ('BB', 2), ('CC', 3)]
🔹 In short: zip() lets you group related items together from different iterables.

map() Function
The map() function takes:

A function

An iterable (like a list)

It applies the function to each item in the iterable — and returns a map object (like a generator) without creating a new list in memory.

Example:

python
Copy
Edit
l1 = [1, 2, 3]
result = map(lambda x: x**2, l1)
print(list(result))
Output:

csharp
Copy
Edit
[1, 4, 9]
🔹 In short: map() helps you apply a rule or transformation to every item in a list.

filter() Function
The filter() function also takes:

A function that returns True or False

An iterable

It filters out only the items where the function returns True.

Example:

python
Copy
Edit
l2 = [1, 2, 3]
result = filter(lambda x: x % 2 == 0, l2)
print(list(result))
Output:

csharp
Copy
Edit
[2]
In short: filter() helps you pick only the items that match a rule