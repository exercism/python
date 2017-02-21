import unittest

import hamming


class HammingTest(unittest.TestCase):

    def test_identical_strands(self):
        self.assertEqual(0, hamming.distance("A", "A"))

    def test_long_identical_strands(self):
        self.assertEqual(0, hamming.distance("GGACTGA", "GGACTGA"))

    def test_complete_distance_in_single_nucleotide_strands(self):
        self.assertEqual(1, hamming.distance("A", "G"))

    def test_complete_distance_in_small_strands(self):
        self.assertEqual(2, hamming.distance("AG", "CT"))

    def test_small_distance_in_small_strands(self):
        self.assertEqual(1, hamming.distance("AT", "CT"))

    def test_small_distance(self):
        self.assertEqual(1, hamming.distance("GGACG", "GGTCG"))

    def test_small_distance_in_long_strands(self):
        self.assertEqual(2, hamming.distance("ACCAGGG", "ACTATGG"))

    def test_non_unique_character_in_first_strand(self):
        self.assertEqual(1, hamming.distance("AGA", "AGG"))

    def test_non_unique_character_in_second_strand(self):
        self.assertEqual(1, hamming.distance("AGG", "AGA"))

    def test_same_nucleotides_in_different_positions(self):
        self.assertEqual(2, hamming.distance("TAG", "GAT"))

    def test_large_distance(self):
        self.assertEqual(4, hamming.distance("GATACA", "GCATAA"))

    def test_large_distance_in_off_by_one_strand(self):
        self.assertEqual(9, hamming.distance("GGACGGATTCTG", "AGGACGGATTCT"))

    def test_empty_strands(self):
        self.assertEqual(0, hamming.distance("", ""))

    def test_disallow_first_strand_longer(self):
        with self.assertRaises(ValueError):
            hamming.distance("AATG", "AAA")

    def test_disallow_second_strand_longer(self):
        with self.assertRaises(ValueError):
            hamming.distance("ATA", "AGTG")


if __name__ == '__main__':
    unittest.main()
