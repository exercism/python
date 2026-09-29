NUCLEOTIDES = 'ATCG'


def count(strand, abbreviation):
    _validate(abbreviation)
    return strand.count(abbreviation)


def nucleotide_counts(strand):
    return {
        abbr: strand.count(abbr)
        for abbr in NUCLEOTIDES
    }


def _validate(abbreviation):
    if abbreviation not in NUCLEOTIDES:
        raise ValueError(f'{abbreviation} is not a nucleotide.')
