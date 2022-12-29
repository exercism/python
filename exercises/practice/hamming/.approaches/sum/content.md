# sum

The benefit of using [`sum()`][sum] is that we can use a list comprehension to create a list of booleans.
Then we can pass that list to `sum()` and it will add up all the booleans.
Where `True` is treated as 1 and `False` is treated as 0.
Then that sum is returned.

This can make the code a bit more concise.

Here is an example with using `sum()` and `zip()`:

```python
def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    return sum(nucleotide_a != nucleotide_b for nucleotide_a, nucleotide_b in zip(strand_a, strand_b))
```

This approach starts by checking if the two strands are of equal length by using [`len()`][len].
If not, a [`ValueError`][value-error] is raised.

After that is checked, a variable `count` is initialized to 0.
The count variable will be used to keep track of the number of differences between the two strands.

This approach uses the [`zip()`][zip] function to iterate over two strings.
You can read more about how to solve this exercise with `zip()` in the [zip approach][approach-zip].

What differs in this approach is that we use a list comprehension to create a list of booleans.
The list comprehension iterates over the tuples returned by `zip()`.
Then under the iteration so are the tuples unpacked into two variables, `nucleotide_a` and `nucleotide_b`.
We then compare the characters `nucleotide_a` and `nucleotide_b`.
If they are not equal, we add `True` to the list.
If they are equal, we add `False` to the list.
The list comprehension is then passed to the `sum()` function.

The [`sum()`][sum] function will add up all the booleans in the list.
Where `True` is treated as 1 and `False` is treated as 0.
You can read more about this behavior in [Boolean as numbers][booleans].
Then that sum is returned.

This approach is also doable with range but it is a bit more verbose:

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
