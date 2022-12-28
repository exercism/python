import unittest, random

from die import (
    number_die,
    letter_die
)


class ResistorColorTrioTest(unittest.TestCase):

    def test_generate_random_numbers_a_few_times(self):
        random.seed(10)
        output_data = [5, 1, 4, 4, 5]
        for variant, output_data in enumerate(output_data, start=1):
            with self.subTest(f'variation #{variant}', output_data=output_data):
                error_msg=f'Expected: {output_data} but got a different number'
                self.assertEqual(number_die(), output_data, msg=error_msg)

    def test_generate_random_numbers_a_lot_of_times(self):
        random.seed(145)
        output_data = [4, 5, 1, 4, 1, 6, 3, 6, 6, 6, 6, 4, 5, 5, 3, 1, 3, 2, 1, 5, 3, 6, 4, 1, 5]
        for variant, output_data in enumerate(output_data, start=1):
            with self.subTest(f'variation #{variant}', output_data=output_data):
                error_msg=f'Expected: {output_data} but got a different number'
                self.assertEqual(number_die(), output_data, msg=error_msg)

    def test_generate_random_numbers_with_a_custom_size(self):
        random.seed(4)
        output_data = [8, 10, 4, 24, 13, 16, 5, 3, 3, 1, 13, 18]
        for variant, output_data in enumerate(output_data, start=1):
            with self.subTest(f'variation #{variant}', output_data=output_data):
                error_msg=f'Expected: {output_data} but got a different number'
                self.assertEqual(number_die(24), output_data, msg=error_msg)

    def test_generate_random_letters_a_few_times(self):
        random.seed(10)
        output_data = ["s", "b", "n", "p", "s"]
        for variant, output_data in enumerate(output_data, start=1):
            with self.subTest(f'variation #{variant}', output_data=output_data):
                error_msg=f'Expected: {output_data} but got a different number'
                self.assertEqual(letter_die(), output_data, msg=error_msg)

    def test_generate_random_letters_a_lot_of_times(self):
        random.seed(145)
        output_data = ["y", "z", "n", "q", "a", "o", "a", "v", "k", "x", "z", "u", "v", "x", "p", "s", "q", "i", "d", "i", "f", "b", "t", "k", "w"]
        for variant, output_data in enumerate(output_data, start=1):
            with self.subTest(f'variation #{variant}', output_data=output_data):
                error_msg=f'Expected: {output_data} but got a different number'
                self.assertEqual(letter_die(), output_data, msg=error_msg)
