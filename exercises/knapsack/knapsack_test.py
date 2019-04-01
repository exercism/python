import unittest

from knapsack import solve_knapsack


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.0.0

class ChangeTest(unittest.TestCase):
    def test_no_items(self):
        self.assertEqual(solve_knapsack(100, []), 0)
    def test_one_item_too_heavy(self):
        self.assertEqual(solve_knapsack(10, [(100, 1)]), 0)
    def test_cannot_be_greedy_by_weight(self):
        self.assertEqual(solve_knapsack(10,
                                        [(2, 5),
                                         (2, 5),
                                         (2, 5),
                                         (2, 5),
                                         (10, 21)]), 21)
    def test_cannot_be_greedy_by_value(self):
        self.assertEqual(solve_knapsack(10, [(2, 20),
                                             (2, 20),
                                             (2, 20),
                                             (2, 20),
                                             (10, 50)]), 80)
    def test_example_knapsack(self):
        self.assertEqual(solve_knapsack(10, [(5, 10),
                                             (4, 40),
                                             (6, 30),
                                             (4, 50)]), 90)
    def test_eight_items(self):
        self.assertEqual(solve_knapsack(104, [(25, 350),
                                              (35, 400),
                                              (45, 450),
                                              (5, 20),
                                              (25, 70),
                                              (3, 8),
                                              (2, 5),
                                              (2, 5)]), 900)
    def test_fifteen_items(self):
        self.assertEqual(solve_knapsack(104, [(70, 135),
                                              (73, 139),
                                              (77, 149),
                                              (80, 150),
                                              (82, 156),
                                              (87, 163),
                                              (90, 173),
                                              (94, 184),
                                              (98, 192),
                                              (106, 201),
                                              (110, 210),
                                              (113, 214),
                                              (115, 221),
                                              (118, 229),
                                              (120, 240)]), 1458)
