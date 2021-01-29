"""Tests for the nucleotide-count exercise

Implementation note:
The count function must raise a ValueError with a meaningful error message
in case of a bad argument.
"""
import unittest

from nucleotide_count import count, nucleotide_counts


class NucleotideCountTest(unittest.TestCase):
    def test_empty_dna_string_has_no_adenosine(self):
        self.assertEqual(count('', 'A'), 0)

    def test_empty_dna_string_has_no_nucleotides(self):
        expected = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
        self.assertEqual(nucleotide_counts(""), expected)

    def test_repetitive_cytidine_gets_counted(self):
        self.assertEqual(count('CCCCC', 'C'), 5)

    def test_repetitive_sequence_has_only_guanosine(self):
        expected = {'A': 0, 'T': 0, 'C': 0, 'G': 8}
        self.assertEqual(nucleotide_counts('GGGGGGGG'), expected)

    def test_counts_only_thymidine(self):
        self.assertEqual(count('GGGGGTAACCCGG', 'T'), 1)

    def test_validates_nucleotides(self):
        with self.assertRaisesWithMessage(ValueError):
            count("GACT", 'X')

    def test_counts_all_nucleotides(self):
        dna = ('AGCTTTTCATTCTGACTGCAACGGGCAATATGTCT'
               'CTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC')
        expected = {'A': 20, 'T': 21, 'G': 17, 'C': 12}
        self.assertEqual(nucleotide_counts(dna), expected)

    # Utility functions
    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")


if __name__ == '__main__':
    unittest.main()
