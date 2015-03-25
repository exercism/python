"""Tests for the nucleotide-count exercise

Implementation note:
The count function must raise a ValueError with a meaningful error message
in case of a bad argument.
"""
import unittest

from dna import count, nucleotide_counts


class DNATest(unittest.TestCase):
    def test_empty_dna_string_has_no_adenosine(self):
        self.assertEqual(0, count('', 'A'))

    @unittest.skip("")
    def test_empty_dna_string_has_no_nucleotides(self):
        expected = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
        self.assertEqual(expected, nucleotide_counts(""))

    @unittest.skip("")
    def test_repetitive_cytidine_gets_counted(self):
        self.assertEqual(5, count('CCCCC', 'C'))

    @unittest.skip("")
    def test_repetitive_sequence_has_only_guanosine(self):
        expected = {'A': 0, 'T': 0, 'C': 0, 'G': 8}
        self.assertEqual(expected, nucleotide_counts('GGGGGGGG'))

    @unittest.skip("")
    def test_counts_only_thymidine(self):
        self.assertEqual(1, count('GGGGGTAACCCGG', 'T'))
        
    @unittest.skip("")
    def test_validates_nucleotides(self):
        with self.assertRaises(ValueError):
            count("GACT", 'X')

    @unittest.skip("")
    def test_counts_all_nucleotides(self):
        dna = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
        expected = {'A': 20, 'T': 21, 'G': 17, 'C': 12}
        self.assertEqual(expected, nucleotide_counts(dna))

if __name__ == '__main__':
    unittest.main()
