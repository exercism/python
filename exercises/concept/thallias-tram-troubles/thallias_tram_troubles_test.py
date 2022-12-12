import unittest
import pytest

from thallias_tram_troubles import time_table_for_a_weekday

class ThalliasTramTroublesTest(unittest.TestCase):

    @pytest.mark.task(taskno=1)
    def test_time_table_for_a_weekday(self):
        input_data = (([["7:00", "12:00", "19:00"], ("7:00", "13:00", "17:00"), ["7:00", "12:00", "17:00"], ("10:00", "12:00", "17:00"), ("7:00", "15:00", "17:00"), ["7:00", "12:00"], ["7:00", "12:00"]],2),
        ((("5:00", "7:00", "12:00", "15:00", "18:00"),("6:00", "8:00", "13:00", "14:00", "17:00"),("4:00", "6:00", "9:00", "12:00", "18:00"),("6:00", "7:30", "16:00", "18:00", "19:00"),("6:00", "9:00", "12:00", "13:00", "18:00"), ("7:00", "8:00", "10:00", "12:00", "19:00"),("7:00", "10:00", "12:00", "15:00", "18:00")), 6)
        )
        output_data = (["7:00", "12:00", "17:00"], ("7:00", "10:00", "12:00", "15:00", "18:00"))

        for variant, (input_data, output_data) in enumerate(zip(input_data, output_data), start=1):
            with self.subTest(f"variation #{variant}", input_data=input_data, output_data=output_data):
                self.assertEqual(time_table_for_a_weekday(*input_data), output_data)
