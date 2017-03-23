import unittest

from prime_factors import prime_factors


class PrimeFactorsTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(prime_factors(1), [])

    def test_2(self):
        self.assertEqual(prime_factors(2), [2])

    def test_3(self):
        self.assertEqual(prime_factors(3), [3])

    def test_4(self):
        self.assertEqual(prime_factors(4), [2, 2])

    def test_6(self):
        self.assertEqual(prime_factors(6), [2, 3])

    def test_8(self):
        self.assertEqual(prime_factors(8), [2, 2, 2])

    def test_9(self):
        self.assertEqual(prime_factors(9), [3, 3])

    def test_27(self):
        self.assertEqual(prime_factors(27), [3, 3, 3])

    def test_625(self):
        self.assertEqual(prime_factors(625), [5, 5, 5, 5])

    def test_901255(self):
        self.assertEqual(prime_factors(901255), [5, 17, 23, 461])

    def test_93819012551(self):
        self.assertEqual(prime_factors(93819012551), [11, 9539, 894119])


if __name__ == '__main__':
    unittest.main()
