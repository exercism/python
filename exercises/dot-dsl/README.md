# DOT DSL

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


## Exception messages

Sometimes it is necessary to raise an exception. When you do this, you should include a meaningful error message to
indicate what the source of the error is. This makes your code more readable and helps significantly with debugging. Not
every exercise will require you to raise an exception, but for those that do, the tests will only pass if you include
a message.

To raise a message with an exception, just write it as an argument to the exception type. For example, instead of
`raise Exception`, you shold write:

```python
raise Exception("Meaningful message indicating the source of the error")
```

## Submitting Exercises

Note that, when trying to submit an exercise, make sure the solution is in the `$EXERCISM_WORKSPACE/python/dot-dsl` directory.

You can find your Exercism workspace by running `exercism debug` and looking for the line that starts with `Workspace`.

For more detailed information about running tests, code style and linting,
please see the [help page](http://exercism.io/languages/python).

## Submitting Incomplete Solutions
It's possible to submit an incomplete solution so you can see how others have completed the exercise.
