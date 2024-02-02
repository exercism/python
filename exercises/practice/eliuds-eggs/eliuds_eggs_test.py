# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/eliuds-eggs/canonical-data.json
# File last updated on 2024-02-02

import unittest

from eliuds_eggs import (
    egg_count,
)


class EliudsEggsTest(unittest.TestCase):
    def test_0_eggs(self):
        expected = 0
        self.assertEqual(egg_count(0), expected)

    def test_1_egg(self):
        expected = 1
        self.assertEqual(egg_count(16), expected)

    def test_4_eggs(self):
        expected = 4
        self.assertEqual(egg_count(89), expected)

    def test_13_eggs(self):
        expected = 13
        self.assertEqual(egg_count(2000000000), expected)
