from datetime import date
import unittest

from meetup import (
    meetup,
    MeetupDayException,
)

# Tests adapted from `problem-specifications//canonical-data.json`


class MeetupTest(unittest.TestCase):
    def test_when_teenth_monday_is_the_13th_the_first_day_of_the_teenth_week(self):
        self.assertEqual(meetup(2013, 5, "teenth", "Monday"), date(2013, 5, 13))

    def test_when_teenth_monday_is_the_19th_the_last_day_of_the_teenth_week(self):
        self.assertEqual(meetup(2013, 8, "teenth", "Monday"), date(2013, 8, 19))

    def test_when_teenth_monday_is_some_day_in_the_middle_of_the_teenth_week(self):
        self.assertEqual(meetup(2013, 9, "teenth", "Monday"), date(2013, 9, 16))

    def test_when_teenth_tuesday_is_the_19th_the_last_day_of_the_teenth_week(self):
        self.assertEqual(meetup(2013, 3, "teenth", "Tuesday"), date(2013, 3, 19))

    def test_when_teenth_tuesday_is_some_day_in_the_middle_of_the_teenth_week(self):
        self.assertEqual(meetup(2013, 4, "teenth", "Tuesday"), date(2013, 4, 16))

    def test_when_teenth_tuesday_is_the_13th_the_first_day_of_the_teenth_week(self):
        self.assertEqual(meetup(2013, 8, "teenth", "Tuesday"), date(2013, 8, 13))

    def test_when_teenth_wednesday_is_some_day_in_the_middle_of_the_teenth_week(self):
        self.assertEqual(meetup(2013, 1, "teenth", "Wednesday"), date(2013, 1, 16))

    def test_when_teenth_wednesday_is_the_13th_the_first_day_of_the_teenth_week(self):
        self.assertEqual(meetup(2013, 2, "teenth", "Wednesday"), date(2013, 2, 13))

    def test_when_teenth_wednesday_is_the_19th_the_last_day_of_the_teenth_week(self):
        self.assertEqual(meetup(2013, 6, "teenth", "Wednesday"), date(2013, 6, 19))

    def test_when_teenth_thursday_is_some_day_in_the_middle_of_the_teenth_week(self):
        self.assertEqual(meetup(2013, 5, "teenth", "Thursday"), date(2013, 5, 16))

    def test_when_teenth_thursday_is_the_13th_the_first_day_of_the_teenth_week(self):
        self.assertEqual(meetup(2013, 6, "teenth", "Thursday"), date(2013, 6, 13))

    def test_when_teenth_thursday_is_the_19th_the_last_day_of_the_teenth_week(self):
        self.assertEqual(meetup(2013, 9, "teenth", "Thursday"), date(2013, 9, 19))

    def test_when_teenth_friday_is_the_19th_the_last_day_of_the_teenth_week(self):
        self.assertEqual(meetup(2013, 4, "teenth", "Friday"), date(2013, 4, 19))

    def test_when_teenth_friday_is_some_day_in_the_middle_of_the_teenth_week(self):
        self.assertEqual(meetup(2013, 8, "teenth", "Friday"), date(2013, 8, 16))

    def test_when_teenth_friday_is_the_13th_the_first_day_of_the_teenth_week(self):
        self.assertEqual(meetup(2013, 9, "teenth", "Friday"), date(2013, 9, 13))

    def test_when_teenth_saturday_is_some_day_in_the_middle_of_the_teenth_week(self):
        self.assertEqual(meetup(2013, 2, "teenth", "Saturday"), date(2013, 2, 16))

    def test_when_teenth_saturday_is_the_13th_the_first_day_of_the_teenth_week(self):
        self.assertEqual(meetup(2013, 4, "teenth", "Saturday"), date(2013, 4, 13))

    def test_when_teenth_saturday_is_the_19th_the_last_day_of_the_teenth_week(self):
        self.assertEqual(meetup(2013, 10, "teenth", "Saturday"), date(2013, 10, 19))

    def test_when_teenth_sunday_is_the_19th_the_last_day_of_the_teenth_week(self):
        self.assertEqual(meetup(2013, 5, "teenth", "Sunday"), date(2013, 5, 19))

    def test_when_teenth_sunday_is_some_day_in_the_middle_of_the_teenth_week(self):
        self.assertEqual(meetup(2013, 6, "teenth", "Sunday"), date(2013, 6, 16))

    def test_when_teenth_sunday_is_the_13th_the_first_day_of_the_teenth_week(self):
        self.assertEqual(meetup(2013, 10, "teenth", "Sunday"), date(2013, 10, 13))

    def test_when_first_monday_is_some_day_in_the_middle_of_the_first_week(self):
        self.assertEqual(meetup(2013, 3, "first", "Monday"), date(2013, 3, 4))

    def test_when_first_monday_is_the_1st_the_first_day_of_the_first_week(self):
        self.assertEqual(meetup(2013, 4, "first", "Monday"), date(2013, 4, 1))

    def test_when_first_tuesday_is_the_7th_the_last_day_of_the_first_week(self):
        self.assertEqual(meetup(2013, 5, "first", "Tuesday"), date(2013, 5, 7))

    def test_when_first_tuesday_is_some_day_in_the_middle_of_the_first_week(self):
        self.assertEqual(meetup(2013, 6, "first", "Tuesday"), date(2013, 6, 4))

    def test_when_first_wednesday_is_some_day_in_the_middle_of_the_first_week(self):
        self.assertEqual(meetup(2013, 7, "first", "Wednesday"), date(2013, 7, 3))

    def test_when_first_wednesday_is_the_7th_the_last_day_of_the_first_week(self):
        self.assertEqual(meetup(2013, 8, "first", "Wednesday"), date(2013, 8, 7))

    def test_when_first_thursday_is_some_day_in_the_middle_of_the_first_week(self):
        self.assertEqual(meetup(2013, 9, "first", "Thursday"), date(2013, 9, 5))

    def test_when_first_thursday_is_another_day_in_the_middle_of_the_first_week(self):
        self.assertEqual(meetup(2013, 10, "first", "Thursday"), date(2013, 10, 3))

    def test_when_first_friday_is_the_1st_the_first_day_of_the_first_week(self):
        self.assertEqual(meetup(2013, 11, "first", "Friday"), date(2013, 11, 1))

    def test_when_first_friday_is_some_day_in_the_middle_of_the_first_week(self):
        self.assertEqual(meetup(2013, 12, "first", "Friday"), date(2013, 12, 6))

    def test_when_first_saturday_is_some_day_in_the_middle_of_the_first_week(self):
        self.assertEqual(meetup(2013, 1, "first", "Saturday"), date(2013, 1, 5))

    def test_when_first_saturday_is_another_day_in_the_middle_of_the_first_week(self):
        self.assertEqual(meetup(2013, 2, "first", "Saturday"), date(2013, 2, 2))

    def test_when_first_sunday_is_some_day_in_the_middle_of_the_first_week(self):
        self.assertEqual(meetup(2013, 3, "first", "Sunday"), date(2013, 3, 3))

    def test_when_first_sunday_is_the_7th_the_last_day_of_the_first_week(self):
        self.assertEqual(meetup(2013, 4, "first", "Sunday"), date(2013, 4, 7))

    def test_when_second_monday_is_some_day_in_the_middle_of_the_second_week(self):
        self.assertEqual(meetup(2013, 3, "second", "Monday"), date(2013, 3, 11))

    def test_when_second_monday_is_the_8th_the_first_day_of_the_second_week(self):
        self.assertEqual(meetup(2013, 4, "second", "Monday"), date(2013, 4, 8))

    def test_when_second_tuesday_is_the_14th_the_last_day_of_the_second_week(self):
        self.assertEqual(meetup(2013, 5, "second", "Tuesday"), date(2013, 5, 14))

    def test_when_second_tuesday_is_some_day_in_the_middle_of_the_second_week(self):
        self.assertEqual(meetup(2013, 6, "second", "Tuesday"), date(2013, 6, 11))

    def test_when_second_wednesday_is_some_day_in_the_middle_of_the_second_week(self):
        self.assertEqual(meetup(2013, 7, "second", "Wednesday"), date(2013, 7, 10))

    def test_when_second_wednesday_is_the_14th_the_last_day_of_the_second_week(self):
        self.assertEqual(meetup(2013, 8, "second", "Wednesday"), date(2013, 8, 14))

    def test_when_second_thursday_is_some_day_in_the_middle_of_the_second_week(self):
        self.assertEqual(meetup(2013, 9, "second", "Thursday"), date(2013, 9, 12))

    def test_when_second_thursday_is_another_day_in_the_middle_of_the_second_week(self):
        self.assertEqual(meetup(2013, 10, "second", "Thursday"), date(2013, 10, 10))

    def test_when_second_friday_is_the_8th_the_first_day_of_the_second_week(self):
        self.assertEqual(meetup(2013, 11, "second", "Friday"), date(2013, 11, 8))

    def test_when_second_friday_is_some_day_in_the_middle_of_the_second_week(self):
        self.assertEqual(meetup(2013, 12, "second", "Friday"), date(2013, 12, 13))

    def test_when_second_saturday_is_some_day_in_the_middle_of_the_second_week(self):
        self.assertEqual(meetup(2013, 1, "second", "Saturday"), date(2013, 1, 12))

    def test_when_second_saturday_is_another_day_in_the_middle_of_the_second_week(self):
        self.assertEqual(meetup(2013, 2, "second", "Saturday"), date(2013, 2, 9))

    def test_when_second_sunday_is_some_day_in_the_middle_of_the_second_week(self):
        self.assertEqual(meetup(2013, 3, "second", "Sunday"), date(2013, 3, 10))

    def test_when_second_sunday_is_the_14th_the_last_day_of_the_second_week(self):
        self.assertEqual(meetup(2013, 4, "second", "Sunday"), date(2013, 4, 14))

    def test_when_third_monday_is_some_day_in_the_middle_of_the_third_week(self):
        self.assertEqual(meetup(2013, 3, "third", "Monday"), date(2013, 3, 18))

    def test_when_third_monday_is_the_15th_the_first_day_of_the_third_week(self):
        self.assertEqual(meetup(2013, 4, "third", "Monday"), date(2013, 4, 15))

    def test_when_third_tuesday_is_the_21st_the_last_day_of_the_third_week(self):
        self.assertEqual(meetup(2013, 5, "third", "Tuesday"), date(2013, 5, 21))

    def test_when_third_tuesday_is_some_day_in_the_middle_of_the_third_week(self):
        self.assertEqual(meetup(2013, 6, "third", "Tuesday"), date(2013, 6, 18))

    def test_when_third_wednesday_is_some_day_in_the_middle_of_the_third_week(self):
        self.assertEqual(meetup(2013, 7, "third", "Wednesday"), date(2013, 7, 17))

    def test_when_third_wednesday_is_the_21st_the_last_day_of_the_third_week(self):
        self.assertEqual(meetup(2013, 8, "third", "Wednesday"), date(2013, 8, 21))

    def test_when_third_thursday_is_some_day_in_the_middle_of_the_third_week(self):
        self.assertEqual(meetup(2013, 9, "third", "Thursday"), date(2013, 9, 19))

    def test_when_third_thursday_is_another_day_in_the_middle_of_the_third_week(self):
        self.assertEqual(meetup(2013, 10, "third", "Thursday"), date(2013, 10, 17))

    def test_when_third_friday_is_the_15th_the_first_day_of_the_third_week(self):
        self.assertEqual(meetup(2013, 11, "third", "Friday"), date(2013, 11, 15))

    def test_when_third_friday_is_some_day_in_the_middle_of_the_third_week(self):
        self.assertEqual(meetup(2013, 12, "third", "Friday"), date(2013, 12, 20))

    def test_when_third_saturday_is_some_day_in_the_middle_of_the_third_week(self):
        self.assertEqual(meetup(2013, 1, "third", "Saturday"), date(2013, 1, 19))

    def test_when_third_saturday_is_another_day_in_the_middle_of_the_third_week(self):
        self.assertEqual(meetup(2013, 2, "third", "Saturday"), date(2013, 2, 16))

    def test_when_third_sunday_is_some_day_in_the_middle_of_the_third_week(self):
        self.assertEqual(meetup(2013, 3, "third", "Sunday"), date(2013, 3, 17))

    def test_when_third_sunday_is_the_21st_the_last_day_of_the_third_week(self):
        self.assertEqual(meetup(2013, 4, "third", "Sunday"), date(2013, 4, 21))

    def test_when_fourth_monday_is_some_day_in_the_middle_of_the_fourth_week(self):
        self.assertEqual(meetup(2013, 3, "fourth", "Monday"), date(2013, 3, 25))

    def test_when_fourth_monday_is_the_22nd_the_first_day_of_the_fourth_week(self):
        self.assertEqual(meetup(2013, 4, "fourth", "Monday"), date(2013, 4, 22))

    def test_when_fourth_tuesday_is_the_28th_the_last_day_of_the_fourth_week(self):
        self.assertEqual(meetup(2013, 5, "fourth", "Tuesday"), date(2013, 5, 28))

    def test_when_fourth_tuesday_is_some_day_in_the_middle_of_the_fourth_week(self):
        self.assertEqual(meetup(2013, 6, "fourth", "Tuesday"), date(2013, 6, 25))

    def test_when_fourth_wednesday_is_some_day_in_the_middle_of_the_fourth_week(self):
        self.assertEqual(meetup(2013, 7, "fourth", "Wednesday"), date(2013, 7, 24))

    def test_when_fourth_wednesday_is_the_28th_the_last_day_of_the_fourth_week(self):
        self.assertEqual(meetup(2013, 8, "fourth", "Wednesday"), date(2013, 8, 28))

    def test_when_fourth_thursday_is_some_day_in_the_middle_of_the_fourth_week(self):
        self.assertEqual(meetup(2013, 9, "fourth", "Thursday"), date(2013, 9, 26))

    def test_when_fourth_thursday_is_another_day_in_the_middle_of_the_fourth_week(self):
        self.assertEqual(meetup(2013, 10, "fourth", "Thursday"), date(2013, 10, 24))

    def test_when_fourth_friday_is_the_22nd_the_first_day_of_the_fourth_week(self):
        self.assertEqual(meetup(2013, 11, "fourth", "Friday"), date(2013, 11, 22))

    def test_when_fourth_friday_is_some_day_in_the_middle_of_the_fourth_week(self):
        self.assertEqual(meetup(2013, 12, "fourth", "Friday"), date(2013, 12, 27))

    def test_when_fourth_saturday_is_some_day_in_the_middle_of_the_fourth_week(self):
        self.assertEqual(meetup(2013, 1, "fourth", "Saturday"), date(2013, 1, 26))

    def test_when_fourth_saturday_is_another_day_in_the_middle_of_the_fourth_week(self):
        self.assertEqual(meetup(2013, 2, "fourth", "Saturday"), date(2013, 2, 23))

    def test_when_fourth_sunday_is_some_day_in_the_middle_of_the_fourth_week(self):
        self.assertEqual(meetup(2013, 3, "fourth", "Sunday"), date(2013, 3, 24))

    def test_when_fourth_sunday_is_the_28th_the_last_day_of_the_fourth_week(self):
        self.assertEqual(meetup(2013, 4, "fourth", "Sunday"), date(2013, 4, 28))

    def test_last_monday_in_a_month_with_four_mondays(self):
        self.assertEqual(meetup(2013, 3, "last", "Monday"), date(2013, 3, 25))

    def test_last_monday_in_a_month_with_five_mondays(self):
        self.assertEqual(meetup(2013, 4, "last", "Monday"), date(2013, 4, 29))

    def test_last_tuesday_in_a_month_with_four_tuesdays(self):
        self.assertEqual(meetup(2013, 5, "last", "Tuesday"), date(2013, 5, 28))

    def test_last_tuesday_in_another_month_with_four_tuesdays(self):
        self.assertEqual(meetup(2013, 6, "last", "Tuesday"), date(2013, 6, 25))

    def test_last_wednesday_in_a_month_with_five_wednesdays(self):
        self.assertEqual(meetup(2013, 7, "last", "Wednesday"), date(2013, 7, 31))

    def test_last_wednesday_in_a_month_with_four_wednesdays(self):
        self.assertEqual(meetup(2013, 8, "last", "Wednesday"), date(2013, 8, 28))

    def test_last_thursday_in_a_month_with_four_thursdays(self):
        self.assertEqual(meetup(2013, 9, "last", "Thursday"), date(2013, 9, 26))

    def test_last_thursday_in_a_month_with_five_thursdays(self):
        self.assertEqual(meetup(2013, 10, "last", "Thursday"), date(2013, 10, 31))

    def test_last_friday_in_a_month_with_five_fridays(self):
        self.assertEqual(meetup(2013, 11, "last", "Friday"), date(2013, 11, 29))

    def test_last_friday_in_a_month_with_four_fridays(self):
        self.assertEqual(meetup(2013, 12, "last", "Friday"), date(2013, 12, 27))

    def test_last_saturday_in_a_month_with_four_saturdays(self):
        self.assertEqual(meetup(2013, 1, "last", "Saturday"), date(2013, 1, 26))

    def test_last_saturday_in_another_month_with_four_saturdays(self):
        self.assertEqual(meetup(2013, 2, "last", "Saturday"), date(2013, 2, 23))

    def test_last_sunday_in_a_month_with_five_sundays(self):
        self.assertEqual(meetup(2013, 3, "last", "Sunday"), date(2013, 3, 31))

    def test_last_sunday_in_a_month_with_four_sundays(self):
        self.assertEqual(meetup(2013, 4, "last", "Sunday"), date(2013, 4, 28))

    def test_when_last_wednesday_in_february_in_a_leap_year_is_the_29th(self):
        self.assertEqual(meetup(2012, 2, "last", "Wednesday"), date(2012, 2, 29))

    def test_last_wednesday_in_december_that_is_also_the_last_day_of_the_year(self):
        self.assertEqual(meetup(2014, 12, "last", "Wednesday"), date(2014, 12, 31))

    def test_when_last_sunday_in_february_in_a_non_leap_year_is_not_the_29th(self):
        self.assertEqual(meetup(2015, 2, "last", "Sunday"), date(2015, 2, 22))

    def test_when_first_friday_is_the_7th_the_last_day_of_the_first_week(self):
        self.assertEqual(meetup(2012, 12, "first", "Friday"), date(2012, 12, 7))

    # Additional tests for this track

    def test_fifth_monday_of_march_2015(self):
        self.assertEqual(meetup(2015, 3, "fifth", "Monday"), date(2015, 3, 30))

    def test_fifth_thursday_of_february_2024(self):
        self.assertEqual(meetup(2024, 2, "fifth", "Thursday"), date(2024, 2, 29))

    def test_fifth_saturday_of_february_2020(self):
        self.assertEqual(meetup(2020, 2, "fifth", "Saturday"), date(2020, 2, 29))

    def test_last_sunday_of_june_2024(self):
        self.assertEqual(meetup(2024, 6, "last", "Sunday"), date(2024, 6, 30))

    def test_teenth_friday_of_may_2022(self):
        self.assertEqual(meetup(2022, 5, "teenth", "Friday"), date(2022, 5, 13))

    def test_nonexistent_fifth_monday_of_february_2022(self):
        with self.assertRaises(MeetupDayException) as err:
            meetup(2022, 2, "fifth", "Monday")
        self.assertEqual(type(err.exception), MeetupDayException)
        self.assertEqual(err.exception.args[0], "That day does not exist.")

    def test_nonexistent_fifth_friday_of_august_2022(self):
        with self.assertRaises(MeetupDayException) as err:
            meetup(2022, 8, "fifth", "Friday")
        self.assertEqual(type(err.exception), MeetupDayException)
        self.assertEqual(err.exception.args[0], "That day does not exist.")

    def test_nonexistent_fifth_thursday_of_may_2023(self):
        with self.assertRaises(MeetupDayException) as err:
            meetup(2023, 5, "fifth", "Thursday")
        self.assertEqual(type(err.exception), MeetupDayException)
        self.assertEqual(err.exception.args[0], "That day does not exist.")
