import unittest

from matrix import Matrix


class MatrixTest(unittest.TestCase):
    def test_extract_a_row(self):
        matrix = Matrix("1 2\n10 20")
        self.assertEqual(matrix.rows[0], [1, 2])

    def test_extract_same_row_again(self):
        matrix = Matrix("9 7\n8 6")
        self.assertEqual(matrix.rows[0], [9, 7])

    def test_extract_other_row(self):
        matrix = Matrix("9 8 7\n19 18 17")
        self.assertEqual(matrix.rows[1], [19, 18, 17])

    def test_extract_other_row_again(self):
        matrix = Matrix("1 4 9\n16 25 36")
        self.assertEqual(matrix.rows[1], [16, 25, 36])

    def test_extract_a_column(self):
        matrix = Matrix("1 2 3\n4 5 6\n7 8 9\n8 7 6")
        self.assertEqual(matrix.columns[0], [1, 4, 7, 8])

    def test_extract_another_column(self):
        matrix = Matrix("89 1903 3\n18 3 1\n9 4 800")
        self.assertEqual(matrix.columns[1], [1903, 3, 4])


if __name__ == '__main__':
    unittest.main()
