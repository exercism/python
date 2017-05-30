#!/usr/bin/env python
class InvalidCodonError(Exception):
    def __init__(self, codon):
        self.codon = codon
        Exception.__init__(self, 'Invalid Codon exception: %s is not a valid \
                           codon' % codon)


class Translation(object):

    # Lookup table
    codonList = {'AUG': "Methionine", 'UUU': "Phenylalanine",
                 'UUC': "Phenylalanine", 'UUA': "Leucine", 'UUG': "Leucine",
                 'UCU': "Serine", 'UCC': "Serine", 'UCA': "Serine",
                 'UCG': "Serine", 'UAU': "Tyrosine", 'UAC': "Tyrosine",
                 'UGU': "Cysteine", 'UGC': "Cysteine", 'UGG': "Tryptophan",
                 'UAA': "STOP", 'UAG': "STOP", 'UGA': "STOP"}

    def __init__(self):
        self.codons = self.codonList

    def ofCodon(self, codon):
        try:
            return self.codons[codon]
        except KeyError:
            raise(InvalidCodonError(codon))

    def ofRNA(self, strand):
        output = []
        for i in range(0, len(strand), 3):
            codon = strand[i:i+3]
            try:
                if self.codons[codon] == 'STOP':
                    return output
                output.append(self.codons[codon])
            except KeyError:
                raise(InvalidCodonError(codon))

        return output
