import unittest

from matrix import Matrix


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.1.0

class MatrixTest(unittest.TestCase):
    def test_extract_row_from_one_number_matrix(self):
        matrix = Matrix("1")
        self.assertEqual(matrix.row(1), [1])

    def test_can_extract_row(self):
        matrix = Matrix("1 2\n3 4")
        self.assertEqual(matrix.row(2), [3, 4])

    def test_extract_row_where_numbers_have_different_widths(self):
        matrix = Matrix("1 2\n10 20")
        self.assertEqual(matrix.row(2), [10, 20])

    def test_can_extract_row_from_non_square_matrix(self):
        matrix = Matrix("1 2 3\n4 5 6\n7 8 9\n8 7 6")
        self.assertEqual(matrix.row(3), [7, 8, 9])

    def test_extract_column_from_one_number_matrix(self):
        matrix = Matrix("1")
        self.assertEqual(matrix.column(1), [1])

    def test_can_extract_column(self):
        matrix = Matrix("1 2 3\n4 5 6\n7 8 9")
        self.assertEqual(matrix.column(3), [3, 6, 9])

    def test_can_extract_column_from_non_square_matrix(self):
        matrix = Matrix("1 2 3\n4 5 6\n7 8 9\n8 7 6")
        self.assertEqual(matrix.column(3), [3, 6, 9, 6])

    def test_extract_column_where_numbers_have_different_widths(self):
        matrix = Matrix("89 1903 3\n18 3 1\n9 4 800")
        self.assertEqual(matrix.column(2), [1903, 3, 4])


if __name__ == '__main__':
    unittest.main()
