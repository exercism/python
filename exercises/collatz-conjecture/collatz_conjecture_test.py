import unittest

from collatz_conjecture import collatz_steps


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.2.1

class CollatzConjectureTest(unittest.TestCase):

    def test_zero_steps_for_one(self):
        self.assertEqual(collatz_steps(1), 0)

    def test_divide_if_even(self):
        self.assertEqual(collatz_steps(16), 4)

    def test_even_and_odd_steps(self):
        self.assertEqual(collatz_steps(12), 9)

    def test_large_number_of_even_and_odd_steps(self):
        self.assertEqual(collatz_steps(1000000), 152)

    def test_zero_is_invalid_input(self):
        with self.assertRaisesWithMessage(ValueError):
            collatz_steps(0)

    def test_negative_number_is_invalid_input(self):
        with self.assertRaisesWithMessage(ValueError):
            collatz_steps(-15)

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
