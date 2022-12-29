# Introduction

There are various ways to solve Hamming.
One approach is to iterate over either a range of indexes or to use [zip][zip].
Another approach is to use the range of indexes.
Some other approaches could be to use enumerate, or filter with lambda.

## General guidance

The goal of this exercise is to compare two DNA strands and count how many of the nucleotides are different from their equivalent in the other string.
The most common way is to use some kind of loop to iterate over the two strands and compare the nucleotides with the same index.

## Approach: Iterating over a range of indexes

Using range is an approach to iterate over a sequence.
Although it is not the most pythonic way, it is a good way to start.
The reason to use range is that it is a built-in function and it is very fast.
The downside is that it only works with iterators that can be indexed, like lists and strings.
While a built in function like `enumerate()` can take any iterator.

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

The `zip()` function returns an iterator of tuples where the first item in each passed iterator is paired together, and then the second item in each passed iterator are paired together etc.
The approach to use `zip()` to iterate removes the need to index the iterators.
The downside is that if you need to index the iterators, zip won't work.
Although it is possible to use `enumerate()` with zip to get the index.

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

Using `sum()` makes it possible to remove the need for a counter variable.
Since there is no need for a counter variable, the code is more concise.
To make use of sum, so are the examples using a [list comprehension][list-comprehension], although it is not required.
Using sum although requires a bit more knowledge of python compared to the other approaches.

With zip:

```python
def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    return sum(nucleotide_a != nucleotide_b for nucleotide_a, nucleotide_b in zip(strand_a, strand_b))
```

With range:

```python
def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    return sum(strand_a[index] != strand_b[index] for index in range(len(strand_a)))
```

For more information, check the [sum approach][approach-sum].

[approach-range]: https://exercism.org/tracks/python/exercises/hamming/approaches/range
[approach-sum]: https://exercism.org/tracks/python/exercises/hamming/approaches/sum
[approach-zip]: https://exercism.org/tracks/python/exercises/hamming/approaches/zip
[list-comprehension]: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
[zip]: https://docs.python.org/3/library/functions.html#zip
