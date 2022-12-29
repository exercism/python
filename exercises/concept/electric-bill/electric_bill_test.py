import unittest
import pytest
from electric_bill import (get_extra_hours,
                                 get_kW_amount,
                                 get_kwh_amount,
                                 get_efficiency,
                                 get_cost)


class ElecticBillTest(unittest.TestCase):

    @pytest.mark.task(taskno=1)
    def test_get_extra_hours(self):
        input_data = [25, 10, 5, 2, 1, 120, 21]
        output_data = [4, 13, 8, 5, 4, 3, 0]

        for variant, (input_data, output_data) in enumerate(zip(input_data, output_data), start=1):
            with self.subTest(f'variation #{variant}', input_data=input_data, output_data=output_data):
                error_msg=f'Expected: {output_data} but got a different amount.'
                self.assertEqual(get_extra_hours(input_data), output_data, msg=error_msg)

    @pytest.mark.task(taskno=2)
    def test_get_kW_amount(self):
        input_data = [1000, 2200, 2900, 900, 1160]
        output_data = [1, 2.2, 2.9, 0.9, 1.2]

        for variant, (input_data, output_data) in enumerate(zip(input_data, output_data), start=1):
            with self.subTest(f'variation #{variant}', input_data=input_data, output_data=output_data):
                error_msg=f'Expected: {output_data} but got a different amount.'
                self.assertEqual(get_kW_amount(input_data), output_data, msg=error_msg)

    @pytest.mark.task(taskno=3)
    def test_get_kwh_amount(self): 
        input_data = (5000000, 2141241, 43252135, 5324623462, 4321512)
        output_data = [1, 0, 12, 1479, 1]

        for variant, (input_data, output_data) in enumerate(zip(input_data, output_data), start=1):
            with self.subTest(f'variation #{variant}', input_data=input_data, output_data=output_data):
                error_msg=f'Expected: {output_data} but got a different amount.'
                self.assertEqual(get_kwh_amount(input_data), output_data, msg=error_msg)

    @pytest.mark.task(taskno=4)
    def test_get_efficiency(self): 
        input_data = [80.0, 99.99, 0.8, 40.0]
        output_data = [0.8, 0.9999, 0.008, 0.4]

        for variant, (input_data, output_data) in enumerate(zip(input_data, output_data), start=1):
            with self.subTest(f'variation #{variant}', input_data=input_data, output_data=output_data):
                error_msg=f'Expected: {output_data} but got a different value.'
                self.assertAlmostEqual(get_efficiency(input_data), output_data, msg=error_msg)

    @pytest.mark.task(taskno=5)
    def test_get_cost(self):
        input_data = ((5000000, 80.0, 0.25), (2141241, 99.99, 2), (43252135, 0.8, 4), (4321512, 40.0, 2))
        output_data = (0.3125, 0, 6000, 5)
        
        for variant, (input_data, output_data) in enumerate(zip(input_data, output_data), start=1):
            with self.subTest(f'variation #{variant}', input_data=input_data, output_data=output_data):
                error_msg=f'Expected: {output_data} but got a different value.'
                self.assertEqual(get_cost(*input_data), output_data, msg=error_msg)
