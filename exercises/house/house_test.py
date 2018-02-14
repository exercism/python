# Rhyme found in http://www.pitt.edu/~dash/type2035.html

import unittest

from house import verse


# Tests adapted from `problem-specifications//canonical-data.json` @ v2.1.0

class VerseTest(unittest.TestCase):
    def test_verse_one(self):
        expected = 'This is the house that Jack built.'
        self.assertEqual(verse(1, 1), expected)

    def test_verse_two(self):
        expected = 'This is the malt\n'\
                   'that lay in the house that Jack built.'
        self.assertEqual(verse(2, 2), expected)

    def test_verse_three(self):
        expected = 'This is the rat\n'\
                   'that ate the malt\n'\
                   'that lay in the house that Jack built.'
        self.assertEqual(verse(3, 3), expected)

    def test_verse_four(self):
        expected = 'This is the cat\n'\
                   'that killed the rat\n'\
                   'that ate the malt\n'\
                   'that lay in the house that Jack built.'
        self.assertEqual(verse(4, 4), expected)

    def test_verse_five(self):
        expected = 'This is the dog\n'\
                   'that worried the cat\n'\
                   'that killed the rat\n'\
                   'that ate the malt\n'\
                   'that lay in the house that Jack built.'
        self.assertEqual(verse(5, 5), expected)

    def test_verse_six(self):
        expected = 'This is the cow with the crumpled horn\n'\
                   'that tossed the dog\n'\
                   'that worried the cat\n'\
                   'that killed the rat\n'\
                   'that ate the malt\n'\
                   'that lay in the house that Jack built.'
        self.assertEqual(verse(6, 6), expected)

    def test_verse_seven(self):
        expected = 'This is the maiden all forlorn\n'\
                   'that milked the cow with the crumpled horn\n'\
                   'that tossed the dog\n'\
                   'that worried the cat\n'\
                   'that killed the rat\n'\
                   'that ate the malt\n'\
                   'that lay in the house that Jack built.'
        self.assertEqual(verse(7, 7), expected)

    def test_verse_eight(self):
        expected = 'This is the man all tattered and torn\n'\
                   'that kissed the maiden all forlorn\n'\
                   'that milked the cow with the crumpled horn\n'\
                   'that tossed the dog\n'\
                   'that worried the cat\n'\
                   'that killed the rat\n'\
                   'that ate the malt\n'\
                   'that lay in the house that Jack built.'
        self.assertEqual(verse(8, 8), expected)

    def test_verse_nine(self):
        expected = 'This is the priest all shaven and shorn\n'\
                   'that married the man all tattered and torn\n'\
                   'that kissed the maiden all forlorn\n'\
                   'that milked the cow with the crumpled horn\n'\
                   'that tossed the dog\n'\
                   'that worried the cat\n'\
                   'that killed the rat\n'\
                   'that ate the malt\n'\
                   'that lay in the house that Jack built.'
        self.assertEqual(verse(9, 9), expected)

    def test_verse_10(self):
        expected = 'This is the rooster that crowed in the morn\n'\
                   'that woke the priest all shaven and shorn\n'\
                   'that married the man all tattered and torn\n'\
                   'that kissed the maiden all forlorn\n'\
                   'that milked the cow with the crumpled horn\n'\
                   'that tossed the dog\n'\
                   'that worried the cat\n'\
                   'that killed the rat\n'\
                   'that ate the malt\n'\
                   'that lay in the house that Jack built.'
        self.assertEqual(verse(10, 10), expected)

    def test_verse_11(self):
        expected = 'This is the farmer sowing his corn\n'\
                   'that kept the rooster that crowed in the morn\n'\
                   'that woke the priest all shaven and shorn\n'\
                   'that married the man all tattered and torn\n'\
                   'that kissed the maiden all forlorn\n'\
                   'that milked the cow with the crumpled horn\n'\
                   'that tossed the dog\n'\
                   'that worried the cat\n'\
                   'that killed the rat\n'\
                   'that ate the malt\n'\
                   'that lay in the house that Jack built.'
        self.assertEqual(verse(11, 11), expected)

    def test_verse_12(self):
        expected = 'This is the horse and the hound and the horn\n'\
                   'that belonged to the farmer sowing his corn\n'\
                   'that kept the rooster that crowed in the morn\n'\
                   'that woke the priest all shaven and shorn\n'\
                   'that married the man all tattered and torn\n'\
                   'that kissed the maiden all forlorn\n'\
                   'that milked the cow with the crumpled horn\n'\
                   'that tossed the dog\n'\
                   'that worried the cat\n'\
                   'that killed the rat\n'\
                   'that ate the malt\n'\
                   'that lay in the house that Jack built.'
        self.assertEqual(verse(12, 12), expected)

    def test_multiple_verses(self):
        expected = 'This is the cat\n'\
                   'that killed the rat\n'\
                   'that ate the malt\n'\
                   'that lay in the house that Jack built.\n\n'\
                   'This is the dog\n'\
                   'that worried the cat\n'\
                   'that killed the rat\n'\
                   'that ate the malt\n'\
                   'that lay in the house that Jack built.\n\n'\
                   'This is the cow with the crumpled horn\n'\
                   'that tossed the dog\n'\
                   'that worried the cat\n'\
                   'that killed the rat\n'\
                   'that ate the malt\n'\
                   'that lay in the house that Jack built.\n\n'\
                   'This is the maiden all forlorn\n'\
                   'that milked the cow with the crumpled horn\n'\
                   'that tossed the dog\n'\
                   'that worried the cat\n'\
                   'that killed the rat\n'\
                   'that ate the malt\n'\
                   'that lay in the house that Jack built.\n\n'\
                   'This is the man all tattered and torn\n'\
                   'that kissed the maiden all forlorn\n'\
                   'that milked the cow with the crumpled horn\n'\
                   'that tossed the dog\n'\
                   'that worried the cat\n'\
                   'that killed the rat\n'\
                   'that ate the malt\n'\
                   'that lay in the house that Jack built.'
        self.assertEqual(verse(4, 8), expected)

    def test_full_rhyme(self):
        expected = 'This is the house that Jack built.\n\n'\
                   'This is the malt\n'\
                   'that lay in the house that Jack built.\n\n'\
                   'This is the rat\n'\
                   'that ate the malt\n'\
                   'that lay in the house that Jack built.\n\n'\
                   'This is the cat\n'\
                   'that killed the rat\n'\
                   'that ate the malt\n'\
                   'that lay in the house that Jack built.\n\n'\
                   'This is the dog\n'\
                   'that worried the cat\n'\
                   'that killed the rat\n'\
                   'that ate the malt\n'\
                   'that lay in the house that Jack built.\n\n'\
                   'This is the cow with the crumpled horn\n'\
                   'that tossed the dog\n'\
                   'that worried the cat\n'\
                   'that killed the rat\n'\
                   'that ate the malt\n'\
                   'that lay in the house that Jack built.\n\n'\
                   'This is the maiden all forlorn\n'\
                   'that milked the cow with the crumpled horn\n'\
                   'that tossed the dog\n'\
                   'that worried the cat\n'\
                   'that killed the rat\n'\
                   'that ate the malt\n'\
                   'that lay in the house that Jack built.\n\n'\
                   'This is the man all tattered and torn\n'\
                   'that kissed the maiden all forlorn\n'\
                   'that milked the cow with the crumpled horn\n'\
                   'that tossed the dog\n'\
                   'that worried the cat\n'\
                   'that killed the rat\n'\
                   'that ate the malt\n'\
                   'that lay in the house that Jack built.\n\n'\
                   'This is the priest all shaven and shorn\n'\
                   'that married the man all tattered and torn\n'\
                   'that kissed the maiden all forlorn\n'\
                   'that milked the cow with the crumpled horn\n'\
                   'that tossed the dog\n'\
                   'that worried the cat\n'\
                   'that killed the rat\n'\
                   'that ate the malt\n'\
                   'that lay in the house that Jack built.\n\n'\
                   'This is the rooster that crowed in the morn\n'\
                   'that woke the priest all shaven and shorn\n'\
                   'that married the man all tattered and torn\n'\
                   'that kissed the maiden all forlorn\n'\
                   'that milked the cow with the crumpled horn\n'\
                   'that tossed the dog\n'\
                   'that worried the cat\n'\
                   'that killed the rat\n'\
                   'that ate the malt\n'\
                   'that lay in the house that Jack built.\n\n'\
                   'This is the farmer sowing his corn\n'\
                   'that kept the rooster that crowed in the morn\n'\
                   'that woke the priest all shaven and shorn\n'\
                   'that married the man all tattered and torn\n'\
                   'that kissed the maiden all forlorn\n'\
                   'that milked the cow with the crumpled horn\n'\
                   'that tossed the dog\n'\
                   'that worried the cat\n'\
                   'that killed the rat\n'\
                   'that ate the malt\n'\
                   'that lay in the house that Jack built.\n\n'\
                   'This is the horse and the hound and the horn\n'\
                   'that belonged to the farmer sowing his corn\n'\
                   'that kept the rooster that crowed in the morn\n'\
                   'that woke the priest all shaven and shorn\n'\
                   'that married the man all tattered and torn\n'\
                   'that kissed the maiden all forlorn\n'\
                   'that milked the cow with the crumpled horn\n'\
                   'that tossed the dog\n'\
                   'that worried the cat\n'\
                   'that killed the rat\n'\
                   'that ate the malt\n'\
                   'that lay in the house that Jack built.'
        self.assertEqual(verse(1, 12), expected)


if __name__ == '__main__':
    unittest.main()
