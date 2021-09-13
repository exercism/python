import unittest
import pytest
from lasagna import (
                    EXPECTED_BAKE_TIME,
                    bake_time_remaining,
                    preparation_time_in_minutes,
                    elapsed_time_in_minutes
                    )


class LasagnaTest(unittest.TestCase):

    @pytest.mark.task(taskno=1)
    def test_EXPECTED_BAKE_TIME(self):
        self.assertEqual(EXPECTED_BAKE_TIME, 40,
                         msg="Expected a constant of EXPECTED_BAKE_TIME with a value of 40.")

    @pytest.mark.task(taskno=2)
    def test_bake_time_remaining(self):
        input_data = [1, 2, 5, 10, 15, 23, 33, 39]
        result_data = [40 - item for item in input_data]
        number_of_variants = range(1, len(input_data) + 1)

        for variant, time, result in zip(number_of_variants, input_data, result_data):
            with self.subTest(f"variation #{variant}", time=time, result=result):
                self.assertEqual(bake_time_remaining(time), result,
                                 msg=f'Expected: {result} but the bake time remaining was calculated incorrectly.')

    @pytest.mark.task(taskno=3)
    def test_preparation_time_in_minutes(self):
        input_data = [1, 2, 5, 8, 11, 15]
        result_data = [item * 2 for item in input_data]
        number_of_variants = range(1, len(input_data) + 1)

        for variant, layers, time in zip(number_of_variants, input_data, result_data):
            with self.subTest(f"variation #{variant}", layers=layers, time=time):
                self.assertEqual(preparation_time_in_minutes(layers), time,
                                 msg=f'Expected: {time} minutes, but preparation time'
                                     f' was calculated incorrectly.')

    @pytest.mark.task(taskno=4)
    def test_elapsed_time_in_minutes(self):
        layer_data = (1, 2, 5, 8, 11, 15)
        time_data = (3, 7, 8, 4, 15, 20)
        result_data = [prep * 2 + elapsed for prep, elapsed in zip(layer_data, time_data)]
        number_of_variants = range(1, len(time_data) + 1)

        for variant, layers, time, total_time in zip(number_of_variants, layer_data, time_data, result_data):
            with self.subTest(f"variation #{variant}", layers=layers, time=time, total_time=total_time):
                failure_msg = f'Expected {time} minutes elapsed, but the timing was calculated incorrectly.'
                self.assertEqual(elapsed_time_in_minutes(layers, time), total_time, msg=failure_msg)

    @pytest.mark.task(taskno=5)
    def test_docstrings_were_written(self):
        functions = [bake_time_remaining, preparation_time_in_minutes, elapsed_time_in_minutes]
        number_of_variants = range(1, len(functions) + 1)

        for variant, function in zip(number_of_variants, functions):
            with self.subTest(f"variation #{variant}", function=function):
                failure_msg = msg = f'Expected a docstring for `{function.__name__}`, but received `None` instead.'
                self.assertIsNotNone(function.__doc__, msg=failure_msg)


if __name__ == "__main__":
    unittest.main()
