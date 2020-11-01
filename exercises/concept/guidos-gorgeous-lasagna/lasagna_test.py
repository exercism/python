import unittest
from lasagna import EXPECTED_BAKE_TIME, bake_time_remaining, preparation_time_in_minutes, elapsed_time_in_minutes


class LasagnaTest(unittest.TestCase):

    def test_EXPECTED_BAKE_TIME(self):
        self.assertEqual(EXPECTED_BAKE_TIME, 40)


    def bake_time_remaining(self):
        input_data = [1, 2, 5, 10, 15, 23, 33, 39 ]
        result_data = [40 - item for item in input_data]

        for time, result in zip(input_data, result_data):
            with self.subTest("bake time remaining variants", time=time, result=result):
                self.assertEqual(bake_time_remaining(time), result)

    def test_preparation_time_in_minutes(self):
        input_data = [1, 2, 5, 8, 11, 15]
        result_data = [item * 2 for item in input_data]

        for layers, time in zip(input_data, result_data):
            with self.subTest("preparation time calculation variants", layers=layers, time=time):
                self.assertEqual(preparation_time_in_minutes(layers), time)

    def test_elapsed_time_in_minutes(self):
        input_data = [1, 2, 5, 8, 11, 15]
        result_data = [item * 2 for item in input_data]

        for layers, time in zip(input_data, result_data):
            with self.subTest("bake time remaining variants", layers=layers, time=time):
                self.assertEqual(elapsed_time_in_minutes(8, 10), 26)

    def test_docstrings(self):
        self.assertIsNotNone(elapsed_time_in_minutes.__doc__)
        self.assertIsNotNone(preparation_time_in_minutes.__doc__)
        self.assertIsNotNone(elapsed_time_in_minutes.__doc__)
