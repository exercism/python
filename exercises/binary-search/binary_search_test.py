import unittest

from binary_search import find

# Tests adapted from `problem-specifications//canonical-data.json`


class BinarySearchTest(unittest.TestCase):
    def test_finds_a_value_in_an_array_with_one_element(self):
        self.assertEqual(find([6], 6), 0)

    def test_finds_a_value_in_the_middle_of_an_array(self):
        self.assertEqual(find([1, 3, 4, 6, 8, 9, 11], 6), 3)

    def test_finds_a_value_at_the_beginning_of_an_array(self):
        self.assertEqual(find([1, 3, 4, 6, 8, 9, 11], 1), 0)

    def test_finds_a_value_at_the_end_of_an_array(self):
        self.assertEqual(find([1, 3, 4, 6, 8, 9, 11], 11), 6)

    def test_finds_a_value_in_an_array_of_odd_length(self):
        self.assertEqual(
            find([1, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 634], 144), 9
        )

    def test_finds_a_value_in_an_array_of_even_length(self):
        self.assertEqual(find([1, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377], 21), 5)

    def test_identifies_that_a_value_is_not_included_in_the_array(self):
        with self.assertRaisesWithMessage(ValueError):
            find([1, 3, 4, 6, 8, 9, 11], 7)

    def test_a_value_smaller_than_the_array_s_smallest_value_is_not_found(self):
        with self.assertRaisesWithMessage(ValueError):
            find([1, 3, 4, 6, 8, 9, 11], 0)

    def test_a_value_larger_than_the_array_s_largest_value_is_not_found(self):
        with self.assertRaisesWithMessage(ValueError):
            find([1, 3, 4, 6, 8, 9, 11], 13)

    def test_nothing_is_found_in_an_empty_array(self):
        with self.assertRaisesWithMessage(ValueError):
            find([], 1)

    def test_nothing_is_found_when_the_left_and_right_bounds_cross(self):
        with self.assertRaisesWithMessage(ValueError):
            find([1, 2], 0)

    # Utility functions
    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")


if __name__ == "__main__":
    unittest.main()
