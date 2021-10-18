import unittest
import pytest
from none import (
    new_seating_chart,
    arrange_reservations,
    find_all_available_seats,
    current_empty_seat_capacity,
    accommodate_waiting_guests,
    empty_seats)


class RestaurantRozalynnTest(unittest.TestCase):

    @pytest.mark.task(taskno=1)
    def test_new_seating_chart_1(self):
        failure_message='The New Seating chart does not match with the expected.'
        self.assertDictEqual(new_seating_chart(3), {1: None, 2: None, 3: None}, msg=failure_message)

    @pytest.mark.task(taskno=1)
    def test_new_seating_chart_2(self):
        expected_results = {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None, 10: None,
                            11: None, 12: None, 13: None, 14: None, 15: None, 16: None, 17: None, 18: None, 19: None,
                            20: None, 21: None, 22: None}
        failure_msg = 'The New Seating chart does not match with the expected.'

        self.assertDictEqual(new_seating_chart(), expected_results, msg=failure_msg)

    @pytest.mark.task(taskno=2)
    def test_arrange_reservations_1(self):
        guests = ['Walter', 'Frank', 'Jenny', 'Carol', 'Alice', 'George']
        expected_results =  {1: 'Frank', 2: 'Jenny', 3: 'Carol', 4: 'Alice', 5: 'George',
                             6: None, 7: None, 8: None, 9: None, 10: None,
                             11: None, 12: None, 13: None, 14: None, 15: None,
                             16: None, 17: None, 18: None, 19: None, 20: None, 21: None, 22: None}
        failure_msg = 'The reservation dict is incorrect'

        self.assertDictEqual(arrange_reservations(guests), expected_results, msg=failure_msg)

    @pytest.mark.task(taskno=2)
    def test_arrange_reservations_2(self):
        expected_result = {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None,
                           10: None, 11: None, 12: None, 13: None, 14: None, 15: None, 16: None, 17: None,
                           18: None,19: None, 20: None, 21: None, 22: None}

        failure_msg = 'The reservation dict is incorrect'

        # pylint: disable= no-value-for-parameter
        self.assertDictEqual(arrange_reservations(), expected_result, failure_msg)

    @pytest.mark.task(taskno=3)
    def test_find_all_available_seats_1(self):
        seats={1: None, 2: 'Frank', 3: 'Jenny', 4: None, 5: 'Alice', 6: 'George', 7: None, 8: 'Carol',
               9: None, 10: None, 11: None, 12: 'Walter'}

        expected_results = [1, 4, 7, 9, 10, 11]

        failure_msg = 'The Available Seat list is incorrect'

        self.assertListEqual(find_all_available_seats(seats), expected_results, msg=failure_msg)

    @pytest.mark.task(taskno=3)
    def test_find_all_available_seats_2(self):
        seats={1: None, 2: None, 3: None, 4: None, 5: 'Alice', 6: None, 7: None,
               8: None, 9: None, 10: None, 11: None, 12: None}

        expected_results = [1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12]
        failure_msg = 'The Available Seat list is incorrect'

        self.assertListEqual(find_all_available_seats(seats), expected_results, failure_msg)

    @pytest.mark.task(taskno=4)
    def test_current_empty_seat_capacity_1(self):

        failure_msg = 'the index of the seat which is empty is invalid.'

        self.assertIs(current_empty_seat_capacity({1: 'Occupied', 2: None, 3: 'Occupied'}), 1, msg=failure_msg)

    @pytest.mark.task(taskno=4)
    def test_current_empty_seat_capacity_2(self):

        seats = {1: 'Occupied', 2: 'Occupied', 3: None, 4: 'Occupied', 5: None}
        failure_msg = 'the index of the seat which is empty is invalid.'

        self.assertIs(current_empty_seat_capacity(seats), 2, msg=failure_msg)

    @pytest.mark.task(taskno=5)
    def test_accommodate_waiting_guests_1(self):
        reservations = {1: 'Carol', 2: 'Alice', 3: 'George', 4: None,
                        5: None, 6: None, 7: 'Frank',8: 'Walter'}

        guests = ['Mort', 'Suze', 'Phillip', 'Tony']

        failure_msg = 'The Accommodation of waiting guests are incorrect'
        self.assertDictEqual(accommodate_waiting_guests(reservations,guests), reservations, msg=failure_msg)

    @pytest.mark.task(taskno=5)
    def test_accommodate_waiting_guests_2(self):
        reservations = {1: None, 2: None, 3: None, 4: 'Carol', 5: 'Alice', 6: 'George', 7: None, 8: None,
                        9: None, 10: None, 11: None, 12: None, 13: None, 14: None, 15: None, 16: None,
                        17: None, 18: 'Frank', 19: 'Jenny', 20: None, 21: None, 22: 'Walter'}

        guests = ['Mort', 'Suze', 'Phillip', 'Tony']

        expected_results = {1: 'Mort', 2: 'Suze', 3: 'Phillip', 4: 'Carol', 5: 'Alice', 6: 'George',
                            7: 'Tony', 8: None, 9: None, 10: None, 11: None, 12: None, 13: None, 14: None,
                            15: None, 16: None, 17: None, 18: 'Frank', 19: 'Jenny', 20: None, 21: None, 22: 'Walter'}

        failure_msg = 'The Accommodation of waiting guests are incorrect'

        self.assertDictEqual(accommodate_waiting_guests(reservations, guests), expected_results, msg=failure_msg)

    @pytest.mark.task(taskno=6)
    def test_empty_seats_1(self):
        seats = {1: 'Alice', 2: None, 3: 'Bob', 4: 'George', 5: 'Gloria'}
        seat_numbers = [5, 3, 1]
        expected_results = {1: None, 2: None, 3: None, 4: 'George', 5: None}

        failure_msg = 'Seats are not emptied properly'
        self.assertDictEqual(empty_seats(seats, seat_numbers), expected_results, msg=failure_msg)

    @pytest.mark.task(taskno=6)
    def test_empty_seats_2(self):
        seats = {1: 'Alice', 2: None, 3: 'Bob', 4: 'George', 5: 'Gloria'}
        seat_numbers = []
        expected_results = {1: 'Alice', 2: None, 3: 'Bob', 4: 'George', 5: 'Gloria'}
        failure_msg = 'Seats are not emptied properly'

        self.assertDictEqual(empty_seats(seats, seat_numbers), expected_results, msg=failure_msg)
