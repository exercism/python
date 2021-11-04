from types import GeneratorType
import unittest
import pytest

from plane_tickets import (
    generate_seats,
    assign_seats
)

class PlaneTicketsTest(unittest.TestCase):

    @pytest.mark.task(taskno=1)
    def test_task_1_type(self): # * Tests if [Task 1] actually returns a generator.
        input = [5]
        output = ["1A"]
        for variant, (input, output) in enumerate(zip(input, output), start=1):
            with self.subTest(f"variation #{variant}", input_data=input, output_data=output):
                generator = generate_seats(input)
                self.assertEqual(generator.__next__(), output)

    @pytest.mark.task(taskno=1)
    def test_task_1_output(self):
        input = [1, 2, 3, 4, 5]
        output = [['1A'], ['1A', '1B'], ['1A', '1B', '1C'] ,['1A', '1B', '1C', '1D'], ['1A', '1B', '1C', '1D', '2A']]
        for variant, (input, output) in enumerate(zip(input, output), start=1):
            with self.subTest(f"variation #{variant}", input_data=input, output_data=output):
                self.assertEqual([seat for seat in generate_seats(input)], output)