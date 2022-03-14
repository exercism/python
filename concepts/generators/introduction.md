# Introduction

A generator in Python is a _callable function_ that returns a [lazy iterator](https://en.wikipedia.org/wiki/Lazy_evaluation).

_Lazy iterators_ are similar to `lists`, and other `iterators`, but with one key difference: They do not store their `values` in memory, but _generate_ their values when needed.
