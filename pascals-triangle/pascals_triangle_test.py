from pascals_triangle import triangle, row, is_triangle

import unittest

class PascalsTriangleTest(unittest.TestCase):
    def test_triangle1(self):
        ans = ['1', '1 1', '1 2 1', '1 3 3 1', '1 4 6 4 1']
        self.assertEqual(ans, triangle(4))

    @unittest.skip("Not implemented yet")
    def test_triangle2(self):
        ans = ['1', '1 1', '1 2 1', '1 3 3 1', '1 4 6 4 1', '1 5 10 10 5 1',
               '1 6 15 20 15 6 1']
        self.assertEqual(ans, triangle(6))

    @unittest.skip("Not implemented yet")
    def test_is_triangle_true(self):
        inp = ['1', '1 1', '1 2 1', '1 3 3 1', '1 4 6 4 1', '1 5 10 10 5 1']
        self.assertEqual(True, is_triangle(inp))

    @unittest.skip("Not implemented yet")
    def test_is_triangle_false(self):
        inp = ['1', '1 1', '1 2 1', '1 4 4 1']
        self.assertEqual(False, is_triangle(inp))

    @unittest.skip("Not implemented yet")
    def test_row1(self):
        ans = '1'
        self.assertEqual(ans, row(0))

    @unittest.skip("Not implemented yet")
    def test_row2(self):
        ans = '1 2 1'
        self.assertEqual(ans, row(2))

    @unittest.skip("Not implemented yet")
    def test_row3(self):
        ans = '1 7 21 35 35 21 7 1'
        self.assertEqual(ans, row(7))


if __name__ == '__main__':
    unittest.main()
