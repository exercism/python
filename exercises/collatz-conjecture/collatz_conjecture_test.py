import unittest

from collatz_conjecture import steps

# Tests adapted from `problem-specifications//canonical-data.json`


class CollatzConjectureTest(unittest.TestCase):
    def test_zero_steps_for_one(self):
        self.assertEqual(steps(1), 0)

    def test_divide_if_even(self):
        self.assertEqual(steps(16), 4)

    def test_even_and_odd_steps(self):
        self.assertEqual(steps(12), 9)

    def test_large_number_of_even_and_odd_steps(self):
        self.assertEqual(steps(1000000), 152)

    def test_zero_is_an_error(self):
        with self.assertRaisesWithMessage(ValueError):
            steps(0)

    def test_negative_value_is_an_error(self):
        with self.assertRaisesWithMessage(ValueError):
            steps(-15)

    # Utility functions
    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")


if __name__ == "__main__":
    unittest.main()
