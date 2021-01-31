import unittest

from grade_school import (
    School,
)

# Tests adapted from `problem-specifications//canonical-data.json`


class GradeSchoolTest(unittest.TestCase):
    def test_adding_a_student_adds_them_to_the_sorted_roster(self):
        school = School()
        school.add_student(name="Aimee", grade=2)
        expected = ["Aimee"]
        self.assertEqual(school.roster(), expected)

    def test_adding_more_students_adds_them_to_the_sorted_roster(self):
        school = School()
        school.add_student(name="Blair", grade=2)
        school.add_student(name="James", grade=2)
        school.add_student(name="Paul", grade=2)
        expected = ["Blair", "James", "Paul"]
        self.assertEqual(school.roster(), expected)

    def test_adding_students_to_different_grades_adds_them_to_the_same_sorted_roster(
        self,
    ):
        school = School()
        school.add_student(name="Chelsea", grade=3)
        school.add_student(name="Logan", grade=7)
        expected = ["Chelsea", "Logan"]
        self.assertEqual(school.roster(), expected)

    def test_roster_returns_an_empty_list_if_there_are_no_students_enrolled(self):
        school = School()
        expected = []
        self.assertEqual(school.roster(), expected)

    def test_student_names_with_grades_are_displayed_in_the_same_sorted_roster(self):
        school = School()
        school.add_student(name="Peter", grade=2)
        school.add_student(name="Anna", grade=1)
        school.add_student(name="Barb", grade=1)
        school.add_student(name="Zoe", grade=2)
        school.add_student(name="Alex", grade=2)
        school.add_student(name="Jim", grade=3)
        school.add_student(name="Charlie", grade=1)
        expected = ["Anna", "Barb", "Charlie", "Alex", "Peter", "Zoe", "Jim"]
        self.assertEqual(school.roster(), expected)

    def test_grade_returns_the_students_in_that_grade_in_alphabetical_order(self):
        school = School()
        school.add_student(name="Franklin", grade=5)
        school.add_student(name="Bradley", grade=5)
        school.add_student(name="Jeff", grade=1)
        expected = ["Bradley", "Franklin"]
        self.assertEqual(school.grade(5), expected)

    def test_grade_returns_an_empty_list_if_there_are_no_students_in_that_grade(self):
        school = School()
        expected = []
        self.assertEqual(school.grade(1), expected)


if __name__ == "__main__":
    unittest.main()
