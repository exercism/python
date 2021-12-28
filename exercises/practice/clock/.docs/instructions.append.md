# Instructions append

## Representing your class

When working with and debugging objects, it's important to have a string representation of that object.
For example, if you were to create a `datetime.datetime` object in a REPL environment, you can see its string representation:

```python
>>> from datetime import datetime
>>> datetime(2022, 5, 4)
datetime.datetime(2022, 5, 4, 0, 0)
```

In this excersise, you will create a custom object, `Clock`, that handles times without dates.
To do this in Python, you would create a `class` to to implement the desired behavior.

One aspect of a class's behavior is how it is represented as a string.
By default, a class's string representation is not very helpful.

```python
>>> Clock(12, 34)
<Clock object st 0x... >
```

To create a more helpful representation, you need to define a `__repr__` method on your class that returns a string.

According to the [specification for a `__repr__` method](https://docs.python.org/3/reference/datamodel.html#object.__repr__), you should ideally have the method return valid Python code that could be used to recreate the object.
That allows you to copy-paste the output directly into code or the REPL.

For example, a `Clock` that represents 11:30 AM could look like this: `Clock(11, 30)`.

Defining a `__repr__` method is good practice for all classes.
When you do, you should consider:

- The information you're returning from this method will be beneficial when you're debugging issues.
- Ideally, you should return a string that is valid Python code.
- If that is not practical, return a description between angle brackets: `< ...a practical description... >`.


### String conversion

In addition to the `__repr__` method, sometimes you'll want an alternative string representation.
This might be used to format the object for program output.
For example, let's look at the `datetime.datetime` class again:

```python
>>> str(datetime.datetime(2022, 5, 4))
'2022-05-04 00:00:00'
```

When a `datetime` object is askes to convert itself to a string, it returns a string formatted according to the ISO 8601 standard, which can be parsed by most datetime libraries.

In this exercise, you will get to write a `__str__` method, too.

```python
>>> str(Clock(11, 30))
'11:30'
```

To support this string conversion, you will need to create a `__str__` method on your class.
