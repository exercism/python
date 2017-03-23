import unittest

from kindergarten_garden import Garden


class KindergartenGardenTests(unittest.TestCase):
    def test_alices_garden(self):
        self.assertEqual(
            Garden("RC\nGG").plants("Alice"),
            "Radishes Clover Grass Grass".split())

    def test_bob_and_charlies_gardens(self):
        garden = Garden("VVCCGG\nVVCCGG")
        self.assertEqual(garden.plants("Bob"), ["Clover"] * 4)
        self.assertEqual(garden.plants("Charlie"), ["Grass"] * 4)

    def test_full_garden(self):
        garden = Garden("VRCGVVRVCGGCCGVRGCVCGCGV\nVRCCCGCRRGVCGCRVVCVGCGCV")
        self.assertEqual(
            garden.plants("Alice"),
            "Violets Radishes Violets Radishes".split())
        self.assertEqual(
            garden.plants("Bob"), "Clover Grass Clover Clover".split())
        self.assertEqual(
            garden.plants("Kincaid"), "Grass Clover Clover Grass".split())
        self.assertEqual(
            garden.plants("Larry"), "Grass Violets Clover Violets".split())

    def test_disordered_test(self):
        garden = Garden(
            "VCRRGVRG\nRVGCCGCV",
            students="Samantha Patricia Xander Roger".split())
        self.assertEqual(
            garden.plants("Patricia"),
            "Violets Clover Radishes Violets".split())
        self.assertEqual(
            garden.plants("Xander"), "Radishes Grass Clover Violets".split())


if __name__ == '__main__':
    unittest.main()
