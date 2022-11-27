# Unpacking and Multiple Assignment

Unpacking refers to the act of extracting the elements of a collection, such as a `list`, `tuple`, or `dict`, using iteration.
Unpacked values can be assigned to variables within the same step.
With unpacking, there are some special operators used: `*` and `**`.

When unpacking a list or tuple, the `*` operator can be used to assign all the remaining elements to a variable.
When unpacking a dictionary, the `**` operator can be used to assign all the remaining key-value pairs to a variable.
When these operators are used without a collection, they _pack_ a number of values into a `list`, `tuple`, or `dict`.

It is common in Python to also exploit this unpacking/packing behavior when defining functions that take an arbitrary number of positional or keyword arguments.
You will often see these "special" parameters defined as `def some_function(*args, **kwargs)`

[Multiple assignment][multiple assignment] is the ability to assign multiple variables in one line.
This allows for code to be more concise and readable, and is done by separating the variables with a comma.

```exercism/caution
`*<variable_name>` and `**<variable_name>` should not be confused with `*` and `**`. While `*` and `**` are used for multiplication and exponentiation respectively, `*<variable_name>` and `**<variable_name>` are used as packing and unpacking operators.
```

[multiple assignment]: https://www.geeksforgeeks.org/assigning-multiple-variables-in-one-line-in-python/
