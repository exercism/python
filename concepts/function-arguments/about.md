# About

For the basics on function arguments, please see the [function concept][function concept].

## Parameter Names

Paramater names, like variable names, must start with a letter or underscore and may contain letters, underscores, or numbers.
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

The first call to `concat` passes the arguments by position.
The second call to `concat` passes the arguments by name, allowing their positions to be changed.

Note that positional arguments cannot follow keyword arguments.

This

```python
>>> print(concat(greeting="Hello, ", "Bob"))
```

results in this error:

```
SyntaxError: positional argument follows keyword argument
```

Requiring positional-only arguments for function calls can be done through the use of the `/` operator in the parameter list.


Following is an example of positional-only arguments:

```python
# Parameters showing a position-only operator. 
>>> def concat(greeting, name, /):
...         return f"{greeting}{name}"

... 
>>> print(concat("Hello, ", "Bob"))
Hello, Bob
...
# Call to the function using keyword arguments.
>>> print(concat(name="Bob", greeting="Hello, "))
Traceback (most recent call last):
    print(concat(name="Bob", greeting="Hello, "))
TypeError: concat() got some positional-only arguments passed as keyword arguments: 'greeting, name'


```

## Keyword Arguments

Keyword arguments use the parameter name when calling a function.
Keyword arguments can optionally be referred to by position.

Following is an example of keyword arguments being referred to by their parameter name and by position:

```python
>>> def concat(greeting, name):
...         return f"{greeting}{name}"
... 
# Function call using parameter names as argument keywords.
>>> print(concat(name="Bob", greeting="Hello, "))
Hello, Bob
...
# Function call with positional data as arguments.
>>> print(concat("Hello, ", "Bob"))
Hello, Bob
>>> print(concat())
Hello, you

```

Requiring keyword-only arguments for function calls can be done through the use of the `*` operator in the parameter list:

Following is an example of keyword-only arguments:

```python
# Function definition requiring keyword-only arguments.
>>> def concat(*, greeting, name):
...         return f"{greeting}{name}"
... 
# Keyword arguments can be in an arbitrary order.
>>> print(concat(name="Bob", greeting="Hello, "))
Hello, Bob
...
# Calling the function with positional data raises an error.
>>> print(concat("Hello, ", "Bob"))
Traceback (most recent call last):
    print(concat("Hello, ", "Bob"))
TypeError: concat() takes 0 positional arguments but 2 were given


```

## Positional or Keyword Arguments

Arguments can be positional or keyword if neither the `/` nor `*` operators are used in the parameter definitions.
Alternately, the positional-or-keyword arguments can be placed between the positional-only parameters on the left and the keyword-only parameters on the right.

Following is an example of positional-only, positional-or-keyword, and keyword-only arguments:

```python
# Position-only argument followed by position-or-keyword, followed by keyword-only.
>>> def concat(greeting, /,  name, *, ending):
...         return f"{greeting}{name}{ending}"
... 
>>> print(concat("Hello, ", "Bob", ending="!"))
Hello, Bob!
>>> print(concat("Hello, ", name="Bob", ending="!"))
Hello, Bob!
...
>>> print(concat(greeting="Hello, ", name="Bob", ending="!"))
Traceback (most recent call last):
    print(concat(greeting="Hello, ", name="Bob", ending="!"))
TypeError: concat() got some positional-only arguments passed as keyword arguments: 'greeting'

```

## `*args`

Code examples will often use a function definition something like the following:

```python
def my_function(*args, **kwargs):
    # code snipped

```

`*args` is a two-part name that represents a `tuple` with an indefinite number of separate positional arguments, also known as a [`variadic argument`][variadic argument].
`args` is the name given to the `tuple` of arguments,  but it could be any other valid Python name, such as `my_args`, `arguments`, etc.
The `*` is the operator which transforms the group of separate arguments into a [`tuple`][tuple].

----
If you have ever [unpacked a tuple][unpack a tuple] you may find the `*` in `*args` to be confusing.
The `*` in a parameter definition, instead of unpacking a tuple, converts one or more positional arguments _into_ a tuple.
We say that the `*` operator is [overloaded], as it has different behavior in different contexts.
For instance, `*` is used for multiplication, it is used for unpacking, and it is used to define an arbitrary number of positional parameters.

----
    
Since a tuple can be iterated, `args` can be passed to any other function which takes an iterable.
Although `*args` is commonly juxtaposed with `**kwargs`, it doesn't have to be.

Following is an example of an arbitrary amount of values being passed to a function between a positonal argument and a keyword argument:

```python

>>> def add(first, *args, last=0):
...         return first + sum(args) + last
... 
>>> print(add(1, 2, 3))
6
>>> print(add(1, 2, 3, last=4))
10
# This uses the unpacking operator * to separate the list elements into positional arguments.
# It does not have the same behavior as the * in *args.
>>> print(add(*[1, 2, 3]))
6

```

Note that when an argument is already in an iterable, such as a tuple or list, it needs to be unpacked before being passed to a function that takes an arbitrary amount of separate arguments.
This is accomplished by `*`, which is the [unpacking operator][unpacking operator].
`*` in this context _unpacks_ the container into its separate elements which are then transformed by `*args` into a tuple.
Where there are only positional arguments, the unpacking action must result in the same number of arguments as there are formal parameters.

Without unpacking the list passed into `add`, the program would error.

```python
>>>> def add(first, *args, last=0):
...         return first + sum(args) + last
... 
>>>> print(add([1, 2, 3]))
Traceback (most recent call last):
    print(add([1, 2, 3]))
    return first + sum(args) + last
TypeError: can only concatenate list (not "int") to list

```

## `**kwargs`

`**kwargs` is a two-part name that represents an indefinite number of separate [key-value pair][key-value] arguments.
`kwargs` is the name of the group of arguments and could be any other name, such as `my_args`, `arguments`, etc.
The `**` transforms the group of named arguments into a [`dictionary`][dictionary] of `{argument name: argument value}` pairs.

Since a dictionary can be iterated, `kwargs` can be passed to any other function which takes an iterable.
Although `**kwargs` is commonly juxtaposed with `*args`, it doesn't have to be.

Following is an example of an arbitrary amount of key-value pairs being passed to a function:

```python
>>> def add(**kwargs):
...         return sum(kwargs.values())
... 
>>> print(add(one=1, two=2, three=3))
6
```

Note that the `dict.values()` method is called to iterate through the `kwargs` dictionary values.

When iterating a dictionary the default is to iterate the keys.

Following is an example of an arbitrary amount of key-value pairs being passed to a function that then iterates over `kwargs.keys()`:

```python
>>> def concat(**kwargs):
             # Join concatenates the key names from `kwargs.keys()`
...         return " ".join(kwargs)
... 
>>> print(concat(one=1, two=2, three=3))
one two three

```


[default arguments]: https://www.geeksforgeeks.org/default-arguments-in-python/
[dictionary]: https://www.w3schools.com/python/python_dictionaries.asp
[function concept]: ../functions/about.md
[key-value]: https://www.pythontutorial.net/python-basics/python-dictionary/
[overloaded]: https://www.geeksforgeeks.org/operator-overloading-in-python/
[tuple]: https://www.w3schools.com/python/python_tuples.asp
[unpack a tuple]: https://www.geeksforgeeks.org/unpacking-a-tuple-in-python/
[unpacking operator]: https://docs.python.org/3/tutorial/controlflow.html#unpacking-argument-lists
[variadic argument]: https://en.wikipedia.org/wiki/Variadic_function
