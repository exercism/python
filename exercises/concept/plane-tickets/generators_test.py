import inspect
import unittest
import pytest

from generators import (
    generate_seat_letters,
    generate_seats,
    assign_seats,
    generate_codes
)

class PlaneTicketsTest(unittest.TestCase):
    @pytest.mark.task(taskno=1)
    def test_task1_returns_generator(self):
        """Test if  generate_seat_letters() returns a generator type."""

        number = 5
        error_message = (f'Called generate_seat_letters({number}). '
                         f'The function returned a {type(generate_seat_letters(number))} type, '
                         f"but the tests expected the function to return a <class 'generator'> type.")

        self.assertTrue(inspect.isgenerator(generate_seat_letters(number)), msg=error_message)

    @pytest.mark.task(taskno=1)
    def test_generate_seat_letters(self):
        test_data = [1, 2, 3, 4, 5]
        result_data = [["A"],
                       ["A", "B"],
                       ["A", "B", "C"],
                       ["A", "B", "C", "D"],
                       ["A", "B", "C", "D", "A"]]

        for variant, (number, expected) in enumerate(zip(test_data, result_data), start=1):
            with self.subTest(f"variation #{variant}", number=number, expected=expected):
                actual_result = list(generate_seat_letters(number))
                error_message = (f'Called generate_seat_letters({number}). '
                                 f'The function returned {actual_result}, but the tests '
                                 f'expected {expected} when generating {number} seat(s).')

                self.assertEqual(actual_result, expected, msg=error_message)

    @pytest.mark.task(taskno=2)
    def test_task2_returns_generator(self):
        """Test if generate_seats() returns a generator type."""

        number = 7
        error_message = (f'Called generate_seats({number}). '
                         f'The function returned a {type(generate_seats(number))} type, '
                         f"but the tests expected the function to return a <class 'generator'> type.")

        self.assertTrue(inspect.isgenerator(generate_seats(number)), msg=error_message)

    @pytest.mark.task(taskno=2)
    def test_generate_seats(self):
        test_data = [1, 2, 3, 4, 5]
        result_data = [["1A"],
                       ["1A", "1B"],
                       ["1A", "1B", "1C"],
                       ["1A", "1B", "1C", "1D"],
                       ["1A", "1B", "1C", "1D", "2A"]]

        for variant, (number, expected) in enumerate(zip(test_data, result_data), start=1):
            with self.subTest(f"variation #{variant}", number=number, expected=expected):
                actual_result = list(generate_seats(number))
                error_message = (f'Called generate_seats({number}). '
                                 f'The function returned {actual_result}, but the tests '
                                 f'expected {expected} when generating {number} seat(s).')

                self.assertEqual(actual_result, expected, msg=error_message)

    @pytest.mark.task(taskno=2)
    def test_generate_seats_skips_row_13(self):
        test_data = [14 * 4]
        result_data = [["1A", "1B", "1C", "1D", "2A", "2B", "2C", "2D",
                        "3A", "3B", "3C", "3D", "4A", "4B", "4C", "4D",
                        "5A", "5B", "5C", "5D", "6A", "6B", "6C", "6D",
                        "7A", "7B", "7C", "7D", "8A", "8B", "8C", "8D",
                        "9A", "9B", "9C", "9D", "10A", "10B", "10C", "10D",
                        "11A", "11B", "11C", "11D", "12A", "12B", "12C", "12D",
                        "14A", "14B", "14C", "14D", "15A", "15B", "15C", "15D"]]

        for variant, (number, expected) in enumerate(zip(test_data, result_data), start=1):
            with self.subTest(f"variation #{variant}", number=number, expected=expected):
                actual_result = list(generate_seats(number))
                error_message = (f'Called generate_seats({number}). '
                                 f'The function returned {actual_result}, but the tests '
                                 f'expected: {expected}, when generating {number} seat(s).')

                self.assertEqual(actual_result, expected, msg=error_message)

    @pytest.mark.task(taskno=3)
    def test_assign_seats(self):
        test_data = [["Passenger1", "Passenger2", "Passenger3", "Passenger4", "Passenger5"],
                     ["TicketNo=5644", "TicketNo=2273", "TicketNo=493", "TicketNo=5411", "TicketNo=824"]]
        result_data = [{"Passenger1": "1A", "Passenger2": "1B",
                        "Passenger3": "1C", "Passenger4": "1D", "Passenger5": "2A"},
                       {"TicketNo=5644": "1A", "TicketNo=2273": "1B",
                        "TicketNo=493": "1C", "TicketNo=5411": "1D", "TicketNo=824": "2A"}]

        for variant, (passengers, expected) in enumerate(zip(test_data, result_data), start=1):
            with self.subTest(f"variation #{variant}", passengers=passengers, expected=expected):
                actual_result = assign_seats(passengers)
                error_message = (f'Called assign_seats({passengers}). '
                                 f'The function returned {actual_result}, but the tests '
                                 f'expected {expected}, when assigning seats.')

                self.assertEqual(actual_result, expected, msg=error_message)

    @pytest.mark.task(taskno=4)
    def test_task4_returns_generator(self):
        """Test if generate_codes() returns a generator type."""

        seat_numbers, flight_id = "11B", "HA80085"
        error_message = (f'Called generate_codes({seat_numbers}, {flight_id}). '
                         f'The function returned a {type(generate_codes(seat_numbers, flight_id))} type, '
                         f"but the tests expected the function to return a <class 'generator'> type.")

        self.assertTrue(inspect.isgenerator(generate_codes(seat_numbers, flight_id)), msg=error_message)


    @pytest.mark.task(taskno=4)
    def test_generate_codes(self):
        test_data = [(["12A", "38B", "69C", "102B"],"KL1022"),
                      (["22C", "88B", "33A", "44B"], "DL1002")]
        result_data = [['12AKL1022000', '38BKL1022000', '69CKL1022000', '102BKL102200'],
                       ['22CDL1002000', '88BDL1002000', '33ADL1002000', '44BDL1002000']]

        for variant, ((seat_numbers, flight_id), expected) in enumerate(zip(test_data, result_data), start=1):
            with self.subTest(f"variation #{variant}", seat_numbbers=seat_numbers,
                              flight_id=flight_id, expected=expected):

                actual_result = list(generate_codes(seat_numbers, flight_id))
                error_message = (f'Called generate_codes({seat_numbers}, {flight_id}). '
                                 f'The function returned {actual_result}, but the tests '
                                 f'expected {expected} when generating ticket numbers.')

                self.assertEqual(list(generate_codes(seat_numbers, flight_id)), expected, msg=error_message)
