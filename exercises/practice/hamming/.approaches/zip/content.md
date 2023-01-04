# zip

```python
def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    count = 0
    for nucleotide_a, nucleotide_b in zip(strand_a, strand_b):
        if nucleotide_a != nucleotide_b:
            count += 1
    return count
```

This approach starts by checking if the two strands are of equal length by using [`len`][len].
If not, a [`ValueError`][value-error] is raised.

After that is checked, a `<count>` variable is initialized to 0.
The count variable will be used to keep track of the number of differences between the two strands.

We use [`zip`][zip] to iterate over the characters in `strand_a` and `strand_b` simultaneously.
`zip` is a built in function.
It takes any number of iterables and returns an iterator of tuples.
Where the i-th tuple contains the i-th element from each of the argument iterables.
For example, the first tuple will contain the first element from each iterable, the second tuple will contain the second element from each iterable, and so on until the shortest iterable is exhausted.

In Python, strings are iterable.

Here is an example of using `zip` to iterate over two strings:

```python
>>> zipped = zip("GGACGG", "AGGACG")
>>> list(zipped)
[('G', 'A'), ('G', 'G'), ('A', 'G'), ('C', 'A'), ('G', 'C'), ('G', 'G')]
```

We then use the `zip` iterator to iterate over the tuples.
We unpack the tuple into two variables, `nucleotide_a` and `nucleotide_b`.
You can read more about unpacking in the concept [concept:python/unpacking-and-multiple-assignment]().

We then compare the characters `nucleotide_a` and `nucleotide_b`.
If they are not equal, we increment the count variable by 1.

After the loop is finished, we return the count variable.

[len]: https://docs.python.org/3/library/functions.html?#len
[value-error]: https://docs.python.org/3/library/exceptions.html#ValueError
[zip]: https://docs.python.org/3.3/library/functions.html#zip
