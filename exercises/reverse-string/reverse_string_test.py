import unittest

from reverse_string import reverse


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.0.1

class ReverseStringTests(unittest.TestCase):
    def empty_string(self):
            self.assertEqual(reverse(''), '')

    def a_word(self):
            self.assertEqual(reverse('robot'), 'tobor')

    def a_capitalized_word(self):
            self.assertEqual(reverse('Ramen'), 'nemaR')

    def a_sentence_with_punctuation(self):
            self.assertEqual(reverse('I\'m hungry!'), '!yrgnuh m\'I')

    def a_palindrome(self):
            self.assertEqual(reverse('racecar'), 'racecar')


if __name__ == '__main__':
    unittest.main()
