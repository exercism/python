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

        # Because we the input list can be mutated, the test data has been created
        # as tuples, which we then convert to a list when the test runs.
        # this makes accurate error messages easier to create.
        test_data = [tuple(),
                     (.5,),
                     (1.5,),
                     (90.33, 40.5, 55.44, 70.05, 30.55, 25.45, 80.45, 95.3, 38.7, 40.3),
                     (50, 36.03, 76.92, 40.7, 43, 78.29, 63.58, 91, 28.6, 88.0)]
        result_data = [[],
                       [0],
                       [2],
                       [90, 40, 55, 70, 31, 25, 80, 95, 39, 40],
                       [50, 36, 77, 41, 43, 78, 64, 91, 29, 88]]

        for variant, (student_scores, expected) in enumerate(zip(test_data, result_data), start=1):
            with self.subTest(f'variation #{variant}', student_scores=student_scores, expected=expected):

                # Because the test_input is a tuple, it has to be converted to a list for the function call.
                actual_result = round_scores(list(student_scores))
                error_message = (f'Called round_scores({list(student_scores)}). '
                                 f'The function returned {sorted(actual_result)} after sorting, but '
                                 f'the tests expected {sorted(expected)} after sorting. '
                                 f'One or more scores were rounded incorrectly.')

                # everything is sorted for easier comparison.
                self.assertEqual(sorted(actual_result), sorted(expected), msg=error_message)

    @pytest.mark.task(taskno=2)
    def test_count_failed_students(self):
        test_data = [[89, 85, 42, 57, 90, 100, 95, 48, 70, 96],
                     [40, 40, 35, 70, 30, 41, 90]]
        result_data = [0,4]

        for variant, (student_scores, expected) in enumerate(zip(test_data, result_data), start=1):
            with self.subTest(f'variation #{variant}',
                              student_scores=student_scores,
                              expected=expected):

                actual_result = count_failed_students(student_scores)
                error_message = (f'Called count_failed_students({student_scores}). '
                                 f'The function returned {actual_result}, but '
                                 f'the tests expected {expected} for the '
                                 'number of students who failed.')

                self.assertEqual(actual_result, expected, msg=error_message)

    @pytest.mark.task(taskno=3)
    def test_above_threshold(self):
        test_data = [([40, 39, 95, 80, 25, 31, 70, 55, 40, 90], 98),
                     ([88, 29, 91, 64, 78, 43, 41, 77, 36, 50], 80),
                     ([100, 89], 100),
                     ([88, 29, 91, 64, 78, 43, 41, 77, 36, 50], 78),
                     ([], 80)]

        result_data = [[],
                       [88, 91],
                       [100],
                       [88, 91, 78],
                       []]

        for variant, (params, expected) in enumerate(zip(test_data, result_data), start=1):
            with self.subTest(f'variation #{variant}', params=params, expected=expected):
                actual_result = above_threshold(*params)
                error_message = (f'Called above_threshold{params}. '
                                 f'The function returned {actual_result}, but '
                                 f'the tests expected {expected} for the '
                                 'scores that are above the threshold.')

                self.assertEqual(actual_result, expected, msg=error_message)

    @pytest.mark.task(taskno=4)
    def test_letter_grades(self):
        test_data = [100, 97, 85, 92, 81]

        result_data = [[41, 56, 71, 86],
                       [41, 55, 69, 83],
                       [41, 52, 63, 74],
                       [41, 54, 67, 80],
                       [41, 51, 61, 71]]

        for variant, (highest, expected) in enumerate(zip(test_data, result_data), start=1):
            with self.subTest(f'variation #{variant}', highest=highest, expected=expected):
                actual_result = letter_grades(highest)
                error_message = (f'Called letter_grades({highest}). '
                                 f'The function returned {actual_result}, but '
                                 f'the tests expected {expected} for the '
                                 'letter grade cutoffs.')

                self.assertEqual(actual_result, expected, msg=error_message)

    @pytest.mark.task(taskno=5)
    def test_student_ranking(self):
        test_data = [([82], ['Betty']),
                     ([88, 73], ['Paul', 'Ernest']),
                     ([100, 98, 92, 86, 70, 68, 67, 60],
                      ['Rui', 'Betty', 'Joci', 'Yoshi', 'Kora', 'Bern', 'Jan', 'Rose'])]

        result_data = [['1. Betty: 82'],
                       ['1. Paul: 88', '2. Ernest: 73'],
                       ['1. Rui: 100', '2. Betty: 98', '3. Joci: 92', '4. Yoshi: 86',
                        '5. Kora: 70', '6. Bern: 68', '7. Jan: 67', '8. Rose: 60']]

        for variant, (params, expected) in enumerate(zip(test_data, result_data), start=1):
            with self.subTest(f'variation #{variant}', params=params, expected=expected):
                actual_result = student_ranking(*params)
                error_message = (f'Called student_ranking{params}. '
                                 f'The function returned {actual_result}, but '
                                 f'the tests expected {expected} for the '
                                 'student rankings.')

                self.assertEqual(actual_result, expected, msg=error_message)

    @pytest.mark.task(taskno=6)
    def test_perfect_score(self):
        test_data = [
                     [['Joci', 100], ['Vlad', 100], ['Raiana', 100], ['Alessandro', 100]],
                     [['Jill', 30], ['Paul', 73]],
                     [],
                     [['Rui', 60], ['Joci', 58], ['Sara', 91], ['Kora', 93], ['Alex', 42],
                      ['Jan', 81], ['Lilliana', 40], ['John', 60], ['Bern', 28], ['Vlad', 55]],

                     [['Yoshi', 52], ['Jan', 86], ['Raiana', 100], ['Betty', 60],
                      ['Joci', 100], ['Kora', 81], ['Bern', 41], ['Rose', 94]]
                     ]


        result_data = [['Joci', 100],[], [], [], ['Raiana', 100]]

        for variant, (student_info, expected) in enumerate(zip(test_data, result_data), start=1):

            with self.subTest(f'variation #{variant}', student_info=student_info, expected=expected):
                actual_result = perfect_score(student_info)
                error_message = (f'Called perfect_score({student_info}). '
                                 f'The function returned {actual_result}, but '
                                 f'the tests expected {expected} for the '
                                 'first "perfect" score.')

                self.assertEqual(actual_result, expected, msg=error_message)
