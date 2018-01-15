import unittest

from word_count import word_count


class WordCountTests(unittest.TestCase):

    def test_count_one_word(self):
        self.assertEqual(
            word_count('word'),
            {'word': 1}
        )

    def test_count_one_of_each(self):
        self.assertEqual(
            word_count('one of each'),
            {'one': 1, 'of': 1, 'each': 1}
        )

    def test_count_multiple_occurences(self):
        self.assertEqual(
            word_count('one fish two fish red fish blue fish'),
            {'one': 1, 'fish': 4, 'two': 1, 'red': 1, 'blue': 1}
        )

    def test_cramped_list(self):
        self.assertEqual(
            word_count('one,two,three'),
            {'one': 1, 'two': 1, 'three': 1}
        )

    def test_expanded_list(self):
        self.assertEqual(
            word_count('one,\ntwo,\nthree'),
            {'one': 1, 'two': 1, 'three': 1}
        )

    def test_ignores_punctuation(self):
        self.assertEqual(
            word_count('car : carpet as java : javascript!!&@$%^&'),
            {'car': 1, 'carpet': 1, 'as': 1, 'java': 1, 'javascript': 1}
        )

    def test_include_numbers(self):
        self.assertEqual(
            word_count('testing 1 2 testing'),
            {'testing': 2, '1': 1, '2': 1}
        )

    def test_mixed_case(self):
        self.assertEqual(
            word_count('go Go GO Stop stop'),
            {'go': 3, 'stop': 2}
        )

    def test_apostrophes(self):
        self.assertEqual(
            word_count("First: don't laugh. Then: don't cry."),
            {'first': 1, "don't": 2, 'laugh': 1, 'then': 1, 'cry': 1}
        )

    def test_quotations(self):
        self.assertEqual(
            word_count("Joe can't tell between 'large' and large."),
            {'joe': 1, "can't": 1, 'tell': 1, 'between': 1, 'large': 2,
             'and': 1}
        )

    # Additional tests for this track

    def test_multiple_spaces(self):
        self.assertEqual(
            word_count('wait for       it'),
            {'wait': 1, 'for': 1, 'it': 1}
        )

    def test_newlines(self):
        self.assertEqual(
            word_count('rah rah ah ah ah\nroma roma ma\n'
                       'ga ga oh la la\nwant your bad romance'),
            {'rah': 2, 'ah': 3, 'roma': 2, 'ma': 1, 'ga': 2, 'oh': 1, 'la': 2,
             'want': 1, 'your': 1, 'bad': 1, 'romance': 1}
        )

    def test_tabs(self):
        self.assertEqual(
            word_count('rah rah ah ah ah\troma roma ma\tga ga oh la la\t'
                       'want your bad romance'),
            {'rah': 2, 'ah': 3, 'roma': 2, 'ma': 1, 'ga': 2, 'oh': 1, 'la': 2,
             'want': 1, 'your': 1, 'bad': 1, 'romance': 1}
        )

    def test_non_alphanumeric(self):
        self.assertEqual(
            word_count('hey,my_spacebar_is_broken.'),
            {'hey': 1, 'my': 1, 'spacebar': 1, 'is': 1, 'broken': 1}
        )


if __name__ == '__main__':
    unittest.main()
