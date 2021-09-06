# Hints

## General

- [The Python Tutorial][the python tutorial] can be a great introduction.
- [Numbers][numbers] in Python can be integers, floats, or complex.

## 1. Define expected bake time in minutes

- You need to [name][naming] a constant, and [assign][assignment] it an integer value.

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

- You need to define a [function][defining-functions] with two parameters.
- Remember: you can always _call_ a function you've defined previously.
- You can use the [mathematical operator for addition][python as a calculator] to sum values.
- This function should [return a value][return].

## 5. Update the recipe with notes

- Clearly [commenting][comments] and [documenting][docstrings] your code according to [PEP257][PEP257] is always recommended.

[the python tutorial]: https://docs.python.org/3/tutorial/introduction.html
[numbers]: https://docs.python.org/3/tutorial/introduction.html#numbers
[naming]: https://realpython.com/python-variables/
[assignment]: https://docs.python.org/3/reference/simple_stmts.html#grammar-token-assignment-stmt
[defining functions]: https://docs.python.org/3/tutorial/controlflow.html#defining-functions
[return]: https://docs.python.org/3/reference/simple_stmts.html#return
[python as a calculator]: https://docs.python.org/3/tutorial/introduction.html#using-python-as-a-calculator
[comments]: https://realpython.com/python-comments-guide/
[docstrings]: https://docs.python.org/3/tutorial/controlflow.html#tut-docstrings
[PEP257]: https://www.python.org/dev/peps/pep-0257/