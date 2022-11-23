# Unpacking and Multiple Assignment

Unpacking refers to the act of extracting the elements of a collection, such as a `list`, `tuple`, or `dictionary`, using iteration.
Unpacked values can be assigned to variables within the same step.
With unpacking, there are some special operators used: `*` and `**`.
When unpacking a list or tuple, the `*` operator can be used to assign all the remaining elements to a variable.
When unpacking a dictionary, the `**` operator can be used to assign all the remaining key-value pairs to a variable.

When these operators are used without a collection it will pack the number of variables into a list, tuple, or dictionary.
It is common to use this kind of behavior when creating functions that take an arbitrary number of arguments.

Multiple assignment is the ability to assign multiple variables in one line.
This is done by separating the variables with a comma.

```exercism/caution
`*<variable_name>` and `**<variable_name>` should not be confused with `*` and `**`. While `*` and `**` are used for multiplication and exponentiation respectively, `*<variable_name>` and `**<variable_name>` are used as packing and unpacking operators.
```

## Multiple assignment

[Multiple assignment][multiple assignment] is the ability to assign multiple variables in one line.
This allows for code to be more concise and readable.
There has to be x number of variables on the left side of the `=` sign and x number of values on the right side of the `=` sign.
To separate the values, use a comma `,`:

```python
>>> a, b = 1, 2
>>> a
1
```

Multiple assignment is not limited to one data type but can instead be used with any data type.
For example:

```python
>>> a, b, c = 1, "Hello", True
>>> a
1

>>> b
'Hello'

>>> c
True
```

Multiple assignment also allows for the swapping of variables in `lists`.
This practice is pretty common in [linear sorting algorithms][sorting algorithms].
For example:

```python
>>> numbers = [1, 2]
>>> numbers[0], numbers[1] = numbers[1], numbers[0]
>>> numbers
[2, 1]
```

It is also possible to assign multiple variables to the same value:

```python
>>> a = b = 1
>>> a
1
>>> b
1
```

## Unpacking

```exercism/note
The examples below use lists but the same concepts apply to tuples.
```

In Python, it is possible to [unpack a `list`/`tuple`/`dictionary`][unpacking] into distinct variables.
Since values appear within lists in a specific order, it is therefore possible to _unpack_ a `list` into variables in the same order.

Unpacking a list into variables:

```python
>>> fruits = ["apple", "banana", "cherry"]
>>> x, y, z = fruits
>>> x
"apple"
```

If there are values that are not needed then you can use `_` to ignore those values:

```python
>>> fruits = ["apple", "banana", "cherry"]
>>> _, _, z = fruits
>>> z
"cherry"
```

You can also do [deep unpacking][deep unpacking] on a `list`, which assigns values from a `list` within a `list` (_this is also known as nested list unpacking_):

```python
>>> fruits_vegetables = [["apple", "banana"], ["carrot", "potato"]]
>>> [[a, b], [c, d]] = fruits_vegetables
>>> a
"apple"

>>> d
"potato"
```

Deep unpacking and normal unpacking can be mixed together:

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

When [unpacking a `list`/`tuple`][packing and unpacking] you can use the `*` operator to capture the remainder values.
This can be used instead of slicing the `list`/`tuple`, which in some situations could be more readable.
For example, we can extract the first element below and then pack the remaining values into a new `list` without the first element:

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
Iteration over dictionaries defaults to the `keys`.
So when unpacking a `dict`, you can only unpack the `keys` and not the `values`:

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

If both `keys` and `values` are needed, use the `items()` method.
Using `items()` will generate tuples with `key-value` pairs.
This is because [`dict.items()` generates a `tuple`][items] and within it there is a `tuple` for each `key-value` pair:.

```python
>>> fruits_inventory = {"apple": 6, "banana": 2, "cherry": 3}
>>> x, y, z = fruits_inventory.items()
>>> x
("apple", 6)
```


## Packing

