import unittest
import pytest
from loops import (
    round_scores,
    count_failed_students,
    above_threshold,
    letter_grades,
    student_ranking,
    perfect_score)


class MakingTheGradeTest(unittest.TestCase):

    @pytest.mark.task(taskno=1)
    def test_round_scores(self):
        data = [
            ([], []),
            ([.5], [0]),
            ([1.5], [2]),
            (
                [90.33, 40.5, 55.44, 70.05, 30.55, 25.45, 80.45, 95.3, 38.7, 40.3],
                [90, 40, 55, 70, 31, 25, 80, 95, 39, 40]),
            (
                [50, 36.03, 76.92, 40.7, 43, 78.29, 63.58, 91, 28.6, 88.0],
                [50, 36, 77, 41, 43, 78, 64, 91, 29, 88])]

        for variant, (student_scores, result) in enumerate(data, start=1):
            error_message = f'Expected: {result} but one or more {student_scores} were rounded incorrectly.'
            with self.subTest(f'variation #{variant}', input=student_scores, output=result):
                self.assertEqual(sorted(round_scores(student_scores)), sorted(result), msg=error_message)

    @pytest.mark.task(taskno=2)
    def test_count_failed_students(self):
        data = [
            ([89, 85, 42, 57, 90, 100, 95, 48, 70, 96], 0),
            ([40, 40, 35, 70, 30, 41, 90], 4)]

        for variant, (student_scores, result) in enumerate(data, start=1):
            error_message = f'Expected the count to be {result}, but the count was not calculated correctly.'
            with self.subTest(f'variation #{variant}', input=student_scores, output=result):
                self.assertEqual(count_failed_students(student_scores), result, msg=error_message)

    @pytest.mark.task(taskno=3)
    def test_above_threshold(self):
        data = [
            (([40, 39, 95, 80, 25, 31, 70, 55, 40, 90], 98), []),
            (([88, 29, 91, 64, 78, 43, 41, 77, 36, 50], 80), [88, 91]),
            (([100, 89], 100), [100]),
            (([88, 29, 91, 64, 78, 43, 41, 77, 36, 50], 78), [88, 91, 78]),
            (([], 80), [])]

        for variant, (params, result) in enumerate(data, start=1):
            error_message = f'Expected: {result} but the number of scores above the threshold is incorrect.'
            with self.subTest(f'variation #{variant}', input=params, output=result):
                self.assertEqual(above_threshold(*params), result, msg=error_message)

    @pytest.mark.task(taskno=4)
    def test_letter_grades(self):
        data = [
            (100, [41, 56, 71, 86]),
            (97, [41, 55, 69, 83]),
            (85, [41, 52, 63, 74]),
            (92, [41, 54, 67, 80]),
            (81, [41, 51, 61, 71])]

        for variant, (highest, result) in enumerate(data, start=1):
            error_message = f'Expected: {result} but the grade thresholds for a high score of {highest} are incorrect.'
            with self.subTest(f'variation #{variant}', input=highest, output=result):
                self.assertEqual(letter_grades(highest), result, msg=error_message)

    @pytest.mark.task(taskno=5)
    def test_student_ranking(self):
        data = [
            (([82], ['Betty']), ['1. Betty: 82']),
            (([88, 73], ['Paul', 'Ernest']), ['1. Paul: 88', '2. Ernest: 73']),
            (
                ([100, 98, 92, 86, 70, 68, 67, 60], ['Rui', 'Betty', 'Joci', 'Yoshi', 'Kora', 'Bern', 'Jan', 'Rose']),
                ['1. Rui: 100', '2. Betty: 98', '3. Joci: 92', '4. Yoshi: 86',
                 '5. Kora: 70', '6. Bern: 68', '7. Jan: 67', '8. Rose: 60'])]

        for variant, (params, result) in enumerate(data, start=1):
            error_message = f'Expected: {result} but the rankings were compiled incorrectly.'
            with self.subTest(f'variation #{variant}', input=params, output=result):
                self.assertEqual(student_ranking(*params), result, msg=error_message)

    @pytest.mark.task(taskno=6)
    def test_perfect_score(self):
        data = [
            ([['Joci', 100], ['Vlad', 100], ['Raiana', 100], ['Alessandro', 100]], ['Joci', 100]),
            ([['Jill', 30], ['Paul', 73], ], []),
            ([], []),
            (
                [['Rui', 60], ['Joci', 58], ['Sara', 91], ['Kora', 93], ['Alex', 42],
                 ['Jan', 81], ['Lilliana', 40], ['John', 60], ['Bern', 28], ['Vlad', 55]], []),
            (
                [['Yoshi', 52], ['Jan', 86], ['Raiana', 100], ['Betty', 60],
                 ['Joci', 100], ['Kora', 81], ['Bern', 41], ['Rose', 94]], ['Raiana', 100])]

        for variant, (student_info, result) in enumerate(data, start=1):
            error_message = f'Expected: {result} but got something different for perfect scores.'
            with self.subTest(f'variation #{variant}', input=student_info, output=result):
                self.assertEqual(perfect_score(student_info), result, msg=error_message)
