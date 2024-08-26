# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/transpose/canonical-data.json
# File last updated on 2024-08-26

import unittest

from transpose import (
    transpose,
)


class TransposeTest(unittest.TestCase):
    def test_empty_string(self):
        lines = ""
        expected = ""

        self.assertEqual(transpose(lines), expected)

    def test_two_characters_in_a_row(self):
        lines = "A1"
        expected = "A\n1"

        self.assertEqual(transpose(lines), expected)

    def test_two_characters_in_a_column(self):
        lines = "A\n1"
        expected = "A1"

        self.assertEqual(transpose(lines), expected)

    def test_simple(self):
        lines = "ABC\n123"
        expected = "A1\nB2\nC3"

        self.assertEqual(transpose(lines), expected)

    def test_single_line(self):
        lines = "Single line."
        expected = "S\ni\nn\ng\nl\ne\n \nl\ni\nn\ne\n."

        self.assertEqual(transpose(lines), expected)

    def test_first_line_longer_than_second_line(self):
        lines = "The fourth line.\nThe fifth line."
        expected = "TT\nhh\nee\n  \nff\noi\nuf\nrt\nth\nh \n l\nli\nin\nne\ne.\n."

        self.assertEqual(transpose(lines), expected)

    def test_second_line_longer_than_first_line(self):
        lines = "The first line.\nThe second line."
        expected = "TT\nhh\nee\n  \nfs\nie\nrc\nso\ntn\n d\nl \nil\nni\nen\n.e\n ."

        self.assertEqual(transpose(lines), expected)

    def test_mixed_line_length(self):
        lines = "The longest line.\nA long line.\nA longer line.\nA line."
        expected = "TAAA\nh   \nelll\n ooi\nlnnn\nogge\nn e.\nglr\nei \nsnl\ntei\n .n\nl e\ni .\nn\ne\n."

        self.assertEqual(transpose(lines), expected)

    def test_square(self):
        lines = "HEART\nEMBER\nABUSE\nRESIN\nTREND"
        expected = "HEART\nEMBER\nABUSE\nRESIN\nTREND"

        self.assertEqual(transpose(lines), expected)

    def test_rectangle(self):
        lines = "FRACTURE\nOUTLINED\nBLOOMING\nSEPTETTE"
        expected = "FOBS\nRULE\nATOP\nCLOT\nTIME\nUNIT\nRENT\nEDGE"

        self.assertEqual(transpose(lines), expected)

    def test_triangle(self):
        lines = "T\nEE\nAAA\nSSSS\nEEEEE\nRRRRRR"
        expected = "TEASER\n EASER\n  ASER\n   SER\n    ER\n     R"

        self.assertEqual(transpose(lines), expected)

    def test_jagged_triangle(self):
        lines = "11\n2\n3333\n444\n555555\n66666"
        expected = "123456\n1 3456\n  3456\n  3 56\n    56\n    5"

        self.assertEqual(transpose(lines), expected)
