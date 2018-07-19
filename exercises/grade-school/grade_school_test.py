import unittest

from grade_school import School


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.0.0

class GradeSchoolTest(unittest.TestCase):
    def test_adding_student_adds_them_to_sorted_roster(self):
        school = School()
        school.add_student(name='Aimee', grade=2)
        expected = ['Aimee']
        self.assertEqual(school.roster(), expected)

    def test_adding_more_students_adds_them_to_sorted_roster(self):
        school = School()
        school.add_student(name='Blair', grade=2)
        school.add_student(name='James', grade=2)
        school.add_student(name='Paul', grade=2)
        expected = ['Blair', 'James', 'Paul']
        self.assertEqual(school.roster(), expected)

    def test_students_in_different_grades_in_same_roster(self):
        school = School()
        school.add_student(name='Chelsea', grade=3)
        school.add_student(name='Logan', grade=7)
        expected = ['Chelsea', 'Logan']
        self.assertEqual(school.roster(), expected)

    def test_roster_returns_empty_list_if_no_students_are_enrolled(self):
        self.assertEqual(School().roster(), [])

    def test_roster_is_sorted_by_grade_then_name(self):
        school = School()
        for name, grade in [
            ('Peter', 2),
            ('Anna', 1),
            ('Barb', 1),
            ('Zoe', 2),
            ('Alex', 2),
            ('Jim', 3),
            ('Charlie', 1),
        ]:
            school.add_student(name, grade)
        expected = ['Anna', 'Barb', 'Charlie', 'Alex', 'Peter', 'Zoe', 'Jim']
        self.assertEqual(school.roster(), expected)

    def test_grade_returns_students_in_that_grade_in_alphabetical_order(self):
        school = School()
        school.add_student(name='Franklin', grade=5)
        school.add_student(name='Bradley', grade=5)
        school.add_student(name='Jeff', grade=1)
        expected = ['Bradley', 'Franklin']
        self.assertEqual(school.grade(5), expected)

    def test_grade_returns_empty_list_if_no_students_are_in_that_grade(self):
        self.assertEqual(School().grade(1), [])


if __name__ == '__main__':
    unittest.main()
