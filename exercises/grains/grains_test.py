import unittest

from grains import (
    on_square,
    total_after,
)


class GrainsTest(unittest.TestCase):
    def test_square_1(self):
        self.assertEqual(on_square(1), 1)
        self.assertEqual(total_after(1), 1)

    def test_square_2(self):
        self.assertEqual(on_square(2), 2)
        self.assertEqual(total_after(2), 3)

    def test_square_3(self):
        self.assertEqual(on_square(3), 4)
        self.assertEqual(total_after(3), 7)

    def test_square_4(self):
        self.assertEqual(on_square(4), 8)
        self.assertEqual(total_after(4), 15)

    def test_square_16(self):
        self.assertEqual(on_square(16), 32768)
        self.assertEqual(total_after(16), 65535)

    def test_square_32(self):
        self.assertEqual(on_square(32), 2147483648)
        self.assertEqual(total_after(32), 4294967295)

    def test_square_64(self):
        self.assertEqual(on_square(64), 9223372036854775808)
        self.assertEqual(total_after(64), 18446744073709551615)

    def test_square_0_raises_exception(self):
        with self.assertRaises(ValueError):
            on_square(0)
        with self.assertRaises(ValueError):
            total_after(0)

    def test_square_negative_raises_exception(self):
        with self.assertRaises(ValueError):
            on_square(-1)
        with self.assertRaises(ValueError):
            total_after(-1)

    def test_square_gt_64_raises_exception(self):
        with self.assertRaises(ValueError):
            on_square(65)
        with self.assertRaises(ValueError):
            total_after(65)


if __name__ == '__main__':
    unittest.main()
