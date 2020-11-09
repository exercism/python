## basics

[Python][python docs] is a [dynamic and strongly][dynamic typing in python] typed [object-oriented][object oriented programming] programming language. It employs both [duck typing][duck typing] and [gradual typing][gradual typing], via [type hints][type hints]. It supports multiple programming paradigms including both imperative (_object-oriented, procedural_) and declarative (_functional, concurrent_) flavors. But do not be fooled: while programming across paradigms is fully _supported_, [everything in Python is an object][everythings an object].

Python puts a strong emphasis on code readability and (_similar to Haskell_) uses [significant indentation][significant indentation] to denote function, method, and class definitions. The [zen of Python (PEP 20)][the zen of python] lays out additional philosophy, as does the essay [What is Pythonic?][what is pythonic].

### Getting Started

Objects are [assigned][assignment statements] to [names][naming and binding] in Python via the `=` or _assignment operator_. [Variables][variables] are written in [`snake_case`][snake case], and _constants_ usually in `SCREAMING_SNAKE_CASE`. A name (_variable or constant_) is not itself _typed_, and can be attached or re-attached to different objects over its lifetime. For extended naming conventions and advice, see [PEP 8][pep8].

```python
>>> my_first_variable = 1
>>> my_first_variable = "Last one, I promise"
>>> print(my_first_variable)

"Last one, I promise"
```

Constants are usually defined on a [module][module] or _global_ level, and although they _can_ be changed, they are _intended_ to be named only once. Their `SCREAMING_SNAKE_CASE` is a message to other developers that the assignment should not be altered:

```python
# All caps signal that this is intended as a constant
MY_FIRST_CONSTANT = 16

# Re-assignment will be allowed by the compiler & interpreter,
# but is VERY strongly discouraged.
# Please don't do: MY_FIRST_CONSTANT = "Some other value"
```

The keyword `def` begins a [function definition][function definition]. It must be followed by the function name and a parenthesized list of zero or more formal [parameters][parameters], which can be of several different varieties, and even [vary][more on functions] in length. The `def` line is terminated with a colon.

Statements for the _body_ of the function begin on the next line down from `def`, and must be _indented in a block_. There is no strict indentation amount (_either space **OR** [tab] characters are acceptable_), but [indentation][indentation] must be _consistent for all indented statements_. Functions explicitly return a value or object via the [`return`][return] keyword. Functions that do not have an explicit `return` expression will return [`None`][none].

```python
#function definition on first line.
def add_two_numbers(number_one, number_two):
  return number_one + number_two  #returns the sum of the numbers, and is indented by 2 spaces.

>>> add_two_numbers(3, 4)
7

#the return statement line does not match the first line indent
>>> def add_three_numbers_misformatted(number_one, number_two, number_three):
...     result = number_one + number_two + number_three   #indented by 4 spaces
...    return result     #this was only indented by 3 spaces
  File "<stdin>", line 3
    return result
                ^
IndentationError: unindent does not match any outer indentation level
```

Functions are [_called_][calls] using their name followed by `()`. The number of arguments passed in the parentheses must match the number of parameters in the original function definition unless [default arguments][default aruguments] have been used:

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


def number_to_the_power_of_default(number_one, number_two=2):
    '''Returns float or int.
       Takes number_one and raises it to the power of number_two, returning the result.
    '''

    return number_one ** number_two

>>> number_to_the_power_of_default(4)
16
```

Methods bound to class names are invoked via dot notation (.), as are functions, constants, or global names imported as part of a module.:

```python

import string

# this is a constant provided by the *string* module
>>> print(string.ascii_lowercase)
"abcdefghijklmnopqrstuvwxyz"

# this is a method call of the str *class*
>>> start_text = "my silly sentence for examples."
>>> str.upper(start_text)
"MY SILLY SENTENCE FOR EXAMPLES."

# this is a method call of an *instance* of the str *class*
>>> start_text.upper()
"MY SILLY SENTENCE FOR EXAMPLES."
```

[Comments][comments] in Python start with a `#` that is not part of a string, and end at line termination. Unlike many other programming languages, Python does not support multi-line comment marks. Each line of a comment block must start with the `#` character. Comments are ignored by the interpreter:

```python
#this is a single line comment

x = "foo"  #this is an in-line comment

#this is a multi-line
#comment block over multiple lines
#these should be used sparingly
```

The first statement of a function body can optionally be a [_docstring_][docstring], which concisely summarizes the function or object's purpose. These docstrings are read by automated documentation tools, and are returned by calling **doc** on the function, method, or class. . They are recommended for programs of any size where documentation is needed:

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
