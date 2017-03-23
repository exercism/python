import unittest

from pascals_triangle import triangle, row, is_triangle


class PascalsTriangleTest(unittest.TestCase):
    def test_triangle1(self):
        ans = ['1', '1 1', '1 2 1', '1 3 3 1', '1 4 6 4 1']
        self.assertEqual(triangle(4), ans)

    def test_triangle2(self):
        ans = ['1', '1 1', '1 2 1', '1 3 3 1', '1 4 6 4 1', '1 5 10 10 5 1',
               '1 6 15 20 15 6 1']
        self.assertEqual(triangle(6), ans)

    def test_is_triangle_true(self):
        inp = ['1', '1 1', '1 2 1', '1 3 3 1', '1 4 6 4 1', '1 5 10 10 5 1']
        self.assertTrue(is_triangle(inp))

    def test_is_triangle_false(self):
        inp = ['1', '1 1', '1 2 1', '1 4 4 1']
        self.assertFalse(is_triangle(inp))

    def test_row1(self):
        ans = '1'
        self.assertEqual(row(0), ans)

    def test_row2(self):
        ans = '1 2 1'
        self.assertEqual(row(2), ans)

    def test_row3(self):
        ans = '1 7 21 35 35 21 7 1'
        self.assertEqual(row(7), ans)


if __name__ == '__main__':
    unittest.main()
