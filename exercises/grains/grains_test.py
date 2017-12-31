import unittest

from grains import (
    on_square,
    total_after,
)


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.0.0

class GrainsTest(unittest.TestCase):
    def test_square_1(self):
        self.assertEqual(on_square(1), 1)

    def test_square_2(self):
        self.assertEqual(on_square(2), 2)

    def test_square_3(self):
        self.assertEqual(on_square(3), 4)

    def test_square_4(self):
        self.assertEqual(on_square(4), 8)

    def test_square_16(self):
        self.assertEqual(on_square(16), 32768)

    def test_square_32(self):
        self.assertEqual(on_square(32), 2147483648)

    def test_square_64(self):
        self.assertEqual(on_square(64), 9223372036854775808)

    def test_square_0_raises_exception(self):
        with self.assertRaisesWithMessage(ValueError):
            on_square(0)
        with self.assertRaisesWithMessage(ValueError):
            total_after(0)

    def test_square_negative_raises_exception(self):
        with self.assertRaisesWithMessage(ValueError):
            on_square(-1)
        with self.assertRaisesWithMessage(ValueError):
            total_after(-1)

    def test_square_gt_64_raises_exception(self):
        with self.assertRaisesWithMessage(ValueError):
            on_square(65)
        with self.assertRaisesWithMessage(ValueError):
            total_after(65)

    def test_total(self):
        self.assertEqual(total_after(64), 18446744073709551615)

    # Utility functions
    def setUp(self):
        try:
            self.assertRaisesRegex = self.assertRaisesRegexp
        except AttributeError:
            pass

    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")


if __name__ == '__main__':
    unittest.main()
