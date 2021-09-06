import unittest
import pytest
from none import (
    new_seating_chart,
    arrange_reservations,
    find_all_available_seats,
    current_empty_seat_capacity,
    accommodate_waiting_guests,
    empty_seats
)


class TestNoneType(unittest.TestCase):

    @pytest.mark.task(taskno=1)
    def test_new_seating_chart_1(self):
        self.assertDictEqual(
            new_seating_chart(3),
            {1: None, 2: None, 3: None},
            msg="The New Seating chart does not match with the expected."
        )

    @pytest.mark.task(taskno=1)
    def test_new_seating_chart_2(self):
        self.assertDictEqual(
            new_seating_chart(),
            {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None, 10: None,
             11: None, 12: None, 13: None, 14: None, 15: None, 16: None, 17: None, 18: None, 19: None,
             20: None, 21: None, 22: None},
            msg="The New Seating chart does not match with the expected."
        )

    @pytest.mark.task(taskno=2)
    def test_arrange_reservations_1(self):
        self.assertDictEqual(
            arrange_reservations(guests=["Walter", "Frank", "Jenny", "Carol", "Alice", "George"]),
            {1: 'Frank', 2: 'Jenny', 3: 'Carol', 4: 'Alice', 5: 'George',
             6: None, 7: None, 8: None, 9: None, 10: None,
             11: None, 12: None, 13: None, 14: None, 15: None,
             16: None, 17: None, 18: None, 19: None, 20: None, 21: None, 22: None},
            msg="The reservation dict is incorrect"
        )

    @pytest.mark.task(taskno=2)
    def test_arrange_reservations_2(self):
        self.assertDictEqual(
            arrange_reservations(),
            {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None, 10: None,
             11: None, 12: None, 13: None, 14: None, 15: None, 16: None, 17: None, 18: None, 19: None, 20: None,
             21: None, 22: None},
            msg="The reservation dict is incorrect"
        )

    @pytest.mark.task(taskno=3)
    def test_find_all_available_seats_1(self):
        self.assertListEqual(
            find_all_available_seats(
                seats={1: None, 2: 'Frank', 3: 'Jenny', 4: None, 5: 'Alice', 6: 'George', 7: None, 8: 'Carol', 9: None,
                       10: None, 11: None, 12: 'Walter'}),
            [1, 4, 7, 9, 10, 11],
            msg="The Available Seat list is incorrect"
        )

    @pytest.mark.task(taskno=3)
    def test_find_all_available_seats_2(self):
        self.assertListEqual(
            find_all_available_seats(
                seats={1: None, 2: None, 3: None, 4: None, 5: 'Alice', 6: None, 7: None, 8: None, 9: None, 10: None,
                       11: None, 12: None}),
            [1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12],
            msg="The Available Seat list is incorrect"
        )

    @pytest.mark.task(taskno=4)
    def test_current_empty_seat_capacityy_1(self):
        self.assertIs(
            current_empty_seat_capacity({1: "Occupied", 2: None, 3: "Occupied"}),
            1,
            msg="the index of the seat which is empty is invalid."
        )

    @pytest.mark.task(taskno=4)
    def test_current_empty_seat_capacityy_2(self):
        self.assertIs(
            current_empty_seat_capacity({1: "Occupied", 2: "Occupied", 3: None, 4: "Occupied", 5: None}),
            2,
            msg="the index of the seat which is empty is invalid."
        )

    @pytest.mark.task(taskno=5)
    def test_accommodate_waiting_guests_1(self):
        starting_reservations = {1: 'Carol', 2: 'Alice', 3: 'George', 4: None, 5: None, 6: None, 7: 'Frank',
                                 8: 'Walter'}
        self.assertDictEqual(
            accommodate_waiting_guests(starting_reservations, ["Mort", "Suze", "Phillip", "Tony"]), starting_reservations,
            msg="The Accommodation of waiting guests are incorrect")

    @pytest.mark.task(taskno=5)
    def test_accommodate_waiting_guests_2(self):
        starting_reservations = {1: None, 2: None, 3: None, 4: 'Carol', 5: 'Alice', 6: 'George', 7: None, 8: None,
                                 9: None, 10: None, 11: None, 12: None, 13: None, 14: None, 15: None, 16: None,
                                 17: None, 18: 'Frank', 19: 'Jenny', 20: None, 21: None, 22: 'Walter'}
        self.assertDictEqual(
            accommodate_waiting_guests(starting_reservations, ["Mort", "Suze", "Phillip", "Tony"]),
            {1: 'Mort', 2: 'Suze', 3: 'Phillip', 4: 'Carol', 5: 'Alice', 6: 'George', 7: 'Tony', 8: None, 9: None,
             10: None, 11: None, 12: None, 13: None, 14: None, 15: None, 16: None, 17: None, 18: 'Frank', 19: 'Jenny',
             20: None, 21: None, 22: 'Walter'},
            msg="The Accommodation of waiting guests are incorrect"
        )

    @pytest.mark.task(taskno=6)
    def test_empty_seats_1(self):
        self.assertDictEqual(
            empty_seats(seats={1: "Alice", 2: None, 3: "Bob", 4: "George", 5: "Gloria"}, seat_numbers=[5, 3, 1]),
            {1: None, 2: None, 3: None, 4: "George", 5: None},
            msg="Seats are not emptied properly"
        )

    @pytest.mark.task(taskno=6)
    def test_empty_seats_2(self):
        self.assertDictEqual(
            empty_seats(seats={1: "Alice", 2: None, 3: "Bob", 4: "George", 5: "Gloria"}, seat_numbers=[]),
            {1: "Alice", 2: None, 3: "Bob", 4: "George", 5: "Gloria"},
            msg="Seats are not emptied properly"
        )
