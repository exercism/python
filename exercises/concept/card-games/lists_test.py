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


class TestToRounds(unittest.TestCase):

    @pytest.mark.task(taskno=1)
    def test_instructions_example(self):
        round_number = 27
        want = [27, 28, 29]
        got = get_rounds(round_number)

        self.assertEqual(
            want,
            got,
            msg=f'Expected {want} but got an incorrect result: {got!r}'
        )

    @pytest.mark.task(taskno=1)
    def test_zero(self):
        round_number = 0
        want = [0, 1, 2]
        got = get_rounds(round_number)

        self.assertEqual(
            want,
            got,
            msg=f'Expected {want} but got an incorrect result: {got!r}'
        )

    @pytest.mark.task(taskno=1)
    def test_random_int(self):
        round_number = random.randint(0, 100)
        want = [round_number + i for i in range(3)]
        got = get_rounds(round_number)

        self.assertEqual(
            want,
            got,
            msg=f'Expected {want} but got an incorrect result: {got!r}'
        )


class TestConcatenateRounds(unittest.TestCase):

    @pytest.mark.task(taskno=2)
    def test_empty(self):
        rounds_1 = []
        rounds_2 = []
        want = []

        self.assertEqual(concatenate_rounds(rounds_1, rounds_2),
            want,
            msg=f'Expected {want} but got an incorrect result.'
            )

    @pytest.mark.task(taskno=2)
    def test_other(self):
        rounds_1 = [1, 2, 3]
        rounds_2 = [4, 5, 6]
        want = [1, 2, 3, 4, 5, 6]

        self.assertEqual(concatenate_rounds(rounds_1, rounds_2),
                         want,
                         msg=f'Expected {want} but got an incorrect result.'
                         )


class TestListContainsRound(unittest.TestCase):

    @pytest.mark.task(taskno=3)
    def test_instructions_example_1(self):
        rounds = [27, 28, 29, 35, 36]
        round_number = 29
        want = True
        got = list_contains_round(rounds, round_number)

        self.assertEqual(
            want,
            got,
            msg=f'Expected {want} but got an incorrect result: {got!r}'
        )

    @pytest.mark.task(taskno=3)
    def test_instructions_example_2(self):
        rounds = [27, 28, 29, 35, 36]
        round_number = 30
        want = False
        got = list_contains_round(rounds, round_number)

        self.assertEqual(
            want,
            got,
            msg=f'Expected {want} but got an incorrect result: {got!r}'
        )

    @pytest.mark.task(taskno=3)
    def test_empty(self):
        rounds = []
        round_number = 1
        want = False
        got = list_contains_round(rounds, round_number)

        self.assertEqual(
            want,
            got,
            msg=f'Expected {want} but got an incorrect result: {got!r}'
        )

    @pytest.mark.task(taskno=3)
    def test_other_true(self):
        rounds = [1, 2, 3]
        round_number = 2
        want = True
        got = list_contains_round(rounds, round_number)

        self.assertEqual(
            want,
            got,
            msg=f'Expected {want} but got an incorrect result: {got!r}'
        )

    @pytest.mark.task(taskno=3)
    def test_other_false(self):
        rounds = [1, 2, 3]
        round_number = 0
        want = False
        got = list_contains_round(rounds, round_number)

        self.assertEqual(
            want,
            got,
            msg=f'Expected {want} but got an incorrect result: {got!r}'
        )


class TestCardAverage(unittest.TestCase):

    @pytest.mark.task(taskno=4)
    def test_instructions_example(self):
        hand = [5, 6, 7]
        want = 6.0
        got = card_average(hand)

        self.assertEqual(
            want,
            got,
            msg=f'Expected {want} but got an incorrect result: {got!r}'
        )

    @pytest.mark.task(taskno=4)
    def test_other(self):
        hand = [1, 2, 3, 4]
        want = 2.5
        got = card_average(hand)

        self.assertEqual(
            want,
            got,
            msg=f'Expected {want} but got an incorrect result: {got!r}'
        )


