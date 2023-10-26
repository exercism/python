# Hints

## General

- To extract multiple arguments in the function parameters so can you pack them with the `*args` operator for `list` or `tuples` or `**kwargs` for keyword-based arguments.
- To pack or unpack use the `*` or `**` operator.

## 1. Create a list of all wagons

- Multiple arguments in the function parameters can be packed with the `*args` operator.

## 2. Fix list of wagons

- Using unpacking with the `*` operator, lets you extract the first two elements of a `list` while keeping the rest intact.
- To add another `list` into an existing `list`, you can use the `*` operator to "spread" the `list`.

## 3. Add missing stops

- Using `**kwargs` as a function parameter will allow an arbitrary number of keyword arguments to be passed.
- Using `**<dict>` as an argument will unpack a dictionary into keyword arguments.
- You can put keyword arguments in a `{}` or `dict()`.
- To get the values out of a dictionary, you can use the `<dict>.values()` method.

## 4. Extend routing information

- Using `**<dict>` as an argument will unpack a dictionary into keyword arguments.
- You can put keyword arguments in a `{}` or `dict()`.

## 5. Fix the wagon depot

- `zip(*iterators)` can use used to transpose a nested `list`.
- To extract data from zipped iterators, you can use a for loop.
- you can also unpack zipped iterators using `*`.  
  `[*content] = zip(iterator_1, iterator_2)` will unzip the `tuple` produced by `zip()` into a `list`.
