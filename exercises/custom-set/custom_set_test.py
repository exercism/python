import unittest

from custom_set import CustomSet


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.3.0

class CustomSetTest(unittest.TestCase):
    def test_sets_with_no_elements_are_empty(self):
        sut = CustomSet()
        self.assertIs(sut.isempty(), True)

    def test_sets_with_elements_are_not_empty(self):
        sut = CustomSet([1])
        self.assertIs(sut.isempty(), False)

    def test_empty_set_contains_nothing(self):
        sut = CustomSet()
        self.assertNotIn(1, sut)

    def test_set_contains_when_element_in_set(self):
        sut = CustomSet([1])
        self.assertIn(1, sut)

    def test_set_does_not_contains_when_element_not_in_set(self):
        sut = CustomSet([1, 2, 3])
        self.assertNotIn(4, sut)

    def test_empty_set_is_subset_of_another_empty_set(self):
        set1 = CustomSet()
        set2 = CustomSet()
        self.assertIs(set1.issubset(set2), True)

    def test_empty_set_is_subset_of_non_empty_set(self):
        set1 = CustomSet()
        set2 = CustomSet([1])
        self.assertIs(set1.issubset(set2), True)

    def test_non_empty_set_is_not_subet_of_empty_set(self):
        set1 = CustomSet([1])
        set2 = CustomSet()
        self.assertIs(set1.issubset(set2), False)

    def test_set_is_subset_of_set_with_exact_same_elements(self):
        set1 = CustomSet([1, 2, 3])
        set2 = CustomSet([1, 2, 3])
        self.assertIs(set1.issubset(set2), True)

    def test_set_is_subset_of_larger_set_with_same_elements(self):
        set1 = CustomSet([1, 2, 3])
        set2 = CustomSet([4, 1, 2, 3])
        self.assertIs(set1.issubset(set2), True)

    def test_set_not_subset_of_set_that_does_not_contain_its_elements(self):
        set1 = CustomSet([1, 2, 3])
        set2 = CustomSet([4, 1, 3])
        self.assertIs(set1.issubset(set2), False)

    def test_empty_set_disjoint_with_itself(self):
        set1 = CustomSet()
        set2 = CustomSet()
        self.assertIs(set1.isdisjoint(set2), True)

    def test_empty_set_disjoint_with_non_empty_set(self):
        set1 = CustomSet()
        set2 = CustomSet([1])
        self.assertIs(set1.isdisjoint(set2), True)

    def test_non_empty_set_disjoint_with_empty_set(self):
        set1 = CustomSet([1])
        set2 = CustomSet()
        self.assertIs(set1.isdisjoint(set2), True)

    def test_sets_not_disjoint_if_element_is_shared(self):
        set1 = CustomSet([1, 2])
        set2 = CustomSet([2, 3])
        self.assertIs(set1.isdisjoint(set2), False)

    def test_sets_disjoint_if_not_elements_are_shared(self):
        set1 = CustomSet([1, 2])
        set2 = CustomSet([3, 4])
        self.assertIs(set1.isdisjoint(set2), True)

    def test_empty_sets_are_equal(self):
        set1 = CustomSet()
        set2 = CustomSet()
        self.assertEqual(set1, set2)

    def test_empty_set_not_equal_to_non_empty_set(self):
        set1 = CustomSet()
        set2 = CustomSet([1, 2, 3])
        self.assertNotEqual(set1, set2)

    def test_non_empty_set_not_equal_to_empty_set(self):
        set1 = CustomSet([1, 2, 3])
        set2 = CustomSet()
        self.assertNotEqual(set1, set2)

    def test_sets_with_same_exact_same_elements_are_equal(self):
        set1 = CustomSet([1, 2])
        set2 = CustomSet([2, 1])
        self.assertEqual(set1, set2)

    def test_sets_with_different_elements_are_not_equal(self):
        set1 = CustomSet([1, 2, 3])
        set2 = CustomSet([1, 2, 4])
        self.assertNotEqual(set1, set2)

    def test_set_is_not_equal_to_larger_set_with_same_elements(self):
        set1 = CustomSet([1, 2, 3])
        set2 = CustomSet([1, 2, 3, 4])
        self.assertNotEqual(set1, set2)

    def test_add_to_empty_set(self):
        sut = CustomSet()
        sut.add(1)
        expected = CustomSet([1])
        self.assertEqual(sut, expected)

    def test_add_to_non_empty_set(self):
        sut = CustomSet([1, 2, 4])
        sut.add(3)
        expected = CustomSet([1, 2, 3, 4])
        self.assertEqual(sut, expected)

    def test_adding_existing_element_does_not_change_set(self):
        sut = CustomSet([1, 2, 3])
        sut.add(3)
        expected = CustomSet([1, 2, 3])
        self.assertEqual(sut, expected)

    def test_intersection_of_two_empty_sets_is_empty_set(self):
        set1 = CustomSet()
        set2 = CustomSet()
        expected = CustomSet()
        self.assertEqual(set1.intersection(set2), expected)

    def test_intersection_of_empty_set_and_non_empty_set_is_empty_set(self):
        set1 = CustomSet()
        set2 = CustomSet([3, 2, 5])
        expected = CustomSet()
        self.assertEqual(set1.intersection(set2), expected)

    def test_intersection_of_non_empty_set_and_empty_set_is_empty_set(self):
        set1 = CustomSet([1, 2, 3, 4])
        set2 = CustomSet()
        expected = CustomSet()
        self.assertEqual(set1.intersection(set2), expected)

    def test_intersection_of_sets_with_no_shared_elements_is_empty_set(self):
        set1 = CustomSet([1, 2, 3])
        set2 = CustomSet([4, 5, 6])
        expected = CustomSet()
        self.assertEqual(set1.intersection(set2), expected)

    def test_intersection_contains_shared_elements_only(self):
        set1 = CustomSet([1, 2, 3, 4])
        set2 = CustomSet([3, 2, 5])
        expected = CustomSet([2, 3])
        self.assertEqual(set1.intersection(set2), expected)

    def test_difference_of_two_empty_sets_is_empty_set(self):
        set1 = CustomSet()
        set2 = CustomSet()
        expected = CustomSet()
        self.assertEqual(set1 - set2, expected)

    def test_difference_of_empty_set_and_non_empty_set_is_empty_set(self):
        set1 = CustomSet()
        set2 = CustomSet([3, 2, 5])
        expected = CustomSet()
        self.assertEqual(set1 - set2, expected)

    def test_difference_of_non_empty_set_and_empty_set_is_non_empty_set(self):
        set1 = CustomSet([1, 2, 3, 4])
        set2 = CustomSet()
        expected = CustomSet([1, 2, 3, 4])
        self.assertEqual(set1 - set2, expected)

    def test_difference_of_non_empty_sets_elements_in_first_set_only(self):
        set1 = CustomSet([3, 2, 1])
        set2 = CustomSet([2, 4])
        expected = CustomSet([1, 3])
        self.assertEqual(set1 - set2, expected)

    def test_union_of_empty_sets_is_empty_set(self):
        set1 = CustomSet()
        set2 = CustomSet()
        expected = CustomSet()
        self.assertEqual(set1 + set2, expected)

    def test_union_of_empty_set_and_non_empty_set_is_the_non_empty_set(self):
        set1 = CustomSet()
        set2 = CustomSet([2])
        expected = CustomSet([2])
        self.assertEqual(set1 + set2, expected)

    def test_union_of_non_empty_set_and_empty_set_is_the_non_empty_set(self):
        set1 = CustomSet([1, 3])
        set2 = CustomSet()
        expected = CustomSet([1, 3])
        self.assertEqual(set1 + set2, expected)

    def test_union_of_non_empty_sets_contains_all_unique_elements(self):
        set1 = CustomSet([1, 3])
        set2 = CustomSet([2, 3])
        expected = CustomSet([1, 2, 3])
        self.assertEqual(set1 + set2, expected)


if __name__ == '__main__':
    unittest.main()
