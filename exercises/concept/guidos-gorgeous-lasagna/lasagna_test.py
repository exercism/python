import unittest
import pytest

# For this first exercise, it is really important to be clear about how we are importing names for tests.
# To that end, we are putting a try/catch around imports and throwing specific messages to help students
# decode that they need to create and title their constants and functions in a specific way.
try:
    from lasagna import (EXPECTED_BAKE_TIME,
                         bake_time_remaining,
                         preparation_time_in_minutes,
                         elapsed_time_in_minutes)

# Here, we are separating the constant import errors from the function name import errors
except ImportError as import_fail:
    message = import_fail.args[0].split('(', maxsplit=1)
    item_name = import_fail.args[0].split()[3]

    if 'EXPECTED_BAKE_TIME' in item_name:
        # pylint: disable=raise-missing-from
        raise ImportError(f'\n\nMISSING CONSTANT --> \nWe can not find or import the constant {item_name} in your'
                          " 'lasagna.py' file.\nDid you misname or forget to define it?") from None
    else:
        item_name = item_name[:-1] + "()'"
        # pylint: disable=raise-missing-from
        raise ImportError("\n\nMISSING FUNCTION --> In your 'lasagna.py' file, we can not find or import the"
                          f' function named {item_name}. \nDid you misname or forget to define it?') from None


# Here begins the formal test cases for the exercise.
class LasagnaTest(unittest.TestCase):

    @pytest.mark.task(taskno=1)
    def test_EXPECTED_BAKE_TIME(self):
        failure_msg = 'Expected a constant of EXPECTED_BAKE_TIME with a value of 40.'
        self.assertEqual(EXPECTED_BAKE_TIME, 40, msg=failure_msg)

    @pytest.mark.task(taskno=2)
    def test_bake_time_remaining(self):
        input_data = [1, 2, 5, 10, 15, 23, 33, 39]
        result_data = [39, 38, 35, 30, 25, 17, 7, 1]

        for variant, (time, expected) in enumerate(zip(input_data, result_data), start=1):
            with self.subTest(f'variation #{variant}', time=time, expected=expected):
                actual_result = bake_time_remaining(time)
                failure_msg = (f'Called bake_time_remaining({time}). ' 
                               f'The function returned {actual_result}, but the tests '
                               f'expected {expected} as the remaining bake time.')

                self.assertEqual(actual_result, expected, msg=failure_msg)

    @pytest.mark.task(taskno=3)
    def test_preparation_time_in_minutes(self):
        input_data = [1, 2, 5, 8, 11, 15]
        result_data = [2, 4, 10, 16, 22, 30]

        for variant, (layers, expected) in enumerate(zip(input_data, result_data), start=1):
            with self.subTest(f'variation #{variant}', layers=layers, expected=expected):
                actual_result = preparation_time_in_minutes(layers)
                failure_msg = (f'Called preparation_time_in_minutes({layers}). '
                               f'The function returned {actual_result}, but the tests '
                               f'expected {expected} as the preparation time.')

                self.assertEqual(actual_result, expected, msg=failure_msg)

    @pytest.mark.task(taskno=4)
    def test_elapsed_time_in_minutes(self):
        layer_data = (1, 2, 5, 8, 11, 15)
        time_data = (3, 7, 8, 4, 15, 20)
        result_data = [5, 11, 18, 20, 37, 50]

        for variant, (layers, time, expected) in enumerate(zip(layer_data, time_data, result_data), start=1):
            with self.subTest(f'variation #{variant}', layers=layers, time=time, expected=expected):
                actual_result = elapsed_time_in_minutes(layers, time)
                failure_msg = (f'Called elapsed_time_in_minutes({layers}, {time}). '
                               f'The function returned {actual_result}, but the tests '
                               f'expected {expected} as the elapsed time.')

                self.assertEqual(actual_result, expected, msg=failure_msg)

    @pytest.mark.task(taskno=5)
    def test_docstrings_were_written(self):
        """Validate function.__doc__ exists for each function.
        Check the attribute dictionary of each listed function
        for the presence of a __doc__ key.

        :return: unexpectedly None error when __doc__ key is missing.
        """
        functions = [bake_time_remaining, preparation_time_in_minutes, elapsed_time_in_minutes]

        for variant, function in enumerate(functions, start=1):
            with self.subTest(f'variation #{variant}', function=function):
                actual_result = function.__doc__
                failure_msg = (f'Called {function.__name__}.__doc__. {actual_result} was returned, '
                               f'but the tests expected a docstring for the {function.__name__} function.')

                # Check that the __doc__ key is populated for the function.
                self.assertIsNotNone(actual_result, msg=failure_msg)
