#!/usr/bin/env python
import unittest

from protein_translation import Translation, InvalidCodonError


class ProteinTranslationTests(unittest.TestCase):

    def setUp(self):
        self.transl = Translation()

    def test_AUG_translates_to_methionine(self):
        self.assertEqual('Methionine', self.transl.ofCodon('AUG'))

    def test_identifies_Phenylalanine_codons(self):
        for codon in ['UUU', 'UUC']:
            self.assertEqual('Phenylalanine', self.transl.ofCodon(codon))

    def test_identifies_Leucine_codons(self):
        for codon in ['UUA', 'UUG']:
            self.assertEqual('Leucine', self.transl.ofCodon(codon))

    def test_identifies_Serine_codons(self):
        for codon in ['UCU', 'UCC', 'UCA', 'UCG']:
            self.assertEqual('Serine', self.transl.ofCodon(codon))

    def test_identifies_Tyrosine_codons(self):
        for codon in ['UAU', 'UAC']:
            self.assertEqual('Tyrosine', self.transl.ofCodon(codon))

    def test_identifies_Cysteine_codons(self):
        for codon in ['UGU', 'UGC']:
            self.assertEqual('Cysteine', self.transl.ofCodon(codon))

    def test_identifies_Tryptophan_codons(self):
        self.assertEqual('Tryptophan', self.transl.ofCodon('UGG'))

    def test_identifies_stop_codons(self):
        for codon in ['UAA', 'UAG', 'UGA']:
            self.assertEqual('STOP', self.transl.ofCodon(codon))

    def test_translates_rna_strand_into_correct_protein(self):
        strand = 'AUGUUUUGG'
        expected = ['Methionine', 'Phenylalanine', 'Tryptophan']
        self.assertEqual(expected, self.transl.ofRNA(strand))

    def test_stops_translation_if_stop_codon_present(self):
        strand = 'AUGUUUUAA'
        expected = ['Methionine', 'Phenylalanine']
        self.assertEqual(expected, self.transl.ofRNA(strand))

    def test_stops_translation_of_longer_strand(self):
        strand = 'UGGUGUUAUUAAUGGUUU'
        expected = ['Tryptophan', 'Cysteine', 'Tyrosine']
        self.assertEqual(expected, self.transl.ofRNA(strand))

    def test_invalid_codons(self):
        strand = 'CARROT'
        self.assertRaises(InvalidCodonError, self.transl.ofRNA, strand)


if __name__ == '__main__':
    unittest.main()
