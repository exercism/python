# Design

## Goal

This concept exercise is meant to teach an understanding/creation/use of `lambda` or `anonymous functions` in python. 

## Learning objectives

- Understand what an `anonymous function` is, and how to create one
  - The syntax of creating a `lambda` 
  - Using different `function argument` flavors with `lambda`
- Understand the differences between `lambdas` and Pythons "regular" `functions`
- Understand what problems are solved by using a `lambda`
- The pitfalls of `lambdas`, and when to avoid them
- Using `lambdas` as `key functions` in other situations such as `sort()` , `sorted()`, `min()`, and `max()`
- Applying arguments to a `lambda` via IIFE (_immediately invoked function expression_)
- Anti-patterns when using `lambdas` 
 
## Out of scope

- `comprehensions`
- `comprehensions` in `lambdas`
- using a `decorator` on a `lambda`
- `functools` (_this will get its own exercise_)
- `generators`
- `map()`, `filter()`, and `reduce()` (_these will get their own exercise_)
- using an `assignment expression` or "walrus" operator (`:=`) in a `lambda`

## Concepts

- `anonymous-functions`
- `lambdas`
- `functions`, 
- `higher-order functions`
- `functions as arguments`
- `functions as returns`
- `nested funcitons`

## Prerequisites

These are the concepts/concept exercises the student needs to complete/understand before solving this concept exercise. 

- `basics`
- `booleans`
- `comparisons`
- `dicts`
- `dict-methods`
- `functions`
- `function-arguments`
- `higher-order functions`
- `iteration`
- `lists`
- `list-methods`
- `numbers`
- `sequences`
- `sets`
- `strings`
- `string-methods`
- `tuples`

## Resources to refer to

