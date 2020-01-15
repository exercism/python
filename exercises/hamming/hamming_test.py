import unittest

from hamming import distance

# Tests adapted from `problem-specifications//canonical-data.json` @ v2.3.0


class HammingTest(unittest.TestCase):
    def test_empty_strands(self):
        self.assertEqual(distance("", ""), 0)

    def test_single_letter_identical_strands(self):
        self.assertEqual(distance("A", "A"), 0)

    def test_single_letter_different_strands(self):
        self.assertEqual(distance("G", "T"), 1)

    def test_long_identical_strands(self):
        self.assertEqual(distance("GGACTGAAATCTG", "GGACTGAAATCTG"), 0)

    def test_long_different_strands(self):
        self.assertEqual(distance("GGACGGATTCTG", "AGGACGGATTCT"), 9)

    def test_disallow_first_strand_longer(self):
        with self.assertRaisesWithMessage(ValueError):
            distance("AATG", "AAA")

    def test_disallow_second_strand_longer(self):
        with self.assertRaisesWithMessage(ValueError):
            distance("ATA", "AGTG")

    def test_disallow_left_empty_strand(self):
        with self.assertRaisesWithMessage(ValueError):
            distance("", "G")

    def test_disallow_right_empty_strand(self):
        with self.assertRaisesWithMessage(ValueError):
            distance("G", "")

    # Utility functions
    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")


if __name__ == "__main__":
    unittest.main()
