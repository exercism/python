# How to implement a Python concept exercise

This document describes the steps required to implement a concept exercise for the Python track.

**Please please please read the docs before starting.** Posting PRs without reading these docs will be a lot more frustrating for you during the review cycle, and exhaust Exercism's maintainers' time. So, before diving into the implementation, please read the following documents:

- [The features of v3][docs-features-of-v3].
- [Rationale for v3][docs-rationale-for-v3].
- [What are concept exercise and how they are structured?][docs-concept-exercises]

Please also watch the following video:

- [The Anatomy of a Concept Exercise][anatomy-of-a-concept-exercise].

As this document is generic, the following placeholders are used:

- `<SLUG>`: the slug of the exercise in kebab-case (e.g. `calculator-conundrum`).
- `<NAME>`: the name of the exercise in snake_case (e.g. `calculator_conundrum`).
- `<CONCEPT_SLUG>`: the slug of one of the exercise's concepts in kebab-case (e.g. `anonymous-methods`).

Before implementing the exercise, please make sure you have a good understanding of what the exercise should be teaching (and what not). This information can be found in the exercise's GitHub issue.

To implement a concept exercise, the following files need to be added:

```
languages
└── python
    ├── concepts
    |   └── &lt;CONCEPT_SLUG&gt;
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
                |   └── example.py
                ├── <NAME>.py
                └── <NAME>_test.py
        └── practice
            └── <SLUG>
                ├── .docs
                |   ├── instructions.md
                |   ├── introduction.md
                |   └── hints.md
                ├── .meta
                |   ├── config.json
                |   └── example.py
                ├── <NAME>.py
                └── <NAME>_test.py

```

## Step 1: Add code files

These are files specific to the Python track:

- `src/<NAME>.py`: the stub implementation file, which is the starting point for students to work on the exercise.
- `test/<NAME>_test.py`: the test suite.
- `.meta/example.py`: an example implementation that passes all the tests.

## Step 2: Add documentation files

How to create the files common to all tracks is described in the [how to implement a concept exercise document][how-to-implement-a-concept-exercise].

## Inspiration

When implementing an exercise, it can be very useful to look at already implemented Python exercises. You can also check the exercise's [general concepts documents][reference] to see if other languages have already implemented an exercise for that concept.

[reference]: ../../../reference
[how-to-implement-a-concept-exercise]: ../../../docs/maintainers/generic-how-to-implement-a-concept-exercise.md
[docs-concept-exercises]: ../../../docs/concept-exercises.md
[docs-rationale-for-v3]: ../../../docs/rationale-for-v3.md
[docs-features-of-v3]: ../../../docs/features-of-v3.md
[anatomy-of-a-concept-exercise]: https://www.youtube.com/watch?v=gkbBqd7hPrA
