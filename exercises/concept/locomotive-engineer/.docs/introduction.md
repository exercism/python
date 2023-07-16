# Unpacking and Multiple Assignment

Unpacking refers to the act of extracting the elements of a collection, such as a `list`, `tuple`, or `dict`, using iteration.
Unpacked values can then be assigned to variables within the same statement, which is commonly referred to as [Multiple assignment][multiple assignment].

The special operators `*` and `**` are often used in unpacking contexts and with multiple assignment.

~~~~exercism/caution
`*<variable_name>` and `**<variable_name>` should not be confused with `*` and `**`. While `*` and `**` are used for multiplication and exponentiation respectively, `*<variable_name>` and `**<variable_name>` are used as packing and unpacking operators.
~~~~

## Multiple assignment

In multiple assignment, the number of variables on the left side of the assignment operator (`=`) must match the number of values on the right side.
To separate the values, use a comma `,`:

```python
>>> a, b = 1, 2
>>> a
1
```

If the multiple assignment gets an incorrect number of variables for the values given, a `ValueError` will be thrown:

```python
>>> x, y, z = 1, 2

ValueError: too many values to unpack (expected 3, got 2)
```

Multiple assignment is not limited to one data type:

```python
>>> x, y, z = 1, "Hello", True
>>> x
1

>>> y
'Hello'

>>> z
True
```

Multiple assignment can be used to swap elements in `lists`.
This practice is pretty common in [sorting algorithms][sorting algorithms].
For example:

```python
>>> numbers = [1, 2]
>>> numbers[0], numbers[1] = numbers[1], numbers[0]
>>> numbers
[2, 1]
```

Since `tuples` are immutable, you can't swap elements in a `tuple`.

## Unpacking

~~~~exercism/note
The examples below use `lists` but the same concepts apply to `tuples`.
~~~~

In Python, it is possible to [unpack the elements of `list`/`tuple`/`dictionary`][unpacking] into distinct variables.
Since values appear within `lists`/`tuples` in a specific order, they are unpacked into variables in the same order:

```python
>>> fruits = ["apple", "banana", "cherry"]
>>> x, y, z = fruits
>>> x
"apple"
```

If there are values that are not needed then you can use `_` to flag them:

```python
>>> fruits = ["apple", "banana", "cherry"]
>>> _, _, z = fruits
>>> z
"cherry"
```

### Deep unpacking

Unpacking and assigning values from a `list`/`tuple` inside of a `list` or `tuple` (_also known as nested lists/tuples_), works in the same way a shallow unpacking does, but often needs qualifiers to clarify the values context or position:

```python
>>> fruits_vegetables = [["apple", "banana"], ["carrot", "potato"]]
>>> [[a, b], [c, d]] = fruits_vegetables
>>> a
"apple"

>>> d
"potato"
```

You can also deeply unpack just a portion of a nested `list`/`tuple`:

```python
>>> fruits_vegetables = [["apple", "banana"], ["carrot", "potato"]]
>>> [a, [c, d]] = fruits_vegetables
>>> a
["apple", "banana"]

>>> c
"carrot"
```

If the unpacking has variables with incorrect placement and/or an incorrect number of values, you will get a `ValueError`:

```python
>>> fruits_vegetables = [["apple", "banana"], ["carrot", "potato"]]
>>> [[a, b], [d]] = fruits_vegetables

ValueError: too many values to unpack (expected 1)
```

### Unpacking a list/tuple with `*`

When [unpacking a `list`/`tuple`][packing and unpacking] you can use the `*` operator to capture the "leftover" values.
This is clearer than slicing the `list`/`tuple` (_which in some situations is less readable_).
For example, we can extract the first element and then assign the remaining values into a new `list` without the first element:

```python
>>> fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
>>> x, *last = fruits
>>> x
"apple"

>>> last
["banana", "cherry", "orange", "kiwi", "melon", "mango"]
```

We can also extract the values at the beginning and end of the `list` while grouping all the values in the middle:

```python
>>> fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
>>> x, *middle, y, z = fruits
>>> y
"melon"

>>> middle
["banana", "cherry", "orange", "kiwi"]
```

We can also use `*` in deep unpacking:

```python
>>> fruits_vegetables = [["apple", "banana", "melon"], ["carrot", "potato", "tomato"]]
>>> [[a, *rest], b] = fruits_vegetables
>>> a
"apple"

>>> rest
["banana", "melon"]
```

### Unpacking a dictionary

[Unpacking a dictionary][packing and unpacking] is a bit different than unpacking a `list`/`tuple`.
Iteration over dictionaries defaults to the **keys**.
So when unpacking a `dict`, you can only unpack the **keys** and not the **values**:

```python
>>> fruits_inventory = {"apple": 6, "banana": 2, "cherry": 3}
>>> x, y, z = fruits_inventory
>>> x
"apple"
```

If you want to unpack the values then you can use the `values()` method:

```python
>>> fruits_inventory = {"apple": 6, "banana": 2, "cherry": 3}
>>> x, y, z = fruits_inventory.values()
>>> x
6
```

If both **keys** and **values** are needed, use the `items()` method.
Using `items()` will generate tuples with **key-value** pairs.
This is because of [`dict.items()` generates an iterable with key-value `tuples`][items].

```python
>>> fruits_inventory = {"apple": 6, "banana": 2, "cherry": 3}
>>> x, y, z = fruits_inventory.items()
>>> x
("apple", 6)
```

