import unittest

from clock import Clock


class ClockTest(unittest.TestCase):
    # Test creating a new clock with an initial time.
    def test_on_the_hour(self):
        self.assertEqual('08:00', str(Clock(8, 0)))

    def test_past_the_hour(self):
        self.assertEqual('11:09', str(Clock(11, 9)))

    def test_midnight_is_zero_hours(self):
        self.assertEqual('00:00', str(Clock(24, 0)))

    def test_hour_rolls_over(self):
        self.assertEqual('01:00', str(Clock(25, 0)))

    def test_hour_rolls_over_continuously(self):
        self.assertEqual('04:00', str(Clock(100, 0)))

    def test_sixty_minutes_is_next_hour(self):
        self.assertEqual('02:00', str(Clock(1, 60)))

    def test_minutes_roll_over(self):
        self.assertEqual('02:40', str(Clock(0, 160)))

    def test_minutes_roll_over_continuously(self):
        self.assertEqual('04:43', str(Clock(0, 1723)))

    def test_hour_and_minutes_roll_over(self):
        self.assertEqual('03:40', str(Clock(25, 160)))

    def test_hour_and_minutes_roll_over_continuously(self):
        self.assertEqual('11:01', str(Clock(201, 3001)))

    def test_hour_and_minutes_roll_over_to_exactly_midnight(self):
        self.assertEqual('00:00', str(Clock(72, 8640)))

    def test_negative_hour(self):
        self.assertEqual('23:15', str(Clock(-1, 15)))

    def test_negative_hour_rolls_over(self):
        self.assertEqual('23:00', str(Clock(-25, 0)))

    def test_negative_hour_rolls_over_continuously(self):
        self.assertEqual('05:00', str(Clock(-91, 0)))

    def test_negative_minutes(self):
        self.assertEqual('00:20', str(Clock(1, -40)))

    def test_negative_minutes_roll_over(self):
        self.assertEqual('22:20', str(Clock(1, -160)))

    def test_negative_minutes_roll_over_continuously(self):
        self.assertEqual('16:40', str(Clock(1, -4820)))

    def test_negative_hour_and_minutes_both_roll_over(self):
        self.assertEqual('20:20', str(Clock(-25, -160)))

    def test_negative_hour_and_minutes_both_roll_over_continuously(self):
        self.assertEqual('22:10', str(Clock(-121, -5810)))

    # Test adding and subtracting minutes.
    def test_add_minutes(self):
        self.assertEqual('10:03', str(Clock(10, 0).add(3)))

    def test_add_no_minutes(self):
        self.assertEqual('06:41', str(Clock(6, 41).add(0)))

    def test_add_to_next_hour(self):
        self.assertEqual('01:25', str(Clock(0, 45).add(40)))

    def test_add_more_than_one_hour(self):
        self.assertEqual('11:01', str(Clock(10, 0).add(61)))

    def test_add_more_than_two_hours_with_carry(self):
        self.assertEqual('03:25', str(Clock(0, 45).add(160)))

    def test_add_across_midnight(self):
        self.assertEqual('00:01', str(Clock(23, 59).add(2)))

    def test_add_more_than_one_day(self):
        self.assertEqual('06:32', str(Clock(5, 32).add(1500)))

    def test_add_more_than_two_days(self):
        self.assertEqual('11:21', str(Clock(1, 1).add(3500)))

    def test_subtract_minutes(self):
        self.assertEqual('10:00', str(Clock(10, 3).add(-3)))

    def test_subtract_to_previous_hour(self):
        self.assertEqual('10:00', str(Clock(10, 3).add(-3)))

    def test_subtract_more_than_an_hour(self):
        self.assertEqual('09:33', str(Clock(10, 3).add(-30)))

    def test_subtract_across_midnight(self):
        self.assertEqual('08:53', str(Clock(10, 3).add(-70)))

    def test_subtract_more_than_two_hours(self):
        self.assertEqual('21:20', str(Clock(0, 0).add(-160)))

    def test_subtract_more_than_two_hours_with_borrow(self):
        self.assertEqual('03:35', str(Clock(6, 15).add(-160)))

    def test_subtract_more_than_one_day(self):
        self.assertEqual('04:32', str(Clock(5, 32).add(-1500)))

    def test_subtract_more_than_two_days(self):
        self.assertEqual('00:20', str(Clock(2, 20).add(-3000)))

    # Construct two separate clocks, set times, test if they are equal.
    def test_clocks_with_same_time(self):
        self.assertEqual(Clock(15, 37), Clock(15, 37))

    def test_clocks_a_minute_apart(self):
        self.assertNotEqual(Clock(15, 36), Clock(15, 37))

    def test_clocks_an_hour_apart(self):
        self.assertNotEqual(Clock(14, 37), Clock(15, 37))

    def test_clocks_with_hour_overflow(self):
        self.assertNotEqual(Clock(10, 37), Clock(34, 37))

    def test_clocks_with_hour_overflow_by_several_days(self):
        self.assertEqual(Clock(3, 11), Clock(99, 11))

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

if __name__ == '__main__':
    unittest.main()
