# Introduction

The aim in this exercise is to determine whether opening and closing brackets are properly paired within the input text.

These brackets may be nested deeply (think Lisp code) and/or dispersed among a lot of other text (think complex LaTeX documents).

Community solutions fall into two main groups:

1.  Those which make a single pass or loop through the input string, maintaining necessary context for matching.
2.  Those which repeatedly make global substitutions within the text for context.


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

The key in this approach is to maintain context by pushing open brackets onto some sort of stack (_in this case appending to a `list`_), then checking if there is a corresponding closing bracket to pair with the top stack item.

See [stack-match][stack-match] approaches for details.


## Repeated-substitution approaches

```python
def is_paired(text):
    text = "".join(item for item in text if item in "()[]{}")
    while "()" in text or "[]" in text or "{}" in text:
        text = text.replace("()","").replace("[]", "").replace("{}","")
    return not text
```

In this approach, we first remove any non-bracket characters, then use a loop to repeatedly remove inner bracket pairs.

See [repeated-substitution][repeated-substitution] approaches for details.


## Other approaches

Languages prizing immutibility are likely to use techniques such as `foldl()` or recursive matching, as discussed on the [Scala track][scala].

This is possible in Python, but can read as unidiomatic and will (likely) result in inefficient code if not done carefully.

For anyone wanting to go down the functional-style path, Python has [`functools.reduce()`][reduce] for folds and added [structural pattern matching][pattern-matching] in Python 3.10.

Recursion is not highly optimised in Python and there is no tail call optimization, but the default stack depth of 1000 should be more than enough for solving this problem recursively.


## Which approach to use

For short, well-defined input strings such as those currently in the test file, repeated-substitution allows a passing solution in very few lines of code.
But as input grows, this method could become less and less performant, due to the multiple passes and changes needed to determine matches.

The single-pass strategy of the stack-match approach allows for stream processing, scales linearly (_`O(n)` time complexity_) with text length, and will remain performant for very large inputs.

Examining the community solutions published for this exercise, it is clear that many programmers prefer the stack-match method which avoids the repeated string copying of the substitution approach.

Thus it is interesting and perhaps humbling to note that repeated-substitution is **_at least_** as fast in benchmarking, even with large (>30 kB) input strings!

See the [performance article][article-performance] for more details.

[article-performance]:https://exercism.org/tracks/python/exercises/matching-brackets/articles/performance
[pattern-matching]: https://docs.python.org/3/whatsnew/3.10.html#pep-634-structural-pattern-matching
[reduce]: https://docs.python.org/3/library/functools.html#functools.reduce
[repeated-substitution]: https://exercism.org/tracks/python/exercises/matching-brackets/approaches/repeated-substitution
[scala]: https://exercism.org/tracks/scala/exercises/matching-brackets/dig_deeper
[stack-match]: https://exercism.org/tracks/python/exercises/matching-brackets/approaches/stack-match
