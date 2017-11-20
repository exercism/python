# Dot Dsl

Write a Domain Specific Language similar to the Graphviz dot language.

A [Domain Specific Language
(DSL)](https://en.wikipedia.org/wiki/Domain-specific_language) is a
small language optimized for a specific domain.

For example the dot language of [Graphviz](http://graphviz.org) allows
you to write a textual description of a graph which is then transformed
into a picture by one of the graphviz tools (such as `dot`). A simple
graph looks like this:

    graph {
        graph [bgcolor="yellow"]
        a [color="red"]
        b [color="blue"]
        a -- b [color="green"]
    }

Putting this in a file `example.dot` and running `dot example.dot -T png
-o example.png` creates an image `example.png` with red and blue circle
connected by a green line on a yellow background.

Create a DSL similar to the dot language.

## Description of DSL

A graph, in this DSL, is an object of type `Graph`, taking a list of one 
or more

+ attributes
+ nodes
+ edges

described as tuples.

The implementations of `Node` and `Edge` provided in `dot_dsl.py`.

Observe the test cases in `dot_dsl_test.py` to understand the DSL's design.

## Submitting Exercises

Note that, when trying to submit an exercise, make sure the solution is in the `exercism/python/<exerciseName>` directory.

For example, if you're submitting `bob.py` for the Bob exercise, the submit command would be something like `exercism submit <path_to_exercism_dir>/python/bob/bob.py`.

For more detailed information about running tests, code style and linting, please see the [help page](http://exercism.io/languages/python).

## Submitting Incomplete Solutions

It's possible to submit an incomplete solution so you can see how others have completed the exercise.
