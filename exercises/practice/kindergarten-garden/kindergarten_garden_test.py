import unittest

from kindergarten_garden import (
    Garden,
)

# Tests adapted from `problem-specifications//canonical-data.json`


class KindergartenGardenTest(unittest.TestCase):
    def test_partial_garden_garden_with_single_student(self):
        garden = Garden("RC\nGG")
        self.assertEqual(
            garden.plants("Alice"), ["Radishes", "Clover", "Grass", "Grass"]
        )

    def test_partial_garden_different_garden_with_single_student(self):
        garden = Garden("VC\nRC")
        self.assertEqual(
            garden.plants("Alice"), ["Violets", "Clover", "Radishes", "Clover"]
        )

    def test_partial_garden_garden_with_two_students(self):
        garden = Garden("VVCG\nVVRC")
        self.assertEqual(
            garden.plants("Bob"), ["Clover", "Grass", "Radishes", "Clover"]
        )

    def test_partial_garden_second_student_s_garden(self):
        garden = Garden("VVCCGG\nVVCCGG")
        self.assertEqual(garden.plants("Bob"), ["Clover", "Clover", "Clover", "Clover"])

    def test_partial_garden_third_student_s_garden(self):
        garden = Garden("VVCCGG\nVVCCGG")
        self.assertEqual(garden.plants("Charlie"), ["Grass", "Grass", "Grass", "Grass"])

    def test_full_garden_for_alice_first_student_s_garden(self):
        garden = Garden("VRCGVVRVCGGCCGVRGCVCGCGV\nVRCCCGCRRGVCGCRVVCVGCGCV")
        self.assertEqual(
            garden.plants("Alice"), ["Violets", "Radishes", "Violets", "Radishes"]
        )

    def test_full_garden_for_bob_second_student_s_garden(self):
        garden = Garden("VRCGVVRVCGGCCGVRGCVCGCGV\nVRCCCGCRRGVCGCRVVCVGCGCV")
        self.assertEqual(garden.plants("Bob"), ["Clover", "Grass", "Clover", "Clover"])

    def test_full_garden_for_kincaid_second_to_last_student_s_garden(self):
        garden = Garden("VRCGVVRVCGGCCGVRGCVCGCGV\nVRCCCGCRRGVCGCRVVCVGCGCV")
        self.assertEqual(
            garden.plants("Kincaid"), ["Grass", "Clover", "Clover", "Grass"]
        )

    def test_full_garden_for_larry_last_student_s_garden(self):
        garden = Garden("VRCGVVRVCGGCCGVRGCVCGCGV\nVRCCCGCRRGVCGCRVVCVGCGCV")
        self.assertEqual(
            garden.plants("Larry"), ["Grass", "Violets", "Clover", "Violets"]
        )

    # Additional tests for this track

    def test_students_are_unordered_first_student(self):
        garden = Garden(
            "VCRRGVRG\nRVGCCGCV", students=["Samantha", "Patricia", "Xander", "Roger"]
        )
        self.assertEqual(
            garden.plants("Patricia"), ["Violets", "Clover", "Radishes", "Violets"]
        )

    def test_students_are_unordered_last_student(self):
        garden = Garden(
            "VCRRGVRG\nRVGCCGCV", students=["Samantha", "Patricia", "Xander", "Roger"]
        )
        self.assertEqual(
            garden.plants("Xander"), ["Radishes", "Grass", "Clover", "Violets"]
        )


if __name__ == "__main__":
    unittest.main()
