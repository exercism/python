"""
You can make the following assumptions about the inputs to the
'sum_of_multiples' function:
    * All input numbers are non-negative 'int's, i.e. natural numbers including
      zero.
    * If a list of factors is given, its elements are uniqe and sorted in
      ascending order.
    * If the 'factors' argument is missing, use the list [3, 5] instead.
"""

import unittest

from sum_of_multiples import sum_of_multiples


class SumOfMultiplesTest(unittest.TestCase):
    def test_sum_to_1(self):
        self.assertEqual(0, sum_of_multiples(1))

    def test_sum_to_3(self):
        self.assertEqual(3, sum_of_multiples(4))

    def test_sum_to_10(self):
        self.assertEqual(23, sum_of_multiples(10))

    def test_sum_to_1000(self):
        self.assertEqual(233168, sum_of_multiples(1000))

    def test_configurable_7_13_17_to_20(self):
        self.assertEqual(51, sum_of_multiples(20, [7, 13, 17]))

    def test_configurable_43_47_to_10000(self):
        self.assertEqual(2203160, sum_of_multiples(10000, [43, 47]))

    def test_configurable_0_to_10(self):
        self.assertEqual(0, sum_of_multiples(10, [0]))

    def test_configurable_0_1_to_10(self):
        self.assertEqual(45, sum_of_multiples(10, [0, 1]))


if __name__ == '__main__':
    unittest.main()
