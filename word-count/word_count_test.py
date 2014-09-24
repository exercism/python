import unittest

from wordcount import word_count


class WordCountTests(unittest.TestCase):
    def test_count_one_word(self):
        self.assertEqual(
            {'word': 1},
            word_count('word')
        )

    def test_count_one_of_each(self):
        self.assertEqual(
            {'one': 1, 'of': 1, 'each': 1},
            word_count('one of each')
        )

    def test_count_multiple_occurences(self):
        self.assertEqual(
            {'one': 1, 'fish': 4, 'two': 1, 'red': 1, 'blue': 1},
            word_count('one fish two fish red fish blue fish')
        )

    def test_preserves_punctuation(self):
        self.assertEqual(
            {'car': 1, 'carpet': 1, 'as': 1, 'java': 1, ':': 2, 'javascript!!&@$%^&': 1},
            word_count('car : carpet as java : javascript!!&@$%^&')
        )

    def test_include_numbers(self):
        self.assertEqual(
            {'testing': 2, '1': 1, '2': 1},
            word_count('testing 1 2 testing')
        )

    def test_mixed_case(self):
        self.assertEqual(
            {'go': 1, 'Go': 1, 'GO': 1},
            word_count('go Go GO')
        )
        
    def test_multiple_spaces(self):
      self.assertEqual(
          {'wait': 1, 'for': 1, 'it': 1},
          word_count('wait for       it')
      )
        
    def test_newlines(self):
        self.assertEqual(
            {'rah': 2, 'ah': 3, 'roma': 2, 'ma': 1, 'ga': 2, 'oh': 1, 'la': 2, 
            'want': 1, 'your': 1, 'bad': 1, 'romance': 1},
            word_count('rah rah ah ah ah\nroma roma ma\nga ga oh la la\nwant your bad romance')
        )

if __name__ == '__main__':
    unittest.main()
