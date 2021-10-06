## Goal

The goal of this exercise is to teach the syntax and use of generators in Python.

## Learning objectives

- Understand what generators are and how/when to use them
- Understand how generators relate to `loops` and `iterators`
- Understand how to use the `yield` keyword
- Understand the `__next__()` method
- Create a generator

## Out of scope

- rich comparison with `__lt__`, `__le__`, `__ne__`, `__ge__`, `__gt__`
- understanding (_and using the concept_) that the `==` operator calls the dunder method `__eq__()` on a specific object, and uses that object's implementation for comparison. Where no implementation is present, the default `__eq__()` from generic `object` is used.
- overloading the default implementation of the `__eq__()` dunder method on a specific object to customize comparison behavior.
- `set operations`
- performance considerations

## Concepts

- Memory and performance characteristics and optimizations
- `throw(type, value=None, traceback=None)`
- `close()`
- `generator expressions`
- `yield from`
- `generators` used as coroutines

## Prerequisites

- `conditionals`
- `dicts`
- `functions`
- `higher-order-functions`
- `lists`
- `loops`
- `iteration`
- `iterators`
- `sequences`

## Resources

- [Generators (Python official docs)](https://docs.python.org/3/howto/functional.html#generators)
- [generator (Python official docs glossary)](https://docs.python.org/3/glossary.html#term-generator)
- [The yield statement (Python official docs)](https://docs.python.org/3/reference/simple_stmts.html#the-yield-statement)
- [Yield expressions (Python official docs)](https://docs.python.org/3/reference/expressions.html#yieldexpr)
- [Iterators(Python official docs)](https://docs.python.org/3/howto/functional.html?#iterators)
- [Generator-iterator methods (Python official docs)](https://docs.python.org/3/reference/expressions.html#generator-iterator-methods)
- [How to Use Generators and yield in Python (Real Python)](https://realpython.com/introduction-to-python-generators/)
