# Introduction

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
...         return f"{x}{y}"
... 
>>> print(concat("Hello, ", "Bob"))
Hello, Bob
>>> print(concat(y="Bob", x="Hello, "))
Hello, Bob

```

Note that positional arguments cannot follow keyword arguments.

This

```python
>>> print(concat(x="Hello, ", "Bob"))
```

results in this error:

```
SyntaxError: positional argument follows keyword argument
```

The first call to `concat` passes the arguments by position.
The second call to `concat` passes the arguments by name, allowing their positions to be changed.

## Keyword Arguments

Keyword arguments are for parameters defined with a [default argument][default arguments].
Keyword arguments can optionally be called by their position.

Following is an example of keyword arguments being called by their keyword and by position:

```python
>>> def concat(x="Hello, ", y="you"):
...         return f"{x}{y}"
... 
>>> print(concat(y="Bob", x="Hello, "))
Hello, Bob
>>> print(concat("Hello, ", y="Bob"))
Hello, Bob
>>> print(concat())
Hello, you

```

[default arguments]: https://www.geeksforgeeks.org/default-arguments-in-python/
[function concept]: ../functions/about.md
