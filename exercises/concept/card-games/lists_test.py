import unittest
import pytest
import random
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
    def test_round_number_zero(self):
        round_number = 0
        want = [0, 1, 2]

        self.assertEqual(want, get_rounds(round_number),
            msg=f'Expected {want} but got an incorrect result.'
        )

    @pytest.mark.task(taskno=1)
    def test_random_int_for_round_number(self):
        round_number = random.randint(0, 100)
        want = [round_number + i for i in range(3)]

        self.assertEqual(get_rounds(round_number), want,
            msg=f'Expected {want} but got an incorrect result.'
        )

    @pytest.mark.task(taskno=2)
    def test_concatenate_empty_rounds(self):
        rounds_1 = []
        rounds_2 = []
        want = []

        self.assertEqual(concatenate_rounds(rounds_1, rounds_2), want,
            msg=f'Expected {want} but got an incorrect result.'
        )

    @pytest.mark.task(taskno=2)
    def test_concatenate_other_rounds(self):
        rounds_1 = [1, 2, 3]
        rounds_2 = [4, 5, 6]
        want = [1, 2, 3, 4, 5, 6]

        self.assertEqual(concatenate_rounds(rounds_1, rounds_2), want,
            msg=f'Expected {want} but got an incorrect result.'
            )

    @pytest.mark.task(taskno=3)
    def test_contains_empty_rounds(self):
        rounds = []
        round_number = 1
        want = False

        self.assertEqual(list_contains_round(rounds, round_number), want,
            msg=f'Expected {want} but got an incorrect result.'
        )

    @pytest.mark.task(taskno=3)
    def test_contains_other_rounds_true(self):
        rounds = [1, 2, 3]
        round_number = 2
        want = True

        self.assertEqual(list_contains_round(rounds, round_number), want,
            msg=f'Expected {want} but got an incorrect result.'
        )

    @pytest.mark.task(taskno=3)
    def test_contains_other_rounds_false(self):
        rounds = [1, 2, 3]
        round_number = 0
        want = False

        self.assertEqual(list_contains_round(rounds, round_number), want,
            msg=f'Expected {want} but got an incorrect result.'
        )

    @pytest.mark.task(taskno=4)
    def test_card_average_other(self):
        hand = [1, 2, 3, 4]
        want = 2.5

        self.assertEqual(card_average(hand), want,
            msg=f'Expected {want} but got an incorrect result.'
        )

    @pytest.mark.task(taskno=5)
    def test_instructions_example_3(self):
        hand = [1, 2, 3, 5, 9]
        want = False

        self.assertEqual(approx_average_is_average(hand), want,
            msg=f'Expected {want} but got an incorrect result.'
        )

    @pytest.mark.task(taskno=5)
    def test_approx_average_median_true(self):
        hand = [1, 2, 4, 5, 8]
        want = True

        self.assertEqual(approx_average_is_average(hand), want,
            msg=f'Expected {want} but got an incorrect result.'
        )

    @pytest.mark.task(taskno=5)
    def test_approx_average_other_true(self):
        hand = [2, 3, 4]
        want = True

        self.assertEqual(approx_average_is_average(hand), want,
            msg=f'Expected {want} but got an incorrect result.'
        )

    @pytest.mark.task(taskno=5)
    def test_approx_average_other_false(self):
        hand = [2, 3, 4, 7, 8]
        want= False

        self.assertEqual(approx_average_is_average(hand), want,
            msg=f'Expected {want} but got an incorrect result.'
        )

    @pytest.mark.task(taskno=6)
    def test_avg_even_odd_other_true(self):
        hand = [5, 6, 7]
        want= True

        self.assertEqual(average_even_is_average_odd(hand), want,
            msg=f'Expected {want} but got an incorrect result.'
        )

    @pytest.mark.task(taskno=6)
    def test_avg_even_odd_other_false(self):
        hand = [5, 6, 8]
        want = False

        self.assertEqual(average_even_is_average_odd(hand), want,
            msg=f'Expected {want} but got an incorrect result.'
        )

    @pytest.mark.task(taskno=7)
    def test_maybe_double_last_other_doubles(self):
        hand = [1, 2, 11]
        want = [1, 2, 22]

        self.assertEqual(maybe_double_last(hand), want,
            msg=f'Expected {want} but got an incorrect result.'
        )

    @pytest.mark.task(taskno=7)
    def test_maybe_double_last_other_no_change(self):
        hand = [1, 2, 3]
        want = [1, 2, 3]

        self.assertEqual(maybe_double_last(hand), want,
            msg=f'Expected {want} but got an incorrect result.'
        )
