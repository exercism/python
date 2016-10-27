#
# =============================================================================
# The test cases below assume two functions are defined:
#
#   - triplets_in_range(min, max)
#       Compute all pythagorean triplets (a,b,c) with min <= a,b,c <= max
#
#   - primitive_triplets(b)
#       Find all primitive pythagorean triplets having b as one of their
#       components
#
#       Args:
#          b - an integer divisible by 4 (see explanantion below)
#
# Note that in the latter function the components other than the argument can
# be quite large.
#
# A primitive pythagorean triplet has its 3 componentes coprime. So, (3,4,5) is
# a primitive pythagorean triplet since 3,4 and 5 don't have a common factor.
# On the other hand, (6,8,10), although a pythagorean triplet, is not primitive
# since 2 divides all three components.
#
# A method for finding all primitive pythagorean triplet is given in wikipedia
# (http://en.wikipedia.org/wiki/Pythagorean_triple#Generating_a_triple). The
# triplet a=(m^2-n^2), b=2*m*n and c=(m^2+n^2), where m and n are coprime and
# m-n>0 is odd, generate a primitive triplet. Note that this implies that b has
# to be divisible by 4 and a and c are odd. Also note that we may have either
# a>b or b>a.
#
# The function primitive_triplets should then use the formula above with b set
# to its argument and find all possible pairs (m,n) such that m>n, m-n is odd,
# b=2*m*n and m and n are coprime.
#
# =============================================================================

import unittest

from pythagorean_triplet import (primitive_triplets, triplets_in_range,
                                 is_triplet)


class PythagoreanTripletTest(unittest.TestCase):

    def test_triplet1(self):
        ans = set([(3, 4, 5)])
        self.assertEqual(ans, primitive_triplets(4))

    def test_triplet2(self):
        ans = set([(13, 84, 85), (84, 187, 205), (84, 437, 445),
                   (84, 1763, 1765)])
        self.assertEqual(ans, primitive_triplets(84))

    def test_triplet3(self):
        ans = set([(29, 420, 421), (341, 420, 541), (420, 851, 949),
                   (420, 1189, 1261), (420, 1739, 1789), (420, 4891, 4909),
                   (420, 11021, 11029), (420, 44099, 44101)])
        self.assertEqual(ans, primitive_triplets(420))

    def test_triplet4(self):
        ans = set([(175, 288, 337), (288, 20735, 20737)])
        self.assertEqual(ans, primitive_triplets(288))

    def test_range1(self):
        ans = set([(3, 4, 5), (6, 8, 10)])
        self.assertEqual(ans, triplets_in_range(1, 10))

    def test_range2(self):
        ans = set([(57, 76, 95), (60, 63, 87)])
        self.assertEqual(ans, triplets_in_range(56, 95))

    def test_is_triplet1(self):
        self.assertEqual(True, is_triplet((29, 20, 21)))

    def test_is_triplet2(self):
        self.assertEqual(False, is_triplet((25, 25, 1225)))

    def test_is_triplet3(self):
        self.assertEqual(True, is_triplet((924, 43, 925)))

    def test_odd_number(self):
        self.assertRaises(ValueError, primitive_triplets, 5)


if __name__ == '__main__':
    unittest.main()