class TestApproxAverageIsAverage(unittest.TestCase):

    @pytest.mark.task(taskno=5)
    def test_instructions_example_1(self):
        hand = [1, 2, 3]
        want = True
        got = approx_average_is_average(hand)

        self.assertEqual(
            want,
            got,
            msg=f'Expected {want} but got an incorrect result: {got!r}'
        )

    @pytest.mark.task(taskno=5)
    def test_instructions_example_2(self):
        hand = [2, 3, 4, 8, 8]
        want = True
        got = approx_average_is_average(hand)

        self.assertEqual(
            want,
            got,
            msg=f'Expected {want} but got an incorrect result: {got!r}'
        )

    @pytest.mark.task(taskno=5)
    def test_instructions_example_3(self):
        hand = [1, 2, 3, 5, 9]
        want = False
        got = approx_average_is_average(hand)

        self.assertEqual(
            want,
            got,
            msg=f'Expected {want} but got an incorrect result: {got!r}'
        )

    @pytest.mark.task(taskno=5)
    def test_other_true(self):
        hand = [2, 3, 4]
        want = True
        got = approx_average_is_average(hand)

        self.assertEqual(
            want,
            got,
            msg=f'Expected {want} but got an incorrect result: {got!r}'
        )

    @pytest.mark.task(taskno=5)
    def test_other_false(self):
        hand = [2, 3, 4, 7, 8]
        want = False
        got = approx_average_is_average(hand)

        self.assertEqual(
            want,
            got,
            msg=f'Expected {want} but got an incorrect result: {got!r}'
        )


class TestAverageEvenIsAverageOdd(unittest.TestCase):

    @pytest.mark.task(taskno=6)
    def test_instructions_example_1(self):
        hand = [1, 2, 3]
        want = True
        got = average_even_is_average_odd(hand)

        self.assertEqual(
            want,
            got,
            msg=f'Expected {want} but got an incorrect result: {got!r}'
        )

    @pytest.mark.task(taskno=6)
    def test_instructions_example_2(self):
        hand = [1, 2, 3, 4]
        want = False
        got = average_even_is_average_odd(hand)

        self.assertEqual(
            want,
            got,
            msg=f'Expected {want} but got an incorrect result: {got!r}'
        )

    @pytest.mark.task(taskno=6)
    def test_other_true(self):
        hand = [5, 6, 7]
        want = True
        got = average_even_is_average_odd(hand)

        self.assertEqual(
            want,
            got,
            msg=f'Expected {want} but got an incorrect result: {got!r}'
        )

    @pytest.mark.task(taskno=6)
    def test_other_false(self):
        hand = [5, 6, 8]
        want = False
        got = average_even_is_average_odd(hand)

        self.assertEqual(
            want,
            got,
            msg=f'Expected {want} but got an incorrect result: {got!r}'
        )


class TestMaybeDoubleLast(unittest.TestCase):

    @pytest.mark.task(taskno=7)
    def test_instructions_example_1(self):
        hand = [5, 9, 11]
        want = [5, 9, 22]
        got = maybe_double_last(hand)

        self.assertEqual(
            want,
            got,
            msg=f'Expected {want} but got an incorrect result: {got!r}'
        )

    @pytest.mark.task(taskno=7)
    def test_instructions_example_2(self):
        hand = [5, 9, 10]
        want = [5, 9, 10]
        got = maybe_double_last(hand)

        self.assertEqual(
            want,
            got,
            msg=f'Expected {want} but got an incorrect result: {got!r}'
        )

    @pytest.mark.task(taskno=7)
    def test_other_doubles(self):
        hand = [1, 2, 11]
        want = [1, 2, 22]
        got = maybe_double_last(hand)

        self.assertEqual(
            want,
            got,
            msg=f'Expected {want} but got an incorrect result: {got!r}'
        )

    @pytest.mark.task(taskno=7)
    def test_other_no_change(self):
        hand = [1, 2, 3]
        want = [1, 2, 3]
        got = maybe_double_last(hand)

        self.assertEqual(
            want,
            got,
            msg=f'Expected {want} but got an incorrect result: {got!r}'
        )
