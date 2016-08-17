import unittest

from perfect_numbers import is_perfect


class PerfectNumbersTest(unittest.TestCase):

    def test_first_perfect_number(self):
        self.assertTrue(is_perfect(6))

    def test_no_perfect_number(self):
        self.assertFalse(is_perfect(8))

    def test_second_perfect_number(self):
        self.assertTrue(is_perfect(28))

    def test_abundant(self):
        self.assertFalse(is_perfect(20))

    def test_answer_to_the_ultimate_question_of_life(self):
        self.assertFalse(is_perfect(42))

    def test_third_perfect_number(self):
        self.assertTrue(is_perfect(496))

    def test_odd_abundant(self):
        self.assertFalse(is_perfect(945))

    def test_fourth_perfect_number(self):
        self.assertTrue(is_perfect(8128))

    def test_fifth_perfect_number(self):
        self.assertTrue(is_perfect(33550336))

    def test_sixth_perfect_number(self):
        self.assertTrue(is_perfect(8589869056))

    def test_seventh_perfect_number(self):
        self.assertTrue(is_perfect(137438691328))

if __name__ == '__main__':
    unittest.main()
