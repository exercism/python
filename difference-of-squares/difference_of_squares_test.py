import unittest

from difference_of_squares import difference, square_of_sum, sum_of_squares


class DifferenceOfSquaresTest(unittest.TestCase):
    def test_square_of_sum_5(self):
        self.assertEqual(225, square_of_sum(5))

    @unittest.skip('not yet implemented')
    def test_sum_of_squares_5(self):
        self.assertEqual(55, sum_of_squares(5))

    @unittest.skip('not yet implemented')
    def test_difference_5(self):
        self.assertEqual(170, difference(5))

    @unittest.skip('not yet implemented')
    def test_square_of_sum_100(self):
        self.assertEqual(25502500, square_of_sum(100))

    @unittest.skip('not yet implemented')
    def test_sum_of_squares_100(self):
        self.assertEqual(338350, sum_of_squares(100))

    @unittest.skip('not yet implemented')
    def test_difference_100(self):
        self.assertEqual(25164150, difference(100))


if __name__ == '__main__':
    unittest.main()
