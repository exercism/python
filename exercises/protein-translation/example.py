#!/usr/bin/env python

# Lookup table
codons = {'AUG': "Methionine", 'UUU': "Phenylalanine",
          'UUC': "Phenylalanine", 'UUA': "Leucine", 'UUG': "Leucine",
          'UCU': "Serine", 'UCC': "Serine", 'UCA': "Serine",
          'UCG': "Serine", 'UAU': "Tyrosine", 'UAC': "Tyrosine",
          'UGU': "Cysteine", 'UGC': "Cysteine", 'UGG': "Tryptophan",
          'UAA': "STOP", 'UAG': "STOP", 'UGA': "STOP"}


def of_codon(codon):
    return codons[codon]


def of_rna(strand):
    output = []
    for i in range(0, len(strand), 3):
        codon = strand[i:i+3]
        if codons[codon] == 'STOP':
            return output
        output.append(codons[codon])

    return output
