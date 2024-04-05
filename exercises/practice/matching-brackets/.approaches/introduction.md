# Introduction

The aim in this exercise is to determine whether opening and closing brackets are properly paired.

The brackets may be nested deeply (think Lisp code) and/or dispersed among a lot of other text (think complex LaTeX documents).

Community solutions fall into two main groups:

- Those which make a single pass through the input string, maintaining necessary context.
- Those which repeatedly make global substitutions within the text.

## Single-pass approaches

```python
def is_paired(input_string):
    bracket_map = {"]" : "[", "}": "{", ")":"("}
    tracking = []

    for element in input_string:
        if element in bracket_map.values():
            tracking.append(element)
        if element in bracket_map:
            if not tracking or (tracking.pop() != bracket_map[element]):
                return False
    return not tracking
```

The key in this approach is to maintain context by pushing open brackets onto some sort of stack, then checking if a closing bracket pairs with the top item on the stack.

See [stack-match][stack-match] approaches for details.

## Repeated-substitution approaches

```python
def is_paired(text):
    text = "".join([x for x in text if x in "()[]{}"])
    while "()" in text or "[]" in text or "{}" in text:
        text = text.replace("()","").replace("[]", "").replace("{}","")
    return not text
```

In this case, we first remove any non-bracket characters, then use a loop to repeatedly remove inner bracket pairs.

See [repeated-substitution][repeated-substitution] approaches for details.

## Other approaches

Functional languages prizing immutibility are likely to use techniques such as `foldl()` or recursive matching, as discussed on the [Scala track][scala].

This is possible in a dynamic scripting language like Python, but certainly unidiomatic and probably inefficient.

For anyone really wanting to go down that route, Python has [`functools.reduce()`][reduce] for folds and added [structural pattern matching][pattern-matching] in Python 3.10.

Recursion is not highly optimised and there is no tail recursion, but the default stack depth of 1000 should be more than enough for this problem.

## Which approach to use

For short, well-defined input strings such as those in the tests, repeated-substitution allows a passing solution in very few lines.

Stack-match is a single-pass approach which allows stream processing, scales linearly with text length and will remain performant for very large inputs.

Examining the community solutions published for this exercise, it is clear that the highest-rep Python programmers generally prefer stack-match, avoiding lots of string copying.

Thus it is interesting, and perhaps humbling, to note that repeated-substitution is *at least* as fast in benchmarking, even with large (>30 kB) input strings!

See the [performance article][article-performance] for more details.

[stack-match]: https://exercism.org/tracks/python/exercises/matching-brackets/approaches/stack-match
[repeated-substitution]: https://exercism.org/tracks/python/exercises/matching-brackets/approaches/repeated-substitution
[article-performance]:https://exercism.org/tracks/python/exercises/matching-brackets/articles/performance
[scala]: https://exercism.org/tracks/scala/exercises/matching-brackets/dig_deeper
[reduce]: https://docs.python.org/3/library/functools.html#functools.reduce
[pattern-matching]: https://docs.python.org/3/whatsnew/3.10.html#pep-634-structural-pattern-matching
