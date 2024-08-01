# Stack Match


```python
def is_paired(input_string):
    bracket_map = {"]" : "[", "}": "{", ")":"("}
    stack = []

    for element in input_string:
        if element in bracket_map.values():
            stack.append(element)
        if element in bracket_map:
            if not stack or (stack.pop() != bracket_map[element]):
                return False
    return not stack
```

The point of this approach is to maintain a context of which bracket sets are currently "open":

- If a left bracket is found, push it onto the stack (_append it to the `list`_).
- If a right bracket is found, **and** it pairs with the last item placed on the stack, pop the bracket off the stack and continue.
- If there is a mismatch, for example `'['` with `'}'` or there is no left bracket on the stack, the code can immediately terminate and return `False`.
- When all the input text is processed, determine if the stack is empty, meaning all left brackets were matched.

In Python, a [`list`][concept:python/lists]() is a good implementation of a stack: it has [`list.append()`][list-append] (_equivalent to a "push"_) and [`lsit.pop()`][list-pop] methods built in.

Some solutions use [`collections.deque()`][collections-deque] as an alternative implementation, though this has no clear advantage (_since the code only uses appends to the right-hand side_) and near-identical runtime performance.

The default iteration for a dictionary is over the _keys_, so the code above uses a plain `bracket_map` to search for right brackets, while `bracket_map.values()` is used to search for left brackets.

Other solutions created two sets of left and right brackets explicitly, or searched a string representation:

```python
    if element in ']})':
```

Such changes made little difference to code length or readability, but ran about 5-fold faster than the dictionary-based solution.

At the end, success is an empty stack, tested above by using the [False-y quality][falsey] of `[]` (_as Python programmers often do_).

To be more explicit, we could alternatively use an equality:

```python
    return stack == []
```

[list-append]: https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
[list-pop]: https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
[collections-deque]: https://docs.python.org/3/library/collections.html#collections.deque
[falsey]: https://docs.python.org/3/library/stdtypes.html#truth-value-testing
