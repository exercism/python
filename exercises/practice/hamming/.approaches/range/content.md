# range

```python
def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    count = 0
    for index in range(len(strand_a)):
        if strand_a[index] != strand_b[index]:
            count += 1
    return count
```

This approach starts by checking if the two strands are of equal length.
If not, a [`ValueError`][value-error] is raised.

After that is checked, a `<count>` variable is initialized to 0.
The count variable will be used to keep track of the number of differences between the two strands.

[`range`][range] in Python is a built-in function that returns a sequence of numbers.
`range` produces an infinite sequence, but it can be limited by providing a `<stop>` argument.
The `range` function can also take a `<start>` argument and a `<step>` argument.
The inputs are built up like this: `range(<start>, <stop>, <step>)`.
When only a `<stop>` argument is provided, `<start>` defaults to 0 and `<step>` defaults to 1.

We use `range` to iterate over the indexes of the `strand_a` string.
We do that by passing the length of the string to `range` by using the built-in function [`len`][len].
Iterating over `range` gives us an index number we can use to access a character in the string.

We can then compare the character at the index in `strand_a` to the character at the same index in `strand_b`.
If the two values are not equal, we increment the `<count>` variable by 1.

After the loop completes, we return the `<count>` variable.

[len]: https://docs.python.org/3/library/functions.html?#len
[range]: https://docs.python.org/3/library/stdtypes.html?#range
[value-error]: https://docs.python.org/3/library/exceptions.html#ValueError
