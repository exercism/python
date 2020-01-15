import unittest

from protein_translation import proteins

# Tests adapted from `problem-specifications//canonical-data.json` @ v1.1.1


class ProteinTranslationTest(unittest.TestCase):
    def test_methionine_rna_sequence(self):
        value = "AUG"
        expected = ["Methionine"]
        self.assertEqual(proteins(value), expected)

    def test_phenylalanine_rna_sequence_1(self):
        value = "UUU"
        expected = ["Phenylalanine"]
        self.assertEqual(proteins(value), expected)

    def test_phenylalanine_rna_sequence_2(self):
        value = "UUC"
        expected = ["Phenylalanine"]
        self.assertEqual(proteins(value), expected)

    def test_leucine_rna_sequence_1(self):
        value = "UUA"
        expected = ["Leucine"]
        self.assertEqual(proteins(value), expected)

    def test_leucine_rna_sequence_2(self):
        value = "UUG"
        expected = ["Leucine"]
        self.assertEqual(proteins(value), expected)

    def test_serine_rna_sequence_1(self):
        value = "UCU"
        expected = ["Serine"]
        self.assertEqual(proteins(value), expected)

    def test_serine_rna_sequence_2(self):
        value = "UCC"
        expected = ["Serine"]
        self.assertEqual(proteins(value), expected)

    def test_serine_rna_sequence_3(self):
        value = "UCA"
        expected = ["Serine"]
        self.assertEqual(proteins(value), expected)

    def test_serine_rna_sequence_4(self):
        value = "UCG"
        expected = ["Serine"]
        self.assertEqual(proteins(value), expected)

    def test_tyrosine_rna_sequence_1(self):
        value = "UAU"
        expected = ["Tyrosine"]
        self.assertEqual(proteins(value), expected)

    def test_tyrosine_rna_sequence_2(self):
        value = "UAC"
        expected = ["Tyrosine"]
        self.assertEqual(proteins(value), expected)

    def test_cysteine_rna_sequence_1(self):
        value = "UGU"
        expected = ["Cysteine"]
        self.assertEqual(proteins(value), expected)

    def test_cysteine_rna_sequence_2(self):
        value = "UGC"
        expected = ["Cysteine"]
        self.assertEqual(proteins(value), expected)

    def test_tryptophan_rna_sequence(self):
        value = "UGG"
        expected = ["Tryptophan"]
        self.assertEqual(proteins(value), expected)

    def test_stop_codon_rna_sequence_1(self):
        value = "UAA"
        expected = []
        self.assertEqual(proteins(value), expected)

    def test_stop_codon_rna_sequence_2(self):
        value = "UAG"
        expected = []
        self.assertEqual(proteins(value), expected)

    def test_stop_codon_rna_sequence_3(self):
        value = "UGA"
        expected = []
        self.assertEqual(proteins(value), expected)

    def test_translate_rna_strand_into_correct_protein_list(self):
        value = "AUGUUUUGG"
        expected = ["Methionine", "Phenylalanine", "Tryptophan"]
        self.assertEqual(proteins(value), expected)

    def test_translation_stops_if_stop_codon_at_beginning_of_sequence(self):
        value = "UAGUGG"
        expected = []
        self.assertEqual(proteins(value), expected)

    def test_translation_stops_if_stop_codon_at_end_of_two_codon_sequence(self):
        value = "UGGUAG"
        expected = ["Tryptophan"]
        self.assertEqual(proteins(value), expected)

    def test_translation_stops_if_stop_codon_at_end_of_three_codon_sequence(self):
        value = "AUGUUUUAA"
        expected = ["Methionine", "Phenylalanine"]
        self.assertEqual(proteins(value), expected)

    def test_translation_stops_if_stop_codon_in_middle_of_three_codon_sequence(self):
        value = "UGGUAGUGG"
        expected = ["Tryptophan"]
        self.assertEqual(proteins(value), expected)

    def test_translation_stops_if_stop_codon_in_middle_of_six_codon_sequence(self):
        value = "UGGUGUUAUUAAUGGUUU"
        expected = ["Tryptophan", "Cysteine", "Tyrosine"]
        self.assertEqual(proteins(value), expected)


if __name__ == "__main__":
    unittest.main()
