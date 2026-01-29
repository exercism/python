# Instructions append

## Class-based solution

The tests for this exercise expect your solution to be implemented as a `RelativeDistance` class in Python.
Your `RelativeDistance` class should be initialized using `family_tree`, a dictionary where the keys are individuals and the values are lists of that individual's children.
You will also need to implement a `degree_of_separation` method which will return the degree of separation between `person_a` and `person_b` who are individuals in the family tree.

If you are unfamiliar with classes in Python, here is a brief overview of how to implement the `RelativeDistance` class:

A class is a blueprint for creating objects, bundling attributes (data) and methods (functionality) together.
In this exercise, you are given stubbed implementations for the `__init__` special method used to create an instance of the `RelativeDistance` class as well as the `degree_of_separation` method.
To access the `family_tree` data from within the `degree_of_separation` method, you will need to first assign it within the `__init__` method to an appropriate attribute on `self`, which represents the current instance of the `RelativeDistance` class.
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

Please check the tests and their expected results carefully.
