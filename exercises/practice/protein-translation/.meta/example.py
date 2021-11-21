CODONS = {'AUG': 'Methionine', 'UUU': 'Phenylalanine',
          'UUC': 'Phenylalanine', 'UUA': 'Leucine', 'UUG': 'Leucine',
          'UCU': 'Serine', 'UCC': 'Serine', 'UCA': 'Serine',
          'UCG': 'Serine', 'UAU': 'Tyrosine', 'UAC': 'Tyrosine',
          'UGU': 'Cysteine', 'UGC': 'Cysteine', 'UGG': 'Tryptophan',
          'UAA': 'STOP', 'UAG': 'STOP', 'UGA': 'STOP'}


def of_codon(codon):
    if codon not in CODONS:
        raise ValueError(f'Invalid codon: {codon}')
    return CODONS[codon]


def proteins(strand):
    protein_list = []
    for codon in map(of_codon, _chunkstring(strand, 3)):
        if codon == 'STOP':
            break
        protein_list.append(codon)
    return protein_list


def _chunkstring(string, number):
    return (string[idx:number + idx] for idx in range(0, len(string), number))
