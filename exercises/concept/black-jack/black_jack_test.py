import unittest
import pytest
from black_jack import (
    number_of_card,
    number_of_ace,
    blackjack
)


class TestComparisons(unittest.TestCase):

    @pytest.mark.task(taskno=1)
    def test_number_of_card(self):
        input_data = ['K', 'A']
        output_data = [10, "ace"]
        number_of_variants = range(1, len(input_data) + 1)

        for variant, input, output in zip(number_of_variants, input_data, output_data):
            with self.subTest(f"variation #{variant}", input=input, output=output):
                self.assertEqual(number_of_card(input[0], input[1]), output,
                                 msg=f'Expected: {output} but the number of cards was calculated incorrectly.')

    @pytest.mark.task(taskno=2)
    def test_number_of_ace(self):
        input_data = [19, 7]
        output_data = [1, 11]
        number_of_variants = range(1, len(input_data) + 1)

        for variant, input, output in zip(number_of_variants, input_data, output_data):
            with self.subTest(f"variation #{variant}", input=input, output=output):
                self.assertEqual(number_of_ace(input[0], input[1]), output,
                                 msg=f'Expected: {output} but the number of Ace cards was calculated incorrectly.')

    @pytest.mark.task(taskno=3)
    def test_blackjack(self):
        input_data = [['A', 'J'], [10, 9]]
        output_data = [True, False]
        number_of_variants = range(1, len(input_data) + 1)

        for variant, input, output in zip(number_of_variants, input_data, output_data):
            with self.subTest(f"variation #{variant}", input=input, output=output):
                self.assertEqual(blackjack(input[0], input[1]), output,
                                 msg=f'Expected: {output} but the value returned was incorrect,')
