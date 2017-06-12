import unittest

from custom_set import CustomSet

class CustomSetTest(unittest.TestCase):
    def setUp(self):
        self.a = CustomSet()
        for number in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]:
            self.a.add(number)
        self.b = CustomSet()
        for number in [2,4,6,8,10,12,14,16,18,20]:
            self.b.add(number)
        self.c = self.a.copy()
        self.d = CustomSet()
        for number in [21,22,23,24,25,26,27,28,29,30]:
            self.d.add(number)

    def test_empty(self):
        empty = CustomSet()
        self.assertTrue(empty.empty())
        self.assertFalse(self.a.empty())

    def test_subset(self):
        self.assertTrue(self.a.subset(b))

    def test_disjoint(self):
        self.assertTrue(self.a.disjoint(d))

    def test_equal(self):
        self.assertTrue(self.a.equals(self.c))

    def test_intersection(self):
        intersection = self.a.intersection(self.b)
        self.assertEqual(intersection, self.b)

    def test_union(self):
        union = self.a.union(self.b)
        self.assertEqual(union, self.a)

    def test_difference(self):
        difference = self.a.difference(self.b)
        self.assertEqual(difference, CustomSet([1,3,5,7,9,11,13,15,17,19]))

    def test_clear(self):
        self.assertEqual(self.a.clear(),CustomSet())

    def test_size(self):
        self.assertEqual(self.b.size(), 10)

    def test_to_list(self):
        self.assertEqual(self.b.to_list(), [2,4,6,8,10,12,14,16,18,20])
