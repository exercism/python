# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/house/canonical-data.json
# File last updated on 2023-07-19

import unittest

from house import (
    recite,
)


class HouseTest(unittest.TestCase):
    def test_verse_one_the_house_that_jack_built(self):
        self.assertEqual(recite(1, 1), ["This is the house that Jack built."])

    def test_verse_two_the_malt_that_lay(self):
        self.assertEqual(
            recite(2, 2), ["This is the malt that lay in the house that Jack built."]
        )

    def test_verse_three_the_rat_that_ate(self):
        self.assertEqual(
            recite(3, 3),
            [
                "This is the rat that ate the malt that lay in the house that Jack built."
            ],
        )

    def test_verse_four_the_cat_that_killed(self):
        self.assertEqual(
            recite(4, 4),
            [
                "This is the cat that killed the rat that ate the malt that lay in the house that Jack built."
            ],
        )

    def test_verse_five_the_dog_that_worried(self):
        self.assertEqual(
            recite(5, 5),
            [
                "This is the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built."
            ],
        )

    def test_verse_six_the_cow_with_the_crumpled_horn(self):
        self.assertEqual(
            recite(6, 6),
            [
                "This is the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built."
            ],
        )

    def test_verse_seven_the_maiden_all_forlorn(self):
        self.assertEqual(
            recite(7, 7),
            [
                "This is the maiden all forlorn that milked the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built."
            ],
        )

    def test_verse_eight_the_man_all_tattered_and_torn(self):
        self.assertEqual(
            recite(8, 8),
            [
                "This is the man all tattered and torn that kissed the maiden all forlorn that milked the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built."
            ],
        )

    def test_verse_nine_the_priest_all_shaven_and_shorn(self):
        self.assertEqual(
            recite(9, 9),
            [
                "This is the priest all shaven and shorn that married the man all tattered and torn that kissed the maiden all forlorn that milked the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built."
            ],
        )

    def test_verse_10_the_rooster_that_crowed_in_the_morn(self):
        self.assertEqual(
            recite(10, 10),
            [
                "This is the rooster that crowed in the morn that woke the priest all shaven and shorn that married the man all tattered and torn that kissed the maiden all forlorn that milked the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built."
            ],
        )

    def test_verse_11_the_farmer_sowing_his_corn(self):
        self.assertEqual(
            recite(11, 11),
            [
                "This is the farmer sowing his corn that kept the rooster that crowed in the morn that woke the priest all shaven and shorn that married the man all tattered and torn that kissed the maiden all forlorn that milked the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built."
            ],
        )

    def test_verse_12_the_horse_and_the_hound_and_the_horn(self):
        self.assertEqual(
            recite(12, 12),
            [
                "This is the horse and the hound and the horn that belonged to the farmer sowing his corn that kept the rooster that crowed in the morn that woke the priest all shaven and shorn that married the man all tattered and torn that kissed the maiden all forlorn that milked the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built."
            ],
        )

    def test_multiple_verses(self):
        self.assertEqual(
            recite(4, 8),
            [
                "This is the cat that killed the rat that ate the malt that lay in the house that Jack built.",
                "This is the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built.",
                "This is the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built.",
                "This is the maiden all forlorn that milked the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built.",
                "This is the man all tattered and torn that kissed the maiden all forlorn that milked the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built.",
            ],
        )

    def test_full_rhyme(self):
        self.assertEqual(
            recite(1, 12),
            [
                "This is the house that Jack built.",
                "This is the malt that lay in the house that Jack built.",
                "This is the rat that ate the malt that lay in the house that Jack built.",
                "This is the cat that killed the rat that ate the malt that lay in the house that Jack built.",
                "This is the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built.",
                "This is the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built.",
                "This is the maiden all forlorn that milked the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built.",
                "This is the man all tattered and torn that kissed the maiden all forlorn that milked the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built.",
                "This is the priest all shaven and shorn that married the man all tattered and torn that kissed the maiden all forlorn that milked the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built.",
                "This is the rooster that crowed in the morn that woke the priest all shaven and shorn that married the man all tattered and torn that kissed the maiden all forlorn that milked the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built.",
                "This is the farmer sowing his corn that kept the rooster that crowed in the morn that woke the priest all shaven and shorn that married the man all tattered and torn that kissed the maiden all forlorn that milked the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built.",
                "This is the horse and the hound and the horn that belonged to the farmer sowing his corn that kept the rooster that crowed in the morn that woke the priest all shaven and shorn that married the man all tattered and torn that kissed the maiden all forlorn that milked the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built.",
            ],
        )
