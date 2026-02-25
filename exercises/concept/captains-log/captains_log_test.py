import unittest
import pytest

from captains_log import (
    random_planet_class,
    random_ship_registry_number,
    random_stardate)


class CaptainsLogTest(unittest.TestCase):

    @pytest.mark.task(taskno=1)
    def test_random_planet_class(self):
        repeats = range(1000)  # may need adjusting?
        planetary_classes = {"D", "H", "J", "K", "L", "M", "N", "R", "T", "Y"}
        actual_results = [random_planet_class() for _ in repeats]

        # are all results valid planetary classes?
        invalid = [planet for planet in actual_results if planet not in planetary_classes]
        error_message1 = (f'Called random_planet_class() {repeats} times.'
                          f'The function returned these invalid results: '
                          f'{invalid}.')
        self.assertEqual(len(invalid), 0, msg=error_message1)

        # are all valid planetary classes generated, with enough repeats?
        missing = [planet for planet in planetary_classes if planet not in set(actual_results)]
        error_message2 = (f'Called random_planet_class() {repeats} times.'
                          f'The function never returned these valid results: '
                          f'{missing}.')
        self.assertEqual(len(missing), 0, msg=error_message2)

    @pytest.mark.task(taskno=2)
    def test_ship_registry_number(self):
        repeats = range(100)  # may need adjusting?
        actual_results = [random_ship_registry_number() for _ in repeats]

        # Do all results have length 8?
        wrong_length = [regno for regno in actual_results if len(regno) != 8]
        error_message1 = (f'Called random_planet_class() {repeats} times.'
                          f'The function returned these invalid results (wrong length): '
                          f'{wrong_length}.')
        self.assertEqual(len(wrong_length), 0, msg=error_message1)

        # Do all results start with "NCC-"?
        wrong_prefix = [regno for regno in actual_results if regno[:4] != 'NCC-']
        error_message2 = (f'Called random_planet_class() {repeats} times.'
                          f'The function returned these invalid results (must start with "NCC-"): '
                          f'{wrong_prefix}.')
        self.assertEqual(len(wrong_prefix), 0, msg=error_message2)

        # Do all results end with a valid 4-digit integer?
        not_int = [regno for regno in actual_results if not (regno[4:]).isdigit()]
        error_message3 = (f'Called random_planet_class() {repeats} times.'
                          f'The function returned these invalid results (must end with a 4-digit integer): '
                          f'{not_int}.')
        self.assertEqual(len(not_int), 0, msg=error_message3)

        # Are all numbers from 1000 to 9999?
        wrong_int = [regno for regno in actual_results if not (1000 <= int(regno[4:]) <= 9999)]
        error_message4 = (f'Called random_planet_class() {repeats} times.'
                          f'The function returned these invalid results (integer must be 1000 to 9999): '
                          f'{wrong_int}.')
        self.assertEqual(len(wrong_int), 0, msg=error_message4)

    @pytest.mark.task(taskno=3)
    def test_stardate(self):
        repeats = range(100)  # may need adjusting?
        actual_results = [random_stardate() for _ in repeats]

        def is_number(s):
            try:
                float(s)
                return True
            except ValueError:
                return False

        # Are all results valid float values?
        not_float = [stardate for stardate in actual_results if not isinstance(stardate, float)]
        error_message1 = (f'Called random_planet_class() {repeats} times.'
                          f'The function returned these invalid results (must be a floating-point number): '
                          f'{not_float}.')
        self.assertEqual(len(not_float), 0, msg=error_message1)

        # Are all results numbers from from 41000 to 42000?
        wrong_number = [stardate for stardate in actual_results if not 41000.0 <= stardate <= 42000.0]
        error_message2 = (f'Called random_planet_class() {repeats} times.'
                          f'The function returned these invalid results (must be from 41000.0 to 42000.0): '
                          f'{wrong_number}.')
        self.assertEqual(len(wrong_number), 0, msg=error_message2)
