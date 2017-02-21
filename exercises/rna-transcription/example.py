import sys

if sys.version_info[0] == 2:
    from string import maketrans
else:
    maketrans = str.maketrans


DNA_CHARS = 'AGCT'
DNA_TO_RNA = maketrans(DNA_CHARS, 'UCGA')


def to_rna(dna_strand):
    valid_chars = set(DNA_CHARS)
    if any(char not in valid_chars for char in dna_strand):
        return ''

    return dna_strand.translate(DNA_TO_RNA)
