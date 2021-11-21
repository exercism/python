DNA_TO_RNA = str.maketrans("AGCT", "UCGA")

def to_rna(dna_strand):
    return dna_strand.translate(DNA_TO_RNA)
