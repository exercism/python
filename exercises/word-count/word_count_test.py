# -*- coding: utf-8 -*-
import unittest

from word_count import word_count


class WordCountTests(unittest.TestCase):

    def test_count_one_word(self):
        self.assertEqual(
            {'word': 1},
            word_count('word')
        )

    @unittest.skip("remove this line to run this test")
    def test_count_one_of_each(self):
        self.assertEqual(
            {'one': 1, 'of': 1, 'each': 1},
            word_count('one of each')
        )

    @unittest.skip("remove this line to run this test")
    def test_count_multiple_occurences(self):
        self.assertEqual(
            {'one': 1, 'fish': 4, 'two': 1, 'red': 1, 'blue': 1},
            word_count('one fish two fish red fish blue fish')
        )

    @unittest.skip("remove this line to run this test")
    def test_handles_cramped_lists(self):
        self.assertEqual(
            {'one': 1, 'two': 1, 'three': 1},
            word_count('one,two,three')
        )

    @unittest.skip("remove this line to run this test")
    def test_handles_expanded_lists(self):
        self.assertEqual(
            {'one': 1, 'two': 1, 'three': 1},
            word_count('one,\ntwo,\nthree')
        )

    @unittest.skip("remove this line to run this test")
    def test_ignore_punctuation(self):
        self.assertEqual(
            {'car': 1, 'carpet': 1, 'as': 1, 'java': 1, 'javascript': 1},
            word_count('car : carpet as java : javascript!!&@$%^&')
        )

    @unittest.skip("remove this line to run this test")
    def test_include_numbers(self):
        self.assertEqual(
            {'testing': 2, '1': 1, '2': 1},
            word_count('testing 1 2 testing')
        )

    @unittest.skip("remove this line to run this test")
    def test_normalize_case(self):
        self.assertEqual(
            [2, 3],
            sorted(list(word_count('go Go GO Stop stop').values()))
        )

    @unittest.skip("remove this line to run this test")
    def test_with_apostrophes(self):
        self.assertEqual(
            {
                "first": 1,
                "don't": 2,
                "laugh": 1,
                "then": 1,
                "cry": 1
            },
            word_count("First: don't laugh. Then: don't cry.")
        )

    @unittest.skip("remove this line to run this test")
    def test_with_quotations(self):
        self.assertEqual(
            {
                "joe": 1,
                "can't": 1,
                "tell": 1,
                "between": 1,
                "large": 2,
                "and": 1
            },
            word_count("Joe can't tell between 'large' and large.")
        )


if __name__ == '__main__':
    unittest.main()
