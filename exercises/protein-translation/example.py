CODONS = {'AUG': "Methionine", 'UUU': "Phenylalanine",
          'UUC': "Phenylalanine", 'UUA': "Leucine", 'UUG': "Leucine",
          'UCU': "Serine", 'UCC': "Serine", 'UCA': "Serine",
          'UCG': "Serine", 'UAU': "Tyrosine", 'UAC': "Tyrosine",
          'UGU': "Cysteine", 'UGC': "Cysteine", 'UGG': "Tryptophan",
          'UAA': "STOP", 'UAG': "STOP", 'UGA': "STOP"}


def of_codon(codon):
    if codon not in CODONS:
        raise ValueError('Invalid codon: {}'.format(codon))
    return CODONS[codon]


def proteins(strand):
    proteins = []
    for codon in map(of_codon, _chunkstring(strand, 3)):
        if codon == 'STOP':
            break
        proteins.append(codon)
    return proteins


def _chunkstring(string, n):
    return (string[i:n + i] for i in range(0, len(string), n))
