# Rhyme found in http://www.pitt.edu/~dash/type2035.html

import unittest

from house import recite


# Tests adapted from `problem-specifications//canonical-data.json` @ v2.2.0

class HouseTest(unittest.TestCase):
    def test_verse_one(self):
        expected = ["This is the house that Jack built."]
        self.assertEqual(recite(1, 1), expected)

    def test_verse_two(self):
        expected = [
            "This is the malt "
            "that lay in the house that Jack built."
        ]
        self.assertEqual(recite(2, 2), expected)

    def test_verse_three(self):
        expected = [
            "This is the rat "
            "that ate the malt "
            "that lay in the house that Jack built."
        ]
        self.assertEqual(recite(3, 3), expected)

    def test_verse_four(self):
        expected = [
            "This is the cat "
            "that killed the rat "
            "that ate the malt "
            "that lay in the house that Jack built."
        ]
        self.assertEqual(recite(4, 4), expected)

    def test_verse_five(self):
        expected = [
            "This is the dog "
            "that worried the cat "
            "that killed the rat "
            "that ate the malt "
            "that lay in the house that Jack built."
        ]
        self.assertEqual(recite(5, 5), expected)

    def test_verse_six(self):
        expected = [
            "This is the cow with the crumpled horn "
            "that tossed the dog "
            "that worried the cat "
            "that killed the rat "
            "that ate the malt "
            "that lay in the house that Jack built."
        ]
        self.assertEqual(recite(6, 6), expected)

    def test_verse_seven(self):
        expected = [
            "This is the maiden all forlorn "
            "that milked the cow with the crumpled horn "
            "that tossed the dog "
            "that worried the cat "
            "that killed the rat "
            "that ate the malt "
            "that lay in the house that Jack built."
        ]
        self.assertEqual(recite(7, 7), expected)

    def test_verse_eight(self):
        expected = [
            "This is the man all tattered and torn "
            "that kissed the maiden all forlorn "
            "that milked the cow with the crumpled horn "
            "that tossed the dog "
            "that worried the cat "
            "that killed the rat "
            "that ate the malt "
            "that lay in the house that Jack built."
        ]
        self.assertEqual(recite(8, 8), expected)

    def test_verse_nine(self):
        expected = [
            "This is the priest all shaven and shorn "
            "that married the man all tattered and torn "
            "that kissed the maiden all forlorn "
            "that milked the cow with the crumpled horn "
            "that tossed the dog "
            "that worried the cat "
            "that killed the rat "
            "that ate the malt "
            "that lay in the house that Jack built."
        ]
        self.assertEqual(recite(9, 9), expected)

    def test_verse_10(self):
        expected = [
            "This is the rooster that crowed in the morn "
            "that woke the priest all shaven and shorn "
            "that married the man all tattered and torn "
            "that kissed the maiden all forlorn "
            "that milked the cow with the crumpled horn "
            "that tossed the dog "
            "that worried the cat "
            "that killed the rat "
            "that ate the malt "
            "that lay in the house that Jack built."
        ]
        self.assertEqual(recite(10, 10), expected)

    def test_verse_11(self):
        expected = [
            "This is the farmer sowing his corn "
            "that kept the rooster that crowed in the morn "
            "that woke the priest all shaven and shorn "
            "that married the man all tattered and torn "
            "that kissed the maiden all forlorn "
            "that milked the cow with the crumpled horn "
            "that tossed the dog "
            "that worried the cat "
            "that killed the rat "
            "that ate the malt "
            "that lay in the house that Jack built."
        ]
        self.assertEqual(recite(11, 11), expected)

    def test_verse_12(self):
        expected = [
            "This is the horse and the hound and the horn "
            "that belonged to the farmer sowing his corn "
            "that kept the rooster that crowed in the morn "
            "that woke the priest all shaven and shorn "
            "that married the man all tattered and torn "
            "that kissed the maiden all forlorn "
            "that milked the cow with the crumpled horn "
            "that tossed the dog "
            "that worried the cat "
            "that killed the rat "
            "that ate the malt "
            "that lay in the house that Jack built."
        ]
        self.assertEqual(recite(12, 12), expected)

    def test_multiple_verses(self):
        expected = [recite(i, i)[0] for i in range(4, 9)]
        self.assertEqual(recite(4, 8), expected)

    def test_full_rhyme(self):
        expected = [recite(i, i)[0] for i in range(1, 13)]
        self.assertEqual(recite(1, 12), expected)


if __name__ == '__main__':
    unittest.main()
