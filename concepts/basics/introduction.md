# Introduction

Python is a [dynamic and strongly typed][dynamic typing in python] programming language.
It employs both [duck typing][duck typing] and [gradual typing][gradual typing], via [type hints][type hints].

Imperative, declarative (e.g., functional), and object-oriented programming _styles_ are all supported, but internally **[everything in Python is an object][everythings an object]**.

Python puts a strong emphasis on code readability and (_similar to Haskell_) uses [significant indentation][significant indentation] to denote function, method, and class definitions.

Python was created by Guido van Rossum and first released in 1991.


## Name Assignment (Variables & Constants)

Programmers can bind [_names_][facts-and-myths-about-python-names] (also called _variables_) to any type of object using the assignment `=` operator: `<name> = <value>`.
A name can be reassigned (or re-bound) to different values (different object types) over its lifetime.


```python
>>> my_first_variable = 1  # my_first_variable bound to an integer object of value one.
>>> my_first_variable = 2  # my_first_variable re-assigned to integer value 2.

>>> print(type(my_first_variable))
<class 'int'>

>>> print(my_first_variable)
2

>>> my_first_variable = "Now, I'm a string." # You may re-bind a name to a different object type and value.
>>> print(type(my_first_variable))
<class 'str'>

>>> print(my_first_variable)
"Now, I'm a string."  # Strings can be declared using single or double quote marks.
```


### Constants

Constants are names meant to be assigned only once in a program.
They should be defined at a [module][module] (file) level, and are typically visible to all functions and classes in the program.
Using `SCREAMING_SNAKE_CASE` signals that the name should not be re-assigned, or its value mutated.


## Functions

The `def` keyword begins a [function definition][function definition].
Each function can have zero or more formal [parameters][parameters] in `()` parenthesis, followed by a `:` colon.
Statements for the _body_ of the function begin on the line following `def` and must be _indented in a block_.


```python
# The body of a function is indented by 2 spaces, & prints the sum of the numbers.
def add_two_numbers(number_one, number_two):
  total = number_one + number_two
  print(total)  

>>> add_two_numbers(3, 4)
7


# Inconsistent indentation in your code blocks will raise an error.
>>> def add_three_numbers_misformatted(number_one, number_two, number_three):
...     result = number_one + number_two + number_three   # This was indented by 4 spaces.
...    print(result)     #this was only indented by 3 spaces
...
...
  File "<stdin>", line 3
    print(result)
    ^
IndentationError: unindent does not match any outer indentation level
```

Functions explicitly return a value or object via the [`return`][return] keyword.
Functions that do not have an explicit `return` expression will _implicitly_ return [`None`][none].

```python
# Function definition on first line.
def add_two_numbers(number_one, number_two):
  result = number_one + number_two
  return result  # Returns the sum of the numbers.

>>> add_two_numbers(3, 4)
7

# This function will return None.
def add_two_numbers(number_one, number_two):
  result = number_one + number_two

>>> print(add_two_numbers(5, 7))
None
```


## Comments

[Comments][comments] in Python start with a `#` that is not part of a string, and end at line termination.
Unlike many other programming languages, Python **does not support** multi-line comment marks.
Each line of a comment block must start with the `#` character.


## Docstrings

The first statement of a function body can optionally be a [_docstring_][docstring], which concisely summarizes the function or object's purpose.
Docstring conventions are laid out in [PEP257][pep257].
Docstrings are declared using triple double quotes (""") indented at the same level as the code block:


```python

# An example from PEP257 of a multi-line docstring.
def complex(real=0.0, imag=0.0):
    """Form a complex number.

    Keyword arguments:
    real -- the real part (default 0.0)
    imag -- the imaginary part (default 0.0)
    """

    if imag == 0.0 and real == 0.0:
        return complex_zero

```

[pep257]: https://www.python.org/dev/peps/pep-0257/
[comments]: https://realpython.com/python-comments-guide/#python-commenting-basics
[docstring]: https://docs.python.org/3/tutorial/controlflow.html#tut-docstrings
[duck typing]: https://en.wikipedia.org/wiki/Duck_typing
[dynamic typing in python]: https://stackoverflow.com/questions/11328920/is-python-strongly-typed
[everythings an object]: https://docs.python.org/3/reference/datamodel.html
[facts-and-myths-about-python-names]: https://nedbatchelder.com/text/names.html
[function definition]: https://docs.python.org/3/tutorial/controlflow.html#defining-functions
[gradual typing]: https://en.wikipedia.org/wiki/Gradual_typing
[module]: https://docs.python.org/3/tutorial/modules.html
[none]: https://docs.python.org/3/library/constants.html
[parameters]: https://docs.python.org/3/glossary.html#term-parameter
[return]: https://docs.python.org/3/reference/simple_stmts.html#return
[type hints]: https://docs.python.org/3/library/typing.html
[significant indentation]: https://docs.python.org/3/reference/lexical_analysis.html#indentation
