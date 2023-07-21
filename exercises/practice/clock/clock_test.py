# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/clock/canonical-data.json
# File last updated on 2023-07-20

import unittest

from clock import (
    Clock,
)


class ClockTest(unittest.TestCase):
    # Create A String Representation
    def test_lunch_time(self):
        self.assertEqual(repr(Clock(12, 0)), "Clock(12, 0)")

    def test_breakfast_time(self):
        self.assertEqual(repr(Clock(6, 45)), "Clock(6, 45)")

    def test_dinner_time(self):
        self.assertEqual(repr(Clock(18, 30)), "Clock(18, 30)")

    # Create A New Clock With An Initial Time
    def test_on_the_hour(self):
        self.assertEqual(str(Clock(8, 0)), "08:00")

    def test_past_the_hour(self):
        self.assertEqual(str(Clock(11, 9)), "11:09")

    def test_midnight_is_zero_hours(self):
        self.assertEqual(str(Clock(24, 0)), "00:00")

    def test_hour_rolls_over(self):
        self.assertEqual(str(Clock(25, 0)), "01:00")

    def test_hour_rolls_over_continuously(self):
        self.assertEqual(str(Clock(100, 0)), "04:00")

    def test_sixty_minutes_is_next_hour(self):
        self.assertEqual(str(Clock(1, 60)), "02:00")

    def test_minutes_roll_over(self):
        self.assertEqual(str(Clock(0, 160)), "02:40")

    def test_minutes_roll_over_continuously(self):
        self.assertEqual(str(Clock(0, 1723)), "04:43")

    def test_hour_and_minutes_roll_over(self):
        self.assertEqual(str(Clock(25, 160)), "03:40")

    def test_hour_and_minutes_roll_over_continuously(self):
        self.assertEqual(str(Clock(201, 3001)), "11:01")

    def test_hour_and_minutes_roll_over_to_exactly_midnight(self):
        self.assertEqual(str(Clock(72, 8640)), "00:00")

    def test_negative_hour(self):
        self.assertEqual(str(Clock(-1, 15)), "23:15")

    def test_negative_hour_rolls_over(self):
        self.assertEqual(str(Clock(-25, 0)), "23:00")

    def test_negative_hour_rolls_over_continuously(self):
        self.assertEqual(str(Clock(-91, 0)), "05:00")

    def test_negative_minutes(self):
        self.assertEqual(str(Clock(1, -40)), "00:20")

    def test_negative_minutes_roll_over(self):
        self.assertEqual(str(Clock(1, -160)), "22:20")

    def test_negative_minutes_roll_over_continuously(self):
        self.assertEqual(str(Clock(1, -4820)), "16:40")

    def test_negative_sixty_minutes_is_previous_hour(self):
        self.assertEqual(str(Clock(2, -60)), "01:00")

    def test_negative_hour_and_minutes_both_roll_over(self):
        self.assertEqual(str(Clock(-25, -160)), "20:20")

    def test_negative_hour_and_minutes_both_roll_over_continuously(self):
        self.assertEqual(str(Clock(-121, -5810)), "22:10")

    # Add Minutes
    def test_add_minutes(self):
        self.assertEqual(str(Clock(10, 0) + 3), "10:03")

    def test_add_no_minutes(self):
        self.assertEqual(str(Clock(6, 41) + 0), "06:41")

    def test_add_to_next_hour(self):
        self.assertEqual(str(Clock(0, 45) + 40), "01:25")

    def test_add_more_than_one_hour(self):
        self.assertEqual(str(Clock(10, 0) + 61), "11:01")

    def test_add_more_than_two_hours_with_carry(self):
        self.assertEqual(str(Clock(0, 45) + 160), "03:25")

    def test_add_across_midnight(self):
        self.assertEqual(str(Clock(23, 59) + 2), "00:01")

    def test_add_more_than_one_day_1500_min_25_hrs(self):
        self.assertEqual(str(Clock(5, 32) + 1500), "06:32")

    def test_add_more_than_two_days(self):
        self.assertEqual(str(Clock(1, 1) + 3500), "11:21")

    # Subtract Minutes
    def test_subtract_minutes(self):
        self.assertEqual(str(Clock(10, 3) - 3), "10:00")

    def test_subtract_to_previous_hour(self):
        self.assertEqual(str(Clock(10, 3) - 30), "09:33")

    def test_subtract_more_than_an_hour(self):
        self.assertEqual(str(Clock(10, 3) - 70), "08:53")

    def test_subtract_across_midnight(self):
        self.assertEqual(str(Clock(0, 3) - 4), "23:59")

    def test_subtract_more_than_two_hours(self):
        self.assertEqual(str(Clock(0, 0) - 160), "21:20")

    def test_subtract_more_than_two_hours_with_borrow(self):
        self.assertEqual(str(Clock(6, 15) - 160), "03:35")

    def test_subtract_more_than_one_day_1500_min_25_hrs(self):
        self.assertEqual(str(Clock(5, 32) - 1500), "04:32")

    def test_subtract_more_than_two_days(self):
        self.assertEqual(str(Clock(2, 20) - 3000), "00:20")

    # Compare Two Clocks For Equality
    def test_clocks_with_same_time(self):
        self.assertEqual(Clock(15, 37), Clock(15, 37))

    def test_clocks_a_minute_apart(self):
        self.assertNotEqual(Clock(15, 36), Clock(15, 37))

    def test_clocks_an_hour_apart(self):
        self.assertNotEqual(Clock(14, 37), Clock(15, 37))

    def test_clocks_with_hour_overflow(self):
        self.assertEqual(Clock(10, 37), Clock(34, 37))

    def test_clocks_with_hour_overflow_by_several_days(self):
        self.assertEqual(Clock(3, 11), Clock(99, 11))

    def test_clocks_with_negative_hour(self):
        self.assertEqual(Clock(22, 40), Clock(-2, 40))

    def test_clocks_with_negative_hour_that_wraps(self):
        self.assertEqual(Clock(17, 3), Clock(-31, 3))

    def test_clocks_with_negative_hour_that_wraps_multiple_times(self):
        self.assertEqual(Clock(13, 49), Clock(-83, 49))

    def test_clocks_with_minute_overflow(self):
        self.assertEqual(Clock(0, 1), Clock(0, 1441))

    def test_clocks_with_minute_overflow_by_several_days(self):
        self.assertEqual(Clock(2, 2), Clock(2, 4322))

    def test_clocks_with_negative_minute(self):
        self.assertEqual(Clock(2, 40), Clock(3, -20))

    def test_clocks_with_negative_minute_that_wraps(self):
        self.assertEqual(Clock(4, 10), Clock(5, -1490))

    def test_clocks_with_negative_minute_that_wraps_multiple_times(self):
        self.assertEqual(Clock(6, 15), Clock(6, -4305))

    def test_clocks_with_negative_hours_and_minutes(self):
        self.assertEqual(Clock(7, 32), Clock(-12, -268))

    def test_clocks_with_negative_hours_and_minutes_that_wrap(self):
        self.assertEqual(Clock(18, 7), Clock(-54, -11513))

    def test_full_clock_and_zeroed_clock(self):
        self.assertEqual(Clock(24, 0), Clock(0, 0))
