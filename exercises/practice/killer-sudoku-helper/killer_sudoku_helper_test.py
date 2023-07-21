# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/killer-sudoku-helper/canonical-data.json
# File last updated on 2023-07-19

import unittest

from killer_sudoku_helper import (
    combinations,
)


class KillerSudokuHelperTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(combinations(1, 1, []), [[1]])

    def test_2(self):
        self.assertEqual(combinations(2, 1, []), [[2]])

    def test_3(self):
        self.assertEqual(combinations(3, 1, []), [[3]])

    def test_4(self):
        self.assertEqual(combinations(4, 1, []), [[4]])

    def test_5(self):
        self.assertEqual(combinations(5, 1, []), [[5]])

    def test_6(self):
        self.assertEqual(combinations(6, 1, []), [[6]])

    def test_7(self):
        self.assertEqual(combinations(7, 1, []), [[7]])

    def test_8(self):
        self.assertEqual(combinations(8, 1, []), [[8]])

    def test_9(self):
        self.assertEqual(combinations(9, 1, []), [[9]])

    def test_cage_with_sum_45_contains_all_digits_1_9(self):
        self.assertEqual(combinations(45, 9, []), [[1, 2, 3, 4, 5, 6, 7, 8, 9]])

    def test_cage_with_only_1_possible_combination(self):
        self.assertEqual(combinations(7, 3, []), [[1, 2, 4]])

    def test_cage_with_several_combinations(self):
        self.assertEqual(combinations(10, 2, []), [[1, 9], [2, 8], [3, 7], [4, 6]])

    def test_cage_with_several_combinations_that_is_restricted(self):
        self.assertEqual(combinations(10, 2, [1, 4]), [[2, 8], [3, 7]])
