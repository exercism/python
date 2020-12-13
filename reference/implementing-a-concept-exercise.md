# How to implement a Python concept exercise

This document describes the steps required to implement a concept exercise for the Python track.

**Please please please read the docs before starting.** Posting PRs without reading these docs will be a lot more frustrating for you during the review cycle, and exhaust Exercism's maintainers' time. So, before diving into the implementation, please read the following documents:

- [The features of v3][docs-features-of-v3].
- [Rationale for v3][docs-rationale-for-v3].
- [What are concept exercise and how they are structured?][docs-concept-exercises]

Please also watch the following video:

- [The Anatomy of a Concept Exercise][anatomy-of-a-concept-exercise].

As this document is generic, the following placeholders are used:

- `<SLUG>`: the slug of the exercise _story title_ in kebab-case (e.g. `calculator-conundrum`).
- `<CONCEPT_NAME>`: the name of the exercise's _concept_ in snake_case (e.g. `anonymous_functions`).
- `<CONCEPT-SLUG>`: the slug of an exercise's _concept_ in kebab-case (e.g. `anonymous-functions`).

Before implementing the exercise, please make sure you have a good understanding of what the exercise should be teaching (and what should not be taught). This information can be found in the exercise's [GitHub issue][github-issues-python], under the `Learning Objectives` and `Out of Scope` sections.

We suggest using a git branch titled after the concept you are writing the exercise for. Please use `[Python]` in the title of your PR, so that it can be easily filtered and note the GitHub issue number in the PR message.

To implement a concept exercise, the following files under `python/concepts` and `python/exercises` will need to be created:

```
languages
└── python
    ├── concepts
    |   └── <CONCEPT-SLUG>
    |       ├── about.md
    |       └── links.json
    └── exercises
        └── concept
            └── <SLUG>
                ├── .docs
                |   ├── instructions.md
                |   ├── introduction.md
                |   └── hints.md
                ├── .meta
                |   ├── config.json
                |   ├── design.md
                |   └── example.py
                ├── <CONCEPT_NAME>.py
                └── <CONCEPT_NAME>_test.py

```

## Step 1: Add `.py` code files

These are files specific to the Python track, and can be added in any order:

- `<SLUG>/<CONCEPT_NAME>.py`
  The stub implementation file, which will be the starting point for students to work on the exercise ([example stub file][example-stub]). Please use `pass` as necessary, and descriptive TODO comments for clarification if the student needs to define a class/function/constant themselves ([example TODO][example-todo]).

- `<SLUG>/<CONCEPT_NAME>_test.py`
  The test suite a submitted solution will be tested against. Tests should be written using [`unittest.TestCase`][unittest] ([example test file][example-testfile]). We do use PyTest as our test runner, but please check with a maintainer before using any PyTest-specific methods.

- `.meta/example.py`
  An idiomatic implementation that passes all the provided tests. This solution file should only use **syntax & concepts introduced in the concept exercise itself, or one of its prerequisites.**. This means avoiding the use of `classes`, `comprehensions`, `generators`, `slice assignment`, `regex`, `filter/map/reduce`, standard library modules (_like `datetime`_), or 3rd-party libraries unless the exercise has introduced these concepts or they appear in the exercise's prerequisite tree. Please follow the [PEP8][pep8] formatting guidelines. Additionally, we'd like you to avoid any single-letter or cryptic variable names.

## Step 2: Add exercise documentation files

How to create the files common to all tracks is described in the [how to implement a concept exercise document][how-to-implement-a-concept-exercise]. All of these files are written in [Markdown][commonmark], and you can find the [Exercism Formatting and Style Guide][style-guide] here. Please pay close attention to the [auto-formatting][auto-formatting] section, to avoid CI test failures.

As a reminder, code elements (functions, keywords, operators) should be wrapped in backticks:

```python
A `set` is an unordered collection of distinct hashable objects. To add something to a `set`, use `set.add()`
```

Which will render:

A `set` is an unordered collection of distinct hashable objects. To add something to a `set`, use `set.add()`

Unless your code is intended to represent a `.py` file, please format longer in-text code examples for the Python REPL -- in the same way the [Python Docs][repl-code-example] do:

```python
# Elements given to the constructor are iterated through and added to the tuple in order.
>>> multiple_elements_string = tuple("Timbuktu")
('T', 'i', 'm', 'b', 'u', 'k', 't', 'u')

>>> multiple_elements = tuple(("Parrot", "Bird", 334782))
("Parrot", "Bird", 334782)

# Iterating through a tuple with a for loop.
>>> for item in multiple_elements_string:
...   print(item)
...
T
i
m
b
u
k
t
u
```

For resource links, we strongly favor linking into relevant parts of the [Python docs][python-docs] as a first source, with other useful and interesting links as a follow-on. Please avoid any paywalled, subscription-based or signup-required links.

## Inspiration

When implementing an exercise, it can be very useful to look at already [implemented Python exercises][python-implementations]. Browsing through concept exercise stories [here][concept-exercise-stories] can also help "jump-start" concept exercise writing. And you can also check the cross-track [general concepts directory][reference] to see if other language tracks have already implemented an exercise for a particular concept. If you adapt a story or exercise, please make sure to include a credit in your exercise `.meta/config.json` file `"forked_from" field:

```json
{
  "authors": [
    {
      "github_username": "aldraco",
      "exercism_username": "aldraco"
    }
  ],
  "editor": {
    "solution_files": ["strings.py"],
    "test_files": ["strings_test.py"]
  },
  "forked_from": ["csharp/strings"]
}
```

## Help

If you have any questions regarding implementing the exercise, please post them as comments in the exercise's GitHub issue, or in the exercism Slack channel.

[reference]: ../../../reference
[how-to-implement-a-concept-exercise]: ../../../docs/maintainers/generic-how-to-implement-a-concept-exercise.md
[docs-concept-exercises]: ../../../docs/concept-exercises.md
[docs-rationale-for-v3]: ../../../docs/rationale-for-v3.md
[docs-features-of-v3]: ../../../docs/features-of-v3.md
[anatomy-of-a-concept-exercise]: https://www.youtube.com/watch?v=gkbBqd7hPrA
[pep8]: https://www.python.org/dev/peps/pep-0008/
[example-todo]: ../exercises/concept/guidos-gorgeous-lasagna/lasagna.py
[example-stub]: ../exercises/concept/ghost-gobble-arcade-game/arcade_game.py
[example-testfile]: ../exercises/concept/little-sisters-essay/string_methods_test.py
[repl-code-example]: https://docs.python.org/3/tutorial/controlflow.html#defining-functions
[commonmark]: https://spec.commonmark.org/
[auto-formatting]: https://github.com/exercism/v3/blob/master/docs/maintainers/style-guide.md#auto-formatting
[style-guide]: https://github.com/exercism/v3/blob/master/docs/maintainers/style-guide.md
[python-implementations]: https://github.com/exercism/v3/tree/master/languages/python/exercises
[concept-exercise-stories]: https://github.com/exercism/v3/tree/master/reference/stories
[github-issues-python]: https://github.com/exercism/v3/issues?q=is%3Aissue+is%3Aopen+%5BPython%5D+in%3Atitle+label%3Atype%2Fnew-exercise
[python-docs]: https://docs.python.org/3/
[unittest]: https://docs.python.org/3/library/unittest.html#unittest.TestCase
