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

The point of this approach is to maintain a context of which brackets are currently open:

- If a left bracket is found, push it onto the stack.
- If a right bracket is found, and it pairs with the top item on the stack, pop the stack and contine.
- If there is a mismatch, for example `'['` with `'}'` or no left bracket on the stack, we can immediately terminate and return `False`.
- When all the input text is processed, determine if the stack is empty, meaning all left brackets were matched.

In Python, a `list` is a good implementation of a stack: it has `append()` (equivalent to push) and `pop()` methods built in.

Some solutions use `collections.deque()` as an alternative implementation, though this has no clear advantage and near-identical runtime performance.

The code above searches `bracket_map` for left brackets, meaning the keys of the dictionary, and `bracket_map.values()` for the right brackets.

Other solutions created two sets of left and right brackets explicitly, or just searched a string representation:

```python
    if element in ']})':
```

Such changes made little difference to code length or readability, but ran about 5-fold faster than the purely dictionary-based solution.

At the end, success is an empty stack, tested above by using the False-like quality of `[]` (as Python programmers often do).

To be more explicit, we could alternatively use an equality:

```python
    return stack == []
```
