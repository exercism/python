import unittest

from perfect_numbers import classify


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.0.1

class PerfectNumbersTest(unittest.TestCase):
    def test_smallest_perfect_number(self):
        self.assertIs(classify(6), "perfect")

    def test_medium_perfect_number(self):
        self.assertIs(classify(28), "perfect")

    def test_large_perfect_number(self):
        self.assertIs(classify(33550336), "perfect")

    # Additional tests for this track
    def test_third_perfect_number(self):
        self.assertIs(classify(496), "perfect")

    def test_fourth_perfect_number(self):
        self.assertIs(classify(8128), "perfect")

    def test_sixth_perfect_number(self):
        self.assertIs(classify(8589869056), "perfect")

    def test_seventh_perfect_number(self):
        self.assertIs(classify(137438691328), "perfect")


class AbundantNumbersTest(unittest.TestCase):
    def test_smallest_abundant_number(self):
        self.assertIs(classify(12), "abundant")

    def test_medium_abundant_number(self):
        self.assertIs(classify(30), "abundant")

    def test_large_abundant_number(self):
        self.assertIs(classify(33550335), "abundant")

    # Additional tests for this track
    def test_answer_to_the_ultimate_question_of_life(self):
        self.assertIs(classify(42), "abundant")

    def test_odd_abundant(self):
        self.assertIs(classify(945), "abundant")

    def test_even_abundant(self):
        self.assertIs(classify(20), "abundant")


class DeficientNumbersTest(unittest.TestCase):
    def test_smallest_prime_deficient_number(self):
        self.assertIs(classify(2), "deficient")

    def test_smallest_nonprime_deficient_number(self):
        self.assertIs(classify(4), "deficient")

    def test_medium_deficient_number(self):
        self.assertIs(classify(32), "deficient")

    def test_large_deficient_number(self):
        self.assertIs(classify(33550337), "deficient")

    def test_edge_case(self):
        self.assertIs(classify(1), "deficient")


class InvalidInputsTest(unittest.TestCase):
    def test_zero(self):
        with self.assertRaisesWithMessage(ValueError):
            classify(0)

    def test_negative(self):
        with self.assertRaisesWithMessage(ValueError):
            classify(-1)

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
