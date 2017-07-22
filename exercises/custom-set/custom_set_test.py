import unittest

from custom_set import CustomSet

class CustomSetTest(unittest.TestCase):
    def test_empty(self):
        empty = CustomSet()
        self.assertTrue(empty.empty())
    
    def test_not_empty(self):
        not_empty = CustomSet(1)
        self.assertFalse(not_empty.empty())
    
    def test_empty_contains_nothing(self):
        empty = CustomSet()
        self.assertFalse(1 in empty)
    
    def test_simple_contains(self):
        simple = CustomSet(1,2,3)
        self.assertTrue(1 in simple)
        self.assertTrue(2 in simple)
        self.assertTrue(3 in simple)
    
    def test_simple_not_contains(self):
        simple = CustomSet(1,2,3)
        self.assertFalse(4 in simple)
    
    def test_empty_subset_of_empty(self):
        empty = CustomSet()
        self.assertTrue(empty.subset(CustomSet()))
    
    def test_empty_subset_of_not_empty(self):
        empty = CustomSet()
        not_empty = CustomSet(1)
        self.assertTrue(not_empty.subset(empty))
    
    def test_non_empty_not_subset_of_empty(self):
        empty = CustomSet()
        not_empty = CustomSet(1)
        self.assertFalse(empty.subset(not_empty))
    
    def test_set_is_subset_of_itself(self):
        test_set = CustomSet(1,2,3)
        self.assertTrue(test_set.subset(CustomSet(1,2,3)))
    
    def test_set_is_subset_of_larger(self):
        test_set = CustomSet(1,2,3)
        larger = CustomSet(1,2,3,4)
        self.assertTrue(larger.subset(test_set))
    
    def test_set_is_not_subset_of_larger(self):
        test_set = CustomSet(1,2,3)
        larger = CustomSet(1,4,5,6)
        self.assertFalse(larger.subset(test_set))

    def test_empty_disjoint_with_empty(self):
        empty = CustomSet()
        self.assertTrue(empty.disjoint(CustomSet()))
    
    def test_empty_disjoint_with_not_empty(self):
        empty = CustomSet()
        not_empty = CustomSet(1,2,3)
        self.assertTrue(empty.disjoint(not_empty))
    
    def test_not_empty_disjoint_with_empty(self):
        empty = CustomSet()
        not_empty = CustomSet(1,2,3)
        self.assertTrue(not_empty.disjoint(empty))
    
    def test_sets_that_share_element_not_disjoint(self):
        seq = CustomSet(1,2,3)
        odds = CustomSet(1,3,5)
        self.assertFalse(odds.disjoint(seq))
        self.assertFalse(seq.disjoint(odds))
    
    def test_sets_that_share_none_disjoint(self):
        seq = CustomSet(1,2,3)
        after = CustomSet(4,5,6)

        self.assertTrue(seq.disjoint(after))
    
    def test_set_with_same_elems_equal(self):
        seq = CustomSet(1,2,3)

        self.assertEqual(seq, seq)
    
    def test_seq_with_different_elems_inequal(self):
        seq = CustomSet(1,2,3)
        after = CustomSet(4,5,6)

        self.assertNotEqual(seq, after)
    
    def test_add_to_empty(self):
        empty = CustomSet()
        empty.add(1)
        expected = CustomSet(1)
        self.assertEqual(empty, expected)
    
    def test_add_to_not_empty(self):
        not_empty = CustomSet(1,2,3)
        not_empty.add(4)
        expected = CustomSet(1,2,3,4)
        self.assertEqual(not_empty, expected)
    
    def test_add_existing_elem(self):
        test_set = CustomSet(1,2,3)
        test_set.add(1)
        expected =  CustomSet(1,2,3)
        self.assertEqual(test_set, expected)
    
    def test_empty_intersection(self):
        empty_intersection = CustomSet().intersection(CustomSet())
        expected = CustomSet()
        self.assertEqual(empty_intersection, expected)
    
    def test_empty_and_non_empty_intersection(self):
        empty = CustomSet()
        non_empty = CustomSet(1,2,3)
        self.assertEqual(non_empty.intersection(empty), empty)
    
    def test_none_shared_intersection(self):
        test_set = CustomSet(1,2,3)
        test_set_2 = CustomSet(4,5,6)
        self.assertEqual(test_set.intersection(test_set_2), CustomSet())
    
    def test_shared_intersection(self):
        expected = CustomSet(1,3)
        self.assertEqual(
            CustomSet(1,2,3).intersection(CustomSet(1,3,5)), 
            expected)
    
    def test_empty_diff(self):
        empty = CustomSet()
        self.assertEqual(empty - empty, CustomSet())
    
    def test_empty_non_empty_diff(self):
        empty = CustomSet()
        non_empty = CustomSet(1,2,3)
        self.assertEqual(empty - non_empty, empty)
        self.assertEqual(non_empty - empty, non_empty)
    
    def test_non_empty_diff(self):
        test_set = CustomSet(1,2,3,4)
        other_set = CustomSet(1,3,5,7)

        self.assertEqual(test_set - other_set, CustomSet(2,4))
        self.assertEqual(other_set - test_set, CustomSet(5,7))
    
    def test_empty_union(self):
        empty = CustomSet()
        self.assertEqual(empty + empty, empty)
    
    def test_non_empty_empty_union(self):
        non_empty = CustomSet(1,2,3)
        empty = CustomSet()
        
        self.assertEqual(non_empty + empty, non_empty)
        self.assertEqual(empty + non_empty,non_empty)
    
    def test_non_empty_union(self):
        result = CustomSet(1,2,3) + CustomSet(2,3)
        self.assertEqual(result, CustomSet(1,2,3))
    
    def test_size(self):
        empty = CustomSet()
        non_empty = CustomSet(1,2,3)
        repeated = CustomSet(1,3,2,1,2,3)

        self.assertEqual(len(empty), 0)
        self.assertEqual(len(non_empty), 3)
        self.assertEqual(len(repeated), 3)
    
    def test_list(self):
        empty = CustomSet()
        non_empty = CustomSet(1,2,3)
        repeated = CustomSet(1,3,2,1,3,2)

        self.assertEqual(list(empty), [])
        self.assertEqual(list(non_empty), [1,2,3])
        self.assertEqual(list(repeated), [1,2,3])