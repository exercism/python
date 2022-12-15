# Introduction

There are various ways to solve Wordy.
Using [`eval`][eval] is a [convenient but potentially dangerous][eval-danger] approach.
Another approach could replace the operation words with [dunder][dunder] methods.

```exercism/note
They are called "dunder" methods because they have **d**ouble **under**scores at the beginning and end of the method name.
They are also called magic methods.
```

The dunder methods can be called by using the [`__getattribute__`][getattribute] method for [`int`][int].

## General guidance

Parsing should verify that the expression in words can be translated to a valid mathematical expression.

## Approach: Dunder methods with `__getattribute__`

```python
OPS = {
    "plus": "__add__",
    "minus": "__sub__",
    "multiplied by": "__mul__",
    "divided by": "__truediv__"
}


def answer(question):
    question = question.removeprefix("What is").removesuffix("?").strip()
    if not question: raise ValueError("syntax error")
    if question.isdigit(): return int(question)

    found_op = False
    for name, op in OPS.items():
        if name in question:
            question = question.replace(name, op)
            found_op = True
    if not found_op: raise ValueError("unknown operation")

    ret = question.split()
    while len(ret) > 1:
        try:
            x, op, y, *tail = ret
            if op not in OPS.values(): raise ValueError("syntax error")
            ret = [int(x).__getattribute__(op)(int(y)), *tail]
        except:
            raise ValueError("syntax error")
    return ret[0]

```

For more information, check the [dunder method with `__getattribute__` approach][approach-dunder-getattribute].

[eval]: https://docs.python.org/3/library/functions.html?#eval
[eval-danger]: https://diveintopython3.net/advanced-iterators.html#eval
[dunder]: https://www.tutorialsteacher.com/python/magic-methods-in-python
[getattribute]: https://docs.python.org/3/reference/datamodel.html?#object.__getattribute__
[int]: https://docs.python.org/3/library/stdtypes.html#typesnumeric
[approach-dunder-getattribute]: https://exercism.org/tracks/python/exercises/wordy/approaches/dunder-getattribute
