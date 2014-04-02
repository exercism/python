from saddle_points import saddle_points

import unittest

class PythagoreanTripletTest(unittest.TestCase):
    def test_one_saddle(self):
        inp = [[9,8,7],[5,3,2],[6,6,7]]
        self.assertEqual(set([(1,0)]), saddle_points(inp))

    def test_no_saddle(self):
        inp = [[2,1],[1,2]]
        ans = set()
        self.assertEqual(ans, saddle_points(inp))

    def test_mult_saddle(self):
        inp = [[5,3,5,4],[6,4,7,3],[5,1,5,3]]
        ans = set([(0,0),(0,2),(2,0),(2,2)])
        self.assertEqual(ans, saddle_points(inp))

    def test_irregular_matrix(self):
        with self.assertRaises(ValueError) as context:
            saddle_points([[1,2,3],[2,3],[3,2,1]])
        self.assertEqual(context.exception.message, 'Matrix with uneven rows')


if __name__ == '__main__':
    unittest.main()
