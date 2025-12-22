# Introduction

There are at least two idiomatic approaches to solve RNA Transcription.
One approach is to use `translate()` with `maketrans()`.
Another approach is to do a dictionary lookup on each character and join the results.

## General guidance

Whichever approach is used needs to return the RNA complement for each DNA value.
The `translate()` method with `maketrans()` transcribes using the [Unicode][Unicode] code points of the characters.
Using a dictionary look-up with `join()` transcribes using the string values of the characters.

## Approach: `translate()` with `maketrans()`

```python
LOOKUP = str.maketrans('GCTA', 'CGAU')


def to_rna(dna_strand):
    return dna_strand.translate(LOOKUP)

```

For more information, check the [`translate()` with `maketrans()` approach][approach-translate-maketrans].

## Approach: dictionary look-up with `join()`

```python
LOOKUP = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}


def to_rna(dna_strand):
    return ''.join(LOOKUP[nucleotide] for nucleotide in dna_strand)

```

For more information, check the [dictionary look-up with `join()` approach][approach-dictionary-join].

## Which approach to use?

If performance matters, consider using the [`translate()` with `maketrans()` approach][approach-translate-maketrans].
How an implementation behaves in terms of performance may depend on the actual data being processed, on hardware, and other factors.

[Unicode]: https://en.wikipedia.org/wiki/Unicode
[approach-translate-maketrans]: https://exercism.org/tracks/python/exercises/rna-transcription/approaches/translate-maketrans
[approach-dictionary-join]: https://exercism.org/tracks/python/exercises/rna-transcription/approaches/dictionary-join
