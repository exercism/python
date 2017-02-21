import unittest

from rna_transcription import to_rna


class DNATests(unittest.TestCase):

    def test_transcribes_guanine_to_cytosine(self):
        self.assertEqual('C', to_rna('G'))

    def test_transcribes_cytosine_to_guanine(self):
        self.assertEqual('G', to_rna('C'))

    def test_transcribes_thymine_to_adenine(self):
        self.assertEqual('A', to_rna('T'))

    def test_transcribes_adenine_to_uracil(self):
        self.assertEqual('U', to_rna('A'))

    def test_transcribes_all_occurences(self):
        self.assertMultiLineEqual('UGCACCAGAAUU', to_rna('ACGTGGTCTTAA'))

    def test_correctly_handles_single_invalid_input(self):
        self.assertEqual('', to_rna('U'))

    def test_correctly_handles_completely_invalid_input(self):
        self.assertMultiLineEqual('', to_rna('XXX'))

    def test_correctly_handles_partially_invalid_input(self):
        self.assertMultiLineEqual('', to_rna('ACGTXXXCTTAA'))


if __name__ == '__main__':
    unittest.main()
