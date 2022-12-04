import unittest

from proverb import (
    proverb,
)

# Tests adapted from `problem-specifications//canonical-data.json`
# PLEASE TAKE NOTE: Expected result lists for these test cases use **implicit line joining.**
# A new line in a result list below **does not** always equal a new list element.
# Check comma placement carefully!


class ProverbTest(unittest.TestCase):
    def test_zero_pieces(self):
        self.assertEqual(proverb(), [])

    def test_one_piece(self):
        self.assertEqual(
            proverb(
                "nail",
            ),
            ["And all for the want of a nail."],
        )

    def test_two_pieces(self):
        self.assertEqual(
            proverb(
                "nail",
                "shoe",
            ),
            [
                "For want of a nail the shoe was lost.",
                "And all for the want of a nail.",
            ],
        )

    def test_three_pieces(self):
        self.assertEqual(
            proverb(
                "nail",
                "shoe",
                "horse",
            ),
            [
                "For want of a nail the shoe was lost.",
                "For want of a shoe the horse was lost.",
                "And all for the want of a nail.",
            ],
        )

    def test_full_proverb(self):
        self.assertEqual(
            proverb(
                "nail",
                "shoe",
                "horse",
                "rider",
                "message",
                "battle",
                "kingdom",
            ),
            [
                "For want of a nail the shoe was lost.",
                "For want of a shoe the horse was lost.",
                "For want of a horse the rider was lost.",
                "For want of a rider the message was lost.",
                "For want of a message the battle was lost.",
                "For want of a battle the kingdom was lost.",
                "And all for the want of a nail.",
            ],
        )

    def test_four_pieces_modernized(self):
        self.assertEqual(
            proverb(
                "pin",
                "gun",
                "soldier",
                "battle",
            ),
            [
                "For want of a pin the gun was lost.",
                "For want of a gun the soldier was lost.",
                "For want of a soldier the battle was lost.",
                "And all for the want of a pin.",
            ],
        )

    # Track-specific tests
    def test_sentence_without_lower_bound(self):
        self.assertEqual(
            proverb("nail", qualifier="horseshoe"),
            ["And all for the want of a horseshoe nail."],
        )

    def test_sentence_without_upper_bound(self):
        self.assertEqual(
            proverb(
                "nail",
                "shoe",
                "horse",
                "rider",
                "message",
                "battle",
                "kingdom",
                qualifier="horseshoe",
            ),
            [
                "For want of a nail the shoe was lost.",
                "For want of a shoe the horse was lost.",
                "For want of a horse the rider was lost.",
                "For want of a rider the message was lost.",
                "For want of a message the battle was lost.",
                "For want of a battle the kingdom was lost.",
                "And all for the want of a horseshoe nail.",
            ],
        )
