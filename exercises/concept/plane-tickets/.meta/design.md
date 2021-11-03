This issue describes how to implement the `generators` concept exercise for the Python track.

## Goal

The goal of this exercise is to teach the syntax and use of `generators` in Python. 

## Learning objectives

-  Understand what generators are and how/when to use them
-  Understand how generators relate to `loops` and `iterators`
-  Understand how to use the `yield` keyword
-  Understand the `__next__()` method
-  Create a generator


## Out of scope

- Memory and performance characteristics and optimizations
- `throw(type, value=None, traceback=None)`
- `close()`
- `generator expressions`
- `yield from`
- `generators` used as coroutines


## Concepts covered

-  `generators`
-  `yield`
-   `__next__()`
-  `iterators`


## Prerequisites

-  `conditionals`
-  `dicts`
-  `functions`
-  `higher-order-functions`
-  `lists`
-  `loops`
-  `iteration`
-  `iterators`
-  `sequences`



## Resources to refer to

-  [Generators (Python official docs)](https://docs.python.org/3/howto/functional.html#generators)
- [generator (Python official docs glossary)](https://docs.python.org/3/glossary.html#term-generator)
- [The yield statement (Python official docs)](https://docs.python.org/3/reference/simple_stmts.html#the-yield-statement)
- [Yield expressions (Python official docs)](https://docs.python.org/3/reference/expressions.html#yieldexpr)
- [Iterators(Python official docs)](https://docs.python.org/3/howto/functional.html?#iterators)
- [Generator-iterator methods (Python official docs)](https://docs.python.org/3/reference/expressions.html#generator-iterator-methods)
- [How to Use Generators and yield in Python (Real Python)](https://realpython.com/introduction-to-python-generators/)

### Hints

-  Referring to one or more of the resources linked above, or analogous resources from a trusted source.
- `Generators` section of the Python Docs Functional How to tutorial:  [Generators](https://docs.python.org/3/howto/functional.html#generators)


## Concept Description 

(_a variant of this can be used for the `v3/languages/python/concepts/<concept>/about.md` doc and this exercises  `introduction.md` doc._)

_**Concept Description Needs to Be Filled In Here/Written**_

_Some "extras" that we might want to include as notes in the concept description, or as links in `links.json`:_

-  Additional `Generator-iterator methods`, such as `generator.send()` and `generator.throw()`
- `generator expressions`
-  Asynchronous generator functions
- `generators` used as coroutines

## Implementing

The general Python track concept exercise implantation guide can be found [here](https://github.com/exercism/v3/blob/master/languages/python/reference/implementing-a-concept-exercise.md).

Tests should be written using `unittest.TestCase` and the test file named `generators_test.py`.

Code in the `.meta/example.py` file should **only use syntax & concepts introduced in this exercise or one of its prerequisites.** Please do not use comprehensions, generator expressions, or other syntax not previously covered.  Please also follow [PEP8](https://www.python.org/dev/peps/pep-0008/) guidelines.

## Help

If you have any questions while implementing the exercise, please post the questions as comments in this issue, or contact one of the maintainers on our Slack channel.


