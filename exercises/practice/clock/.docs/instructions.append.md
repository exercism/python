# Instructions append


## How this exercise is implemented for the Python track


The tests for this exercise expect that your clock will be implemented in a `Clock` `class`.
If you are unfamiliar with classes in Python, [concept:python/classes]() and [classes][classes in python] (_from the Python docs_) are good places to start.


## Representing your class

When working with and debugging [objects][what-is-an-object], it's important to have a good representation of that object.
For example — if you were to create a new [`datetime.datetime`][datetime] object in the Python [REPL][REPL] environment, you could view its [string representation][str-rep-classes]:


```python
>>> from datetime import datetime
>>> new_date = datetime(2022, 5, 4)
>>> new_date
datetime.datetime(2022, 5, 4, 0, 0)
```

Your Clock `class` should create a custom `object` that handles times _without_ dates.
One important aspect of this `class` will be how it is represented as a _string_.
Other programmers who use or call Clock `objects` created from the Clock `class` will refer to this string representation for debugging and other activities.
However, the default representation on a custom `class` is not very helpful:


```python
>>> Clock(12, 34)
<Clock object st 0x102807b20 >
```

To create a more helpful representation, you can define a [`__repr__`][repr-method] [special method][dunder-methods] on the `class`.

Ideally, that `__repr__` method returns valid Python code that can be used to recreate the object when passed to [`eval()`][eval-built-in] — as laid out in the [specification for a `__repr__` method][repr-docs].
Returning valid Python code allows another developer to copy-paste the `str` directly into code or the REPL.
A `Clock` that represents 11:30 AM could look like this:

```python
 `Clock(11, 30)`
```

Defining a `__repr__` method is good practice for all custom classes.
Some additional things to consider:

- The information returned from this method should be beneficial when debugging issues.
- _Ideally_, the method returns a string that is valid Python code — although that might not always be possible.
- If valid Python code is not practical, returning a description between angle brackets: `< ...a practical description... >` is the convention.


### String conversion

In addition to the `__repr__` method, there might also be a need for an alternative "human-readable" string representation of the `class`.
This might be used to format the object for program output or documentation.
This is done by writing a [`__str__`][str-dunder] special method.
Looking at `datetime.datetime` again:


```python
>>> str(datetime.datetime(2022, 5, 4))
'2022-05-04 00:00:00'
```

When a `datetime` object is asked to convert itself to a string representation, it returns a `str` formatted according to the [ISO 8601 standard][ISO 8601], which can be parsed by most datetime libraries into a human-readable date and time.

In this exercise, you will get a chance to write a `__str__` method for your Clock, as well as a `__repr__` method.

```python
>>> str(Clock(11, 30))
'11:30'
```

To support this string conversion, you will need to create a `__str__` special method on your `class` that returns a more "human-readable" string showing the Clock time.

If you don't create a `__str__` method and you call `str()` on your class, Python will try calling `__repr__` on your class as a fallback.
So if you only implement one of these two special methods, it would be better to create a `__repr__` rather than just a `__str__`.


[ISO 8601]: https://www.iso.org/iso-8601-date-and-time-format.html
[REPL]: https://pythonprogramminglanguage.com/repl/
[classes in python]: https://docs.python.org/3/tutorial/classes.html
[datetime]: https://docs.python.org/3/library/datetime.html#available-types
[dunder-methods]: https://www.pythonmorsels.com/every-dunder-method/
[eval-built-in]: https://docs.python.org/3/library/functions.html#eval
[repr-docs]: https://docs.python.org/3/reference/datamodel.html#object.__repr__
[repr-method]: https://docs.python.org/3/library/functions.html#repr
[str-dunder]: https://docs.python.org/3/reference/datamodel.html#object.__str__
[str-rep-classes]: https://www.digitalocean.com/community/tutorials/python-str-repr-functions#introduction
[what-is-an-object]: https://realpython.com/ref/glossary/object/
