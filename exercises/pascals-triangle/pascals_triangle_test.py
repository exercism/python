import unittest

from pascals_triangle import rows


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.2.0

TRIANGLE = [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]


class PascalsTriangleTest(unittest.TestCase):
    def test_zero_rows(self):
        self.assertEqual(rows(0), [])

    def test_single_row(self):
        self.assertEqual(rows(1), TRIANGLE[:1])

    def test_two_rows(self):
        self.assertEqual(rows(2), TRIANGLE[:2])

    def test_three_rows(self):
        self.assertEqual(rows(3), TRIANGLE[:3])

    def test_four_rows(self):
        self.assertEqual(rows(4), TRIANGLE[:4])

    def test_five_rows(self):
        self.assertEqual(rows(5), TRIANGLE[:5])

    def test_six_rows(self):
        self.assertEqual(rows(6), TRIANGLE[:6])

    def test_ten_rows(self):
        self.assertEqual(rows(10), TRIANGLE[:10])

    def test_negative_rows(self):
        self.assertEqual(rows(-1), None)


if __name__ == '__main__':
    unittest.main()
