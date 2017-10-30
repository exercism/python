import unittest

from spiral_matrix import matrix

# Tests adapted from `problem-specifications//canonical-data.json` @ v1.0.0

class SpiralMatrixTests(unittest.TestCase):
    def test_empty_spiral(self):
        expected = []
        self.assertEqual(matrix(0),expected)

    def test_trivial_spiral(self):
        expected = [[1]]
        self.assertEqual(matrix(1),expected)

    def test_spiral_size_2(self):
        expected = [[1,2],
                    [4,3]]
        self.assertEqual(matrix(2),expected)

    def test_spiral_size_3(self):
        expected = [[1,2,3],
                    [8,9,4],
                    [7,6,5]]
        self.assertEqual(matrix(3),expected)

    def test_spiral_size_4(self):
        expected = [[1,2,3,4],
                    [12,13,14,5],
                    [11,16,15,6],
                    [10, 9, 8,7]]
        self.assertEqual(matrix(4),expected)

    def test_spiral_size_5(self):
        expected = [[1,2,3,4,5],
                    [16,17,18,19,6],
                    [15,24,25,20,7],
                    [14,23,22,21,8],
                    [13,12,11,10,9]]
        self.assertEqual(matrix(5),expected)
        
if __name__ == '__main__':
    unittest.main()
