try:
    from series import Series
except ImportError:
    raise SystemExit('Could not find series.py. Does it exist?')

import unittest


class SeriesTest(unittest.TestCase):
    def test_slices_of_one(self):
        self.assertEqual([[0], [1], [2], [3], [4]],
                         Series("01234").slices(1))

    def test_slices_of_two(self):
        self.assertEqual([[9, 7], [7, 8], [8, 6], [6, 7],
                          [7, 5], [5, 6], [6, 4]],
                         Series("97867564").slices(2))

    def test_slices_of_three(self):
        self.assertEqual([[9, 7, 8], [7, 8, 6], [8, 6, 7],
                          [6, 7, 5], [7, 5, 6], [5, 6, 4]],
                         Series("97867564").slices(3))

    def test_slices_of_four(self):
        self.assertEqual([[0, 1, 2, 3], [1, 2, 3, 4]],
                         Series("01234").slices(4))

    def test_slices_of_five(self):
        self.assertEqual([[0, 1, 2, 3, 4]],
                         Series("01234").slices(5))

    def test_overly_long_slice(self):
        self.assertRaisesRegexp(ValueError,
                                "^Invalid slice length for this series: 4$",
                                Series("012").slices, 4)

    def test_overly_short_slice(self):
        self.assertRaisesRegexp(ValueError,
                                "^Invalid slice length for this series: 0$",
                                Series("01234").slices, 0)


if __name__ == '__main__':
    unittest.main()
