import unittest

from hamming import (
    distance,
)

# Tests adapted from `problem-specifications//canonical-data.json`


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
        with self.assertRaises(ValueError) as err:
            distance("AATG", "AAA")

        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "Strands must be of equal length.")

    def test_disallow_second_strand_longer(self):
        with self.assertRaises(ValueError) as err:
            distance("ATA", "AGTG")

        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "Strands must be of equal length.")

    def test_disallow_empty_first_strand(self):
        with self.assertRaises(ValueError) as err:
            distance("", "G")

        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "Strands must be of equal length.")

    def test_disallow_empty_second_strand(self):
        with self.assertRaises(ValueError) as err:
            distance("G", "")

        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "Strands must be of equal length.")
