import unittest
import pytest
from black_jack import (
    value_of_card,
    value_of_ace,
    is_blackjack,
    can_split_pairs,
    can_double_down
)


class BlackJackTest(unittest.TestCase):

    @pytest.mark.task(taskno=1)
    def test_value_of_card(self):
        data = [
            ('2', 2),
            ('5', 5),
            ('8', 8),
            ('10', 10),
            ('J', 10),
            ('Q', 10),
            ('K', 10),
        ]

        for variant, (card, value) in enumerate(data, 1):
            with self.subTest(f'variation #{variant}', input=card, output=value):
                self.assertEqual(
                    value,
                    value_of_card(card),
                    msg=f'Expected {value} as the value of {card}.'
                )

    @pytest.mark.task(taskno=2)
    def test_value_of_ace(self):
        data = [
            (2, 11),
            (5, 11),
            (7, 11),
            (9, 11),
            (10, 11),
            (11, 1),
            (12, 1),
            (15, 1),
            (19, 1),
            (20, 1),
        ]

        for variant, (hand_value, ace_value) in enumerate(data, 1):
            with self.subTest(f'variation #{variant}', input=hand_value, output=ace_value):
                self.assertEqual(
                    ace_value,
                    value_of_ace(hand_value),
                    msg=f'Expected {ace_value} as the value of ace when the hand is worth {hand_value}.'
                )

    @pytest.mark.task(taskno=3)
    def test_is_blackjack(self):
        data = [
            (['A', 'K'], True),
            (['10', 'A'], True),
            (['10', '9'], False),
            (['A', 'A'], False),
        ]

        for variant, (hand, blackjack) in enumerate(data, 1):
            with self.subTest(f'variation #{variant}', input=hand, output=blackjack):
                self.assertEqual(
                    blackjack,
                    is_blackjack(hand),
                    msg=f'Hand {hand} {"is" if blackjack else "is not"} a blackjack.'
                )

    @pytest.mark.task(taskno=4)
    def test_can_split_pairs(self):
        data = [
            (['Q', 'K'], True),
            (['6', '6'], True),
            (['A', 'A'], True),
            (['10', 'A'], False),
            (['10', '9'], False),
        ]

        for variant, (hand, split_pairs) in enumerate(data, 1):
            with self.subTest(f'variation #{variant}', input=hand, output=split_pairs):
                self.assertEqual(
                    split_pairs,
                    can_split_pairs(hand),
                    msg=f'Hand {hand} {"can" if split_pairs else "cannot"} be split into pairs.'
                )

    @pytest.mark.task(taskno=5)
    def test_can_double_down(self):
        data = [
            (['A', '9'], True),
            (['K', 'A'], True),
            (['4', '5'], True),
            (['A', 'A'], False),
            (['10', '2'], False),
            (['10', '9'], False),
        ]

        for variant, (hand, double_down) in enumerate(data, 1):
            with self.subTest(f'variation #{variant}', input=hand, output=double_down):
                self.assertEqual(
                    double_down,
                    can_double_down(hand),
                    msg=f'Hand {hand} {"can" if double_down else "cannot"} be doubled down.'
                )
