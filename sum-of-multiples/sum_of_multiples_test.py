import unittest

from sum_of_multiples import SumOfMultiples


class SumOfMultiplesTest(unittest.TestCase):
    def test_sum_to_1(self):
        self.assertEqual(0, SumOfMultiples().to(1))

    def test_sum_to_3(self):
        self.assertEqual(3, SumOfMultiples().to(4))

    def test_sum_to_10(self):
        self.assertEqual(23, SumOfMultiples().to(10))

    def test_sum_to_1000(self):
        self.assertEqual(233168, SumOfMultiples().to(1000))

    def test_configurable_7_13_17_to_20(self):
        self.assertEqual(51, SumOfMultiples(7, 13, 17).to(20))

    def test_configurable_43_47_to_10000(self):
        self.assertEqual(2203160, SumOfMultiples(43, 47).to(10000))


if __name__ == '__main__':
    unittest.main()
