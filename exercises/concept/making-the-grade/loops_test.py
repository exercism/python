import unittest
import pytest
from loops import (
    round_scores,
    count_failed_students,
    above_threshold,
    letter_grades,
    student_ranking,
    perfect_score,
)


class MakingTheGradeTest(unittest.TestCase):

    @pytest.mark.task(taskno=1)
    def test_round_scores(self):
        input_data = [
            [90.33, 40.5, 55.44, 70.05, 30.55, 25.45, 80.45, 95.3, 38.7, 40.3],
            [],
            [50, 36.03, 76.92, 40.7, 43, 78.29, 63.58, 91, 28.6, 88.0],
            [.5],
            [1.5]
        ]
        result_data = [
            [40, 39, 95, 80, 25, 31, 70, 55, 40, 90],
            [],
            [88, 29, 91, 64, 78, 43, 41, 77, 36, 50],
            [0],
            [2]
        ]
        number_of_variants = range(1, len(input_data) + 1)

        for variant, scores, results in zip(number_of_variants, input_data, result_data):
            with self.subTest(f"variation #{variant}", scores=scores, results=results):
                self.assertEqual(sorted(round_scores(scores)), sorted(results),
                                 msg=f'Expected: {results} but one or more {scores} were rounded incorrectly.')


    @pytest.mark.task(taskno=2)
    def test_no_failed_students(self):
        scores = [89, 85, 42, 57, 90, 100, 95, 48, 70, 96]
        expected = 0
        self.assertEqual(count_failed_students(scores), expected,
        msg=f"Expected the count to be {expected}, but the count wasn't calculated correctly.")

    @pytest.mark.task(taskno=2)
    def test_some_failed_students(self):
        scores = [40, 40, 35, 70, 30, 41, 90]
        expected = 4
        self.assertEqual(count_failed_students(scores), expected,
            msg=f"Expected the count to be {expected}, but the count wasn't calculated correctly.")

    @pytest.mark.task(taskno=3)
    def test_above_threshold(self):
        input_data = [
            [40, 39, 95, 80, 25, 31, 70, 55, 40, 90],
            [88, 29, 91, 64, 78, 43, 41, 77, 36, 50],
            [100, 89],
            [88, 29, 91, 64, 78, 43, 41, 77, 36, 50],
            []
        ]
        thresholds = [98, 80, 100, 78, 80]
        result_data = [
            [],
            [88, 91],
            [100],
            [88, 91, 78],
            []
        ]
        number_of_variants = range(1, len(input_data) + 1)

        for variant, score, threshold, result in zip(number_of_variants, input_data, thresholds, result_data):
            with self.subTest(f"variation #{variant}", score=score, threshold=threshold, result=result):
                self.assertEqual(above_threshold(score, threshold), result,
                                 msg=f'Expected: {result} but the number of scores above {threshold} is incorrect.')

    @pytest.mark.task(taskno=4)
    def test_letter_grades(self):
        input_data = [100, 97, 85, 92, 81]
        result_data = [
            [41, 56, 71, 86],
            [41, 55, 69, 83],
            [41, 52, 63, 74],
            [41, 54, 67, 80],
            [41, 51, 61, 71]
        ]
        number_of_variants = range(1, len(input_data) + 1)

        for variant, highest, result in zip(number_of_variants, input_data, result_data):
            with self.subTest(f"variation #{variant}", highest=highest, result=result):
                self.assertEqual(letter_grades(highest), result,
                                 msg=f'Expected: {result} but the grade thresholds for a high score of {highest} are incorrect.')


    @pytest.mark.task(taskno=5)
    def test_student_ranking(self):
        scores = [
            [100, 98, 92, 86, 70, 68, 67, 60, 50],
            [82],
            [88, 73],
        ]
        names = [
            ['Rui', 'Betty', 'Joci', 'Yoshi', 'Kora', 'Bern', 'Jan', 'Rose'],
            ['Betty'],
            ['Paul', 'Ernest'],
        ]
        result_data = [
            ['1. Rui: 100', '2. Betty: 98', '3. Joci: 92', '4. Yoshi: 86',
             '5. Kora: 70', '6. Bern: 68', '7. Jan: 67', '8. Rose: 60'],
            ['1. Betty: 82'],
            ['1. Paul: 88', '2. Ernest: 73']
        ]
        number_of_variants = range(1, len(scores) + 1)

        for variant, scores, names, results in zip(number_of_variants, scores, names, result_data):
            with self.subTest(f"variation #{variant}", scores=scores, names=names, results=results):\
                self.assertEqual(student_ranking(scores, names), results,
                                 msg=f'Expected: {results} but the rankings were compiled incorrectly.')

    @pytest.mark.task(taskno=6)
    def test_perfect_score(self):
       input_data =  [
                        [['Rui', 60],['Joci', 58],['Sara', 91],['Kora', 93], ['Alex', 42],
                         ['Jan', 81],['Lilliana', 40],['John', 60],['Bern', 28],['Vlad', 55]],

                        [['Yoshi', 52],['Jan', 86], ['Raiana', 100], ['Betty', 60],
                         ['Joci', 100],['Kora', 81],['Bern', 41], ['Rose', 94]],

                        [['Joci', 100],['Vlad', 100],['Raiana', 100],['Alessandro', 100]],
                        [['Jill', 30], ['Paul', 73],],
                        []
                    ]
       result_data = [
           "No perfect score.",
           ['Raiana', 100],
           ['Joci', 100],
           "No perfect score.",
           "No perfect score."
       ]

       number_of_variants = range(1, len(input_data) + 1)

       for variant, scores, results in zip(number_of_variants, input_data, result_data):
           with self.subTest(f"variation #{variant}", scores=scores, results=results):
               self.assertEqual(perfect_score(scores), results,
                                msg=f'Expected: {results} but got something different for perfect scores.')