- [Python Docs: Defining Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [Python Docs Tutorial: Lambda Expressions](https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions)
- [Functions as Objects in Python](https://medium.com/python-pandemonium/function-as-objects-in-python-d5215e6d1b0d)
- [Composing Programs: Higher-Order Functions](https://composingprograms.com/pages/16-higher-order-functions.html)
- [Learn by Example: Python Lambda Function](https://www.learnbyexample.org/python-lambda-function/)
- [Real Python: How to Use Python Lambda Fuctions](https://realpython.com/python-lambda/)
- [Trey Hunner: Overusing Lambda expressions in Python](https://treyhunner.com/2018/09/stop-writing-lambda-expressions/)
 
* ### Hints

 For more information on writing hints see [hints](https://github.com/exercism/docs/blob/main/building/tracks/concept-exercises.md#file-docshintsmd)

 * You can refer to one or more of the resources linked above, or analogous resources from a trusted source. We prefer using links within the [Python Docs](https://docs.python.org/3/) as the primary go-to, but other resources listed above are also good. Please try to avoid paid or subscription-based links if possible.

* ### `links.json`

 For more information, see [concept links file](https://github.com/exercism/docs/blob/main/building/tracks/concepts.md#file-linksjson)

 * The same resources listed in this issue can be used as a starting point for the [ `concepts/links.json`](https://github.com/exercism/docs/blob/main/anatomy/tracks/concepts.md#file-linksjson) file, if it doesn\'t already exist.
 * If there are particularly good/interesting information sources for this concept that extend or supplement the concept exercise material & the resources already listed -- please add them to the `links.json` document.

## Concept Description

Please see the following for more details on these files: [concepts](https://exercism.org/docs/building/tracks/concepts) & [concept exercises](https://exercism.org/docs/building/tracks/concept-exercises)

* ### Concept `about.md`

 **Concept file/issue**: [anonymous-functions directory with stubbed files](https://github.com/exercism/python/tree/main/concepts/anonymous-functions) -- **Content is TBD** and should be completed as part of this exercise creation. `Anonymous-functions` concept write-ups and associated files can be included in the PR for this issue, or as a separate PR linked to this issue.

  For more information, see [Concept `about.md`](https://github.com/exercism/docs/blob/main/building/tracks/concepts.md#file-aboutmd)
 
   - This file provides information about this concept for a student who has completed the corresponding concept exercise. It is intended as a reference for continued learning. 

* ### Concept `introduction.md`

 For more information, see [Concept `introduction.md`](https://github.com/exercism/docs/blob/main/building/tracks/concepts.md#file-introductionmd)

 * This can also be a summary/paraphrase of the document listed above, and will provide a brief introduction of the concept for a student who has **not yet** completed the concept exercise.  It should contain a good summation of the concept, but not go into lots of detail.

* ### Exercise `introduction.md`

 For more information, see [**Exercise** `introduction.md`](https://github.com/exercism/docs/blob/main/building/tracks/concept-exercises.md#file-docsintroductionmd)

 - This should also summarize/paraphrase the above document, but with enough information and examples for the student to complete the tasks outlined in this concept exercise.

## Test-runner

No changes required to the [Python Test Runner](https://github.com/exercism/python-test-runner) at this time. 

## Representer

No changes required to the [Python Representer](https://github.com/exercism/python-representer/) at this time. 

## Analyzer

No changes required to the [Python Analyzer](https://github.com/exercism/python-analyzer/) at this time. 

## Exercise Metadata - Track

For more information on concept exercises and formatting for the Python track `config.json`, please see [concept exercise metadata](https://github.com/exercism/docs/blob/main/building/tracks/concept-exercises.md#metadata). The track `config.json` file can be found in the [root of this `Python` repo](https://github.com/exercism/python/blob/main/config.json).

You can use the below for the exercise **UUID**. You can also generate a new one via [exercism configlet](https://github.com/exercism/configlet), [uuidgenerator.net](https://www.uuidgenerator.net/version4), or any other favorite method. The UUID must be a valid [**V4 UUID**](https://en.wikipedia.org/wiki/Universally_unique_identifier).


- **Exercise UUID** : `1e636fd3-6143-484e-a4fc-0ed6157fdfa1`
- **concepts** should be filled in from the Concepts section in this issue
- **prerequisites** should be filled in from the Prerequisites section in this issue 

## Exercise Metadata Files Under `.meta/config.json`

For more information on exercise `.meta/` files and formatting, see [concept exercise metadata files](https://github.com/exercism/docs/blob/main/building/tracks/concept-exercises.md#files)

- `.meta/config.json` - see [this link](https://github.com/exercism/docs/blob/main/building/tracks/concept-exercises.md#file-metaconfigjson) for the fields and formatting of this file.

- `.meta/design.md` - see [this link](https://github.com/exercism/docs/blob/main/building/tracks/concept-exercises.md#file-metadesignmd) for the formatting of this file. Please use the **Goal**, **Learning Objectives**,**Concepts**, **Prerequisites** and , **Out of Scope** sections from this issue.

## Implementation Notes

- Code in the `.meta/examplar.py` file should **only use syntax & concepts introduced in this exercise or one of its prerequisite exercises.** We run all our `examplar.py` files through PyLint, but do not require module docstrings. We **do** require function docstrings similar to [PEP257](https://www.python.org/dev/peps/pep-0257/). See [this concept exercise `exemplar.py`](https://github.com/exercism/python/blob/main/exercises/concept/meltdown-mitigation/.meta/exemplar.py) for an example.
- Please **do not use** comprehensions, generator expressions, or other syntax not previously covered. Please also follow [PEP8](https://www.python.org/dev/peps/pep-0008/) guidelines.
- In General, tests should be written using `unittest.TestCase` and the test file should be named `<EXERCISE-NAME>_test.py`. 

 - All asserts should contain a "user friendly" failure message (_these will display on the website_). 
 - We use a `PyTest custom mark` to link test cases to exercise task numbers. 
 - We also use `unittest.subtest` to parameterize test input where/when needed. 
  Here is an [example testfile](https://github.com/exercism/python/blob/main/exercises/concept/making-the-grade/loops_test.py) that shows all three of these in action.

- While we do use [PyTest](https://docs.pytest.org/en/stable/) as our test runner and for some implementation tests, please check with a maintainer before using a PyTest test method, fixture, or feature.
- Our markdown and JSON files are checked against [prettier](https://prettier.io/). We recommend [setting prettier up locally](https://prettier.io/docs/en/install.html) and running it prior to submitting your PR to avoid any CI errors.