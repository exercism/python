# Instructions append

The tests for this exercise expect your clock will be implemented via a Clock `class` in Python.
If you are unfamiliar with classes in Python, [classes][classes in python] from the Python docs is a good place to start.
## Representing your class

When working with and debugging objects, it's important to have a string representation of that object.
For example, if you were to create a new `datetime.datetime` object in the Python [REPL][REPL] environment, you could see its string representation:

```python
>>> from datetime import datetime
>>> new_date = datetime(2022, 5, 4)
>>> new_date
datetime.datetime(2022, 5, 4, 0, 0)

Your Clock `class` will create a custom `object` that handles times without dates.
One important aspect of this `class` will be how it is represented as a _string_.
Other programmers who use or call Clock `objects` created from the Clock `class` will refer to this string representation for debugging and other activities.  
However, the default string representation on a `class` is usually not very helpful.

```python
>>> Clock(12, 34)
<Clock object st 0x102807b20 >
```

To create a more helpful representation, you can define a `__repr__` method on the `class` that returns a string.

Ideally, the `__repr__` method returns valid Python code that can be used to recreate the object -- as laid out in the [specification for a `__repr__` method][repr-docs].
Returning valid Python code allows you to copy-paste the `str` directly into code or the REPL.

For example, a `Clock` that represents 11:30 AM could look like this: `Clock(11, 30)`.

Defining a `__repr__` method is good practice for all classes.
Some things to consider:

- The information returned from this method should be beneficial when debugging issues.
- _Ideally_, the method returns a string that is valid Python code -- although that might not always be possible.
- If valid Python code is not practical, returning a description between angle brackets: `< ...a practical description... >` is the convention.


### String conversion

In addition to the `__repr__` method, there might also be a need for an alternative "human-readable" string representation of the `class`.
This might be used to format the object for program output or documentation.
Looking at `datetime.datetime` again:

```python
>>> str(datetime.datetime(2022, 5, 4))
'2022-05-04 00:00:00'
```

When a `datetime` object is asked to convert itself to a string representation, it returns a `str` formatted according to the [ISO 8601 standard][ISO 8601], which can be parsed by most datetime libraries into a human-readable date and time.

In this exercise, you will get a chance to write a `__str__` method, as well as a `__repr__`.

```python
>>> str(Clock(11, 30))
'11:30'
```

To support this string conversion, you will need to create a `__str__` method on your class that returns a more "human readable" string showing the Clock time.

If you don't create a `__str__` method and you call `str()` on your class, python will try calling `__repr__` on your class as a fallback. So if you only implement one of the two, it would be better to create a `__repr__` method.

[repr-docs]: https://docs.python.org/3/reference/datamodel.html#object.__repr__
[classes in python]: https://docs.python.org/3/tutorial/classes.html
[REPL]: https://pythonprogramminglanguage.com/repl/
[ISO 8601]: https://www.iso.org/iso-8601-date-and-time-format.html

