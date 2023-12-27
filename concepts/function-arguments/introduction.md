# Introduction

For the basics on function arguments, please see the [function concept][function concept].

## Parameter Names

Parameter names, like variable names, must start with a letter or underscore and may contain letters, underscores, or numbers.
Parameter names should not contain spaces or punctuation.

## Positional Arguments

Positional arguments are values passed to a function in the same order as the parameters which bind to them.
Positional arguments can optionally be passed by using their parameter name.

Following is an example of positional arguments being passed by position and by their parameter name:

```python
>>> def concat(greeting, name):
...         return f"{greeting}{name}"
... 
# Passing data to the function by position.
>>> print(concat("Hello, ", "Bob"))
Hello, Bob
... 
# Passing data to the function using the parameter name.
>>> print(concat(name="Bob", greeting="Hello, "))
Hello, Bob

```

The first call to concat passes the arguments by position.
The second call to concat passes the arguments by name, allowing their positions to be changed.

Note that positional arguments cannot follow keyword arguments.

This

```python
>>> print(concat(greeting="Hello, ", "Bob"))
```

results in this error:

```
SyntaxError: positional argument follows keyword argument
```

## Keyword Arguments

Keyword arguments use the parameter name when calling a function.
Keyword arguments can optionally be referred to by position.

Following is an example of keyword arguments being referred to by their parameter name and by position:

```python
>>> def concat(greeting="Hello, ", name="you"):
...         return f"{greeting}{name}"
... 
# Function call using parameter names as argument keywords.
>>> print(concat(name="Bob", greeting="Hello, "))
Hello, Bob
...
# Function call with positional data as arguments.
>>> print(concat("Hello, ", name="Bob"))
Hello, Bob
>>> print(concat())
Hello, you

```

[default arguments]: https://www.geeksforgeeks.org/default-arguments-in-python/
[function concept]: ../functions/about.md
[parameters]: https://www.codecademy.com/learn/flask-introduction-to-python/modules/learn-python3-functions/cheatsheet
