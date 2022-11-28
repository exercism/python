# Dunder methods with `__getattribute__`

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

    foundOp = False
    for name, op in OPS.items():
        if name in question:
            question = question.replace(name, op)
            foundOp = True
    if not foundOp: raise ValueError("unknown operation")

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

This approach begins by defining a [dictionary][dictionaries] of the word keys with their related [dunder][dunder] methods.

```exercism/note
They are called "dunder" methods because they have **d**ouble **under**scores at the beginning and end of the method name.
They are also called magic methods.
```

Since only whole numbers are involved, the dunder methods are those for [`int`][int].
The supported methods for `int` can be found by using `print(dir(int))`.
The built-in [`dir`][dir] function returns a list of valid attributes for an object.

Python doesn't _enforce_ having real constant values,
but the `OPS` dictionary is defined with all uppercase letters, which is the naming convention for a Python [constant][const].
It indicates that the value is not intended to be changed.

The input question to the `answer` function is cleaned using the [`removeprefix`][removeprefix], [`removesuffix`][removesuffix], and [`strip`][strip] methods.
If the input has no characters left, it uses the [falsiness][falsiness] of an empty string with the [`not`][not] operator to return the [`ValueError`][value-error].

Next, the [`isdigit`][isdigit] method is used to see if all of the remaining characters in the input are digits.
If so, it uses the [`int()`][int-constructor] constructor to return the string as an integer.

Next, the elements in the `OPS` dictionary are iterated.
If the key name is in the input, then the [`replace()`][replace] method is used to replace the name in the input with the dunder method value.
If none of the key names are found in the input, then a `ValueError` is returned for having an unknown operation.

At this point the input question is [`split()`][split] into a list of its separate words, which is then iterated.

The dunder methods can be called by using the [`__getattribute__`][getattribute] method for [`int`][int].

[dictionaries]: https://docs.python.org/3/tutorial/datastructures.html#dictionaries
[dunder]: https://www.tutorialsteacher.com/python/magic-methods-in-python
[int]: https://docs.python.org/3/library/stdtypes.html#typesnumeric
[dir]: https://docs.python.org/3/library/functions.html?#dir
[const]: https://realpython.com/python-constants/
[removeprefix]: https://docs.python.org/3/library/stdtypes.html#str.removeprefix
[removesuffix]: https://docs.python.org/3/library/stdtypes.html#str.removesuffix
[strip]: https://docs.python.org/3/library/stdtypes.html#str.strip
[not]: https://docs.python.org/3/library/operator.html?#operator.__not__
[falsiness]: https://www.pythontutorial.net/python-basics/python-boolean/
[value-error]: https://docs.python.org/3/library/exceptions.html?#ValueError
[isdigit]: https://docs.python.org/3/library/stdtypes.html?#str.isdigit
[int-constructor]: https://docs.python.org/3/library/functions.html?#int
[replace]: https://docs.python.org/3/library/stdtypes.html?#str.replace
[split]: https://docs.python.org/3/library/stdtypes.html?#str.split

[getattribute]: https://docs.python.org/3/reference/datamodel.html?#object.__getattribute__

