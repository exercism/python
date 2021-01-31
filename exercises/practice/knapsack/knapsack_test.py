import unittest

from knapsack import (
    maximum_value,
)

# Tests adapted from `problem-specifications//canonical-data.json`


class KnapsackTest(unittest.TestCase):
    def test_no_items(self):
        self.assertEqual(maximum_value(100, []), 0)

    def test_one_item_too_heavy(self):
        self.assertEqual(maximum_value(10, [{"weight": 100, "value": 1}]), 0)

    def test_five_items_cannot_be_greedy_by_weight(self):
        self.assertEqual(
            maximum_value(
                10,
                [
                    {"weight": 2, "value": 5},
                    {"weight": 2, "value": 5},
                    {"weight": 2, "value": 5},
                    {"weight": 2, "value": 5},
                    {"weight": 10, "value": 21},
                ],
            ),
            21,
        )

    def test_five_items_cannot_be_greedy_by_value(self):
        self.assertEqual(
            maximum_value(
                10,
                [
                    {"weight": 2, "value": 20},
                    {"weight": 2, "value": 20},
                    {"weight": 2, "value": 20},
                    {"weight": 2, "value": 20},
                    {"weight": 10, "value": 50},
                ],
            ),
            80,
        )

    def test_example_knapsack(self):
        self.assertEqual(
            maximum_value(
                10,
                [
                    {"weight": 5, "value": 10},
                    {"weight": 4, "value": 40},
                    {"weight": 6, "value": 30},
                    {"weight": 4, "value": 50},
                ],
            ),
            90,
        )

    def test_8_items(self):
        self.assertEqual(
            maximum_value(
                104,
                [
                    {"weight": 25, "value": 350},
                    {"weight": 35, "value": 400},
                    {"weight": 45, "value": 450},
                    {"weight": 5, "value": 20},
                    {"weight": 25, "value": 70},
                    {"weight": 3, "value": 8},
                    {"weight": 2, "value": 5},
                    {"weight": 2, "value": 5},
                ],
            ),
            900,
        )

    def test_15_items(self):
        self.assertEqual(
            maximum_value(
                750,
                [
                    {"weight": 70, "value": 135},
                    {"weight": 73, "value": 139},
                    {"weight": 77, "value": 149},
                    {"weight": 80, "value": 150},
                    {"weight": 82, "value": 156},
                    {"weight": 87, "value": 163},
                    {"weight": 90, "value": 173},
                    {"weight": 94, "value": 184},
                    {"weight": 98, "value": 192},
                    {"weight": 106, "value": 201},
                    {"weight": 110, "value": 210},
                    {"weight": 113, "value": 214},
                    {"weight": 115, "value": 221},
                    {"weight": 118, "value": 229},
                    {"weight": 120, "value": 240},
                ],
            ),
            1458,
        )


if __name__ == "__main__":
    unittest.main()
