# Introduction

There are various ways to solve Hamming.
One approach is to iterate over either a range of indexes or to use [zip][zip].
Another approach is to use the range of indexes.
Some other approaches include the use of [`enumerate`][enumerate], or [`filter`][filter] with a [`lambda`][lambda].

## General guidance

The goal of this exercise is to compare two DNA strands and count how many of the nucleotides are different from their equivalent in the other string.
The most common solution uses some kind of loop to iterate over the two strands and compare nucleotides with the same index.

## Approach: Iterating over a range of indexes

Using [`range`][range] is an approach to iterate over a sequence.
Although it may not be the most _pythonic_ strategy, it is a good way to start.
`range` is a [built-in function][built-in-functions] and it is very fast.
The downside is that `range` only works with [iterators][iterators] that can be indexed, like [concept:python/lists](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range) and [concept:python/strings](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str).
While the built-in function `enumerate` can take any iterator.

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

For more information, check the [range approach][approach-range].

## Approach: Iterating with zip

The built-in `zip` function returns an iterator of [concept:python/tuples](https://docs.python.org/3.10/tutorial/datastructures.html#tuples-and-sequences) where the first item in each passed iterator is paired together, and then the second item in each passed iterator are paired together, and so on.
Using `zip()` to iterate removes the need to index into the strands.
The downside is that if you _need to_ index into your iterators, `zip` won't work.
Although it is possible to combine `zip` with `enumerate` to generate indexes.

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

For more information, check the [zip approach][approach-zip].

## Approach: Using sum

Using the built-in [`sum`][sum] removes the need for a counter variable.
Removing the counter variable makes the code more concise.
The examples making use of `sum` also use a [generator expression][generator-expression], although that it is not required.
Using `sum` in this fashion requires a bit more Python knowledge compared to the other approaches.

With `zip`:

```python
def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    return sum(nucleotide_a != nucleotide_b for 
    nucleotide_a, nucleotide_b in zip(strand_a, strand_b))
```

With `range`:

```python
def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    return sum(strand_a[index] != strand_b[index] for 
    index in range(len(strand_a)))
```

For more information, check the [sum approach][approach-sum].

[approach-range]: https://exercism.org/tracks/python/exercises/hamming/approaches/range
[approach-sum]: https://exercism.org/tracks/python/exercises/hamming/approaches/sum
[approach-zip]: https://exercism.org/tracks/python/exercises/hamming/approaches/zip
[built-in-functions]:  https://docs.python.org/3.10/library/functions.html
[enumerate]:  https://docs.python.org/3.10/library/functions.html#enumerate
[filter]: https://docs.python.org/3.10/library/functions.html#filter
[generator-expression]: https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-generator_expression
[iterators]: https://docs.python.org/3/glossary.html#term-iterator
[lambda]: https://docs.python.org/3/glossary.html#term-lambda
[range]:  https://docs.python.org/3.10/library/functions.html#func-range
[sum]: https://docs.python.org/3/library/functions.html#sum
[zip]: https://docs.python.org/3.10/library/functions.html#zip

