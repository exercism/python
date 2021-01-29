import unittest

from point_mutations import hamming_distance


class PointMutationsTest(unittest.TestCase):
    def test_no_difference_between_empty_strands(self):
        self.assertEqual(hamming_distance('', ''), 0)

    def test_no_difference_between_identical_strands(self):
        self.assertEqual(hamming_distance('GGACTGA', 'GGACTGA'), 0)

    def test_complete_hamming_distance_in_small_strand(self):
        self.assertEqual(hamming_distance('ACT', 'GGA'), 3)

    def test_hamming_distance_in_off_by_one_strand(self):
        self.assertEqual(
            hamming_distance('GGACGGATTCTGACCTGGACTAATTTTGGGG',
                             'AGGACGGATTCTGACCTGGACTAATTTTGGGG'), 19)

    def test_small_hamming_distance_in_middle_somewhere(self):
        self.assertEqual(hamming_distance('GGACG', 'GGTCG'), 1)

    def test_larger_distance(self):
        self.assertEqual(hamming_distance('ACCAGGG', 'ACTATGG'), 2)

    def test_ignores_extra_length_on_other_strand_when_longer(self):
        self.assertEqual(hamming_distance('AAACTAGGGG', 'AGGCTAGCGGTAGGAC'), 3)

    def test_ignores_extra_length_on_original_strand_when_longer(self):
        self.assertEqual(
            hamming_distance('GACTACGGACAGGGTAGGGAAT', 'GACATCGCACACC'), 5)


if __name__ == '__main__':
    unittest.main()
