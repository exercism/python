DNA_TO_RNA = {ord(d): r for d, r in zip("AGCT", "UCGA")}

def to_rna(dna_strand):
    return dna_strand.translate(DNA_TO_RNA)
