# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/zebra-puzzle/canonical-data.json
# File last updated on 2023-07-19

import unittest

from zebra_puzzle import (
    drinks_water,
    owns_zebra,
)


class ZebraPuzzleTest(unittest.TestCase):
    def test_resident_who_drinks_water(self):
        self.assertEqual(drinks_water(), "Norwegian")

    def test_resident_who_owns_zebra(self):
        self.assertEqual(owns_zebra(), "Japanese")
