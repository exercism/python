# sum

The benefit of using `sum` is that we can use a generator expression to create a list of booleans.
We can then pass that generator to `sum` and it will iterate through and add up all the booleans.
Where `True` is treated as 1 and `False` is treated as 0.
Then that total is returned.

This can make the code a bit more concise.

Here is an example using `sum` with `zip`:

```python
def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    return sum(nucleotide_a != nucleotide_b for nucleotide_a, nucleotide_b in zip(strand_a, strand_b))
```

This approach starts by checking if the two strands are of equal length by using [`len`][len].
If not, a [`ValueError`][value-error] is raised.

After that is checked, a `<count>` variable is initialized to 0.
The count variable will be used to keep track of the number of differences between the two strands.

This approach uses the [`zip`][zip] function to iterate over two strings.
You can read more about how to solve this exercise with `zip` in the [zip approach][approach-zip].

What differs in this approach is that we use a generator expression to create booleans.
The generator expression returns an iterator over the tuples returned by `zip`.
Within the iteration, the tuples are unpacked into two variables, `nucleotide_a` and `nucleotide_b`.
We can then compare `nucleotide_a` and `nucleotide_b`.
If they are **not** equal, `True` is produced.
If they **are** equal, `False` is produced.
The generator expression is then passed to the `sum` function.

`sum` will then iterate over the generator expression and add up all the booleans.
Where `True` is treated as 1 and `False` is treated as 0.
You can read more about this behavior in [Boolean as numbers][booleans].
Finally the totaled booleans are returned.

This approach is also doable with `range` but it is a bit more verbose:

```python
def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    return sum(strand_a[index] != strand_b[index] for index in range(len(strand_a)))
```

[approach-zip]: https://exercism.org/tracks/python/exercises/hamming/approaches/zip
[booleans]: https://realpython.com/python-boolean/#python-booleans-as-numbers
[len]: https://docs.python.org/3/library/functions.html?#len
[sum]: https://docs.python.org/3/library/functions.html?#sum
[value-error]: https://docs.python.org/3/library/exceptions.html#ValueError
[zip]: https://docs.python.org/3.3/library/functions.html#zip
