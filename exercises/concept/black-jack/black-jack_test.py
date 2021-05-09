import unittest
from comparisons import *


class TestComparisons(unittest.TestCase):

    # Problem 1
    def test_number_of_card(self):
        input_data = [
            # input : card
            'K',
            'A'
        ]
        output_data = [10, "ace"]
        for input, output in zip(input_data, output_data):
            with self.subTest(input=input, output=output):
                self.assertEqual(number_of_card(input[0], input[1]), output)

    # Problem 2
    def test_number_of_ace(self):
        input_data = [
            # input : hand
            19,
            7
        ]
        output_data = [1, 11]
        for input, output in zip(input_data, output_data):
            with self.subTest(input=input, output=output):
                self.assertEqual(number_of_ace(input[0], input[1]), output)

    # Problem 3
    def test_blackjack(self):
        input_data = [
            # input : hand
            ['A', 'J'],
            [10, 9]
        ]
        output_data = [True, False]
        for input, output in zip(input_data, output_data):
            with self.subTest(input=input, output=output):
                self.assertEqual(blackjack(input[0], input[1]), output)