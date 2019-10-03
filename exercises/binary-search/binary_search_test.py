import unittest

from binary_search import find

# Tests adapted from `problem-specifications//canonical-data.json` @ v1.3.0


class BinarySearchTest(unittest.TestCase):
    def test_finds_a_value_in_an_array_with_one_element(self):
        input_array = [6]
        input_search_value = 6
        expected = 0
        self.assertEqual(find(input_array, input_search_value), expected)

    def test_finds_a_value_in_the_middle_of_an_array(self):
        input_array = [1, 3, 4, 6, 8, 9, 11]
        input_search_value = 6
        expected = 3
        self.assertEqual(find(input_array, input_search_value), expected)

    def test_finds_a_value_at_the_beginning_of_an_array(self):
        input_array = [1, 3, 4, 6, 8, 9, 11]
        input_search_value = 1
        expected = 0
        self.assertEqual(find(input_array, input_search_value), expected)

    def test_finds_a_value_at_the_end_of_an_array(self):
        input_array = [1, 3, 4, 6, 8, 9, 11]
        input_search_value = 11
        expected = 6
        self.assertEqual(find(input_array, input_search_value), expected)

    def test_finds_a_value_in_an_array_of_odd_length(self):
        input_array = [1, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 634]
        input_search_value = 144
        expected = 9
        self.assertEqual(find(input_array, input_search_value), expected)

    def test_finds_a_value_in_an_array_of_even_length(self):
        input_array = [1, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
        input_search_value = 21
        expected = 5
        self.assertEqual(find(input_array, input_search_value), expected)

    def test_identifies_that_a_value_is_not_included_in_the_array(self):
        input_array = [1, 3, 4, 6, 8, 9, 11]
        input_search_value = 7
        expected = {"error": "value not in array"}
        self.assertEqual(find(input_array, input_search_value), expected)

    def test_a_value_smaller_than_the_array_s_smallest_value_is_not_found(self):
        input_array = [1, 3, 4, 6, 8, 9, 11]
        input_search_value = 0
        expected = {"error": "value not in array"}
        self.assertEqual(find(input_array, input_search_value), expected)

    def test_a_value_larger_than_the_array_s_largest_value_is_not_found(self):
        input_array = [1, 3, 4, 6, 8, 9, 11]
        input_search_value = 13
        expected = {"error": "value not in array"}
        self.assertEqual(find(input_array, input_search_value), expected)

    def test_nothing_is_found_in_an_empty_array(self):
        input_array = []
        input_search_value = 1
        expected = {"error": "value not in array"}
        self.assertEqual(find(input_array, input_search_value), expected)

    def test_nothing_is_found_when_the_left_and_right_bounds_cross(self):
        input_array = [1, 2]
        input_search_value = 0
        expected = {"error": "value not in array"}
        self.assertEqual(find(input_array, input_search_value), expected)


if __name__ == "__main__":
    unittest.main()
