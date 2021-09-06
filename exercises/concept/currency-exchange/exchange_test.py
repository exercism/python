import unittest
import pytest
from exchange import (
    estimate_value,
    get_change,
    get_value,
    get_number_of_bills,
    exchangeable_value,
    unexchangeable_value
)


class TestNumbers(unittest.TestCase):

    @pytest.mark.task(taskno=1)
    def test_estimate_value(self):
        input_data = [(100000, 0.84), (700000, 10.1)]
        output_data = [119047, 69306]
        number_of_variants = range(1, len(input_data) + 1)

        for variant, input, output in zip(number_of_variants, input_data, output_data):
            with self.subTest(f"variation #{variant}", input=input, output=output):
                self.assertEqual(int(estimate_value(input[0], input[1])), output)

    @pytest.mark.task(taskno=2)
    def test_get_change(self):
        input_data = [(463000, 5000), (1250, 120), (15000, 1380)]
        output_data = [458000, 1130, 13620]
        number_of_variants = range(1, len(input_data) + 1)

        for variant, input, output in zip(number_of_variants, input_data, output_data):
            with self.subTest(f"variation #{variant}", input=input, output=output):
                self.assertEqual(get_change(input[0], input[1]), output)

    @pytest.mark.task(taskno=3)
    def test_get_value(self):
        input_data = [(10000, 128), (50, 360), (200, 200)]
        output_data = [1280000, 18000, 40000]
        number_of_variants = range(1, len(input_data) + 1)

        for variant, input, output in zip(number_of_variants, input_data, output_data):
            with self.subTest(f"variation #{variant}", input=input, output=output):
                self.assertEqual(get_value(input[0], input[1]), output)

    @pytest.mark.task(taskno=4)
    def test_get_number_of_bills(self):
        input_data = [(163270, 50000), (54361, 1000)]
        output_data = [3, 54]
        number_of_variants = range(1, len(input_data) + 1)

        for variant, input, output in zip(number_of_variants, input_data, output_data):
            with self.subTest(f"variation #{variant}", input=input, output=output):
                self.assertEqual(get_number_of_bills(input[0], input[1]), output)

    @pytest.mark.task(taskno=5)
    def test_exchangeable_value(self):
        input_data = [
            (100000, 10.61, 10, 1),
            (1500, 0.84, 25, 40),
            (470000, 1050, 30, 10000000000),
            (470000, 0.00000009, 30, 700),
            (425.33, 0.0009, 30, 700)
        ]
        output_data = [8568, 1400, 0, 4017094016600, 363300]
        number_of_variants = range(1, len(input_data) + 1)

        for variant, input, output in zip(number_of_variants, input_data, output_data):
            with self.subTest(f"variation #{variant}", input=input, output=output):
                self.assertEqual(exchangeable_value(input[0], input[1], input[2], input[3]), output)

    @pytest.mark.task(taskno=6)
    def test_unexchangeable_value(self):
        input_data = [
            (100000, 10.61, 10, 1),
            (1500, 0.84, 25, 40),
            (425.33, 0.0009, 30, 700),
            (12000, 0.0096, 10, 50)
        ]
        output_data = [0, 28, 229, 13]
        number_of_variants = range(1, len(input_data) + 1)

        for variant, input, output in zip(number_of_variants, input_data, output_data):
            with self.subTest(f"variation #{variant}", input=input, output=output):
                self.assertEqual(unexchangeable_value(input[0], input[1], input[2], input[3]), output)
