import unittest
import pytest

from lists import (
    get_rounds,
    concatenate_rounds,
    list_contains_round,
    card_average,
    approx_average_is_average,
    average_even_is_average_odd,
    maybe_double_last,
)


class CardGamesTest(unittest.TestCase):

    @pytest.mark.task(taskno=1)
    def test_get_rounds(self):

        input_data = [0, 1, 10, 27, 99, 666]
        result_data = [[0, 1, 2], [1, 2, 3],
                       [10, 11, 12], [27, 28, 29],
                       [99, 100, 101], [666, 667, 668]]

        for variant, (number, expected) in enumerate(zip(input_data, result_data), start=1):
            with self.subTest(f'variation #{variant}', number=number, expected=expected):
                actual_result = get_rounds(number)
                error_message = (f'Called get_rounds({number}). '
                                 f'The function returned {actual_result}, '
                                 f'but the tests expected rounds {expected} '
                                 f'given the current round {number}.')

                self.assertEqual(actual_result, expected, msg=error_message)

    @pytest.mark.task(taskno=2)
    def test_concatenate_rounds(self):

        input_data = [([], []), ([0, 1], []), ([], [1, 2]),
                      ([1], [2]), ([27, 28, 29], [35, 36]),
                      ([1, 2, 3], [4, 5, 6])]

        result_data = [[], [0, 1], [1, 2], [1, 2],
                       [27, 28, 29, 35, 36],
                       [1, 2, 3, 4, 5, 6]]

        for variant, ((rounds_1, rounds_2), expected) in enumerate(zip(input_data, result_data), start=1):
            with self.subTest(f'variation #{variant}', rounds_1=rounds_1, rounds_2=rounds_2, expected=expected):
                actual_result = concatenate_rounds(rounds_1, rounds_2)
                error_message = (f'Called concatenate_rounds({rounds_1}, {rounds_2}). '
                                 f'The function returned {actual_result}, but the tests '
                                 f'expected {expected} as the concatenation '
                                 f'of {rounds_1} and {rounds_2}.')

                self.assertEqual(actual_result, expected, msg=error_message)

    @pytest.mark.task(taskno=3)
    def test_list_contains_round(self):

        input_data = [([], 1), ([1, 2, 3], 0),
                      ([27, 28, 29, 35, 36], 30),
                      ([1], 1), ([1, 2, 3], 1),
                      ([27, 28, 29, 35, 36], 29)]
        result_data = [False, False, False, True, True, True]

        for variant, ((rounds, round_number), expected) in enumerate(zip(input_data, result_data), start=1):
            with self.subTest(f'variation #{variant}', rounds=rounds, round_number=round_number, expected=expected):
                actual_result = list_contains_round(rounds, round_number)
                error_message = (f'Called list_contains_round({rounds}, {round_number}). '
                                 f'The function returned {actual_result}, but round {round_number} '
                                 f'{"is" if expected else "is not"} in {rounds}.')

                self.assertEqual(actual_result, expected, msg=error_message)

    @pytest.mark.task(taskno=4)
    def test_card_average(self):

        input_data = [[1], [5, 6, 7], [1, 2, 3, 4], [1, 10, 100]]
        result_data = [1.0, 6.0, 2.5, 37.0]

        for variant, (hand, expected) in enumerate(zip(input_data, result_data), start=1):
            with self.subTest(f'variation #{variant}', hand=hand, expected=expected):
                actual_result = card_average(hand)
                error_message = (f'Called card_average({hand}). '
                                 f'The function returned {actual_result}, but '
                                 f'the tests expected {expected} as the average of {hand}.')

                self.assertEqual(actual_result, expected, msg=error_message)

    @pytest.mark.task(taskno=5)
    def test_approx_average_is_average(self):

        input_data = [[0, 1, 5], [3, 6, 9, 12, 150], [1, 2, 3, 5, 9],
                      [2, 3, 4, 7, 8], [1, 2, 3], [2, 3, 4],
                      [2, 3, 4, 8, 8], [1, 2, 4, 5, 8]]

        result_data = [False, False, False, False, True, True, True, True]

        for variant, (hand, expected) in enumerate(zip(input_data, result_data), start=1):
            with self.subTest(f'variation #{variant}', hand=hand, expected=expected):
                actual_result = approx_average_is_average(hand)
                error_message = (f'Called approx_average_is_average({hand}). '
                                 f'The function returned {actual_result}, but '
                                 f'the hand {hand} {"does" if expected else "does not"} '
                                 f'yield the same approximate average.')

                self.assertEqual(actual_result, expected, msg=error_message)

    @pytest.mark.task(taskno=6)
    def test_average_even_is_average_odd(self):

        input_data = [[5, 6, 8], [1, 2, 3, 4], [1, 2, 3], [5, 6, 7], [1, 3, 5, 7, 9]]
        result_data = [False, False, True, True, True]

        for variant, (input_hand, expected) in enumerate(zip(input_data, result_data), start=1):
            with self.subTest(f'variation #{variant}', input_hand=input_hand, expected=expected):
                actual_result = average_even_is_average_odd(input_hand)
                error_message = (f'Called average_even_is_average_odd({input_hand}). '
                                 f'The function returned {actual_result}, but '
                                 f'the hand {"does" if expected else "does not"} '
                                 f'yield the same odd-even average.')

                self.assertEqual(actual_result, expected, msg=error_message)

    @pytest.mark.task(taskno=7)
    def test_maybe_double_last(self):

        input_data = [(1, 2, 11), (5, 9, 11), (5, 9, 10), (1, 2, 3), (1, 11, 8)]
        result_data = [[1, 2, 22], [5, 9, 22], [5, 9, 10], [1, 2, 3], [1, 11, 8]]

        for variant, (hand, expected) in enumerate(zip(input_data, result_data), start=1):
            with self.subTest(f'variation #{variant}', hand=list(hand), expected=expected):
                actual_result = maybe_double_last(list(hand))
                error_message = (f'Called maybe_double_last({list(hand)}). '
                                 f'The function returned {actual_result}, but '
                                 f'the tests expected {expected} as the maybe-doubled version of {list(hand)}.')

                self.assertEqual(actual_result, expected, msg=error_message)
