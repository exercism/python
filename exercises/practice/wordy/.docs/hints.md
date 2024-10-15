# Hints

## General

-  This challenge is all about validating, "cleaning up", and processing the given question in the **_correct order_**.
-  If you read the directions and tests carefully, you will find there are three conditions that need to be met for a question to be "valid".
If a question is not valid, you will need to [raise ][raise-statement] a [ValueError][value-error] with a message (_`ValueError("unknown operation")`_).
   It is best if you get this particular check out of the way before doing anything else.
-  Processing a question before calculating the answer is all about utilizing [string methods][str-methods].
A few popular ones to investigate include `str.removeprefix`, `str.removesuffix`, `str.replace`, and `str.strip`.
Others you might want to check out are `str.startswith`, `str.endswith`, and `in` (_which can apply to more than just strings_).

-  It is possible to iterate over a string.  However, it is **much** easier to iterate over a list of _words_ if the string you are processing is a sentence or fragment with spaces.  [`str.split`][split]  can break apart a string and return a list of "words".
-  A [`while-loop`][while-loop] is very useful for iterating over the question to process items.
-  For fewer error checks and cleaner error-handling, a [`try-except`][handling-exceptions] is recommended as you process the question.
-  **Remember**: the question is processed **_left-to-right_**.  That means "1 plus 12 minus 3 multiplied by 4" gets processed by:
   -  Calculating "1 plus 12" (13),
   -  Calculating "13 minus 3" (10),
   -  Calculating "10 multiplied by 4" (40).
   -  The result of the first calculation is _concatenated with the remainder of the question to form a new question for the next step_.
       -  This technique is sometimes called [the accumulator pattern][accumulator-pattern], or [fold][fold] / [foldl][foldl] in functional programming languages like [Haskell][haskell-folds] or Lisp.
       -  Python includes two methods that are purpose-built to apply the `accumulator-pattern` to iterable data structures like `lists`, `tuples`, and `strings`.
               [`functools.reduce`][reduce] and [`itertools.accumulate`][accumulate] could be interesting to investigate here.

-  This exercise has many potential solutions and many paths you can take along the way.
   No path is manifestly "better" than another, although a particular path may be more interesting or better suited to what you want to learn or explore right now.


[accumulate]: https://docs.python.org/3/library/itertools.html#itertools.accumulate
[accumulator-pattern]: https://muzny.github.io/csci1200-notes/08/2/accumulator.html
[fold]: https://en.wikipedia.org/wiki/Fold_(higher-order_function)
[foldl]: https://slim.computer/eecs-111-ta-guide/material/higher-order/Fold.html
[handling-exceptions]: https://docs.python.org/3.11/tutorial/errors.html#handling-exceptions
[haskell-folds]: https://www.ashwinnarayan.com/post/a-study-on-haskell-folds/
[raise-statement]: https://docs.python.org/3/reference/simple_stmts.html#the-raise-statement
[reduce]: https://docs.python.org/3/library/functools.html#functools.reduce
[split]: https://docs.python.org/3.9/library/stdtypes.html#str.split
[str-methods]: https://docs.python.org/3/library/stdtypes.html#string-methods
[value-error]: https://docs.python.org/3.11/library/exceptions.html#ValueError
[while-loop]: https://python-practice.com/learn/loops/while_loop/
