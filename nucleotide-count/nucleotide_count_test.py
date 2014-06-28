"""Tests for the nucleotide-count exercise

Implementation note:
The DNA.count method must raise a ValueError with a meaningful error message
in case of a bad argument.
"""
import unittest

from dna import DNA


class DNATest(unittest.TestCase):
    def test_empty_dna_string_has_no_adenosine(self):
        self.assertEqual(0, DNA('').count('A'))

    def test_empty_dna_string_has_no_nucleotides(self):
        expected = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
        self.assertEqual(expected, DNA("").nucleotide_counts())

    def test_repetitive_cytidine_gets_counted(self):
        self.assertEqual(5, DNA('CCCCC').count('C'))

    def test_repetitive_sequence_has_only_guanosine(self):
        expected = {'A': 0, 'T': 0, 'C': 0, 'G': 8}
        self.assertEqual(expected, DNA('GGGGGGGG').nucleotide_counts())

    def test_counts_only_thymidine(self):
        self.assertEqual(1, DNA('GGGGGTAACCCGG').count('T'))

    def test_counts_a_nucleotide_only_once(self):
        dna = DNA('CGATTGGG')
        self.assertEqual(2, dna.count('T'))

    def test_dna_has_no_uracil(self):
        self.assertEqual(0, DNA('GATTACA').count('U'))

    def test_dna_counts_do_not_change_after_counting_uracil(self):
        dna = DNA('GATTACA')
        expected = {"A": 3, "T": 2, "C": 1, "G": 1}
        self.assertEqual(expected, dna.nucleotide_counts())

    def test_validates_nucleotides(self):
        self.assertRaises(ValueError, DNA("GACT").count, 'X')

    def test_counts_all_nucleotides(self):
        dna = DNA("AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGT"
                  "GTCTGATAGCAGC")
        expected = {'A': 20, 'T': 21, 'G': 17, 'C': 12}
        self.assertEqual(expected, dna.nucleotide_counts())

if __name__ == '__main__':
    unittest.main()
