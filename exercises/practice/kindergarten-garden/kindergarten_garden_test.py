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

    def test_full_garden_for_charlie(self):
        garden = Garden("VRCGVVRVCGGCCGVRGCVCGCGV\nVRCCCGCRRGVCGCRVVCVGCGCV")
        self.assertEqual(
            garden.plants("Charlie"), ["Violets", "Violets", "Clover", "Grass"]
        )

    def test_full_garden_for_david(self):
        garden = Garden("VRCGVVRVCGGCCGVRGCVCGCGV\nVRCCCGCRRGVCGCRVVCVGCGCV")
        self.assertEqual(
            garden.plants("David"), ["Radishes", "Violets", "Clover", "Radishes"]
        )

    def test_full_garden_for_eve(self):
        garden = Garden("VRCGVVRVCGGCCGVRGCVCGCGV\nVRCCCGCRRGVCGCRVVCVGCGCV")
        self.assertEqual(garden.plants("Eve"), ["Clover", "Grass", "Radishes", "Grass"])

    def test_full_garden_for_fred(self):
        garden = Garden("VRCGVVRVCGGCCGVRGCVCGCGV\nVRCCCGCRRGVCGCRVVCVGCGCV")
        self.assertEqual(
            garden.plants("Fred"), ["Grass", "Clover", "Violets", "Clover"]
        )

    def test_full_garden_for_ginny(self):
        garden = Garden("VRCGVVRVCGGCCGVRGCVCGCGV\nVRCCCGCRRGVCGCRVVCVGCGCV")
        self.assertEqual(garden.plants("Ginny"), ["Clover", "Grass", "Grass", "Clover"])

    def test_full_garden_for_harriet(self):
        garden = Garden("VRCGVVRVCGGCCGVRGCVCGCGV\nVRCCCGCRRGVCGCRVVCVGCGCV")
        self.assertEqual(
            garden.plants("Harriet"), ["Violets", "Radishes", "Radishes", "Violets"]
        )

    def test_full_garden_for_ileana(self):
        garden = Garden("VRCGVVRVCGGCCGVRGCVCGCGV\nVRCCCGCRRGVCGCRVVCVGCGCV")
        self.assertEqual(
            garden.plants("Ileana"), ["Grass", "Clover", "Violets", "Clover"]
        )

    def test_full_garden_for_joseph(self):
        garden = Garden("VRCGVVRVCGGCCGVRGCVCGCGV\nVRCCCGCRRGVCGCRVVCVGCGCV")
        self.assertEqual(
            garden.plants("Joseph"), ["Violets", "Clover", "Violets", "Grass"]
        )

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
