# Introduction

A generator in Python is a _callable function_ or expression that returns a special type of [iterator][iterator] called [generator iterator][generator-iterator].
`Generator-iterators` are [lazy][lazy iterator]: they do not store their `values` in memory, but _generate_ their values when needed.

A generator function looks like any other function, but contains one or more [yield expressions][yield expression].
Each `yield` will suspend code execution, saving the current execution state (_including all local variables and try-statements_).
When the generator function resumes, it picks up state from the suspension - unlike regular functions which reset with every call.

[lazy iterator]: https://en.wikipedia.org/wiki/Lazy_evaluation
[iterator]: https://docs.python.org/3.11/glossary.html#term-iterator
[yield expression]: https://docs.python.org/3.11/reference/expressions.html#yield-expressions
[generator-iterator]: https://docs.python.org/3.11/glossary.html#term-generator-iterator
