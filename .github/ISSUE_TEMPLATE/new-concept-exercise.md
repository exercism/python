---
name: New Concept Exercise
about: New Python V3 Concept Exercise
title: "[V3] Implement New Concept Exercise: <concept-SLUG>"
labels: 'help wanted, new exercise :sparkles:'
assignees: ''

---

This issue describes how to implement the `<concept-SLUG>` concept exercise for the python track.



## Getting started

**Please please please read the docs before starting.** Posting PRs without reading these docs will be a lot more frustrating for you during the review cycle, and exhaust Exercism's maintainers' time. So, before diving into the implementation, please read up on the following documents:

- [The features of v3](https://github.com/exercism/docs/tree/main/product)
- [The Anatomy of Exercism](https://github.com/exercism/docs/tree/main/anatomy) & [The Anatomy of a Language Track](https://github.com/exercism/docs/tree/main/anatomy/tracks)
- [Concepts](https://github.com/exercism/docs/blob/main/anatomy/tracks/concepts.md) & [Concept Exercises](https://github.com/exercism/docs/blob/main/anatomy/tracks/concept-exercises.md)



Watching the following video is also helpful. It is a bit outdated, but is good for describing the general process:

- [The Anatomy of a Concept Exercise](https://www.youtube.com/watch?v=gkbBqd7hPrA).



## Goal

This concept exercise is meant to teach an understanding/use of`<concept-SLUG>`.  

[Add additional detail here as needed]



## Learning objectives

[Please list the learning objectives of this concept exercise here.  See the below list for an example.]



-----**example** please replace with this exericses' learning objectives. --------

- understanding (_and using the concept_) that the `==` operator calls the dunder method `__eq__()` on a specific object, and uses that object's implementation for comparison.  Where no implementation is present, the default `__eq__()` from _generic_ `object` is used.
- the same applies for operators `<`, `<=`, `!=`, `>=`, `>` and correspondents dunder methods `__lt__`, `__le__`, `__ne__`, `__ge__`, `__gt__`
- overriding the default implementation of the `__eq__()` dunder method on a specific object to customize comparison behavior.
- overriding the default implementations of the `__lt__`, `__le__`, `__ne__`, `__ge__`, `__gt__` dunder methods on a specific object to customize comparison behavior.
- return the singleton `NotImplemented` if the called operation is not implemented  

---------------.--------------------------------------------------------------------------------



##Out of scope

[Please list the concept considerations that will NOT be covered, and are out of scope.  See the below list for an example.]



-----**example** please replace with this exercises' out of scope list. --------

- performance considerations

---------------.--------------------------------------------------------------------------------



## Concepts

[Please list the concepts/methods that will  be included in the exercise.  See the below list for an example.]



-----**example** please replace with this exercises' concepts list. --------

- `__eq__`, `__lt__`, `__le__`, `__ne__`, `__ge__`, `__gt__` dunder methods
- comparison behavior customization
- dunder methods override

---------------.--------------------------------------------------------------------------------



## Prerequisites

[Please list the concepts the student needs to complete/understand before solving this exercise.  See the below list for an example.]



-----**example** please replace with this exercises' prerequisites list. --------

- Method overriding
- Comparison priority in Python
- Comparison operators`==`, `>`, `<`, `!=`
- Identity methods `is` and `is not`
- Use the _value comparison operators_ `==`, `>`, `<`, `!=` with _numeric types_
- Use the _value comparison operators_ `==`, `>`, `<`, `!=` with _non-numeric types_
- `basics`
- `booleans`
- `classes`
- `numbers`
- `sequences`
- `iteration`

---------------.--------------------------------------------------------------------------------



## Resources to refer to

[Below, list/link to resources that the exercise writer can use or consult in writing the exercise.  This list is a suggestion to get them started writing.]



*  
*  
* 



* ### Hints

  ​	For more information on writing hints see [hints](https://github.com/exercism/docs/blob/main/anatomy/tracks/concept-exercises.md#file-docshintsmd) 

  * You can refer to one or more of the resources linked above, or analogous resources from a trusted source.  We prefer using links within the  [Python Docs](https://docs.python.org/3/) as the primary go-to, but other resources listed above are also good.

    

* ### `links.json`

  *  The same resources can be used for the [ `concepts/links.json`](https://github.com/exercism/docs/blob/main/anatomy/tracks/concepts.md#file-linksjson)  file, if it doesn't already exist.
  *  If there are particularly good/interesting informations sources for this concept that extend or supplement the concept exercise material, please add them to this document.



## Concept Description

[Link to the concept `about.md` file in the Concept section below.  If the file still needs to be written, please link to the **GitHub issue** filed for the concept `about.md` file.]



Please see the following for more details on these files:  [concepts](https://github.com/exercism/docs/blob/main/anatomy/tracks/concepts.md#file-linksjson)

* ### Concept `about.md`

  [<concept-SLUG>]() and/or [<GitHub issue link>]()

* ### Exercise `introduction.md`

  For more information, see [Exercise `introduction.md`](https://github.com/exercism/docs/blob/main/anatomy/tracks/concept-exercises.md#file-docsintroductionmd)

​           This should summarize  the above document, with  enough information for the student to complete the tasks in the concept exercise.

* ### Concept `introduction.md`

  For more information, see [Concept `introduction.md`](https://github.com/exercism/docs/blob/main/anatomy/tracks/concepts.md#file-introductionmd)

​         This should also be a summary of the above document, and will provide a brief introduction of the concept for a student who has **not yet** completed the concept exercise.



## Representer

No changes required.



## Analyzer

No changes required.



## Exercise UUID

[please generate a UUID for this exercise for `config.json`]

one of these tools can be used, or you can use your favorite method of generating a **V4 UUID**

[exercism configlet](https://github.com/exercism/configlet)

[uuidgenerator.net](https://www.uuidgenerator.net/version4)



**Exercise UUID** : `<exercise-UUID>`



## Implementation Notes

Code in the `.meta/examplar.py` file should **only use syntax & concepts introduced in this exercise or one of its prerequisite exercises.** 
Please **do not use** comprehensions, generator expressions, or other syntax not previously covered.  Please also follow [PEP8](https://www.python.org/dev/peps/pep-0008/) guidelines.

In General, tests should be written using `unittest.TestCase` and the test file should be named `<EXERCISE-NAME>_test.py`.

While we do use [PyTest](https://docs.pytest.org/en/stable/) as our test runner and for some implementation tests, please check with a maintainer before using  a PyTest test method, fixture,  or feature.

Our markdown and JSON files are checked against [prettier](https://prettier.io/) .  We recommend [setting prettier up locally](https://prettier.io/docs/en/install.html) and running it prior to submitting your PR  to avoid any CI errors.  



## Help

If you have any questions while implementing the exercise, please post the questions as comments in this issue, or contact one of the maintainers on our Slack channel.
