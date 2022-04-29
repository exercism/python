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

        input_vars = [0, 1, 10, 27, 99, 666]

        results = [[0, 1, 2], [1, 2, 3],
                   [10, 11, 12], [27, 28, 29],
                   [99, 100, 101], [666, 667, 668]]

        for variant, (number, rounds) in enumerate(zip(input_vars, results), start=1):
            error_message = f'Expected rounds {rounds} given the current round {number}.'
            with self.subTest(f'variation #{variant}', input=number, output=rounds):
                self.assertEqual(rounds, get_rounds(number), msg=error_message)

    @pytest.mark.task(taskno=2)
    def test_concatenate_rounds(self):

        input_vars = [([], []), ([0, 1], []), ([], [1, 2]),
                      ([1], [2]), ([27, 28, 29], [35, 36]),
                      ([1, 2, 3], [4, 5, 6])]

        results = [[], [0, 1], [1, 2], [1, 2],
                   [27, 28, 29, 35, 36],
                   [1, 2, 3, 4, 5, 6]]

        for variant, ((rounds_1, rounds_2), rounds) in enumerate(zip(input_vars, results), start=1):
            error_message = f'Expected {rounds} as the concatenation of {rounds_1} and {rounds_2}.'
            with self.subTest(f'variation #{variant}', input=(rounds_1, rounds_2), output=rounds):
                self.assertEqual(rounds, concatenate_rounds(rounds_1, rounds_2), msg=error_message)

    @pytest.mark.task(taskno=3)
    def test_list_contains_round(self):

        input_vars = [([], 1), ([1, 2, 3], 0), ([27, 28, 29, 35, 36], 30),
                      ([1], 1), ([1, 2, 3], 1), ([27, 28, 29, 35, 36], 29)]

        results = [False, False, False, True, True, True]

        for variant, ((rounds, round_number), contains) in enumerate(zip(input_vars, results), start=1):
            error_message = f'Round {round_number} {"is" if contains else "is not"} in {rounds}.'
            with self.subTest(f'variation #{variant}', input=(rounds, round_number), output=contains):
                self.assertEqual(contains, list_contains_round(rounds, round_number), msg=error_message)

    @pytest.mark.task(taskno=4)
    def test_card_average(self):

        input_vars = [[1], [5, 6, 7], [1, 2, 3, 4], [1, 10, 100]]

        results = [1.0, 6.0, 2.5, 37.0]

        for variant, (hand, average) in enumerate(zip(input_vars, results), start=1):
            error_message = f'Expected {average} as the average of {hand}.'
            with self.subTest(f'variation #{variant}', input=hand, output=average):
                self.assertEqual(average, card_average(hand), msg=error_message)

    @pytest.mark.task(taskno=5)
    def test_approx_average_is_average(self):

        input_vars = [[0, 1, 5], [3, 6, 9, 12, 150], [1, 2, 3, 5, 9],
                      [2, 3, 4, 7, 8], [1, 2, 3], [2, 3, 4],
                      [2, 3, 4, 8, 8], [1, 2, 4, 5, 8]]

        results = [False, False, False, False, True, True, True, True]

        for variant, (hand, same) in enumerate(zip(input_vars, results), start=1):
            error_message = f'Hand {hand} {"does" if same else "does not"} yield the same approximate average.'
            with self.subTest(f'variation #{variant}', input=hand, output=same):
                self.assertEqual(same, approx_average_is_average(hand), msg=error_message)

    @pytest.mark.task(taskno=6)
    def test_average_even_is_average_odd(self):

        input_vars = [[5, 6, 8], [1, 2, 3, 4], [1, 2, 3], [5, 6, 7], [1, 3, 5, 7, 9]]

        results = [False, False, True, True, True]

        for variant, (hand, same) in enumerate(zip(input_vars, results), start=1):
            error_message = f'Hand {hand} {"does" if same else "does not"} yield the same odd-even average.'
            with self.subTest(f'variation #{variant}', input=hand, output=same):
                self.assertEqual(same, average_even_is_average_odd(hand), msg=error_message)

    @pytest.mark.task(taskno=7)
    def test_maybe_double_last(self):

        input_vars = [[1, 2, 11], [5, 9, 11], [5, 9, 10], [1, 2, 3]]

        results = [[1, 2, 22], [5, 9, 22], [5, 9, 10], [1, 2, 3]]

        for variant, (hand, doubled_hand) in enumerate(zip(input_vars, results), start=1):
            error_message = f'Expected {doubled_hand} as the maybe-doubled version of {hand}.'
            with self.subTest(f'variation #{variant}', input=hand, output=doubled_hand):
                self.assertEqual(doubled_hand, maybe_double_last(hand), msg=error_message)
