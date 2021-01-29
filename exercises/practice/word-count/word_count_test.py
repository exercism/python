import unittest

from word_count import count_words

# Tests adapted from `problem-specifications//canonical-data.json`


class WordCountTest(unittest.TestCase):
    def test_count_one_word(self):
        self.assertEqual(count_words("word"), {"word": 1})

    def test_count_one_of_each_word(self):
        self.assertEqual(count_words("one of each"), {"one": 1, "of": 1, "each": 1})

    def test_multiple_occurrences_of_a_word(self):
        self.assertEqual(
            count_words("one fish two fish red fish blue fish"),
            {"one": 1, "fish": 4, "two": 1, "red": 1, "blue": 1},
        )

    def test_handles_cramped_lists(self):
        self.assertEqual(count_words("one,two,three"), {"one": 1, "two": 1, "three": 1})

    def test_handles_expanded_lists(self):
        self.assertEqual(
            count_words("one,\ntwo,\nthree"), {"one": 1, "two": 1, "three": 1}
        )

    def test_ignore_punctuation(self):
        self.assertEqual(
            count_words("car: carpet as java: javascript!!&@$%^&"),
            {"car": 1, "carpet": 1, "as": 1, "java": 1, "javascript": 1},
        )

    def test_include_numbers(self):
        self.assertEqual(
            count_words("testing, 1, 2 testing"), {"testing": 2, "1": 1, "2": 1}
        )

    def test_normalize_case(self):
        self.assertEqual(count_words("go Go GO Stop stop"), {"go": 3, "stop": 2})

    def test_with_apostrophes(self):
        self.assertEqual(
            count_words("First: don't laugh. Then: don't cry."),
            {"first": 1, "don't": 2, "laugh": 1, "then": 1, "cry": 1},
        )

    def test_with_quotations(self):
        self.assertEqual(
            count_words("Joe can't tell between 'large' and large."),
            {"joe": 1, "can't": 1, "tell": 1, "between": 1, "large": 2, "and": 1},
        )

    def test_substrings_from_the_beginning(self):
        self.assertEqual(
            count_words("Joe can't tell between app, apple and a."),
            {
                "joe": 1,
                "can't": 1,
                "tell": 1,
                "between": 1,
                "app": 1,
                "apple": 1,
                "and": 1,
                "a": 1,
            },
        )

    def test_multiple_spaces_not_detected_as_a_word(self):
        self.assertEqual(
            count_words(" multiple   whitespaces"), {"multiple": 1, "whitespaces": 1}
        )

    def test_alternating_word_separators_not_detected_as_a_word(self):
        self.assertEqual(
            count_words(",\n,one,\n ,two \n 'three'"), {"one": 1, "two": 1, "three": 1}
        )

    # Additional tests for this track

    def test_tabs(self):
        self.assertEqual(
            count_words(
                "rah rah ah ah ah	roma roma ma	ga ga oh la la	want your bad romance"
            ),
            {
                "rah": 2,
                "ah": 3,
                "roma": 2,
                "ma": 1,
                "ga": 2,
                "oh": 1,
                "la": 2,
                "want": 1,
                "your": 1,
                "bad": 1,
                "romance": 1,
            },
        )

    def test_non_alphanumeric(self):
        self.assertEqual(
            count_words("hey,my_spacebar_is_broken"),
            {"hey": 1, "my": 1, "spacebar": 1, "is": 1, "broken": 1},
        )

    def test_multiple_apostrophes_ignored(self):
        self.assertEqual(count_words("''hey''"), {"hey": 1})


if __name__ == "__main__":
    unittest.main()
