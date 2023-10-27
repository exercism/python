# Hints

## General

- [The Python Tutorial][the python tutorial] can be a great introduction.
- [PEP 8][pep8] is the Python code style guide.
- [PEP 257][PEP257] details Python docstring conventions.
- [Numbers][numbers] in Python can be integers, floats, or complex.


## 1. Define expected bake time in minutes

- You need to [name][naming] a constant, and [assign][assignment] it an [integer][numbers] value.

## 2. Calculate remaining bake time in minutes

- You need to define a [function][defining functions] with a single parameter representing the time elapsed so far.
- Use the [mathematical operator for subtraction][numbers] to subtract values.
- This function should [return a value][return].

## 3. Calculate preparation time in minutes

- You need to define a [function][defining functions] with a single parameter representing the number of layers.
- Use the [mathematical operator for multiplication][numbers] to multiply values.
- You could define an extra _constant_ for the time in minutes per layer rather than using a "magic number" in your code.
- This function should [return a value][return].

## 4. Calculate total elapsed cooking time (prep + bake) in minutes

- You need to define a [function][defining functions] with two parameters.
- Remember: you can always _call_ a function you've defined previously.
- You can use the [mathematical operator for addition][python as a calculator] to sum values.
- This function should [return a value][return].

## 5. Update the recipe with notes

- Clearly [commenting][comments] and [documenting][docstrings] your code according to [PEP257][pep257] is always recommended.

[assignment]: https://docs.python.org/3/reference/simple_stmts.html#grammar-token-assignment-stmt
[comments]: https://realpython.com/python-comments-guide/
[defining functions]: https://docs.python.org/3/tutorial/controlflow.html#defining-functions
[docstrings]: https://docs.python.org/3/tutorial/controlflow.html#tut-docstrings
[naming]: https://realpython.com/python-variables/
[numbers]: https://docs.python.org/3/tutorial/introduction.html#numbers
[pep257]: https://www.python.org/dev/peps/pep-0257/
[python as a calculator]: https://docs.python.org/3/tutorial/introduction.html#using-python-as-a-calculator
[return]: https://docs.python.org/3/reference/simple_stmts.html#return
[the python tutorial]: https://docs.python.org/3/tutorial/introduction.html
