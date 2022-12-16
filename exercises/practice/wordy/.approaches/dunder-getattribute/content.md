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

This approach begins by defining a [dictionary][dictionaries] of the word keys with their related [dunder][dunder] methods.

```exercism/note
They are called "dunder" methods because they have **d**ouble **under**scores at the beginning and end of the method name.
They are also called magic methods.
```

Since only whole numbers are involved, the dunder methods are those for [`int`][int].
The supported methods for `int` can be found by using `print(dir(int))`.

```exercism/note
The built-in [`dir`](https://docs.python.org/3/library/functions.html?#dir) function returns a list of valid attributes for an object.
```

Python doesn't _enforce_ having real constant values,
but the `OPS` dictionary is defined with all uppercase letters, which is the naming convention for a Python [constant][const].
It indicates that the value is not intended to be changed.

The input question to the `answer` function is cleaned using the [`removeprefix`][removeprefix], [`removesuffix`][removesuffix], and [`strip`][strip] methods.
The method calls are [chained][method-chaining], so that the output from one call is the input for the next call.
If the input has no characters left,
it uses the [falsiness][falsiness] of an empty string with the [`not`][not] operator to return the [`ValueError`][value-error] for having a syntax error.

Next, the [`isdigit`][isdigit] method is used to see if all of the remaining characters in the input are digits.
If so, it uses the [`int()`][int-constructor] constructor to return the string as an integer.

Next, the elements in the `OPS` dictionary are iterated.
If the key name is in the input, then the [`replace()`][replace] method is used to replace the name in the input with the dunder method value.
If none of the key names are found in the input, then a `ValueError` is returned for having an unknown operation.

At this point the input question is [`split()`][split] into a list of its words, which is then iterated while its [`len()`][len] is greater than 1.

Within a [try][exception-handling], the list is [destructured][destructure] into `x, op, y, *tail`.
If `op` is not in the supported dunder methods, it raises `ValueError("syntax error")`.
If there are any other exceptions raised in the try, `except` raises `ValueError("syntax error")`

Next, it converts `x` to an `int` and calls the [`__getattribute__`][getattribute] for its dunder method and calls it,
passing it `y` converted to an `int`.

It sets the list to the result of the dunder method plus the remaining elements in `*tail`.

```exercism/note
The `*` prefix in `*tail` [unpacks](https://treyhunner.com/2018/10/asterisks-in-python-what-they-are-and-how-to-use-them/) the `tail` list back into its elements.
This concept is also a part of [unpacking-and-multiple-assignment](https://exercism.org/tracks/python/concepts/unpacking-and-multiple-assignment) concept in the syllabus.
```

When the loop exhausts, the first element of the list is selected as the function return value.

[dictionaries]: https://docs.python.org/3/tutorial/datastructures.html#dictionaries
[dunder]: https://www.tutorialsteacher.com/python/magic-methods-in-python
[int]: https://docs.python.org/3/library/stdtypes.html#typesnumeric
[const]: https://realpython.com/python-constants/
[removeprefix]: https://docs.python.org/3/library/stdtypes.html#str.removeprefix
[removesuffix]: https://docs.python.org/3/library/stdtypes.html#str.removesuffix
[strip]: https://docs.python.org/3/library/stdtypes.html#str.strip
[method-chaining]: https://www.tutorialspoint.com/Explain-Python-class-method-chaining
[not]: https://docs.python.org/3/library/operator.html?#operator.__not__
[falsiness]: https://www.pythontutorial.net/python-basics/python-boolean/
[value-error]: https://docs.python.org/3/library/exceptions.html?#ValueError
[isdigit]: https://docs.python.org/3/library/stdtypes.html?#str.isdigit
[int-constructor]: https://docs.python.org/3/library/functions.html?#int
[replace]: https://docs.python.org/3/library/stdtypes.html?#str.replace
[split]: https://docs.python.org/3/library/stdtypes.html?#str.split
[len]: https://docs.python.org/3/library/functions.html?#len
[exception-handling]: https://docs.python.org/3/tutorial/errors.html#handling-exceptions
[destructure]: https://riptutorial.com/python/example/14981/destructuring-assignment
[getattribute]: https://docs.python.org/3/reference/datamodel.html?#object.__getattribute__
