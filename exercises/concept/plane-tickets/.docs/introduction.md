# Introduction

A generator in Python is a _callable function_ that returns a [lazy iterator](https://en.wikipedia.org/wiki/Lazy_evaluation).

_Lazy iterators_ are similar to iterables such as `lists`, and other types of `iterators` in Python -- but with one key difference: `generators` do not store their `values` in memory, but _generate_ their values as needed or when called.
