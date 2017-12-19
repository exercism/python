import unittest

from proverb import proverb


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.0.0

class ProverbTest(unittest.TestCase):
    def test_zero_pieces(self):
        self.assertEqual(proverb([]), "")

    def test_one_piece(self):
        inputs = ["nail"]
        expected = "And all for the want of a nail."
        self.assertEqual(proverb(inputs), expected)

    def test_two_pieces(self):
        inputs = ["nail", "shoe"]
        expected = "\n".join(["For want of a nail the shoe was lost.",
                              "And all for the want of a nail."])
        self.assertEqual(proverb(inputs), expected)

    def test_three_pieces(self):
        inputs = ["nail", "shoe", "horse"]
        expected = "\n".join(["For want of a nail the shoe was lost.",
                              "For want of a shoe the horse was lost.",
                              "And all for the want of a nail."])
        self.assertEqual(proverb(inputs), expected)

    def test_full_proverb(self):
        inputs = ["nail", "shoe", "horse", "rider",
                  "message", "battle", "kingdom"]
        expected = "\n".join(["For want of a nail the shoe was lost.",
                              "For want of a shoe the horse was lost.",
                              "For want of a horse the rider was lost.",
                              "For want of a rider the message was lost.",
                              "For want of a message the battle was lost.",
                              "For want of a battle the kingdom was lost.",
                              "And all for the want of a nail."])
        self.assertEqual(proverb(inputs), expected)

    def test_four_pieces_modernised(self):
        inputs = ["pin", "gun", "soldier", "battle"]
        expected = "\n".join(["For want of a pin the gun was lost.",
                              "For want of a gun the soldier was lost.",
                              "For want of a soldier the battle was lost.",
                              "And all for the want of a pin."])
        self.assertEqual(proverb(inputs), expected)


if __name__ == '__main__':
    unittest.main()
