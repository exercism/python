import unittest

from perfect_numbers import is_perfect


class PerfectNumbersTest(unittest.TestCase):

    def test_first_perfect_number(self):
        self.assertIs(is_perfect(6), True)

    def test_no_perfect_number(self):
        self.assertIs(is_perfect(8), False)

    def test_second_perfect_number(self):
        self.assertIs(is_perfect(28), True)

    def test_abundant(self):
        self.assertIs(is_perfect(20), False)

    def test_answer_to_the_ultimate_question_of_life(self):
        self.assertIs(is_perfect(42), False)

    def test_third_perfect_number(self):
        self.assertIs(is_perfect(496), True)

    def test_odd_abundant(self):
        self.assertIs(is_perfect(945), False)

    def test_fourth_perfect_number(self):
        self.assertIs(is_perfect(8128), True)

    def test_fifth_perfect_number(self):
        self.assertIs(is_perfect(33550336), True)

    def test_sixth_perfect_number(self):
        self.assertIs(is_perfect(8589869056), True)

    def test_seventh_perfect_number(self):
        self.assertIs(is_perfect(137438691328), True)


if __name__ == '__main__':
    unittest.main()
