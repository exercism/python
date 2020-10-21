[Python](https://docs.python.org/3/) is a [dynamic and strongly](https://stackoverflow.com/questions/11328920/is-python-strongly-typed) typed [object-oriented](https://en.wikipedia.org/wiki/Object-oriented_programming) programming language. As of version 3.5, it employs both [duck typing](https://en.wikipedia.org/wiki/Duck_typing) and [gradual typing](https://en.wikipedia.org/wiki/Gradual_typing), via [type hints](https://docs.python.org/3/library/typing.html). It supports both imperative (_object-oriented, procedural_) and declarative (_functional, concurrent_) programming paradigms. But do not be fooled: while programming in other paradigms is fully _supported_, [everything in Python is an object](https://docs.python.org/3/reference/datamodel.html).

Python was created by Guido van Rossum and first released in 1991. The [Python Software Foundation](https://www.python.org/psf/) manages and directs resources for Python and CPython development and receives proposals for changes to the language from [members](https://www.python.org/psf/membership/) of the community via [Python Enhancement Proposals or PEPs](https://www.python.org/dev/peps/).

Python puts a strong emphasis on code readability and (_similar to Haskell_) uses [significant indentation](https://docs.python.org/3/reference/lexical_analysis.html#indentation) to denote function, method, and class definitions. The [zen of Python (PEP 20)](https://www.python.org/dev/peps/pep-0020/) lays out additional inspiration and philosophy.

Objects are [assigned](https://docs.python.org/3/reference/simple_stmts.html#assignment-statements) to [names](https://docs.python.org/3/reference/executionmodel.html#naming-and-binding) in Python via the `=` or _assignment operator_. [Variables](https://realpython.com/python-variables/) are written in [`snake_case`](https://en.wikipedia.org/wiki/Snake_case), and _constants_ usually in `SCREAMING_SNAKE_CASE`. A name (_variable or constant_) is not itself _typed_, and can be attached or re-attached to different objects over its lifetime. For extended naming conventions and advice, see [PEP 8](https://www.python.org/dev/peps/pep-0008/).

```python
>>> my_first_variable = 1
>>> my_first_variable = "Last one, I promise"
>>> print(my_first_variable)
"Last one, I promise"
```

Constants are usually defined on a [module](https://docs.python.org/3/tutorial/modules.html) or _global_ level, and although they _can_ be changed, they are _intended_ to be named only once. Their `SCREAMING_SNAKE_CASE` is a message to other developers that the assignment should not be altered:

```python
# All caps signal that this is intended as a constant
MY_FIRST_CONSTANT = 16

# Re-assignment will be allowed by the compiler & interpreter,
# but is VERY strongly discouraged.
# Please don't do: MY_FIRST_CONSTANT = "Some other value"
```

In Python, units of functionality are encapsulated in [functions](https://docs.python.org/3/reference/compound_stmts.html#function), which are themselves [objects](https://docs.python.org/3/reference/datamodel.html#the-standard-type-hierarchy) (_Its [turtles all the way down](https://en.wikipedia.org/wiki/Turtles_all_the_way_down)_).

Functions can be executed by themselves, passed as arguments to other functions, nested, or bound to a class. When functions are bound to a [class](https://docs.python.org/3/reference/datamodel.html#classes) name, they're referred to as [methods](https://docs.python.org/3/c-api/method.html#method-objects). Related functions and classes (_with their methods_) can be grouped together in the same file or [module](https://docs.python.org/3/reference/datamodel.html#modules), and imported in part or in whole for use in other programs.

The keyword `def` begins a [function definition](https://docs.python.org/3/tutorial/controlflow.html#defining-functions). It must be followed by the function name and a parenthesized list of zero or more formal [parameters](https://docs.python.org/3/glossary.html#term-parameter), which can be of several different varieties, and even [vary](https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions) in length.

The `def` line is terminated with a colon. Statements for the _body_ of the function begin on the next line, and must be _indented in a block_. There is no strict indentation amount (_either space **OR** [tab] characters are acceptable_), but [indentation](https://docs.python.org/3/reference/lexical_analysis.html#indentation) must be _consistent for all indented statements_. Functions explicitly return a value or object via the [`return`](https://docs.python.org/3/reference/simple_stmts.html#return) keyword. Functions that do not have an explicit `return` expression will return [`None`](https://docs.python.org/3/library/constants.html):

```python
#function definition on first line.
def add_two_numbers(number_one, number_two):
    return number_one + number_two  #returns the sum of the numbers

>>> add_two_numbers(3, 4)
7

#this function has no return keyword, and so will return None
def multiply_two_numbers(number_one, number_two):
    result = number_one * number_two

>>> print(multiply_two_numbers(6, 8))
None
```

Functions are [called](https://docs.python.org/3/reference/expressions.html#calls) using their name followed by `()`. The number of arguments passed in the parentheses must match the number of parameters in the original function definition unless [default arguments](https://docs.python.org/3/tutorial/controlflow.html#default-argument-values) have been used:

```python
def number_to_the_power_of(number_one, number_two):
    '''Returns float or int.

       Takes number_one and raises it to the power of number_two, returning the result.
    '''

    return number_one ** number_two

>>> number_to_the_power_of(3,3)
27

>>> number_to_the_power_of(4,)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: number_to_the_power_of() missing 1 required positional argument: 'number_two'

...

def number_to_the_power_of_default(number_one, number_two=2):
    '''Returns float or int.

       Takes number_one and raises it to the power of number_two, returning the result.
    '''

    return number_one ** number_two

>>> number_to_the_power_of_default(4)
16
```

Methods bound to class names are invoked via _dot notation_ (`.`), as are functions, constants, or global names imported as part of a _module_.:

```python
import string

#this is a constant provided by the *string* module
>>> print(string.ascii_lowercase)
"abcdefghijklmnopqrstuvwxyz"

#this is a method call of the str *class*
>>> start_text = "my silly sentence for examples."
>>> str.upper(start_text)
"MY SILLY SENTENCE FOR EXAMPLES."

#this is a method call of an *instance* of the str *class*
>>> start_text.upper()
"MY SILLY SENTENCE FOR EXAMPLES."
```

[Comments](https://realpython.com/python-comments-guide/#python-commenting-basics) in Python start with a `#` that is not part of a string, and end at line termination. Unlike many other programming languages, Python does not support multi-line comment marks. Each line of a comment block must start with the `#` character. Comments are ignored by the interpreter:

```python
#this is a single line comment

x = "foo"  #this is an in-line comment

#this is a multi-line
#comment block over multiple lines
#these should be used sparingly
```

The first statement of a function body can optionally be a [docstring](https://docs.python.org/3/tutorial/controlflow.html#tut-docstrings), which concisely summarizes the function or object's purpose. These docstrings are read by automated documentation tools, and are returned by calling `__doc__` on the function, method, or class. They are recommended for programs of any size where documentation is needed:

```python
#an example on a user-defined function
def number_to_the_power_of(number_one, number_two):
    '''Returns float or int.

       Takes number_one and raises it to the power of number_two, returning the result.
    '''

    return number_one ** number_two

>>> print(number_to_the_power_of.__doc__)
Returns float or int.

       Takes number_one and raises it to the power of number_two, returning the result.

#an example for a built-in type: str
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

Docstrings can also include [doctests](https://docs.python.org/3/library/doctest.html), which are interactive examples of how a method or function should work. Doctests can be read and run by PyTest, or by importing the `doctest` module.
