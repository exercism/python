import unittest

from pythagorean_triplet import triplets_with_sum


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.0.0

class PythagoreanTripletTest(unittest.TestCase):
    def test_triplets_sum_12(self):
        expected = set([(3, 4, 5)])
        self.assertEqual(triplets_with_sum(12), expected)

    def test_triplets_sum_108(self):
        expected = set([(27, 36, 45)])
        self.assertEqual(triplets_with_sum(108), expected)

    def test_triplets_sum_1000(self):
        expected = set([(200, 375, 425)])
        self.assertEqual(triplets_with_sum(1000), expected)

    def test_no_triplet_exists(self):
        expected = set([])
        self.assertEqual(triplets_with_sum(1001), expected)

    def test_two_matching_triplets(self):
        expected = set([(9, 40, 41), (15, 36, 39)])
        self.assertEqual(triplets_with_sum(90), expected)

    def test_several_matching_triplets(self):
        expected = set([(40, 399, 401),
                        (56, 390, 394),
                        (105, 360, 375),
                        (120, 350, 370),
                        (140, 336, 364),
                        (168, 315, 357),
                        (210, 280, 350),
                        (240, 252, 348)])
        self.assertEqual(triplets_with_sum(840), expected)

    def test_triplets_for_large_numbers(self):
        expected = set([(1200, 14375, 14425),
                        (1875, 14000, 14125),
                        (5000, 12000, 13000),
                        (6000, 11250, 12750),
                        (7500, 10000, 12500)])
        self.assertEqual(triplets_with_sum(30000), expected)


if __name__ == '__main__':
    unittest.main()
