NUCLEOTIDES = 'ATCGU'


def count(strand, abbreviation):
    _validate(abbreviation)
    return strand.count(abbreviation)


def nucleotide_counts(strand):
    for x in strand:
        _validate(x)
    return {
        abbr: strand.count(abbr)
        for abbr in 'ATGC'
    }


def _validate(abbreviation):
    if abbreviation not in NUCLEOTIDES:
        raise ValueError('%s is not a nucleotide.' % abbreviation)
