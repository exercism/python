# About

For the basics on function arguments, please see the [function concept][function concept].

## Parameter Names

Paramater names, like variable names, must start with a letter or underscore and may contain letters, underscores, or numbers.
Parameter names should not contain spaces or punctuation.

## Positional Arguments

Positional arguments are for parameters defined without a [default argument][default arguments].
Positional arguments can optionally be called by their keyword.

Following is an example of positional arguments being called by position and by their keyword:

```python
>>> def concat(x, y):
        return f"{x}{y}"


>>> print(concat("Hello, ", "Bob"))
Hello, Bob
>>> print(concat(y="Bob", x="Hello, "))
Hello, Bob

```

The first call to `concat` passes the arguments by position.
The second call to `concat` passes the arguments by keyword, allowing their positions to be changed.

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

```

Arguments can be forced to be keyword--only through the use of the `*` operator.

Following is an example of keyword-only arguments:

```python
>>> def concat(*, x="Hello, ", y="you"):
        return f"{x}{y}"


>>> print(concat(y="Bob", x="Hello, "))
Hello, Bob
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

## `**vargs`

[default arguments]: https://www.geeksforgeeks.org/default-arguments-in-python/
[function concept]: ../functions/about.md

