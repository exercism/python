# basics

[Python][python docs] is a [dynamic and strongly][dynamic typing in python] typed [object-oriented][object oriented programming] programming language.
It employs both [duck typing][duck typing] and [gradual typing][gradual typing], via [type hints][type hints].
It supports multiple programming paradigms including both imperative (_object-oriented, procedural_) and declarative (_functional, concurrent_) flavors.
But do not be fooled: while programming across paradigms is fully _supported_, [everything in Python is an object][everythings an object].

Python was created by Guido van Rossum and first released in 1991. The [Python Software Foundation][psf] manages and directs resources for Python and CPython development and receives proposals for changes to the language from [members][psf membership] of the community via [Python Enhancement Proposals or PEPs][peps].

Python puts a strong emphasis on code readability and (_similar to Haskell_) uses [significant indentation][significant indentation] to denote function, method, and class definitions.
The [zen of Python (PEP 20)][the zen of python] and [What is Pythonic?][what is pythonic] lay out additional philosophies.

Complete documentation for the current release can be found at [docs.python.org][python docs].

- [Python Tutorial][python tutorial]
- [Python Library Reference][python library reference]
- [Python Language Reference][python language reference]
- [Python HOW TOs][python how tos]
- [Python FAQs][python faqs]
- [Python Glossary of Terms][python glossary of terms]


## Getting Started

Objects are [assigned][assignment statements] to [names][naming and binding] in Python via the `=` or _assignment operator_. [Variables][variables] are written in [`snake_case`][snake case], and constants usually in `SCREAMING_SNAKE_CASE`.

A `name` (_variable or constant_) is not itself typed, and can be attached or re-attached to different objects or values over its lifetime.
For extended naming conventions and formatting advice, see [PEP 8][pep8].

```python
>>> my_first_variable = 1
>>> my_first_variable = "Last one, I promise"
>>> print(my_first_variable)

"Last one, I promise"
```

Constants are usually defined on a [module][module] or `global` level, and although they _can_ be changed, they are _intended_ to be assigned only once.

Their `SCREAMING_SNAKE_CASE` is a message to other developers that the assignment should not be altered.

```python
# All caps signal that this is intended as a constant
MY_FIRST_CONSTANT = 16

# Re-assignment will be allowed by the compiler & interpreter,
# but is VERY strongly discouraged.
# Please don't do: MY_FIRST_CONSTANT = "Some other value"
```

In Python, units of functionality are encapsulated in [_functions._][functions], which are themselves [objects][objects] (_Its [turtles all the way down][turtles all the way down]_).

Functions can be executed by themselves, passed as arguments to other functions, nested, or bound to a class.
When functions are bound to a [class][classes] name, they're referred to as [methods][method objects].
Related functions and classes (_with their methods_) can be grouped together in the same file or module, and imported in part or in whole for use in other programs.

The keyword `def` begins a [function definition][function definition].
`def` must be followed by the function name and a parenthesized list of zero or more formal [parameters][parameters].
 Parameters can be of several different varieties, and can even [vary][more on functions] in length.
The `def` line is terminated with a colon (`:`).

Statements for the `function body` begin on the line following `def`, and must be _indented in a block_.
There is no strict indentation amount (_either space **OR** [tab] characters are acceptable_), but [indentation][indentation] must be _consistent for all indented statements_.
Functions explicitly return a value or object via the [`return`][return] keyword.

```python
# Function definition on first line.
>>> def add_two_numbers(number_one, number_two):
...   return number_one + number_two  # Returns the sum of the numbers, and is indented by 2 spaces.

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

Inconsistent indentation will raise an error:

```python
# The return statement line does not match the first line indent.
>>> def add_three_numbers_misformatted(number_one, number_two, number_three):
...     result = number_one + number_two + number_three   # Indented by 4 spaces.
...    return result     #this was only indented by 3 spaces
  File "<stdin>", line 3
    return result
                ^
