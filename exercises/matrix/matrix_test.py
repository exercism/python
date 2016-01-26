import unittest

from matrix import Matrix


class MatrixTest(unittest.TestCase):
    def test_extract_a_row(self):
        matrix = Matrix("1 2\n10 20")
        self.assertEqual([1, 2], matrix.rows[0])

    def test_extract_same_row_again(self):
        matrix = Matrix("9 7\n8 6")
        self.assertEqual([9, 7], matrix.rows[0])

    def test_extract_other_row(self):
        matrix = Matrix("9 8 7\n19 18 17")
        self.assertEqual([19, 18, 17], matrix.rows[1])

    def test_extract_other_row_again(self):
        matrix = Matrix("1 4 9\n16 25 36")
        self.assertEqual([16, 25, 36], matrix.rows[1])

    def test_extract_a_column(self):
        matrix = Matrix("1 2 3\n4 5 6\n7 8 9\n8 7 6")
        self.assertEqual([1, 4, 7, 8], matrix.columns[0])

    def test_extract_another_column(self):
        matrix = Matrix("89 1903 3\n18 3 1\n9 4 800")
        self.assertEqual([1903, 3, 4], matrix.columns[1])


if __name__ == '__main__':
    unittest.main()
