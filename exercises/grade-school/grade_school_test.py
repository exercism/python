from collections import Sequence
from types import GeneratorType
import unittest

from grade_school import School


class SchoolTest(unittest.TestCase):
    def setUp(self):
        # assertCountEqual is py3, py2 only knowns assetItemsEqual
        if not hasattr(self, 'assertCountEqual'):
            self.assertCountEqual = self.assertItemsEqual
        self.school = School("Haleakala Hippy School")

    def test_an_empty_school(self):
        for n in range(1, 9):
            self.assertCountEqual(set(), self.school.grade(n))

    def test_add_student(self):
        self.school.add("Aimee", 2)
        self.assertCountEqual(("Aimee",), self.school.grade(2))

    def test_add_more_students_in_same_class(self):
        self.school.add("James", 2)
        self.school.add("Blair", 2)
        self.school.add("Paul", 2)
        self.assertCountEqual(("James", "Blair", "Paul"), self.school.grade(2))

    def test_add_students_to_different_grades(self):
        self.school.add("Chelsea", 3)
        self.school.add("Logan", 7)
        self.assertCountEqual(("Chelsea",), self.school.grade(3))
        self.assertCountEqual(("Logan",), self.school.grade(7))

    def test_get_students_in_a_grade(self):
        self.school.add("Franklin", 5)
        self.school.add("Bradley", 5)
        self.school.add("Jeff", 1)
        self.assertCountEqual(("Franklin", "Bradley"), self.school.grade(5))

    def test_get_students_in_a_non_existant_grade(self):
        self.assertCountEqual(set(), self.school.grade(1))

    def test_sort_school(self):

        students = [
            (3, ("Kyle",)),
            (4, ("Christopher", "Jennifer",)),
            (6, ("Kareem",))
        ]
        for grade, students_in_grade in students:
            for student in students_in_grade:
                self.school.add(student, grade)

        result = self.school.sort()

        # Attempts to catch false positives
        self.assertTrue(isinstance(result, Sequence) or
                        isinstance(result, GeneratorType) or
                        callable(getattr(result, '__reversed__', False)))

        result_list = list(result.items() if hasattr(result, "items")
                           else result)

        self.assertEqual(result_list, students)


if __name__ == '__main__':
    unittest.main()
