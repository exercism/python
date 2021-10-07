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
        data = [
            (0, [0, 1, 2]),
            (1, [1, 2, 3]),
            (10, [10, 11, 12]),
            (27, [27, 28, 29]),
            (99, [99, 100, 101]),
            (666, [666, 667, 668]),
        ]

        for variant, (number, rounds) in enumerate(data, start=1):
            with self.subTest(f'variation #{variant}', input=number, output=rounds):
                error_message = f'Expected rounds {rounds} given the current round {number}.'
                self.assertEqual(rounds, get_rounds(number), msg=error_message)

    @pytest.mark.task(taskno=2)
    def test_concatenate_rounds(self):
        data = [
            (([], []), []),
            (([0, 1], []), [0, 1]),
            (([], [1, 2]), [1, 2]),
            (([1], [2]), [1, 2]),
            (([27, 28, 29], [35, 36]), [27, 28, 29, 35, 36]),
            (([1, 2, 3], [4, 5, 6]), [1, 2, 3, 4, 5, 6]),
        ]

        for variant, ((rounds_1, rounds_2), rounds) in enumerate(data, start=1):
            with self.subTest(f'variation #{variant}', input=(rounds_1, rounds_2), output=rounds):
                error_message = f'Expected {rounds} as the concatenation of {rounds_1} and {rounds_2}.'
                self.assertEqual(rounds, concatenate_rounds(rounds_1, rounds_2), msg=error_message)

    @pytest.mark.task(taskno=3)
    def test_list_contains_round(self):
        data = [
            (([], 1), False),
            (([1, 2, 3], 0), False),
            (([27, 28, 29, 35, 36], 30), False),
            (([1], 1), True),
            (([1, 2, 3], 1), True),
            (([27, 28, 29, 35, 36], 29), True),
        ]

        for variant, ((rounds, round_number), contains) in enumerate(data, start=1):
            with self.subTest(f'variation #{variant}', input=(rounds, round_number), output=contains):
                error_message = f'Round {round_number} {"is" if contains else "is not"} in {rounds}.'
                self.assertEqual(contains,list_contains_round(rounds, round_number),msg=error_message)

    @pytest.mark.task(taskno=4)
    def test_card_average(self):
        data = [
            ([1], 1.0),
            ([5, 6, 7], 6.0),
            ([1, 2, 3, 4], 2.5),
            ([1, 10, 100], 37.0),
        ]

        for variant, (hand, average) in enumerate(data, start=1):
            with self.subTest(f'variation #{variant}', input=hand, output=average):
                msg=f'Expected {average} as the average of {hand}.'
                self.assertEqual(average,card_average(hand),msg=msg)

    @pytest.mark.task(taskno=5)
    def test_approx_average_is_average(self):
        data = [
            ([0, 1, 5], False),
            ([3, 6, 9, 12, 150], False),
            ([1, 2, 3, 5, 9], False),
            ([2, 3, 4, 7, 8], False),
            ([1, 2, 3], True),
            ([2, 3, 4], True),
            ([2, 3, 4, 8, 8], True),
            ([1, 2, 4, 5, 8], True),
        ]

        for variant, (hand, same) in enumerate(data, start=1):
            with self.subTest(f'variation #{variant}', input=hand, output=same):
                error_message = f'Hand {hand} {"does" if same else "does not"} yield the same approximate average.'
                self.assertEqual(same, approx_average_is_average(hand), msg=error_message)

    @pytest.mark.task(taskno=6)
    def test_average_even_is_average_odd(self):
        data = [
            ([5, 6, 8], False),
            ([1, 2, 3, 4], False),
            ([1, 2, 3], True),
            ([5, 6, 7], True),
        ]

        for variant, (hand, same) in enumerate(data, start=1):
            with self.subTest(f'variation #{variant}', input=hand, output=same):
                msg=f'Hand {hand} {"does" if same else "does not"} yield the same odd-even average.'
                self.assertEqual(same, average_even_is_average_odd(hand),msg=msg)

    @pytest.mark.task(taskno=7)
    def test_maybe_double_last(self):
        data = [
            ([1, 2, 11], [1, 2, 22]),
            ([5, 9, 11], [5, 9, 22]),
            ([5, 9, 10], [5, 9, 10]),
            ([1, 2, 3], [1, 2, 3]),
        ]

        for variant, (hand, doubled_hand) in enumerate(data, start=1):
            with self.subTest(f'variation #{variant}', input=hand, output=doubled_hand):
                msg=f'Expected {doubled_hand} as the maybe-doubled version of {hand}.'
                self.assertEqual(doubled_hand,maybe_double_last(hand),msg=msg)
