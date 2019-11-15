import unittest

from grains import square, total

# Tests adapted from `problem-specifications//canonical-data.json` @ v1.2.0


class GrainsTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(square(1), 1)

    def test_2(self):
        self.assertEqual(square(2), 2)

    def test_3(self):
        self.assertEqual(square(3), 4)

    def test_4(self):
        self.assertEqual(square(4), 8)

    def test_16(self):
        self.assertEqual(square(16), 32768)

    def test_32(self):
        self.assertEqual(square(32), 2147483648)

    def test_64(self):
        self.assertEqual(square(64), 9223372036854775808)

    def test_square_0_raises_an_exception(self):
        with self.assertRaisesWithMessage(ValueError):
            square(0)

    def test_negative_square_raises_an_exception(self):
        with self.assertRaisesWithMessage(ValueError):
            square(-1)

    def test_square_greater_than_64_raises_an_exception(self):
        with self.assertRaisesWithMessage(ValueError):
            square(65)

    def test_returns_the_total_number_of_grains_on_the_board(self):
        self.assertEqual(total(), 18446744073709551615)

    # Utility functions
    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")


if __name__ == "__main__":
    unittest.main()