As with unpacking, _packing_ uses the same `*` and `**` operators.
[Packing][packing and unpacking]] is the ability to group multiple values into one variable.
This is useful for when you want to _unpack_ values, make changes, and then _pack_ the results back into a variable.
It also makes it possible to perform merges on 2 or more `lists`/`tuples`/`dicts`.

### Packing a list/tuple with `*`

Packing a `list`/`tuple` is done by using the `*` operator
This will pack all the variables into a list/tuple.

```python
>>> fruits = ["apple", "banana", "cherry"]
>>> more_fruits = ["orange", "kiwi", "melon", "mango"]
>>> combined_fruits_lists = [*fruits, *more_fruits]

>>> combined_fruits_lists
["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
```

### Packing a dictionary with `**`

Packing a dictionary is done by using the `**` operator.
This will pack all the variables into a dictionary.

```python
>>> fruits_inventory = {"apple": 6, "banana": 2, "cherry": 3}
>>> more_fruits_inventory = {"orange": 4, "kiwi": 1, "melon": 2, "mango": 3}
>>> combined_fruits_inventory = {**fruits_inventory, **more_fruits_inventory}

>>> combined_fruits_inventory
{"apple": 6, "banana": 2, "cherry": 3, "orange": 4, "kiwi": 1, "melon": 2, "mango": 3}
```

## Usage of `*` and `**` with a function

### Packing with function parameters

When you have a function that accepts an arbitrary or large number of arguments, you can use [`*args` or `**kwargs`][args and kwargs] to pack or group those parameters together.
`*args` is used for packing/signifying an arbitrary number of positional (non-keyworded) arguments.
`**kwargs` is used for packing/signifying an arbitrary number of keyword arguments to a function.

Usage of `*args`:

```python
>>> def my_function(*args):
...     print(args)

>>> my_function(1, 2, 3)
(1, 2, 3)

>>> my_function("Hello", "World")
("Hello", "World")

>>> my_function(1, 2, 3, "Hello", "Mars")
(1, 2, 3, "Hello", "Mars")
```

Usage of `**kwargs`:

```python
>>> def my_function(**kwargs):
...   print(kwargs)

>>> my_function(a=1, b=2, c=3)
{"a": 1, "b": 2, "c": 3}
```

`*args` and `**kwargs` can also be used in combination with one another:

```python
>>> def my_function(*args, **kwargs):
...   print(sum(args))
...   for key, value in kwargs.items():
...     print(f"{key} = {value}")

>>> my_function(1, 2, 3, a=1, b=2, c=3)
6
a = 1
b = 2
c = 3
```

You can also write parameters before `*args` to allow for specific positional arguments.
Individual keyword arguments then have to be before `**kwargs`.

```exercism/caution
[Arguments have to be structured][Positional and keyword arguments] like this:

`def my_function(<positional_args>, *args, <key-word_args>, **kwargs)`

If you don't follow this order then you will get an error.
```

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
This is very useful for functions that don't accept an `iterable` or `iterator`:

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
Since `zip()` takes multiple iterables and returns a list of tuples with the values from each iterable grouped:

```python
>>> values = (['x', 'y', 'z'], [1, 2, 3], [True, False, True])
>>> a, *rest = zip(*values)
>>> rest
[('y', 2, False), ('z', 3, True)]
```

[multiple assignment]: https://www.geeksforgeeks.org/assigning-multiple-variables-in-one-line-in-python/
[sorting algorithms]: https://realpython.com/sorting-algorithms-python/
[unpacking]: https://www.geeksforgeeks.org/unpacking-arguments-in-python/?ref=rp
[deep unpacking]: https://mathspp.com/blog/pydonts/deep-unpacking#deep-unpacking
[packing and unpacking]: https://www.geeksforgeeks.org/packing-and-unpacking-arguments-in-python/
[items]: https://www.geeksforgeeks.org/python-dictionary-items-method/
[args and kwargs]: https://www.geeksforgeeks.org/args-kwargs-python/
