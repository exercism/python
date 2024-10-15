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

This approach begins by defining a [dictionary][dictionaries] of the word keys with their related [`dunder-methods`][dunder] methods.
Since only whole numbers are involved, the available `dunder-methods` are those for the [`int`][int] class/namespace.
The supported methods for the `int()` namespace can be found by using `print(dir(int))` or `print(int.__dict__)` in a Python terminal.
See [`SO: Difference between dir() and __dict__`][dir-vs-__dict__] for more details.

<br>

~~~~exercism/note
The built-in [`dir`](https://docs.python.org/3/library/functions.html?#dir) function returns a list of all valid attributes for an object.
The `dunder-method` [`<object>.__dict__`](https://docs.python.org/3/reference/datamodel.html#object.__dict__) is a mapping of an objects writable attributes.
~~~~

<br>

The `OPS` dictionary is defined with all uppercase letters, which is the naming convention for a Python [constant][const].
It indicates that the value should not be changed.

The input question to the `answer()` function is cleaned using the [`removeprefix`][removeprefix], [`removesuffix`][removesuffix], and [`strip`][strip] string methods.
The method calls are [chained][method-chaining], so that the output from one call is the input for the next call.
If the input has no characters left,
it uses the [falsiness][falsiness] of an empty string with the [`not`][not] operator to return a `ValueError("syntax error")`.

Next, the [`isdigit`][isdigit] method is used to see if the remaining characters in the input are digits.
If so, it uses the [`int()`][int-constructor] constructor to return the string as an integer.

Next, the elements in the `OPS` dictionary are iterated over.
If the key name is in the input, then the [`str.replace`][replace] method is used to replace the name in the input with the `dunder-method` value.
If none of the key names are found in the input, a `ValueError("unknown operation")` is returned.

At this point the input question is [`split()`][split] into a `list` of its words, which is then iterated over while its [`len()`][len] is greater than 1.

Within a [try-except][exception-handling] block, the list is [unpacked][unpacking] (_see also [Concept: unpacking][unpacking-and-multiple-assignment]_) into the variables `x, op, y, and *tail`.
If `op` is not in the supported `dunder-methods` dictionary, a `ValueError("syntax error")` is raised.
If there are any other exceptions raised within the `try` block, they are "caught"/ handled in the `except` clause by raising a `ValueError("syntax error")`.

Next, `x` is converted to an `int` and  [`__getattribute__`][getattribute] is called for the `dunder-method` (`op`) to apply to `x`.
`y` is then converted to an `int` and passed as the second arguemnt to `op`.

Then `ret` is redefined to a `list` containing the result of the dunder method plus the remaining elements in `*tail`.

When the loop exhausts, the first element of the list is selected as the function return value.

[const]: https://realpython.com/python-constants/
[dictionaries]: https://docs.python.org/3/tutorial/datastructures.html#dictionaries
[dir-vs-__dict__]: https://stackoverflow.com/a/14361362
[dunder]: https://www.tutorialsteacher.com/python/magic-methods-in-python
[exception-handling]: https://docs.python.org/3/tutorial/errors.html#handling-exceptions
[falsiness]: https://www.pythontutorial.net/python-basics/python-boolean/
[getattribute]: https://docs.python.org/3/reference/datamodel.html?#object.__getattribute__
[int-constructor]: https://docs.python.org/3/library/functions.html?#int
[int]: https://docs.python.org/3/library/stdtypes.html#typesnumeric
[isdigit]: https://docs.python.org/3/library/stdtypes.html?#str.isdigit
[len]: https://docs.python.org/3/library/functions.html?#len
[method-chaining]: https://www.tutorialspoint.com/Explain-Python-class-method-chaining
[not]: https://docs.python.org/3/library/operator.html?#operator.__not__
[removeprefix]: https://docs.python.org/3/library/stdtypes.html#str.removeprefix
[removesuffix]: https://docs.python.org/3/library/stdtypes.html#str.removesuffix
[replace]: https://docs.python.org/3/library/stdtypes.html?#str.replace
[split]: https://docs.python.org/3/library/stdtypes.html?#str.split
[strip]: https://docs.python.org/3/library/stdtypes.html#str.strip
[unpacking]: https://treyhunner.com/2018/10/asterisks-in-python-what-they-are-and-how-to-use-them/
[unpacking-and-multiple-assignment]: https://exercism.org/tracks/python/concepts/unpacking-and-multiple-assignment