## Packing

[Packing][packing and unpacking] is the ability to group multiple values into one `list` that is assigned to a variable.
This is useful when you want to _unpack_ values, make changes, and then _pack_ the results back into a variable.
It also makes it possible to perform merges on 2 or more `lists`/`tuples`/`dicts`.

### Packing a list/tuple with `*`

Packing a `list`/`tuple` can be done using the `*` operator.
This will pack all the values into a `list`/`tuple`.

```python
>>> fruits = ("apple", "banana", "cherry")
>>> more_fruits = ["orange", "kiwi", "melon", "mango"]

# fruits and more_fruits are unpacked and then their elements are packed into combined_fruits
>>> combined_fruits = *fruits, *more_fruits

# If there is no * on to the left of the "=" the result is a tuple
>>> combined_fruits
("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")

# If the * operator is used on the left side of "=" the result is a list
>>> *combined_fruits_too, = *fruits, *more_fruits
>>> combined_fruits_too
['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']
```

### Packing a dictionary with `**`

Packing a dictionary is done by using the `**` operator.
This will pack all **key**-**value** pairs from one dictionary into another dictionary, or combine two dictionaries together.

```python
>>> fruits_inventory = {"apple": 6, "banana": 2, "cherry": 3}
>>> more_fruits_inventory = {"orange": 4, "kiwi": 1, "melon": 2, "mango": 3}

# fruits_inventory and more_fruits_inventory are unpacked into key-values pairs and combined.
>>> combined_fruits_inventory = {**fruits_inventory, **more_fruits_inventory}

# then the pairs are packed into combined_fruits_inventory
>>> combined_fruits_inventory
{"apple": 6, "banana": 2, "cherry": 3, "orange": 4, "kiwi": 1, "melon": 2, "mango": 3}
```

## Usage of `*` and `**` with functions

### Packing with function parameters

When you create a function that accepts an arbitrary number of arguments, you can use [`*args` or `**kwargs`][args and kwargs] in the function definition.
`*args` is used to pack an arbitrary number of positional (non-keyworded) arguments and
`**kwargs` is used to pack an arbitrary number of keyword arguments.

Usage of `*args`:

```python
# This function is defined to take any number of positional arguments

>>> def my_function(*args):
...     print(args)

# Arguments given to the function are packed into a tuple

>>> my_function(1, 2, 3)
(1, 2, 3)

>>> my_function("Hello")
("Hello")

>>> my_function(1, 2, 3, "Hello", "Mars")
(1, 2, 3, "Hello", "Mars")
```

Usage of `**kwargs`:

```python
# This function is defined to take any number of keyword arguments

>>> def my_function(**kwargs):
...   print(kwargs)

# Arguments given to the function are packed into a dictionary

>>> my_function(a=1, b=2, c=3)
{"a": 1, "b": 2, "c": 3}
```

`*args` and `**kwargs` can also be used in combination with one another:

```python
>>> def my_function(*args, **kwargs):
...   print(sum(args))
...   for key, value in kwargs.items():
...       print(str(key) + " = " + str(value))

>>> my_function(1, 2, 3, a=1, b=2, c=3)
6
a = 1
b = 2
c = 3
```

You can also write parameters before `*args` to allow for specific positional arguments.
Individual keyword arguments then have to appear before `**kwargs`.

~~~~exercism/caution
[Arguments have to be structured](https://www.python-engineer.com/courses/advancedpython/18-function-arguments/) like this:

`def my_function(<positional_args>, *args, <key-word_args>, **kwargs)`

If you don't follow this order then you will get an error.
~~~~

```python
>>> def my_function(a, b, *args):
...   print(a)
...   print(b)
...   print(args)

>>> my_function(1, 2, 3, 4, 5)
1
2
(3, 4, 5)
```

Writing arguments in an incorrect order will result in an error:

```python
>>>def my_function(*args, a, b):
... print(args)

>>>my_function(1, 2, 3, 4, 5)
Traceback (most recent call last):
  File "c:\something.py", line 3, in <module>
    my_function(1, 2, 3, 4, 5)
TypeError: my_function() missing 2 required keyword-only arguments: 'a' and 'b'
```

### Unpacking into function calls

You can use `*` to unpack a `list`/`tuple` of arguments into a function call.
This is very useful for functions that don't accept an `iterable`:

```python
>>> def my_function(a, b, c):
...   print(c)
...   print(b)
...   print(a)

numbers = [1, 2, 3]
>>> my_function(*numbers)
3
2
1
```

Using `*` unpacking with the `zip()` function is another common use case.
Since `zip()` takes multiple iterables and returns a `list` of `tuples` with the values from each `iterable` grouped:

```python
>>> values = (['x', 'y', 'z'], [1, 2, 3], [True, False, True])
>>> a, *rest = zip(*values)
>>> rest
[('y', 2, False), ('z', 3, True)]
```

[args and kwargs]: https://www.geeksforgeeks.org/args-kwargs-python/
[items]: https://www.geeksforgeeks.org/python-dictionary-items-method/
[multiple assignment]: https://www.geeksforgeeks.org/assigning-multiple-variables-in-one-line-in-python/
[packing and unpacking]: https://www.geeksforgeeks.org/packing-and-unpacking-arguments-in-python/
[sorting algorithms]: https://realpython.com/sorting-algorithms-python/
[unpacking]: https://www.geeksforgeeks.org/unpacking-arguments-in-python/?ref=rp
