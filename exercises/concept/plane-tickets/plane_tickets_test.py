from typing import Generator
import unittest
import pytest

from plane_tickets import (
    generate_seats,
    assign_seats,
    generate_codes
)

class PlaneTicketsTest(unittest.TestCase):


    @pytest.mark.task(taskno=1)
    def test_task1_is_generator(self):  # * Tests if [Task 1] actually returns a generator.
        input_var = 5
        output_type = Generator
        error_message = f"Expected: {str(output_type)} type, but got a different type."
        self.assertIsInstance(generate_seats(input_var), output_type, msg=error_message)

    @pytest.mark.task(taskno=1)
    def test_task1_output(self):
        input_vars = [1, 2, 3, 4, 5]
        output = [["1A"], ["1A", "1B"], ["1A", "1B", "1C"], ["1A", "1B", "1C", "1D"], ["1A", "1B", "1C", "1D", "2A"]]
        for variant, (input_var, output) in enumerate(zip(input_vars, output), start=1):
            error_message = f"Expected: {output}, but something went wrong while generating {input_var} seat(s)."
            with self.subTest(f"variation #{variant}", input_data=input_var, output_data=output):
                self.assertEqual(list(generate_seats(input_var)), output, msg=error_message)

    @pytest.mark.task(taskno=1)
    def test_task1_skips_row_13(self):
        input_vars = [14 * 4]
        output = [["1A", "1B", "1C", "1D", "2A", "2B", "2C", "2D",
                   "3A", "3B", "3C", "3D", "4A", "4B", "4C", "4D",
                   "5A", "5B", "5C", "5D", "6A", "6B", "6C", "6D",
                   "7A", "7B", "7C", "7D", "8A", "8B", "8C", "8D",
                   "9A", "9B", "9C", "9D", "10A", "10B", "10C", "10D",
                   "11A", "11B", "11C", "11D", "12A", "12B", "12C", "12D",
                   "14A", "14B", "14C", "14D", "15A", "15B", "15C", "15D"]]
        for variant, (input_var, output) in enumerate(zip(input_vars, output), start=1):
            error_message = f"Expected: {output}, but something went wrong while generating {input_var} seat(s)."
            with self.subTest(f"variation #{variant}", input_data=input_var, output_data=output):
                self.assertEqual(list(generate_seats(input_var)), output, msg=error_message)

    @pytest.mark.task(taskno=2)
    def test_task2(self):
        input_vars = [["Passenger1", "Passenger2", "Passenger3", "Passenger4", "Passenger5"], 
                      ["TicketNo=5644", "TicketNo=2273", "TicketNo=493", "TicketNo=5411", "TicketNo=824"]]
        output = [{"Passenger1": "1A", "Passenger2": "1B", "Passenger3": "1C", "Passenger4": "1D", "Passenger5": "2A"}, 
                  {"TicketNo=5644": "1A", "TicketNo=2273": "1B", "TicketNo=493": "1C", "TicketNo=5411": "1D", "TicketNo=824": "2A"}]
        for variant, (input_var, output) in enumerate(zip(input_vars, output), start=1):
            error_message = f"Expected: {output}, but something went wrong while assigning seats to passengers {input_var}."
            with self.subTest(f"variation #{variant}", input_data=input_var, output_data=output):
                self.assertEqual(assign_seats(input_var), output, msg=error_message)

    @pytest.mark.task(taskno=3)
    def test_task3_is_generator(self):
        input_var = ("11B", "HA80085")
        output_type = Generator
        error_message = f"Expected: {str(output_type)} type, but got a different type."
        self.assertIsInstance(generate_codes(input_var[0], input_var[1]), output_type, msg=error_message)

    @pytest.mark.task(taskno=3)
    def test_task3(self):
        input_vars = [(["12A", "38B", "69C", "102B"],"KL1022"),
                      (["22C", "88B", "33A", "44B"], "DL1002")]
        output = [['12AKL1022000', '38BKL1022000', '69CKL1022000', '102BKL102200'],
                  ['22CDL1002000', '88BDL1002000', '33ADL1002000', '44BDL1002000']]
        for variant, (input_var, output) in enumerate(zip(input_vars, output), start=1):
            error_message = f"Expected: {input_var}, but something went wrong while generating ticket numbers."
            with self.subTest(f"variation #{variant}", input_data=input_var, output_data=output):
                self.assertEqual(list(generate_codes(input_var[0], input_var[1])), output, msg=error_message)