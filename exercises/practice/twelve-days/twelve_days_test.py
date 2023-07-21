# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/twelve-days/canonical-data.json
# File last updated on 2023-07-19

import unittest

from twelve_days import (
    recite,
)

# PLEASE TAKE NOTE: Expected result lists for these test cases use **implicit line joining.**
# A new line in a result list below **does not** always equal a new list element.
# Check comma placement carefully!


class TwelveDaysTest(unittest.TestCase):
    def test_first_day_a_partridge_in_a_pear_tree(self):
        expected = [
            "On the first day of Christmas my true love gave to me: "
            "a Partridge in a Pear Tree."
        ]
        self.assertEqual(recite(1, 1), expected)

    def test_second_day_two_turtle_doves(self):
        expected = [
            "On the second day of Christmas my true love gave to me: "
            "two Turtle Doves, "
            "and a Partridge in a Pear Tree."
        ]
        self.assertEqual(recite(2, 2), expected)

    def test_third_day_three_french_hens(self):
        expected = [
            "On the third day of Christmas my true love gave to me: "
            "three French Hens, "
            "two Turtle Doves, "
            "and a Partridge in a Pear Tree."
        ]
        self.assertEqual(recite(3, 3), expected)

    def test_fourth_day_four_calling_birds(self):
        expected = [
            "On the fourth day of Christmas my true love gave to me: "
            "four Calling Birds, "
            "three French Hens, "
            "two Turtle Doves, "
            "and a Partridge in a Pear Tree."
        ]
        self.assertEqual(recite(4, 4), expected)

    def test_fifth_day_five_gold_rings(self):
        expected = [
            "On the fifth day of Christmas my true love gave to me: "
            "five Gold Rings, "
            "four Calling Birds, "
            "three French Hens, "
            "two Turtle Doves, "
            "and a Partridge in a Pear Tree."
        ]
        self.assertEqual(recite(5, 5), expected)

    def test_sixth_day_six_geese_a_laying(self):
        expected = [
            "On the sixth day of Christmas my true love gave to me: "
            "six Geese-a-Laying, "
            "five Gold Rings, "
            "four Calling Birds, "
            "three French Hens, "
            "two Turtle Doves, "
            "and a Partridge in a Pear Tree."
        ]
        self.assertEqual(recite(6, 6), expected)

    def test_seventh_day_seven_swans_a_swimming(self):
        expected = [
            "On the seventh day of Christmas my true love gave to me: "
            "seven Swans-a-Swimming, "
            "six Geese-a-Laying, "
            "five Gold Rings, "
            "four Calling Birds, "
            "three French Hens, "
            "two Turtle Doves, "
            "and a Partridge in a Pear Tree."
        ]
        self.assertEqual(recite(7, 7), expected)

    def test_eighth_day_eight_maids_a_milking(self):
        expected = [
            "On the eighth day of Christmas my true love gave to me: "
            "eight Maids-a-Milking, "
            "seven Swans-a-Swimming, "
            "six Geese-a-Laying, "
            "five Gold Rings, "
            "four Calling Birds, "
            "three French Hens, "
            "two Turtle Doves, "
            "and a Partridge in a Pear Tree."
        ]
        self.assertEqual(recite(8, 8), expected)

    def test_ninth_day_nine_ladies_dancing(self):
        expected = [
            "On the ninth day of Christmas my true love gave to me: "
            "nine Ladies Dancing, "
            "eight Maids-a-Milking, "
            "seven Swans-a-Swimming, "
            "six Geese-a-Laying, "
            "five Gold Rings, "
            "four Calling Birds, "
            "three French Hens, "
            "two Turtle Doves, "
            "and a Partridge in a Pear Tree."
        ]
        self.assertEqual(recite(9, 9), expected)

    def test_tenth_day_ten_lords_a_leaping(self):
        expected = [
            "On the tenth day of Christmas my true love gave to me: "
            "ten Lords-a-Leaping, "
            "nine Ladies Dancing, "
            "eight Maids-a-Milking, "
            "seven Swans-a-Swimming, "
            "six Geese-a-Laying, "
            "five Gold Rings, "
            "four Calling Birds, "
            "three French Hens, "
            "two Turtle Doves, "
            "and a Partridge in a Pear Tree."
        ]
        self.assertEqual(recite(10, 10), expected)

    def test_eleventh_day_eleven_pipers_piping(self):
        expected = [
            "On the eleventh day of Christmas my true love gave to me: "
            "eleven Pipers Piping, "
            "ten Lords-a-Leaping, "
            "nine Ladies Dancing, "
            "eight Maids-a-Milking, "
            "seven Swans-a-Swimming, "
            "six Geese-a-Laying, "
            "five Gold Rings, "
            "four Calling Birds, "
            "three French Hens, "
            "two Turtle Doves, "
            "and a Partridge in a Pear Tree."
        ]
        self.assertEqual(recite(11, 11), expected)

    def test_twelfth_day_twelve_drummers_drumming(self):
        expected = [
            "On the twelfth day of Christmas my true love gave to me: "
            "twelve Drummers Drumming, "
            "eleven Pipers Piping, "
            "ten Lords-a-Leaping, "
            "nine Ladies Dancing, "
            "eight Maids-a-Milking, "
            "seven Swans-a-Swimming, "
            "six Geese-a-Laying, "
            "five Gold Rings, "
            "four Calling Birds, "
            "three French Hens, "
            "two Turtle Doves, "
            "and a Partridge in a Pear Tree."
        ]
        self.assertEqual(recite(12, 12), expected)

    def test_recites_first_three_verses_of_the_song(self):
        expected = [recite(n, n)[0] for n in range(1, 4)]
        self.assertEqual(recite(1, 3), expected)

    def test_recites_three_verses_from_the_middle_of_the_song(self):
        expected = [recite(n, n)[0] for n in range(4, 7)]
        self.assertEqual(recite(4, 6), expected)

    def test_recites_the_whole_song(self):
        expected = [recite(n, n)[0] for n in range(1, 13)]
        self.assertEqual(recite(1, 12), expected)
