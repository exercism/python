# Introduction

There are at least two idiomatic approaches to solve RNA Transcription.
One approach is to use `translate()` with `maketrans()`.
Another approach is to do a dictionary lookup on each character and join the results.

## General guidance

Whichever approach is used needs to return the RNA complement for each DNA value.
The `translate()` method with `maketrans()` transcribes using the [ASCII][ASCII] values of the characters.
Using a dictionary look-up with `join()` transcribes using the string values of the characters.

## Approach: `translate()` with `maketrans()`

```python
LOOKUP = str.maketrans("GCTA", "CGAU")


def to_rna(dna_strand):
    return dna_strand.translate(LOOKUP)

```

For more information, check the [`translate()` with `maketrans()` approach][approach-translate-maketrans].

## Approach: dictionary look-up with `join()`

```python
LOOKUP = {"G": "C", "C": "G", "T": "A", "A": "U"}


def to_rna(dna_strand):
    return ''.join(LOOKUP[chr] for chr in dna_strand)

```

For more information, check the [dictionary look-up with `join()` approach][approach-dictionary-join].

## Which approach to use?

The `translate()` with `maketrans()` approach benchmarked over four times faster than the dictionary look-up with `join()` approach.

[ASCII]: https://www.asciitable.com/
[approach-translate-maketrans]: https://exercism.org/tracks/python/exercises/rna-transcription/approaches/translate-maketrans
[approach-dictionary-join]: https://exercism.org/tracks/python/exercises/rna-transcription/approaches/dictionary-join
