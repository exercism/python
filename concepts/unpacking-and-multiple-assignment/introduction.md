# Unpacking and Multiple Assignment

Unpacking refers to the act of extracting the elements of a collection, such as a `list`, `tuple`, or `dict`, using iteration.
Unpacked values can then be assigned to variables within the same statement.
A very common example of this behavior is `for item in list`, where `item` takes on the value of each `list` element in turn throughout the iteration.

[Multiple assignment][multiple assignment] is the ability to assign multiple variables to unpacked values within one statement.
This allows for code to be more concise and readable, and is done by separating the variables to be assigned with a comma such as `first, second, third = (1,2,3)` or `for index, item in enumerate(iterable)`.

The special operators `*` and `**` are often used in unpacking contexts.
`*` can be used to combine multiple `lists`/`tuples` into one `list`/`tuple` by _unpacking_ each into a new common `list`/`tuple`.
`**` can be used to combine multiple dictionaries into one dictionary by _unpacking_ each into a new common `dict`.

When the `*` operator is used without a collection,it _packs_ a number of values into a `list`.
This is often used in multiple assignment to group all "leftover" elements that do not have individual assignments into a single variable.

It is common in Python to also exploit this unpacking/packing behavior when using or defining functions that take an arbitrary number of positional or keyword arguments.
You will often see these "special" parameters defined as `def some_function(*args, **kwargs)` and the "special" arguments used as `some_function(*some_tuple, **some_dict)`.


```exercism/caution
`*<variable_name>` and `**<variable_name>` should not be confused with `*` and `**`. While `*` and `**` are used for multiplication and exponentiation respectively, `*<variable_name>` and `**<variable_name>` are used as packing and unpacking operators.
```


[multiple assignment]: https://www.geeksforgeeks.org/assigning-multiple-variables-in-one-line-in-python/
