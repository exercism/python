from types import GeneratorType
import unittest
import pytest

from plane_tickets import (
    generate_seats,
    assign_seats
)

class PlaneTicketsTest(unittest.TestCase):

    @pytest.mark.task(taskno=1)
    def test_task_1_type(self):
        input = [5]
        output = ["1A"]
        for variant, (input, output) in enumerate(zip(input, output), start=1):
            with self.subTest(f"variation #{variant}", input_data=input, output_data=output):
                generator = generate_seats(input)
                self.assertEqual(generator.__next__(), output)
