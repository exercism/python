import timeit

loops = 1_000_000

val = timeit.timeit("""to_rna("ACGTGGTCTTAA")""",
                    """
LOOKUP = str.maketrans("GCTA","CGAU")

def to_rna(dna_strand):
    return dna_strand.translate(LOOKUP)

""", number=loops) / loops

print(f"translate maketrans: {val}")

val = timeit.timeit("""to_rna("ACGTGGTCTTAA")""",
                    """
LOOKUP = {"G": "C", "C": "G", "T": "A", "A": "U"}

def to_rna(dna_strand):
    return ''.join(LOOKUP[chr] for chr in dna_strand)

""", number=loops) / loops

print(f"dictionary join:     {val}")
