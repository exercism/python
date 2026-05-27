# Introduction

For the basics on function arguments, please see the [function concept][function concept].

## Parameter Names

[Parameter names][parameters], like variable names, must start with a letter or underscore and may contain letters, underscores, or numbers.
Parameter names should not contain spaces or punctuation.


## Positional Arguments

Positional arguments are values passed to a function in the same order as the parameters which bind to them.
They can optionally be passed by using their parameter name:


```python
def concat(greeting, name):
    return f"{greeting}{name}"
 
# Passing data to the function by position.
print(concat("Hello, ", "Judy"))
#->  Hello, Judy

# Passing data to the function using the parameter name.
print(concat(name="Sally", greeting="Hello, "))
#-> Hello, Sally
```

The first call to concat passes the arguments by position.
The second call to concat passes the arguments by _name_, allowing their positions to be changed.

Note that positional arguments cannot follow arguments passed by name (_also called [keyword arguments][keyword-arguments]. **Not** to be confused with var-positional parameters or [**kwargs][kwargs]_).

This set of arguments:

```python
>>> print(concat(greeting="Hello, ", "Zed"))
```

will result in this error:

```
SyntaxError: positional argument follows keyword argument
```

## Default Argument Values

[Default values][default arguments] for one or more arguments can be supplied in the parameter list.
This allows the function to be called with _fewer_ arguments if needed.
Default values can be overridden by calling the function with new arguments in place of the defaults:


```python
# Note the default arguments for both greeting and name.
def concat(greeting="Hello, ", name="you"):
    return f"{greeting}{name}"
 
# Function call overriding the defaults
print(concat(name="Jerry", greeting="Hello, "))
#-> Hello, Jerry

# Function call without arguments resulting in the defaults being used.
print(concat())
#-> Hello, you
```

## Keyword Arguments

Keyword arguments use the parameter name when passing arguments to a function.
They can optionally be referred to by position:


```python
# Note the default arguments for both greeting and name.
def concat(greeting="Hello, ", name="you"):
    return f"{greeting}{name}"

# Function call using parameter names as argument keywords.
print(concat(name="Jerry", greeting="Hello, "))
#-> Hello, Jerry

# Function call with positional data as arguments.
print(concat("Hello, ", "Isaac"))
#-> Hello, Isaac
```

[default arguments]: https://www.geeksforgeeks.org/default-arguments-in-python/
[function concept]: https://github.com/exercism/python/blob/main/concepts/functions/about.md
[keyword-arguments]: https://docs.python.org/3/glossary.html#term-argument
[kwargs]: https://docs.python.org/3/glossary.html#term-parameter
[parameters]: https://www.codecademy.com/learn/flask-introduction-to-python/modules/learn-python3-functions/cheatsheet
