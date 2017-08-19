import unittest

from collatz_conjecture import collatz_steps

# Test cases adapted from `x-common//canonical-data.json` @ version: 1.1.1


class CollatzConjectureTests(unittest.TestCase):

    def test_zero_steps_for_one(self):
        self.assertEqual(collatz_steps(1), 0)

    def test_divide_if_even(self):
        self.assertEqual(collatz_steps(16), 4)

    def test_even_and_odd_steps(self):
        self.assertEqual(collatz_steps(12), 9)

    def test_large_number_of_even_and_odd_steps(self):
        self.assertEqual(collatz_steps(1000000), 152)

    def test_zero_is_invalid_input(self):
        self.assertEqual(collatz_steps(0), None)

    def test_negative_number_is_invalid_input(self):
        self.assertEqual(collatz_steps(-1), None)

        self.assertEqual(collatz_steps(-15), None)


if __name__ == '__main__':
    unittest.main()
