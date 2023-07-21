# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/pythagorean-triplet/canonical-data.json
# File last updated on 2023-07-19

import unittest

from pythagorean_triplet import (
    triplets_with_sum,
)


class PythagoreanTripletTest(unittest.TestCase):
    def test_triplets_whose_sum_is_12(self):
        self.assertCountEqual(triplets_with_sum(12), [[3, 4, 5]])

    def test_triplets_whose_sum_is_108(self):
        self.assertCountEqual(triplets_with_sum(108), [[27, 36, 45]])

    def test_triplets_whose_sum_is_1000(self):
        self.assertCountEqual(triplets_with_sum(1000), [[200, 375, 425]])

    def test_no_matching_triplets_for_1001(self):
        self.assertCountEqual(triplets_with_sum(1001), [])

    def test_returns_all_matching_triplets(self):
        self.assertCountEqual(triplets_with_sum(90), [[9, 40, 41], [15, 36, 39]])

    def test_several_matching_triplets(self):
        self.assertCountEqual(
            triplets_with_sum(840),
            [
                [40, 399, 401],
                [56, 390, 394],
                [105, 360, 375],
                [120, 350, 370],
                [140, 336, 364],
                [168, 315, 357],
                [210, 280, 350],
                [240, 252, 348],
            ],
        )

    def test_triplets_for_large_number(self):
        self.assertCountEqual(
            triplets_with_sum(30000),
            [
                [1200, 14375, 14425],
                [1875, 14000, 14125],
                [5000, 12000, 13000],
                [6000, 11250, 12750],
                [7500, 10000, 12500],
            ],
        )
