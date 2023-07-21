# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/two-fer/canonical-data.json
# File last updated on 2023-07-19

import unittest

from two_fer import (
    two_fer,
)


class TwoFerTest(unittest.TestCase):
    def test_no_name_given(self):
        self.assertEqual(two_fer(), "One for you, one for me.")

    def test_a_name_given(self):
        self.assertEqual(two_fer("Alice"), "One for Alice, one for me.")

    def test_another_name_given(self):
        self.assertEqual(two_fer("Bob"), "One for Bob, one for me.")
