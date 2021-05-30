# Design


## Goal

The goal of this exercise is to teach the student what is a `conditional` and how they are used in Python.

## Learning objectives

- learn some general things about `control flow` in python
- create a `conditional` structure to choose something, take a decision
- use an `if...else` structure
- use an `if..elif...else` structure

## Out of scope

- `ternary expressions`

## Concepts

- `conditionals`
- `if`
- `elif`
- `else`

## Prerequisites

- `basics`
- `bools`
- `comparisons`

## Resources to refer to

- [if statement][if statement]
- [control flow tools][control flow tools]
- [Real Python : Conditional Statements in Python][conditional statements in python]

## Hints

For more information on writing hints see [hints](https://github.com/exercism/docs/blob/main/anatomy/tracks/concept-exercises.md#file-docshintsmd)

  * You can refer to one or more of the resources linked , or analogous resources from a trusted source.  We prefer using links within the  [Python Docs](https://docs.python.org/3/) as the primary go-to, but other resources listed above are also good.  Please try to avoid paid or subscription-based links if possible.

* ### `links.json`

  For more information, see [concept links file](https://github.com/exercism/docs/blob/main/anatomy/tracks/concepts.md#file-linksjson)

  -  The same resources listed can be used as a starting point for the [ `concepts/links.json`](https://github.com/exercism/docs/blob/main/anatomy/tracks/concepts.md#file-linksjson)  file, if it doesn't already exist.
  -  If there are particularly good/interesting information sources for this concept that extend or supplement the concept exercise material & the resources already listed -- please add them to the `links.json` document.

## Representer

No changes needed

## Analyzer

No changes needed at this time.

## Implementing

- Code in the `.meta/examplar.py` file should **only use syntax & concepts introduced in this exercise or one of its prerequisite exercises.**

- Please **do not use** comprehensions, generator expressions, or other syntax not previously covered.  Please also follow [PEP8](https://www.python.org/dev/peps/pep-0008/) guidelines.

- In General, tests should be written using `unittest.TestCase` and the test file should be named `<EXERCISE-NAME>_test.py` or `<CONCEPT-SLUG>_test.py`.


- While we do use [PyTest](https://docs.pytest.org/en/stable/) as our test runner and for some implementation tests, please check with a maintainer before using  a PyTest test method, fixture,  or feature.

- Our markdown and JSON files are checked against [prettier](https://prettier.io/) .  We recommend [setting prettier up locally](https://prettier.io/docs/en/install.html) and running it prior to submitting your PR  to avoid any CI errors.

## Edits

edited for updated naming by @yawpitch
edited for prerequisites and learning objectives detail by @BethanyG

[if statement]: https://docs.python.org/3/reference/compound_stmts.html#the-if-statement
[control flow tools]: https://docs.python.org/3/tutorial/controlflow.html#more-control-flow-tools
[conditional statements in python]: https://realpython.com/python-conditional-statements/
