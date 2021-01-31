import unittest

from custom_set import (
    CustomSet,
)

# Tests adapted from `problem-specifications//canonical-data.json`


class CustomSetTest(unittest.TestCase):
    def test_sets_with_no_elements_are_empty(self):
        sut = CustomSet()
        self.assertIs(sut.isempty(), True)

    def test_sets_with_elements_are_not_empty(self):
        sut = CustomSet([1])
        self.assertIs(sut.isempty(), False)

    def test_nothing_is_contained_in_an_empty_set(self):
        sut = CustomSet()
        self.assertNotIn(1, sut)

    def test_when_the_element_is_in_the_set(self):
        sut = CustomSet([1, 2, 3])
        self.assertIn(1, sut)

    def test_when_the_element_is_not_in_the_set(self):
        sut = CustomSet([1, 2, 3])
        self.assertNotIn(4, sut)

    def test_empty_set_is_a_subset_of_another_empty_set(self):
        set1 = CustomSet()
        set2 = CustomSet()
        self.assertIs(set1.issubset(set2), True)

    def test_empty_set_is_a_subset_of_non_empty_set(self):
        set1 = CustomSet()
        set2 = CustomSet([1])
        self.assertIs(set1.issubset(set2), True)

    def test_non_empty_set_is_not_a_subset_of_empty_set(self):
        set1 = CustomSet([1])
        set2 = CustomSet()
        self.assertIs(set1.issubset(set2), False)

    def test_set_is_a_subset_of_set_with_exact_same_elements(self):
        set1 = CustomSet([1, 2, 3])
        set2 = CustomSet([1, 2, 3])
        self.assertIs(set1.issubset(set2), True)

    def test_set_is_a_subset_of_larger_set_with_same_elements(self):
        set1 = CustomSet([1, 2, 3])
        set2 = CustomSet([4, 1, 2, 3])
        self.assertIs(set1.issubset(set2), True)

    def test_set_is_not_a_subset_of_set_that_does_not_contain_its_elements(self):
        set1 = CustomSet([1, 2, 3])
        set2 = CustomSet([4, 1, 3])
        self.assertIs(set1.issubset(set2), False)

    def test_the_empty_set_is_disjoint_with_itself(self):
        set1 = CustomSet()
        set2 = CustomSet()
        self.assertIs(set1.isdisjoint(set2), True)

    def test_empty_set_is_disjoint_with_non_empty_set(self):
        set1 = CustomSet()
        set2 = CustomSet([1])
        self.assertIs(set1.isdisjoint(set2), True)

    def test_non_empty_set_is_disjoint_with_empty_set(self):
        set1 = CustomSet([1])
        set2 = CustomSet()
        self.assertIs(set1.isdisjoint(set2), True)

    def test_sets_are_not_disjoint_if_they_share_an_element(self):
        set1 = CustomSet([1, 2])
        set2 = CustomSet([2, 3])
        self.assertIs(set1.isdisjoint(set2), False)

    def test_sets_are_disjoint_if_they_share_no_elements(self):
        set1 = CustomSet([1, 2])
        set2 = CustomSet([3, 4])
        self.assertIs(set1.isdisjoint(set2), True)

    def test_empty_sets_are_equal(self):
        set1 = CustomSet()
        set2 = CustomSet()
        self.assertEqual(set1, set2)

    def test_empty_set_is_not_equal_to_non_empty_set(self):
        set1 = CustomSet()
        set2 = CustomSet([1, 2, 3])
        self.assertNotEqual(set1, set2)

    def test_non_empty_set_is_not_equal_to_empty_set(self):
        set1 = CustomSet([1, 2, 3])
        set2 = CustomSet()
        self.assertNotEqual(set1, set2)

    def test_sets_with_the_same_elements_are_equal(self):
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
        expected = CustomSet([3])
        sut.add(3)
        self.assertEqual(sut, expected)

    def test_add_to_non_empty_set(self):
        sut = CustomSet([1, 2, 4])
        expected = CustomSet([1, 2, 3, 4])
        sut.add(3)
        self.assertEqual(sut, expected)

    def test_adding_an_existing_element_does_not_change_the_set(self):
        sut = CustomSet([1, 2, 3])
        expected = CustomSet([1, 2, 3])
        sut.add(3)
        self.assertEqual(sut, expected)

    def test_intersection_of_two_empty_sets_is_an_empty_set(self):
        set1 = CustomSet()
        set2 = CustomSet()
        expected = CustomSet()
        self.assertEqual(set1.intersection(set2), expected)

    def test_intersection_of_an_empty_set_and_non_empty_set_is_an_empty_set(self):
        set1 = CustomSet()
        set2 = CustomSet([3, 2, 5])
        expected = CustomSet()
        self.assertEqual(set1.intersection(set2), expected)

    def test_intersection_of_a_non_empty_set_and_an_empty_set_is_an_empty_set(self):
        set1 = CustomSet([1, 2, 3, 4])
        set2 = CustomSet()
        expected = CustomSet()
        self.assertEqual(set1.intersection(set2), expected)

    def test_intersection_of_two_sets_with_no_shared_elements_is_an_empty_set(self):
        set1 = CustomSet([1, 2, 3])
        set2 = CustomSet([4, 5, 6])
        expected = CustomSet()
        self.assertEqual(set1.intersection(set2), expected)

    def test_intersection_of_two_sets_with_shared_elements_is_a_set_of_the_shared_elements(
        self,
    ):
        set1 = CustomSet([1, 2, 3, 4])
        set2 = CustomSet([3, 2, 5])
        expected = CustomSet([2, 3])
        self.assertEqual(set1.intersection(set2), expected)

    def test_difference_of_two_empty_sets_is_an_empty_set(self):
        set1 = CustomSet()
        set2 = CustomSet()
        expected = CustomSet()
        self.assertEqual(set1 - set2, expected)

    def test_difference_of_empty_set_and_non_empty_set_is_an_empty_set(self):
        set1 = CustomSet()
        set2 = CustomSet([3, 2, 5])
        expected = CustomSet()
        self.assertEqual(set1 - set2, expected)

    def test_difference_of_a_non_empty_set_and_an_empty_set_is_the_non_empty_set(self):
        set1 = CustomSet([1, 2, 3, 4])
        set2 = CustomSet()
        expected = CustomSet([1, 2, 3, 4])
        self.assertEqual(set1 - set2, expected)

    def test_difference_of_two_non_empty_sets_is_a_set_of_elements_that_are_only_in_the_first_set(
        self,
    ):
        set1 = CustomSet([3, 2, 1])
        set2 = CustomSet([2, 4])
        expected = CustomSet([1, 3])
        self.assertEqual(set1 - set2, expected)

    def test_union_of_empty_sets_is_an_empty_set(self):
        set1 = CustomSet()
        set2 = CustomSet()
        expected = CustomSet()
        self.assertEqual(set1 + set2, expected)

    def test_union_of_an_empty_set_and_non_empty_set_is_the_non_empty_set(self):
        set1 = CustomSet()
        set2 = CustomSet([2])
        expected = CustomSet([2])
        self.assertEqual(set1 + set2, expected)

    def test_union_of_a_non_empty_set_and_empty_set_is_the_non_empty_set(self):
        set1 = CustomSet([1, 3])
        set2 = CustomSet()
        expected = CustomSet([1, 3])
        self.assertEqual(set1 + set2, expected)

    def test_union_of_non_empty_sets_contains_all_unique_elements(self):
        set1 = CustomSet([1, 3])
        set2 = CustomSet([2, 3])
        expected = CustomSet([3, 2, 1])
        self.assertEqual(set1 + set2, expected)


if __name__ == "__main__":
    unittest.main()
