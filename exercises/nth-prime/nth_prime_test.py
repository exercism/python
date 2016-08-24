import unittest

from nth_prime import nth_prime


class NthPrimeTests(unittest.TestCase):
    def test_first_prime(self):
        self.assertEqual(2, nth_prime(1))

    def test_sixth_prime(self):
        self.assertEqual(13, nth_prime(6))

    def test_first_twenty_primes(self):
        self.assertEqual([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31,
                          37, 41, 43, 47, 53, 59, 61, 67, 71],
                         [nth_prime(n) for n in range(1, 21)])

    def test_prime_no_10000(self):
        self.assertEqual(104729, nth_prime(10000))


if __name__ == '__main__':
    unittest.main()
