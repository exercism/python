# basics

Python is a [dynamic and strongly][dynamic typing in python] typed [object-oriented][object oriented programming] programming language.
It employs both [duck typing][duck typing] and [gradual typing][gradual typing], via [type hints][type hints].
Imperative, declarative (e.g., functional), and object-oriented programming _styles_ are all supported, but internally [everything in Python is an object][everythings an object].

Python puts a strong emphasis on code readability and (_similar to Haskell_) uses [significant indentation][significant indentation] to denote function, method, and class definitions.


The [zen of Python (PEP 20)][the zen of python] and [What is Pythonic?][what is pythonic] lay out additional philosophies

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

~~~~


## Name Assignment and Re-assignment

In Python, there are no keywords to define variables or constants.
Both are [_names_][facts-and-myths-about-python-names] that help programmers reference values (_objects_) in a program and are written differently only by convention.
On Exercism, [variables][variables] are always written in [`snake_case`][snake case], and _constants_ in `SCREAMING_SNAKE_CASE`.

Names are assigned to values using `=`, or the [_assignment operator_][assignment statements] (`<name> = <value>`).
A name (_variable or constant_) can be re-assigned over its lifetime to different values/object types.

For example, `my_first_variable` can be re-assigned many times using `=`, and can refer to different object types with each re-assignment:

```python
# Assigning my_first_variable to a numeric value.
>>> my_first_variable = 1
>>> print(type(my_first_variable))
<class 'int'>

>>> print(my_first_variable)
1

# Reassigning my_first_variable to a new string value.
>>> my_first_variable = "Now, I'm a string."
>>> print(type(my_first_variable))
<class 'str'>

>>> print(my_first_variable)
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

In Python, units of functionality are encapsulated in [_functions._][functions], which are themselves [objects][objects] (_it's [turtles all the way down][turtles all the way down]_).

Functions can be executed by themselves, passed as arguments to other functions, nested, or bound to a class.
When functions are bound to a [class][classes] name, they're referred to as [methods][method objects].
Related functions and classes (_with their methods_) can be grouped together in the same file or module, and imported in part or in whole for use in other programs.

The keyword `def` begins a [function definition][function definition].
It must be followed by the function name and a parenthesized list of zero or more formal [parameters][parameters].
Parameters can be of several different varieties, and can even [vary][more on functions] in length.

The `def` line is terminated with a colon (`:`):

```python
# Function definition.
def my_function_name(parameter, second_parameter):
    <function body>

```

Statements for the `function body` begin on the line following `def` and must be _indented in a block_.
There is no strict indentation amount (_either space **OR** [tab] characters are acceptable_), but [indentation][indentation] must be _consistent_ for all indented statements.


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
  return number_one + number_two  # Returns the sum of the numbers.

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

Functions are [_called_][calls] using their name followed by `()`.
The number of arguments passed in the parentheses must match the number of parameters in the original function definition unless [default arguments][default arguments] have been used.

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


Adding a [default value][default arguments] for a parameter can defend against such errors:

```python
# Note the default value of 2 assigned below.
def number_to_the_power_of_default(number_one, number_two=2):
    """Raise a number to an arbitrary power.
    
    :param number_one: int the base number.
    :param number_two: int the power to raise the base number to.
    :return: int - number raised to power of second number
    
    Takes number_one and raises it to the power of number_two, returning the result.
    """

    return number_one ** number_two

# Because there was a default value, this call with only one argument does not throw an error.
>>> number_to_the_power_of_default(4)
16
```


Methods bound to class names are invoked via dot notation (`<class name>.<method name>(<parameters>))`, as are functions (`<module name>.<function name>(<parameters>)`), constants (`<module name>.<constant name>`), or any other global names imported as part of a module.:

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

import string

# This is a constant provided by the *string* module.
>>> alphabet = string.ascii_lowercase
>>> print(alphabet)
"abcdefghijklmnopqrstuvwxyz"
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
[assignment statements]: https://docs.python.org/3/reference/simple_stmts.html#assignment-statements
[calls]: https://docs.python.org/3/reference/expressions.html#calls
[classes]: https://docs.python.org/3/reference/datamodel.html#classes
[comments]: https://realpython.com/python-comments-guide/#python-commenting-basics
[default arguments]: https://docs.python.org/3/tutorial/controlflow.html#default-argument-values
[docstring]: https://docs.python.org/3/tutorial/controlflow.html#tut-docstrings
[doctests]: https://docs.python.org/3/library/doctest.html
[duck typing]: https://en.wikipedia.org/wiki/Duck_typing
[dynamic typing in python]: https://stackoverflow.com/questions/11328920/is-python-strongly-typed
[everythings an object]: https://docs.python.org/3/reference/datamodel.html
[facts-and-myths-about-python-names]: https://nedbatchelder.com/text/names.html
[function definition]: https://docs.python.org/3/tutorial/controlflow.html#defining-functions
[functions]: https://docs.python.org/3/reference/compound_stmts.html#function
[gradual typing]: https://en.wikipedia.org/wiki/Gradual_typing
[indentation]: https://docs.python.org/3/reference/lexical_analysis.html#indentation
[method objects]: https://docs.python.org/3/c-api/method.html#method-objects
[module]: https://docs.python.org/3/tutorial/modules.html
[more on functions]: https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions
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
[snake case]: https://en.wikipedia.org/wiki/Snake_case
[the zen of python]: https://www.python.org/dev/peps/pep-0020/
[turtles all the way down]: https://en.wikipedia.org/wiki/Turtles_all_the_way_down
[type hints]: https://docs.python.org/3/library/typing.html
[variables]: https://realpython.com/python-variables/
[what is pythonic]: https://blog.startifact.com/posts/older/what-is-pythonic.html
