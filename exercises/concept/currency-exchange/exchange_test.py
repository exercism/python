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
        test_data = [(100000, 0.8), (700000, 10.0)]
        result_data = [125000, 70000]

        for variant, (params, expected) in enumerate(zip(test_data, result_data), start=1):
            budget, exchange_rate = params

            with self.subTest(f"variation #{variant}",
                              budget=budget,
                              exchange_rate=exchange_rate,
                              expected=expected):

                actual_result = exchange_money(*params)
                error_message = (f'Called exchange_money{budget, exchange_rate}. '
                                 f'The function returned {actual_result}, but '
                                 f'The tests expected {expected} when exchanging'
                                 f' {budget} at a rate of {exchange_rate}.')

                self.assertAlmostEqual(actual_result, expected, msg=error_message)

    @pytest.mark.task(taskno=2)
    def test_get_change(self):
        test_data = [(463000, 5000), (1250, 120), (15000, 1380)]
        result_data = [458000, 1130, 13620]

        for variant, (params, expected) in enumerate(zip(test_data, result_data), start=1):
            budget, exchanging_value = params

            with self.subTest(f"variation #{variant}",
                              budget=budget,
                              exchanging_value=exchanging_value,
                              expected=expected):

                actual_result = get_change(*params)
                error_message = (f'Called get_change{budget, exchanging_value}. '
                                 f'The function returned {actual_result}, but '
                                 f'The tests expected {expected} left in your budget.')

                self.assertAlmostEqual(actual_result, expected, msg=error_message)

    @pytest.mark.task(taskno=3)
    def test_get_value_of_bills(self):
        test_data = [(10000, 128), (50, 360), (200, 200)]
        result_data = [1280000, 18000, 40000]

        for variant, (params, expected) in enumerate(zip(test_data, result_data), start=1):
            denomination, number_of_bills = params

            with self.subTest(f"variation #{variant}",
                              denomination=denomination,
                              number_of_bills=number_of_bills,
                              expected=expected):

                actual_result = get_value_of_bills(*params)
                error_message = (f'Called get_value_of_bills{denomination, number_of_bills}. '
                                 f'The function returned {actual_result}, but '
                                 f'The tests expected {expected} for the bills value.')

                self.assertEqual(actual_result, expected, msg=error_message)

    @pytest.mark.task(taskno=4)
    def test_get_number_of_bills(self):
        test_data = [(163270, 50000), (54361, 1000)]
        result_data = [3, 54]

        for variant, (params, expected) in enumerate(zip(test_data, result_data), start=1):
            amount, denomination = params

            with self.subTest(f"variation #{variant}",
                              amount=amount,
                              denomination=denomination,
                              expected=expected):

                actual_result = get_number_of_bills(amount, denomination)
                error_message = (f'Called get_number_of_bills{amount, denomination}. '
                                 f'The function returned {actual_result} bills, but '
                                 f'The tests expected {expected} bills.')

                self.assertEqual(actual_result, expected, msg=error_message)

    @pytest.mark.task(taskno=5)
    def test_get_leftover_of_bills(self):
        test_data = [(10.1, 10), (654321.0, 5), (3.14, 2)]
        result_data = [0.1, 1.0, 1.14]

        for variant, (params, expected) in enumerate(zip(test_data, result_data), start=1):
            amount, denomination = params

            with self.subTest(f"variation #{variant}",
                              amount=amount,
                              denomination=denomination,
                              expected=expected):

                actual_result = get_leftover_of_bills(*params)
                error_message = (f'Called get_leftover_of_bills{amount, denomination}. '
                                 f'The function returned {actual_result}, but '
                                 f'The tests expected {expected} as the leftover amount.')

                self.assertAlmostEqual(actual_result, expected, msg=error_message)

    @pytest.mark.task(taskno=6)
    def test_exchangeable_value(self):
        test_data = [(100000, 10.61, 10, 1),
                     (1500, 0.84, 25, 40),
                     (470000, 1050, 30, 10000000000),
                     (470000, 0.00000009, 30, 700),
                     (425.33, 0.0009, 30, 700)]

        result_data = [8568, 1400, 0, 4017094016600, 363300]

        for variant, (params, expected) in enumerate(zip(test_data, result_data), start=1):
            budget, exchange_rate, spread, denomination = params

            with self.subTest(f"variation #{variant}",
                              budget=budget,
                              exchange_rate=exchange_rate,
                              spread=spread,
                              denomination=denomination,
                              expected=expected):

                actual_result = exchangeable_value(budget, exchange_rate, spread, denomination)
                error_message = (f'Called exchangeable_value{budget, exchange_rate, spread, denomination}. '
                                 f'The function returned {actual_result}, but '
                                 f'The tests expected {expected} as the maximum '
                                 f'value of the new currency .')

                self.assertEqual(actual_result, expected, msg=error_message)
