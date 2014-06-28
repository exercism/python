import unittest

from dna import to_rna


class DNATests(unittest.TestCase):
    def test_transcribes_cytidine_unchanged(self):
        self.assertEqual('C', to_rna('G'))

    def test_transcribes_guanosine_unchanged(self):
        self.assertEqual('G', to_rna('C'))

    def test_transcribes_adenosine_unchanged(self):
        self.assertEqual('A', to_rna('T'))

    def test_transcribes_thymidine_to_uracil(self):
        self.assertEqual('U', to_rna('A'))

    def test_transcribes_all_occurences(self):
        self.assertEqual('UGCACCAGAAUU', to_rna('ACGTGGTCTTAA'))

if __name__ == '__main__':
    unittest.main()
