try:
    from series import Series
except ImportError:
    raise SystemExit('Could not find series.py. Does it exist?')

import unittest


class SeriesTest(unittest.TestCase):
    def test_slices_of_two(self):
        self.assertEqual([[9, 7], [7, 8], [8, 6], [6, 7],
                          [7, 5], [5, 6], [6, 4]],
                         Series("97867564").slices(2))

    def test_overly_long_slice(self):
        self.assertRaisesRegexp(ValueError,
                                "^Invalid slice length for this series: 4$",
                                Series("012").slices, 4)

    def test_largest_product_of_2(self):
        self.assertEqual(72, Series("0123456789").largest_product(2))

    def test_tiny_number(self):
        self.assertEqual(9, Series("19").largest_product(2))

    def test_largest_product_of_3(self):
        self.assertEqual(270, Series("1027839564").largest_product(3))

    def test_big_number(self):
        self.assertEqual(28350,
                         Series("52677741234314237566414902593461595376319419"
                                "139427").largest_product(6))

    def test_identity(self):
        self.assertEqual(1, Series("").largest_product(0))

    def test_slices_bigger_than_number(self):
        self.assertRaisesRegexp(ValueError,
                                "^Invalid slice length for this series: 4$",
                                Series("012").largest_product, 4)


if __name__ == '__main__':
    unittest.main()
