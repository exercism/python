import sys

if sys.version_info[0] == 2:
    from string import maketrans
else:
    maketrans = str.maketrans

DNA_TO_RNA = maketrans("AGCT", "UCGA")

def to_rna(dna_strand):
    return dna_strand.translate(DNA_TO_RNA)
