import unittest

from zebra_puzzle import drinks_water, owns_zebra

# Tests adapted from `problem-specifications//canonical-data.json` @ v1.1.0


class ZebraPuzzleTest(unittest.TestCase):
    def test_resident_who_drinks_water(self):
        expected = "Norwegian"
        self.assertEqual(drinksWater(), expected)

    def test_resident_who_owns_zebra(self):
        expected = "Japanese"
        self.assertEqual(ownsZebra(), expected)


if __name__ == "__main__":
    unittest.main()
