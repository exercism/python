from saddle_points import saddle_points

import unittest

class SaddlePointTest(unittest.TestCase):
    def test_one_saddle(self):
        inp = [[9,8,7],[5,3,2],[6,6,7]]
        self.assertEqual(set([(1,0)]), saddle_points(inp))

    def test_no_saddle(self):
        self.assertEqual(set(), saddle_points([[2,1],[1,2]]))

    def test_mult_saddle(self):
        inp = [[5,3,5,4],[6,4,7,3],[5,1,5,3]]
        ans = set([(0,0),(0,2),(2,0),(2,2)])
        self.assertEqual(ans, saddle_points(inp))

    def test_empty_matrix(self):
        self.assertEqual(set(), saddle_points([]))

    def test_irregular_matrix(self):
        with self.assertRaisesRegexp(ValueError, 'irregular matrix'):
            saddle_points([[1,2,3],[2,3],[3,2,1]])


if __name__ == '__main__':
    unittest.main()
