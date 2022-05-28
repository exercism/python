# About

For the basics on function arguments, please see the [function concept][function concept].

## Parameter Names

Paramater names, like variable names, must start with a letter or underscore and may contain letters, underscores, or numbers.
Parameter names should not contain spaces or punctuation.

## Positional Arguments

Positional arguments are for parameters defined without a [default argument][default arguments].
Positional arguments can optionally be called by their name.

Following is an example of positional arguments being called by position and by their name:

```python
>>> def concat(x, y):
        return f"{x}{y}"


>>> print(concat("Hello, ", "Bob"))
Hello, Bob
>>> print(concat(y="Bob", x="Hello, "))
Hello, Bob

```

The first call to `concat` passes the arguments by position.
The second call to `concat` passes the arguments by name, allowing their positions to be changed.

Note that positional arguments cannot follow keyword arguments.

This

```python
>>> print(concat(x="Hello, ", "Bob"))
```

results in this error:

```
SyntaxError: positional argument follows keyword argument
```

Arguments can be forced to be positional-only through the use of the `/` operator.

Following is an example of positional-only arguments:

```python
>>> def concat(x, y, /):
        return f"{x}{y}"


>>> print(concat("Hello, ", "Bob"))
Hello, Bob
>>> print(concat(y="Bob", x="Hello, "))
Traceback (most recent call last):
    print(concat(y="Bob", x="Hello, "))
TypeError: concat() got some positional-only arguments passed as keyword arguments: 'x, y'

```

## Keyword Arguments

Keyword arguments are for parameters defined with a [default argument][default arguments].
Keyword arguments can optionally be called by their position.

Following is an example of keyword arguments being called by their keyword and by position:

```python
>>> def concat(x="Hello, ", y="you"):
        return f"{x}{y}"


>>> print(concat(y="Bob", x="Hello, "))
Hello, Bob
>>> print(concat("Hello, ", "Bob"))
Hello, Bob
>>> print(concat())
Hello, you

```

Arguments can be forced to be keyword--only through the use of the `*` operator.

Following is an example of keyword-only arguments:

```python
>>> def concat(*, x="Hello, ", y="you"):
        return f"{x}{y}"


>>> print(concat(y="Bob", x="Hello, "))
Hello, Bob
>>> print(concat())
Hello, you
>>> print(concat("Hello, ", "Bob"))
Traceback (most recent call last):
    print(concat("Hello, ", "Bob"))
TypeError: concat() takes 0 positional arguments but 2 were given

```

## Positional or Keyword Arguments

Arguments can be positional or keyword if neither the `/` nor `*` operators are used in the parameter definitions.
Alternately, the positional-or-keyword arguemtns can be placed between the positional-only parameters on the left and the keyword-only parameters on the right.

Following is an example of positional-only, positional-or-keyword, and keyword-only arguments:

```python
>>> def concat(x, /,  y="you", *, z="."):
        return f"{x}{y}{z}"


>>> print(concat("Hello, ", "Bob", z="!"))
Hello, Bob!
>>> print(concat("Hello, ", y="Bob", z="!"))
Hello, Bob!
>>> print(concat("Hello, "))
Hello, you.
>>> print(concat(x="Hello, ", y="Bob", z="!"))
Traceback (most recent call last):
    print(concat(x="Hello, ", y="Bob", z="!"))
TypeError: concat() got some positional-only arguments passed as keyword arguments: 'x'

```

## `*args`

Code examples will often use a function definition something like the following:

```python
def my_function(*args, **kwargs):
    # code snipped

```

`*args` is a two-part name that represents an indefinite number of separate positional arguments, which is also known as a variadic argument.
`args` is the name of the group of arguments and could be any other name, such as `my_args`, `arguments`, etc.
The `*` is the operator which transforms the group of separate arguments into a [`tuple`][tuple].
Since a tuple can be iterated, `args` can be passed to any other function which takes an iterable.
Although `*args` is commonly juxtaposed with `**kwargs`, it doesn't have to be.

Following is an example of an arbitrary amount of values being passed to a function between a positonal argument and a keyword argument:

```python

>>> def add(first, *args, last=0):
        return first + sum(args) + last


>>> print(add(1, 2, 3))
6
>>> print(add(1, 2, 3, last=4))
10
>>> print(add(*[1, 2, 3]))
6

```

Note that when an argument is already in an iterable, such as a tuple or list, it needs to be unpacked before being passed to a function that takes an arbitrary amount of separate arguments.
This is accomplished by `*`, which is the [unpacking operator][unpacking operator].
This unpacks the list into its separate elements which are then transformed by `*args` into a tuple.
Without unpacking the list passed into `add`, the program would error.

```python
>>>> def add(first, *args, last=0):
        return first + sum(args) + last


>>>> print(add([1, 2, 3]))
Traceback (most recent call last):
    print(add([1, 2, 3]))
    return first + sum(args) + last
TypeError: can only concatenate list (not "int") to list

```

What happened is that the `*` in `*args` only unpacked the list into its separate elements, and it was done.
It did not reassemble the elements into a tuple.

## `**kwargs`

`**kwargs` is a two-part name that represents an indefinite number of separate [key-value pair][key-value] arguments.
`kwargs` is the name of the group of arguments and could be any other name, such as `my_args`, `arguments`, etc.
The `**` is the operator which transforms the group of separate arguments into a [`dictionary`][dictionary].
Since a dictionary can be iterated, `kwargs` can be passed to any other function which takes an iterable.
Although `**kwargs` is commonly juxtaposed with `*args`, it doesn't have to be.

Following is an example of an arbitrary amount of key-value pairs being passed to a function:

```python
>>> def add(**kwargs):
        return sum(kwargs.values())


>>> print(add(one=1, two=2, three=3))
6
```

Note that the `values()` method is called to iterate on the dictionary values.
When iterating a dictionary the default is to iterate the keys.

Following is an example of an arbitrary amount of key-value pairs being passed to a function that iterates the keys:

```python
>>> def concat(**kwargs):
        return " ".join(kwargs)


>>> print(concat(one=1, two=2, three=3))
one two three

```

[default arguments]: https://www.geeksforgeeks.org/default-arguments-in-python/
[dictionary]: https://www.w3schools.com/python/python_dictionaries.asp
[function concept]: ../functions/about.md
[key-value]: https://www.pythontutorial.net/python-basics/python-dictionary/
[tuple]: https://www.w3schools.com/python/python_tuples.asp
[unpacking operator]: https://docs.python.org/3/tutorial/controlflow.html#unpacking-argument-lists