IndentationError: unindent does not match any outer indentation level
```

Functions are [_called_][calls] using their name followed by `()`.
The number of arguments passed in the parentheses must match the number of parameters in the original function definition unless [default arguments][default arguments] have been used.

```python
>>> def number_to_the_power_of(number_one, number_two):
        """Raise a number to an arbitrary power.
        
        :param number_one: int the base number.
        :param number_two: int the power to raise the base number to.
        :return: int - number raised to power of second number
        
        Takes number_one and raises it to the power of number_two, returning the result.
        """

...     return number_one ** number_two


>>> number_to_the_power_of(3,3)
27
```

A mis-match between parameters and arguments will raise an error:

```python
>>> number_to_the_power_of(4,)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: number_to_the_power_of() missing 1 required positional argument: 'number_two'

```

Adding a [default value][default arguments] for a parameter can defend against such errors:

```python
def number_to_the_power_of_default(number_one, number_two=2):
    """Raise a number to an arbitrary power.
    
    :param number_one: int the base number.
    :param number_two: int the power to raise the base number to.
    :return: int - number raised to power of second number
    
    Takes number_one and raises it to the power of number_two, returning the result.
    """

    return number_one ** number_two

>>> number_to_the_power_of_default(4)
16
```

Methods bound to class names are invoked via dot notation (`<class_name>.<method_name>()`), as are functions, constants, or global names imported as part of a module.:

```python

import string

# This is a constant provided by the *string* module.
>>> print(string.ascii_lowercase)
"abcdefghijklmnopqrstuvwxyz"

# This is a method call of the str *class*.
>>> start_text = "my silly sentence for examples."
>>> str.upper(start_text)
"MY SILLY SENTENCE FOR EXAMPLES."

# This is a method call of an *instance* of the str *class*.
>>> start_text.upper()
"MY SILLY SENTENCE FOR EXAMPLES."
```

[Comments][comments] in Python start with a `#` that is not part of a string, and end at line termination.
Unlike many other programming languages, Python does not support multi-line comment marks.
Each line of a comment block must start with the `#` character.
Comments are ignored by the interpreter:

```python
# This is a single line comment.

x = "foo"  # This is an in-line comment.

# This is a multi-line
# comment block over multiple lines --
# these should be used sparingly.
```

The first statement of a function body can optionally be a [_docstring_][docstring], which concisely summarizes the function or object's purpose.
Docstrings are read by automated documentation tools and are returned by calling `.__doc__` on the function, method, or class name.
They are recommended for programs of any size where documentation is needed, and their conventions are laid out in [PEP257][PEP257]:


```python
# An example on a user-defined function.
def number_to_the_power_of(number_one, number_two):
    """Raise a number to an arbitrary power.
    
    :param number_one: int the base number.
    :param number_two: int the power to raise the base number to.
    :return: int - number raised to power of second number
    
    Takes number_one and raises it to the power of number_two, returning the result.
    """

    return number_one ** number_two

>>> print(number_to_the_power_of.__doc__)
Returns float or int.

       Takes number_one and raises it to the power of number_two, returning the result.

# __doc__() for the built-in type: str.
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

Docstrings can also include [doctests][doctests], which are interactive examples of how a method or function should work.
Doctests can be read and run by PyTest, or by importing the `doctest` module.

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
[function definition]: https://docs.python.org/3/tutorial/controlflow.html#defining-functions
[functions]: https://docs.python.org/3/reference/compound_stmts.html#function
[gradual typing]: https://en.wikipedia.org/wiki/Gradual_typing
[indentation]: https://docs.python.org/3/reference/lexical_analysis.html#indentation
[method objects]: https://docs.python.org/3/c-api/method.html#method-objects
[module]: https://docs.python.org/3/tutorial/modules.html
[more on functions]: https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions
[naming and binding]: https://docs.python.org/3/reference/executionmodel.html#naming-and-binding
[none]: https://docs.python.org/3/library/constants.html
[object oriented programming]: https://en.wikipedia.org/wiki/Object-oriented_programming
[objects]: https://docs.python.org/3/reference/datamodel.html#the-standard-type-hierarchy
[parameters]: https://docs.python.org/3/glossary.html#term-parameter
[pep8]: https://www.python.org/dev/peps/pep-0008/
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
