# Introduction

Python is a [dynamic and strongly][dynamic typing in python] typed programming language.
It employs both [duck typing][duck typing] and [gradual typing][gradual typing] via [type hints][type hints].

While Python supports many different programming _styles_, internally **everything in Python is an [object][everythings an object]**.
This includes numbers, strings, lists, and even functions.

We'll dig more into what all of that means as we continue through the track.

This first exercise introduces 4 major Python language features:
1.  Name Assignment (_variables and constants_),
2.  Functions (_the `def` keyword and the `return` keyword_),
3.  Comments, and
4.  Docstrings.


~~~~exercism/note

In general, content, tests, and analyzer tooling for the Python track follow the style conventions outlined in [PEP 8](https://www.python.org/dev/peps/pep-0008/) and [PEP 257](https://www.python.org/dev/peps/pep-0257/) for Python code style, with the additional (strong) suggestion that there be no single letter variable names.

On the Python track, [variables][variables] are always written in [`snake_case`][snake case], and constants in `SCREAMING_SNAKE_CASE`.

[variables]: https://realpython.com/python-variables/
[snake case]: https://en.wikipedia.org/wiki/Snake_case
~~~~


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
Functions that do not have an _explicit_ `return` expression will _implicitly_ return [`None`][none].

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


### Calling Functions

Functions are [_called_][calls] or invoked using their name followed by `()`.
Dot (`.`) notation is used for calling functions defined inside a class or module.

```python
>>> def number_to_the_power_of(number_one, number_two):
        return number_one ** number_two
...

>>> number_to_the_power_of(3,3) # Invoking the function with the arguments 3 and 3.
27


# A mis-match between the number of parameters and the number of arguments will raise an error.
>>> number_to_the_power_of(4,)
...
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: number_to_the_power_of() missing 1 required positional argument: 'number_two'


# Calling methods or functions in classes and modules.
>>> start_text = "my silly sentence for examples."
>>> str.upper(start_text)  # Calling the upper() method for the built-in str class.
"MY SILLY SENTENCE FOR EXAMPLES."

# Importing the math module
import math

>>> math.pow(2,4)  # Calling the pow() function from the math module
>>> 16.0
```


## Comments

[Comments][comments] in Python start with a `#` that is not part of a string, and end at line termination.
Unlike many other programming languages, Python **does not support** multi-line comment marks.
Each line of a comment block must start with the `#` character.


## Docstrings

The first statement of a function body can optionally be a [_docstring_][docstring], which concisely summarizes the function or object's purpose.
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


Docstrings are read by automated documentation tools and are returned by calling the special attribute `.__doc__` on the function, method, or class name.
Docstring conventions are laid out in [PEP257][pep257].

Docstrings can also function as [lightweight unit tests][doctests], which will be covered in a later exercise.


```python
# An example on a user-defined function.
>>> def number_to_the_power_of(number_one, number_two):
        """Raise a number to an arbitrary power.

        :param number_one: int the base number.
        :param number_two: int the power to raise the base number to.
        :return: int - number raised to power of second number

        Takes number_one and raises it to the power of number_two, returning the result.
        """

        return number_one ** number_two
...

# Calling the .__doc__ attribute of the function and printing the result.
>>> print(number_to_the_power_of.__doc__)
Raise a number to an arbitrary power.

    :param number_one: int the base number.
    :param number_two: int the power to raise the base number to.
    :return: int - number raised to power of second number

    Takes number_one and raises it to the power of number_two, returning the result.
```

[calls]: https://docs.python.org/3/reference/expressions.html#calls
[comments]: https://realpython.com/python-comments-guide/#python-commenting-basics
[docstring]: https://docs.python.org/3/tutorial/controlflow.html#tut-docstrings
[doctests]: https://docs.python.org/3/library/doctest.html
[duck typing]: https://en.wikipedia.org/wiki/Duck_typing
[dynamic typing in python]: https://stackoverflow.com/questions/11328920/is-python-strongly-typed
[everythings an object]: https://docs.python.org/3/reference/datamodel.html
[facts-and-myths-about-python-names]: https://nedbatchelder.com/text/names.html
[function definition]: https://docs.python.org/3/tutorial/controlflow.html#defining-functions
[gradual typing]: https://en.wikipedia.org/wiki/Gradual_typing
[module]: https://docs.python.org/3/tutorial/modules.html
[none]: https://docs.python.org/3/library/constants.html
[parameters]: https://docs.python.org/3/glossary.html#term-parameter
[pep257]: https://www.python.org/dev/peps/pep-0257/
[return]: https://docs.python.org/3/reference/simple_stmts.html#return
[type hints]: https://docs.python.org/3/library/typing.html
