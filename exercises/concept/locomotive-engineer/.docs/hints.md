# Hints

## General

## 1. Create a list of all wagons

- Multiple arguments in the function parameters can be packed with the `*args` operator.

## 2. Fix list of wagons

- Using unpacking with the `*` operator, lets you extract the first two elements of a list while keeping the rest intact.
- To add another list into an existing list, you can use the `*` operator to "spread" the list.

## 3. Add missing stops

- Using `**kwargs` as a function argument will mutiple keyword arguments into a `dict`.
- Using `**(dict)` will unpack a dictonary into keyword arguments.
- You can put keyword arguments in a `{}` or `dict()`.
- To get the values out of a dictionary, you can use the `<dict>.values()` method.

## 4. Extend routing information

- Using `**(dict)` will unpack a dictonary into keyword arguments.
- You can put keyword arguments in a `{}` or `dict()`.

## 5. Fix the wagon depot

- Using `zip(*iterators)` can use used to transpose a nested list.
- To extract data from the ziped iterators, you can use a for loop.
