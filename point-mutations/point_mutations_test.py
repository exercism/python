import unittest

from dna import hamming_distance


class DNATest(unittest.TestCase):
    def test_no_difference_between_empty_strands(self):
        self.assertEqual(0, hamming_distance('', ''))

    def test_no_difference_between_identical_strands(self):
        self.assertEqual(0, hamming_distance('GGACTGA', 'GGACTGA'))

    def test_complete_hamming_distance_in_small_strand(self):
        self.assertEqual(3, hamming_distance('ACT', 'GGA'))

    def test_hamming_distance_in_off_by_one_strand(self):
        self.assertEqual(19,
                         hamming_distance('GGACGGATTCTGACCTGGACTAATTTTGGGG',
                                          'AGGACGGATTCTGACCTGGACTAATTTTGGGG'))

    def test_small_hamming_distance_in_middle_somewhere(self):
        self.assertEqual(1, hamming_distance('GGACG', 'GGTCG'))

    def test_larger_distance(self):
        self.assertEqual(2, hamming_distance('ACCAGGG', 'ACTATGG'))

    def test_ignores_extra_length_on_other_strand_when_longer(self):
        self.assertEqual(3, hamming_distance('AAACTAGGGG', 'AGGCTAGCGGTAGGAC'))

    def test_ignores_extra_length_on_original_strand_when_longer(self):
        self.assertEqual(5, hamming_distance('GACTACGGACAGGGTAGGGAAT',
                                             'GACATCGCACACC'))

if __name__ == '__main__':
    unittest.main()
