import unittest

import hamming


class HammingTest(unittest.TestCase):

    def test_no_difference_between_identical_strands(self):
        self.assertEqual(0, hamming.distance('A', 'A'))

    def test_complete_hamming_distance_of_for_single_nucleotide_strand(self):
        self.assertEqual(1, hamming.distance('A', 'G'))

    def test_complete_hamming_distance_of_for_small_strand(self):
        self.assertEqual(2, hamming.distance('AG', 'CT'))

    def test_small_hamming_distance(self):
        self.assertEqual(1, hamming.distance('AT', 'CT'))

    def test_small_hamming_distance_in_longer_strand(self):
        self.assertEqual(1, hamming.distance('GGACG', 'GGTCG'))

    def test_large_hamming_distance(self):
        self.assertEqual(4, hamming.distance('GATACA', 'GCATAA'))

    def test_hamming_distance_in_very_long_strand(self):
        self.assertEqual(9, hamming.distance('GGACGGATTCTG', 'AGGACGGATTCT'))

    def test_hamming_distance_unequal_strings_1(self):
        self.assertIsNone(hamming.distance('AAA', 'AAAG'))

    def test_hamming_distance_unequal_strings_2(self):
        self.assertIsNone(hamming.distance('AAAG', 'AAA'))

if __name__ == '__main__':
    unittest.main()
