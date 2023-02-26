# basics

Python is a [dynamic and strongly][dynamic typing in python] typed [object-oriented][object oriented programming] programming language.
It employs both [duck typing][duck typing] and [gradual typing][gradual typing], via [type hints][type hints].
Imperative, declarative (e.g., functional), and object-oriented programming _styles_ are all supported, but internally **[everything in Python is an object][everythings an object]**.

Python puts a strong emphasis on code readability and (_similar to Haskell_) uses [significant indentation][significant indentation] to denote function, method, and class definitions.

Python was created by Guido van Rossum and first released in 1991. The [Python Software Foundation][psf] manages and directs resources for Python and CPython development and receives proposals for changes to the language from [members][psf membership] of the community via [Python Enhancement Proposals or PEPs][peps].


Complete documentation for the current release can be found at [docs.python.org][python docs].

- [Python Tutorial][python tutorial]
- [Python Library Reference][python library reference]
- [Python Language Reference][python language reference]
- [Python HOW TOs][python how tos]
- [Python FAQs][python faqs]
- [Python Glossary of Terms][python glossary of terms]


This concept introduces 4 major Python language features: Name Assignment (_variables and constants_), Functions (_and the return keyword_), Comments, and Docstrings.


~~~~exercism/note

In general, content, tests, and analyzer tooling for the Python track follow the style conventions outlined in [PEP 8](https://www.python.org/dev/peps/pep-0008/) and [PEP 257](https://www.python.org/dev/peps/pep-0257/) for Python code style, with the additional (strong) suggestion that there be no single letter variable names.

The [zen of Python (PEP 20)][the zen of python] and [What is Pythonic?][what is pythonic] lay out additional philosophies.

On the Python track, [variables][variables] are always written in [`snake_case`][snake case], and constants in `SCREAMING_SNAKE_CASE`


[snake case]: https://en.wikipedia.org/wiki/Snake_case
[variables]: https://realpython.com/python-variables/
[what is pythonic]: https://blog.startifact.com/posts/older/what-is-pythonic.html
[the zen of python]: https://www.python.org/dev/peps/pep-0020/
~~~~


## Name Assignment (Variables & Constants)

In Python, there are no keywords used in creating variables or constants.
Instead, programmer defined [_names_][facts-and-myths-about-python-names] (also called _variables__) can be bound to any type of object using the assignment `=` operator: `<name> = <value>`.
A name can be reassigned (or re-bound) to different values (different object types) over its lifetime.

For example, `my_first_variable` can be re-assigned many times using `=`, and can refer to different object types with each re-assignment:


```python
>>> my_first_variable = 1  # Name bound to an integer object of value one.
>>> my_first_variable = 2  # Name re-assigned to integer value 2.

>>> print(type(my_first_variable))
<class 'int'>

>>> print(my_first_variable)
2

>>> my_first_variable = "Now, I'm a string." # You may re-bind a name to a different object type and value.
>>> print(type(my_first_variable))
<class 'str'>

>>> print(my_first_variable)
"Now, I'm a string."  # Strings can be declared using single or double quote marks.

import collections
>>> my_first_variable = collections.Counter([1,1,2,3,3,3,4,5,6,7]) # Now the name has been re-bound to a Counter object.
>>> print(type(my_first_variable))
<class 'collections.Counter'>

>>> print(my_first_variable)
>>> Counter({3: 3, 1: 2, 2: 1, 4: 1, 5: 1, 6: 1, 7: 1})
```


### Constants

Constants are names meant to be assigned only once in a program.
They should be defined at a [module][module] (file) level, and are typically visible to all functions and classes in the program.
Using `SCREAMING_SNAKE_CASE` signals that the name should not be re-assigned, or its value mutated.


```python
# All caps signal that this is intended as a constant.
MY_FIRST_CONSTANT = 16

# Re-assignment will be allowed by the compiler & interpreter,
# but this is VERY strongly discouraged.
# Please don't do this, it could create problems in your program!
MY_FIRST_CONSTANT = "Some other value"
```


## Functions

In Python, units of functionality are encapsulated in [_functions._][functions], which are themselves [objects][objects] (_it's [turtles all the way down][turtles all the way down]_).

Functions can be executed by themselves, passed as arguments to other functions, nested, or bound to a class.
When functions are bound to a [class][classes] name, they're referred to as [methods][method objects].
Related functions and classes (_with their methods_) can be grouped together in the same file or module, and imported in part or in whole for use in other programs.

The `def` keyword begins a [function definition][function definition].
Each function can have zero or more formal [parameters][parameters] in `()` parenthesis, followed by a `:` colon.
Statements for the _body_ of the function begin on the line following `def` and must be _indented in a block_.


```python
# The body of this function is indented by 2 spaces, & prints the sum of the numbers
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

```


Docstrings are read by automated documentation tools and are returned by calling the special attribute `.__doc__` on the function, method, or class name.
They are recommended for programs of any size where documentation is needed, and their conventions are laid out in [PEP257][pep257].

Docstrings can also function as [lightweight unit tests][doctests], which can be read and run by PyTest, or by importing the `doctest` module.
Testing and `doctest` will be covered in a later concept.


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
[calls]: https://docs.python.org/3/reference/expressions.html#calls
[classes]: https://docs.python.org/3/reference/datamodel.html#classes
[comments]: https://realpython.com/python-comments-guide/#python-commenting-basics
[docstring]: https://docs.python.org/3/tutorial/controlflow.html#tut-docstrings
[doctests]: https://docs.python.org/3/library/doctest.html
[duck typing]: https://en.wikipedia.org/wiki/Duck_typing
[dynamic typing in python]: https://stackoverflow.com/questions/11328920/is-python-strongly-typed
[everythings an object]: https://docs.python.org/3/reference/datamodel.html
[facts-and-myths-about-python-names]: https://nedbatchelder.com/text/names.html
[function definition]: https://docs.python.org/3/tutorial/controlflow.html#defining-functions
[functions]: https://docs.python.org/3/reference/compound_stmts.html#function
[gradual typing]: https://en.wikipedia.org/wiki/Gradual_typing
[method objects]: https://docs.python.org/3/c-api/method.html#method-objects
[module]: https://docs.python.org/3/tutorial/modules.html
[none]: https://docs.python.org/3/library/constants.html
[object oriented programming]: https://en.wikipedia.org/wiki/Object-oriented_programming
[objects]: https://docs.python.org/3/reference/datamodel.html#the-standard-type-hierarchy
[parameters]: https://docs.python.org/3/glossary.html#term-parameter
[peps]: https://www.python.org/dev/peps/
[psf membership]: https://www.python.org/psf/membership/
[psf]: https://www.python.org/psf/
[python docs]: https://docs.python.org/3/
[python faqs]: https://docs.python.org/3/faq/index.html
[python glossary of terms]: https://docs.python.org/3/glossary.html
[python how tos]: https://docs.python.org/3/howto/index.html
[python language reference]: https://docs.python.org/3/reference/index.html
[python library reference]: https://docs.python.org/3/library/index.html
[python tutorial]: https://docs.python.org/3/tutorial/index.html
[return]: https://docs.python.org/3/reference/simple_stmts.html#return
[significant indentation]: https://docs.python.org/3/reference/lexical_analysis.html#indentation
[turtles all the way down]: https://en.wikipedia.org/wiki/Turtles_all_the_way_down
[type hints]: https://docs.python.org/3/library/typing.html
