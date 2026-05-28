# Instructions append

## How this exercise is structured for the Python track

The tests for this exercise expect your solution to be implemented as a RelativeDistance `class` in Python.
If you are unfamiliar with `class`es in Python, [concept:python/classes]() and [classes][classes in python] (_from the Python docs_) are good places to start.


`RelativeDistance` should be initialized (_see [__init__()][init] for more information_)_ using `family_tree`, a dictionary where the `keys` are individuals and `values` are `list`s of that individual's children.
You will also need to implement a `degree_of_separation` [method][methods] which will return the degree of separation between `person_a` and `person_b` who are individuals in the passed-in family tree.


You are given a stubbed implementation for the `__init__` [special method][special-methods] used to create an instance of the `RelativeDistance` class, as well as a stub of the `degree_of_separation` method.
First, you will need to customize the `__init__` with an appropriate attribute on `self` (_the instance_) to represent the `family_tree` data.
Then you can add your logic to the `degree_of_separation` method to calculate the degree of separation between `person_a` and `person_b`.


## Exception messages

Sometimes it is necessary to [raise an exception](https://docs.python.org/3/tutorial/errors.html#raising-exceptions).
When you do this, you should always include a **meaningful error message** to indicate what the source of the error is.
This makes your code more readable and helps significantly with debugging.
For situations where you know that the error source will be a certain type, you can choose to raise one of the [built in error types](https://docs.python.org/3/library/exceptions.html#base-classes), but should still include a meaningful message.

This particular exercise requires that you use the [raise statement](https://docs.python.org/3/reference/simple_stmts.html#the-raise-statement) to "throw" multiple `ValueError`s.
In the first scenario, you will need to raise a `ValueError` when either one or both of the people passed to the `RelativeDistance.degree_of_separation` method are not present in the family tree.
If both people are present in the family tree, you will need to raise a `ValueError` when there is no valid connection between them as defined by the rules.
The tests will only pass if you both `raise` the expected `exception` type and include the expected message with it.

Please check the tests and their expected results carefully, as these instructions are not exhaustive.


[classes in python]: https://docs.python.org/3/tutorial/classes.html
[init]: https://docs.python.org/3/reference/datamodel.html#object.__init__
[methods]: https://docs.python.org/3/tutorial/classes.html#class-definition-syntax
[special-methods]: https://docs.python.org/3.11/reference/datamodel.html#special-method-names
