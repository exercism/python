# Introduction

There are various ways to solve Hamming.
One approach is to iterate over either a range of indexs or to use [zip][zip].
Another appraoch is to use the range of indexs.

## General guidance

The goal of this exercise is to compare two DNA strands and count how many of the nucleotides are different from their equivalent in the other string.
The most common way is to use some kind of loop to iterate over the two strands and compare the nucleotides which has the same index.

## Approach: Iterating over a range of indexes

```python
def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    count = 0
    for x in range(len(strand_a)):
        if strand_a[x] != strand_b[x]:
            count += 1
    return count
```

For more information, check the [range approach][approach-range].

## Approach: Iterating with zip

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

[zip]: https://docs.python.org/3/library/functions.html#zip
[approach-range]: https://exercism.org/tracks/python/exercises/hamming/approaches/range
[approach-sum]: https://exercism.org/tracks/python/exercises/hamming/approaches/sum
[approach-zip]: https://exercism.org/tracks/python/exercises/hamming/approaches/zip
