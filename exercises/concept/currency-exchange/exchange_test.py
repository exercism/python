import unittest
import pytest
from exchange import (
    exchange_money,
    get_change,
    get_value_of_bills,
    get_number_of_bills,
    get_leftover_of_bills,
    exchangeable_value)


class CurrencyExchangeTest(unittest.TestCase):

    @pytest.mark.task(taskno=1)
    def test_exchange_money(self):
        input_data = [(100000, 0.8), (700000, 10.0)]
        output_data = [125000, 70000]

        for variant, (input_data, output_data) in enumerate(zip(input_data, output_data), start=1):
            with self.subTest(f"variation #{variant}", input_data=input_data, output_data=output_data):
                self.assertAlmostEqual(exchange_money(input_data[0], input_data[1]), output_data)

    @pytest.mark.task(taskno=2)
    def test_get_change(self):
        input_data = [(463000, 5000), (1250, 120), (15000, 1380)]
        output_data = [458000, 1130, 13620]

        for variant, (input_data, output_data) in enumerate(zip(input_data, output_data), start=1):
            with self.subTest(f"variation #{variant}", input_data=input_data, output_data=output_data):
                self.assertAlmostEqual(get_change(input_data[0], input_data[1]), output_data)

    @pytest.mark.task(taskno=3)
    def test_get_value_of_bills(self):
        input_data = [(10000, 128), (50, 360), (200, 200)]
        output_data = [1280000, 18000, 40000]

        for variant, (input_data, output_data) in enumerate(zip(input_data, output_data), start=1):
            with self.subTest(f"variation #{variant}", input_data=input_data, output_data=output_data):
                self.assertEqual(get_value_of_bills(input_data[0], input_data[1]), output_data)

    @pytest.mark.task(taskno=4)
    def test_get_number_of_bills(self):
        input_data = [(163270, 50000), (54361, 1000)]
        output_data = [3, 54]

        for variant, (input_data, output_data) in enumerate(zip(input_data, output_data), start=1):
            with self.subTest(f"variation #{variant}", input_data=input_data, output_data=output_data):
                self.assertEqual(get_number_of_bills(input_data[0], input_data[1]), output_data)

    @pytest.mark.task(taskno=5)
    def test_get_leftover_of_bills(self):
        input_data = [(10.1, 10), (654321.0, 5), (3.14, 2)]
        output_data = [0.1, 1.0, 1.14]

        for variant, (input_data, output_data) in enumerate(zip(input_data, output_data), start=1):
            with self.subTest(f"variation #{variant}", input_data=input_data, output_data=output_data):
                self.assertAlmostEqual(get_leftover_of_bills(input_data[0], input_data[1]), output_data)

    @pytest.mark.task(taskno=6)
    def test_exchangeable_value(self):
        inputs = [
            (100000, 10.61, 10, 1),
            (1500, 0.84, 25, 40),
            (470000, 1050, 30, 10000000000),
            (470000, 0.00000009, 30, 700),
            (425.33, 0.0009, 30, 700)]

        output_data = [8568, 1400, 0, 4017094016600, 363300]

        for variant, (inputs, output_data) in enumerate(zip(inputs, output_data), start=1):
            with self.subTest(f"variation #{variant}", inputs=inputs, output_data=output_data):
                self.assertEqual(exchangeable_value(inputs[0], inputs[1], inputs[2], inputs[3]), output_data)
