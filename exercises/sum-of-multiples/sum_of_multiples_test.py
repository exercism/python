"""
You can make the following assumptions about the inputs to the
'sum_of_multiples' function:
    * All input numbers are non-negative 'int's, i.e. natural numbers including
      zero.
    * A list of factors must be given, and its elements are unique and sorted in
      ascending order.
"""

import unittest

from sum_of_multiples import sum_of_multiples


class SumOfMultiplesTest(unittest.TestCase):
    def test_sum_to_1(self):
        self.assertEqual(0, sum_of_multiples(1, [3, 5]))

    def test_sum_to_3(self):
        self.assertEqual(3, sum_of_multiples(4, [3, 5]))

    def test_sum_to_10(self):
        self.assertEqual(23, sum_of_multiples(10, [3, 5]))

    def test_sum_to_100(self):
        self.assertEqual(2318, sum_of_multiples(100, [3, 5]))

    def test_sum_to_1000(self):
        self.assertEqual(233168, sum_of_multiples(1000, [3, 5]))

    def test_configurable_7_13_17_to_20(self):
        self.assertEqual(51, sum_of_multiples(20, [7, 13, 17]))

    def test_configurable_4_6_to_15(self):
        self.assertEqual(30, sum_of_multiples(15, [4, 6]))

    def test_configurable_5_6_8_to_150(self):
        self.assertEqual(4419, sum_of_multiples(150, [5, 6, 8]))

    def test_configurable_43_47_to_10000(self):
        self.assertEqual(2203160, sum_of_multiples(10000, [43, 47]))

    def test_configurable_0_to_10(self):
        self.assertEqual(0, sum_of_multiples(10, [0]))

    def test_configurable_0_1_to_10(self):
        self.assertEqual(45, sum_of_multiples(10, [0, 1]))


if __name__ == '__main__':
    unittest.main()
