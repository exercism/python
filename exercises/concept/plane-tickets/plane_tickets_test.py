from types import GeneratorType
import unittest
import pytest

from plane_tickets import (
    generate_seats,
    assign_seats
)

class PlaneTicketsTest(unittest.TestCase):

    @pytest.mark.task(taskno=1)
    def test_task1_type(self): # * Tests if [Task 1] actually returns a generator.
        input = [5]
        output = ["1A"]
        for variant, (input, output) in enumerate(zip(input, output), start=1):
            with self.subTest(f"variation #{variant}", input_data=input, output_data=output):
                generator = generate_seats(input)
                self.assertEqual(generator.__next__(), output)

    @pytest.mark.task(taskno=1)
    def test_task1_basic(self):
        input = [1, 2, 3, 4, 5]
        output = [['1A'], ['1A', '1B'], ['1A', '1B', '1C'] ,['1A', '1B', '1C', '1D'], ['1A', '1B', '1C', '1D', '2A']]
        for variant, (input, output) in enumerate(zip(input, output), start=1):
            with self.subTest(f"variation #{variant}", input_data=input, output_data=output):
                self.assertEqual([seat for seat in generate_seats(input)], output)
                
    @pytest.mark.task(taskno=1)
    def test_task1_skips_row_13(self):
        input = [14*4]
        output = [['1A', '1B', '1C', '1D', '2A', '2B', '2C', '2D', '3A', '3B', '3C', '3D', '4A', '4B', '4C', '4D', '5A', '5B', '5C', '5D', '6A', '6B', '6C', '6D', '7A', '7B', '7C', '7D', '8A', '8B', '8C', '8D', '9A', '9B', '9C', '9D', '10A', '10B', '10C', '10D', '11A', '11B', '11C', '11D', '12A', '12B', '12C', '12D', '14A', '14B', '14C', '14D', '15A', '15B', '15C', '15D']]
        for variant, (input, output) in enumerate(zip(input, output), start=1):
            with self.subTest(f"variation #{variant}", input_data=input, output_data=output):
                self.assertEqual([seat for seat in generate_seats(input)], output)
            