import unittest

from nth_prime import nth_prime


# Tests adapted from `problem-specifications//canonical-data.json` @ v2.1.0

class NthPrimeTests(unittest.TestCase):
    def test_first_prime(self):
        self.assertEqual(nth_prime(1), 2)

    def test_second_prime(self):
        self.assertEqual(nth_prime(2), 3)

    def test_sixth_prime(self):
        self.assertEqual(nth_prime(6), 13)

    def test_big_prime(self):
        self.assertEqual(nth_prime(10001), 104743)

    def test_there_is_no_zeroth_prime(self):
        with self.assertRaisesWithMessage(ValueError):
            nth_prime(0)

    # additional track specific test
    def test_first_twenty_primes(self):
        self.assertEqual([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31,
                          37, 41, 43, 47, 53, 59, 61, 67, 71],
                         [nth_prime(n) for n in range(1, 21)])

    # Utility functions
    def setUp(self):
        try:
            self.assertRaisesRegex
        except AttributeError:
            self.assertRaisesRegex = self.assertRaisesRegexp

    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")


if __name__ == '__main__':
    unittest.main()
