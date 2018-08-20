import unittest

from pythagorean_triplet import (
    primitive_triplets,
    triplets_in_range,
    is_triplet
)


class PythagoreanTripletTest(unittest.TestCase):
    def test_triplet1(self):
        ans = set([(3, 4, 5)])
        self.assertEqual(primitive_triplets(4), ans)

    def test_triplet2(self):
        ans = set([(13, 84, 85), (84, 187, 205), (84, 437, 445),
                   (84, 1763, 1765)])
        self.assertEqual(primitive_triplets(84), ans)

    def test_triplet3(self):
        ans = set([(29, 420, 421), (341, 420, 541), (420, 851, 949),
                   (420, 1189, 1261), (420, 1739, 1789), (420, 4891, 4909),
                   (420, 11021, 11029), (420, 44099, 44101)])
        self.assertEqual(primitive_triplets(420), ans)

    def test_triplet4(self):
        ans = set([(175, 288, 337), (288, 20735, 20737)])
        self.assertEqual(primitive_triplets(288), ans)

    def test_range1(self):
        ans = set([(3, 4, 5), (6, 8, 10)])
        self.assertEqual(triplets_in_range(1, 10), ans)

    def test_range2(self):
        ans = set([(57, 76, 95), (60, 63, 87)])
        self.assertEqual(triplets_in_range(56, 95), ans)

    def test_is_triplet1(self):
        self.assertIs(is_triplet((29, 20, 21)), True)

    def test_is_triplet2(self):
        self.assertIs(is_triplet((25, 25, 1225)), False)

    def test_is_triplet3(self):
        self.assertIs(is_triplet((924, 43, 925)), True)

    def test_odd_number(self):
        with self.assertRaisesWithMessage(ValueError):
            primitive_triplets(5)

    # Utility functions
    def setUp(self):
        try:
            self.assertRaisesRegex
        except AttributeError:
            self.assertRaisesRegex = self.assertRaisesRegexp

    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")


if __name__ == '__main__':
    unittest.main()
