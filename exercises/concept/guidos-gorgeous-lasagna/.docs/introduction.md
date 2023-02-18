# Introduction

Python is a [dynamic and strongly][dynamic typing in python] typed [object-oriented][object oriented programming] programming language.
It employs both [duck typing][duck typing] and [gradual typing][gradual typing], via [type hints][type hints].
Python supports Imperative, declarative (e.g. functional), and object oriented programming _styles_, but internally [everything in Python is an object][everythings an object].

This exercise introduces 4 major Python language features:  Names (_variables and constants_), Functions (_and the return keyword_), Comments, and Docstrings.


~~~~exercism/note

In general, content, tests, and analyzer tooling for the Python track follow the style conventions outlined in [PEP 8](https://www.python.org/dev/peps/pep-0008/) and [PEP 257](https://www.python.org/dev/peps/pep-0257/) for Python code style, with the additional (strong) suggestion that there be no single letter variable names.

~~~~


## Name Assignment and Re-assignment


There are no keywords in Python to define variables or constants and there is no difference in the way Python treats them.
Both are considered [_names_][facts-and-myths-about-python-names] that help programmers reference values (_objects_) in a program and are written differently only by convention.
On Exercism, [variables][variables] are always written in [`snake_case`][snake case], and _constants_ in `SCREAMING_SNAKE_CASE`.

Names are assigned to values via `=`, or the [_assignment operator_][assignment statements]: `<name> = <value>`.
A name (_variable or constant_) can be assigned or re-assigned over its lifetime to different values/different object types.
For example, `my_first_variable` can be assigned and re-assigned many times using `=`, and can refer to different object types with each re-assignment:

```python
# Assigning my_first_variable to a numeric value.
>>> my_first_variable = 1
>>> print(type(my_first_variable))
...
<class 'int'>

>>> print(my_first_variable)
...
1

# Reassigning my_first_variable to a new string value.
>>> my_first_variable = "Now, I'm a string."
>>> print(type(my_first_variable))
...
<class 'str'>

>>> print(my_first_variable)
...
"Now, I'm a string."
```


### Constants

Constants are typically defined at a [module][module] level, being values that are accessible outside function or class scope.
Constant names **_can be reassigned to new values_**, but they are _intended_ to be named only once.
Using `SCREAMING_SNAKE_CASE` warns other programmers that these names should not be mutated or reassigned.


```python
# All caps signal that this is intended as a constant.
MY_FIRST_CONSTANT = 16

# Re-assignment will be allowed by the compiler & interpreter,
# but this is VERY strongly discouraged.
# Please don't: MY_FIRST_CONSTANT = "Some other value"
```


## Functions

The keyword `def` begins a [function definition][function definition].
It must be followed by the function name and a parenthesized list of zero or more formal [parameters][parameters].
 Parameters can be of several different varieties, and can even [vary][more on functions] in length.
The `def` line is terminated with a colon.

```python
# function definition
def my_function_name(parameter, second_parameter):
    <function body>
    
```

Statements for the _body_ of the function begin on the line following `def` and must be _indented in a block_.
There is no strict indentation amount (_either space **OR** [tab] characters are acceptable_), but [indentation][indentation] must be _consistent for all indented statements_.


```python
# Function definition on first line.
def add_two_numbers(number_one, number_two):
  print(number_one + number_two)  # Prints the sum of the numbers, and is indented by 2 spaces.

>>> add_two_numbers(3, 4)
7
```

Functions explicitly return a value or object via the [`return`][return] keyword.

```python
# Function definition on first line.
def add_two_numbers(number_one, number_two):
  return number_one + number_two # Returns the sum of the numbers.

>>> add_two_numbers(3, 4)
7
```

Functions that do not have an explicit `return` expression will return [`None`][none].

```python
# This function will return None.
def add_two_numbers(number_one, number_two):
  result = number_one + number_two

>>> print(add_two_numbers(5, 7))
None
```

While you may choose any indentation depth, _inconsistent_ indentation in your code blocks will raise an error:

```python
# The return statement line does not match the first line indent.
>>> def add_three_numbers_misformatted(number_one, number_two, number_three):
...     result = number_one + number_two + number_three   # Indented by 4 spaces.
...    return result     #this was only indented by 3 spaces
...
...  
  File "<stdin>", line 3
    return result
                ^
IndentationError: unindent does not match any outer indentation level
```

### Calling Functions

Functions are [_called_][calls] or invoked using their name followed by `()`.
The number of arguments passed in the parentheses must match the number of parameters in the original function definition..

```python
>>> def number_to_the_power_of(number_one, number_two): 
        return number_one ** number_two
...

>>> number_to_the_power_of(3,3)
27
```

A mis-match between the number of parameters and the number of arguments will raise an error:

```python
>>> number_to_the_power_of(4,)
...
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: number_to_the_power_of() missing 1 required positional argument: 'number_two'

```

Calling functions defined inside a class (_class methods_) use `<class name>.<method name>(<parameters>)`, otherwise known as dot (.) notation:

```python
# This is an example of a method call of the built in str class.
# Define a variable and assign it to a string.
>>> start_text = "my silly sentence for examples."

# Uppercase the string by calling the upper method from the str class.
>>> str.upper(start_text)
"MY SILLY SENTENCE FOR EXAMPLES."


# Below is an example of a method call of the built in list class.
# Define an empty list
>>> my_list = []

# Add an element to the list by calling the append method from the list class.
>>> my_list.append(start_text)
>>> print(my_list)
["my silly sentence for examples."]
```


## Comments


[Comments][comments] in Python start with a `#` that is not part of a string, and end at line termination.
Unlike many other programming languages, Python **does not support** multi-line comment marks.
Each line of a comment block must start with the `#` character.

Comments are ignored by the interpreter:

```python
# This is a single line comment.

x = "foo"  # This is an in-line comment.

# This is a multi-line
# comment block over multiple lines --
# these should be used sparingly.
```

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
    ...

```

Docstrings are read by automated documentation tools and are returned by calling the special attribute `.__doc__` on the function, method, or class name.
Docstrings can also function as [lightweight unit tests][doctests], which will be covered in a later exercise.
They are recommended for programs of any size where documentation is needed, and their conventions are laid out in [PEP257][PEP257].


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

# Printing the __doc__ attribute for the built-in type: str.
>>> print(str.__doc__)
str(object='') -> str
str(bytes_or_buffer[, encoding[, errors]]) -> str

Create a new string object from the given object. If encoding or
errors is specified, then the object must expose a data buffer
that will be decoded using the given encoding and error handler.
Otherwise, returns the result of object.__str__() (if defined)
or repr(object).
encoding defaults to sys.getdefaultencoding().
errors defaults to 'strict'.
```

[PEP257]: https://www.python.org/dev/peps/pep-0257/
[assignment statements]: https://docs.python.org/3/reference/simple_stmts.html#assignment-statements
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
[indentation]: https://docs.python.org/3/reference/lexical_analysis.html#indentation
[module]: https://docs.python.org/3/tutorial/modules.html
[more on functions]: https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions
[none]: https://docs.python.org/3/library/constants.html
[object oriented programming]: https://en.wikipedia.org/wiki/Object-oriented_programming
[parameters]: https://docs.python.org/3/glossary.html#term-parameter
[return]: https://docs.python.org/3/reference/simple_stmts.html#return
[snake case]: https://en.wikipedia.org/wiki/Snake_case
[type hints]: https://docs.python.org/3/library/typing.html
[variables]: https://realpython.com/python-variables/
