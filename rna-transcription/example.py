import sys

if sys.version_info[0] == 2:
    from string import maketrans
else:
    maketrans = str.maketrans


class DNA(object):
    rna_translation = maketrans('AGCT', 'UCGA')

    def __init__(self, strand):
        self.strand = strand

    def to_rna(self):
        return self.strand.translate(self.rna_translation)
