import unittest

from kindergarten_garden import Garden


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.1.1

class KindergartenGardenTest(unittest.TestCase):
    def test_garden_with_single_student(self):
        self.assertEqual(
            Garden("RC\nGG").plants("Alice"),
            "Radishes Clover Grass Grass".split())

    def test_different_garden_with_single_student(self):
        self.assertEqual(
            Garden("VC\nRC").plants("Alice"),
            "Violets Clover Radishes Clover".split())

    def test_garden_with_two_students(self):
        garden = Garden("VVCG\nVVRC")
        self.assertEqual(
            garden.plants("Bob"), "Clover Grass Radishes Clover".split())

    def test_multiple_students_for_the_same_garden_with_three_students(self):
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

    # Additional tests for this track
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
