import unittest

from difference_of_squares import difference, square_of_sum, sum_of_squares


# test cases adapted from `x-common//canonical-data.json` @ version: 1.0.0

class DifferenceOfSquaresTest(unittest.TestCase):
    def test_square_of_sum_5(self):
        self.assertEqual(square_of_sum(5), 225)

    def test_square_of_sum_10(self):
        self.assertEqual(square_of_sum(10), 3025)

    def test_square_of_sum_100(self):
        self.assertEqual(square_of_sum(100), 25502500)

    def test_sum_of_squares_5(self):
        self.assertEqual(sum_of_squares(5), 55)

    def test_sum_of_squares_10(self):
        self.assertEqual(sum_of_squares(10), 385)

    def test_sum_of_squares_100(self):
        self.assertEqual(sum_of_squares(100), 338350)

    def test_difference_of_squares_0(self):
        self.assertEqual(difference(0), 0)

    def test_difference_of_squares_5(self):
        self.assertEqual(difference(5), 170)

    def test_difference_of_squares_10(self):
        self.assertEqual(difference(10), 2640)

    def test_difference_of_squares_100(self):
        self.assertEqual(difference(100), 25164150)


if __name__ == '__main__':
    unittest.main()
