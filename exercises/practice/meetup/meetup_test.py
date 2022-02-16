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
        self.assertEqual(meetup(2013, 3, "1st", "Monday"), date(2013, 3, 4))

    def test_when_first_monday_is_the_1st_the_first_day_of_the_first_week(self):
        self.assertEqual(meetup(2013, 4, "1st", "Monday"), date(2013, 4, 1))

    def test_when_first_tuesday_is_the_7th_the_last_day_of_the_first_week(self):
        self.assertEqual(meetup(2013, 5, "1st", "Tuesday"), date(2013, 5, 7))

    def test_when_first_tuesday_is_some_day_in_the_middle_of_the_first_week(self):
        self.assertEqual(meetup(2013, 6, "1st", "Tuesday"), date(2013, 6, 4))

    def test_when_first_wednesday_is_some_day_in_the_middle_of_the_first_week(self):
        self.assertEqual(meetup(2013, 7, "1st", "Wednesday"), date(2013, 7, 3))

    def test_when_first_wednesday_is_the_7th_the_last_day_of_the_first_week(self):
        self.assertEqual(meetup(2013, 8, "1st", "Wednesday"), date(2013, 8, 7))

    def test_when_first_thursday_is_some_day_in_the_middle_of_the_first_week(self):
        self.assertEqual(meetup(2013, 9, "1st", "Thursday"), date(2013, 9, 5))

    def test_when_first_thursday_is_another_day_in_the_middle_of_the_first_week(self):
        self.assertEqual(meetup(2013, 10, "1st", "Thursday"), date(2013, 10, 3))

    def test_when_first_friday_is_the_1st_the_first_day_of_the_first_week(self):
        self.assertEqual(meetup(2013, 11, "1st", "Friday"), date(2013, 11, 1))

    def test_when_first_friday_is_some_day_in_the_middle_of_the_first_week(self):
        self.assertEqual(meetup(2013, 12, "1st", "Friday"), date(2013, 12, 6))

    def test_when_first_saturday_is_some_day_in_the_middle_of_the_first_week(self):
        self.assertEqual(meetup(2013, 1, "1st", "Saturday"), date(2013, 1, 5))

    def test_when_first_saturday_is_another_day_in_the_middle_of_the_first_week(self):
        self.assertEqual(meetup(2013, 2, "1st", "Saturday"), date(2013, 2, 2))

    def test_when_first_sunday_is_some_day_in_the_middle_of_the_first_week(self):
        self.assertEqual(meetup(2013, 3, "1st", "Sunday"), date(2013, 3, 3))

    def test_when_first_sunday_is_the_7th_the_last_day_of_the_first_week(self):
        self.assertEqual(meetup(2013, 4, "1st", "Sunday"), date(2013, 4, 7))

    def test_when_second_monday_is_some_day_in_the_middle_of_the_second_week(self):
        self.assertEqual(meetup(2013, 3, "2nd", "Monday"), date(2013, 3, 11))

    def test_when_second_monday_is_the_8th_the_first_day_of_the_second_week(self):
        self.assertEqual(meetup(2013, 4, "2nd", "Monday"), date(2013, 4, 8))

    def test_when_second_tuesday_is_the_14th_the_last_day_of_the_second_week(self):
        self.assertEqual(meetup(2013, 5, "2nd", "Tuesday"), date(2013, 5, 14))

    def test_when_second_tuesday_is_some_day_in_the_middle_of_the_second_week(self):
        self.assertEqual(meetup(2013, 6, "2nd", "Tuesday"), date(2013, 6, 11))

    def test_when_second_wednesday_is_some_day_in_the_middle_of_the_second_week(self):
        self.assertEqual(meetup(2013, 7, "2nd", "Wednesday"), date(2013, 7, 10))

    def test_when_second_wednesday_is_the_14th_the_last_day_of_the_second_week(self):
        self.assertEqual(meetup(2013, 8, "2nd", "Wednesday"), date(2013, 8, 14))

    def test_when_second_thursday_is_some_day_in_the_middle_of_the_second_week(self):
        self.assertEqual(meetup(2013, 9, "2nd", "Thursday"), date(2013, 9, 12))

    def test_when_second_thursday_is_another_day_in_the_middle_of_the_second_week(self):
        self.assertEqual(meetup(2013, 10, "2nd", "Thursday"), date(2013, 10, 10))

    def test_when_second_friday_is_the_8th_the_first_day_of_the_second_week(self):
        self.assertEqual(meetup(2013, 11, "2nd", "Friday"), date(2013, 11, 8))

    def test_when_second_friday_is_some_day_in_the_middle_of_the_second_week(self):
        self.assertEqual(meetup(2013, 12, "2nd", "Friday"), date(2013, 12, 13))

    def test_when_second_saturday_is_some_day_in_the_middle_of_the_second_week(self):
        self.assertEqual(meetup(2013, 1, "2nd", "Saturday"), date(2013, 1, 12))

    def test_when_second_saturday_is_another_day_in_the_middle_of_the_second_week(self):
        self.assertEqual(meetup(2013, 2, "2nd", "Saturday"), date(2013, 2, 9))

    def test_when_second_sunday_is_some_day_in_the_middle_of_the_second_week(self):
        self.assertEqual(meetup(2013, 3, "2nd", "Sunday"), date(2013, 3, 10))

    def test_when_second_sunday_is_the_14th_the_last_day_of_the_second_week(self):
        self.assertEqual(meetup(2013, 4, "2nd", "Sunday"), date(2013, 4, 14))

    def test_when_third_monday_is_some_day_in_the_middle_of_the_third_week(self):
        self.assertEqual(meetup(2013, 3, "3rd", "Monday"), date(2013, 3, 18))

    def test_when_third_monday_is_the_15th_the_first_day_of_the_third_week(self):
        self.assertEqual(meetup(2013, 4, "3rd", "Monday"), date(2013, 4, 15))

    def test_when_third_tuesday_is_the_21st_the_last_day_of_the_third_week(self):
        self.assertEqual(meetup(2013, 5, "3rd", "Tuesday"), date(2013, 5, 21))

    def test_when_third_tuesday_is_some_day_in_the_middle_of_the_third_week(self):
        self.assertEqual(meetup(2013, 6, "3rd", "Tuesday"), date(2013, 6, 18))

    def test_when_third_wednesday_is_some_day_in_the_middle_of_the_third_week(self):
        self.assertEqual(meetup(2013, 7, "3rd", "Wednesday"), date(2013, 7, 17))

    def test_when_third_wednesday_is_the_21st_the_last_day_of_the_third_week(self):
        self.assertEqual(meetup(2013, 8, "3rd", "Wednesday"), date(2013, 8, 21))

    def test_when_third_thursday_is_some_day_in_the_middle_of_the_third_week(self):
        self.assertEqual(meetup(2013, 9, "3rd", "Thursday"), date(2013, 9, 19))

    def test_when_third_thursday_is_another_day_in_the_middle_of_the_third_week(self):
        self.assertEqual(meetup(2013, 10, "3rd", "Thursday"), date(2013, 10, 17))

    def test_when_third_friday_is_the_15th_the_first_day_of_the_third_week(self):
        self.assertEqual(meetup(2013, 11, "3rd", "Friday"), date(2013, 11, 15))

    def test_when_third_friday_is_some_day_in_the_middle_of_the_third_week(self):
        self.assertEqual(meetup(2013, 12, "3rd", "Friday"), date(2013, 12, 20))

    def test_when_third_saturday_is_some_day_in_the_middle_of_the_third_week(self):
        self.assertEqual(meetup(2013, 1, "3rd", "Saturday"), date(2013, 1, 19))

    def test_when_third_saturday_is_another_day_in_the_middle_of_the_third_week(self):
        self.assertEqual(meetup(2013, 2, "3rd", "Saturday"), date(2013, 2, 16))

    def test_when_third_sunday_is_some_day_in_the_middle_of_the_third_week(self):
        self.assertEqual(meetup(2013, 3, "3rd", "Sunday"), date(2013, 3, 17))

    def test_when_third_sunday_is_the_21st_the_last_day_of_the_third_week(self):
        self.assertEqual(meetup(2013, 4, "3rd", "Sunday"), date(2013, 4, 21))

    def test_when_fourth_monday_is_some_day_in_the_middle_of_the_fourth_week(self):
        self.assertEqual(meetup(2013, 3, "4th", "Monday"), date(2013, 3, 25))

    def test_when_fourth_monday_is_the_22nd_the_first_day_of_the_fourth_week(self):
        self.assertEqual(meetup(2013, 4, "4th", "Monday"), date(2013, 4, 22))

    def test_when_fourth_tuesday_is_the_28th_the_last_day_of_the_fourth_week(self):
        self.assertEqual(meetup(2013, 5, "4th", "Tuesday"), date(2013, 5, 28))

    def test_when_fourth_tuesday_is_some_day_in_the_middle_of_the_fourth_week(self):
        self.assertEqual(meetup(2013, 6, "4th", "Tuesday"), date(2013, 6, 25))

    def test_when_fourth_wednesday_is_some_day_in_the_middle_of_the_fourth_week(self):
        self.assertEqual(meetup(2013, 7, "4th", "Wednesday"), date(2013, 7, 24))

    def test_when_fourth_wednesday_is_the_28th_the_last_day_of_the_fourth_week(self):
        self.assertEqual(meetup(2013, 8, "4th", "Wednesday"), date(2013, 8, 28))

    def test_when_fourth_thursday_is_some_day_in_the_middle_of_the_fourth_week(self):
        self.assertEqual(meetup(2013, 9, "4th", "Thursday"), date(2013, 9, 26))

    def test_when_fourth_thursday_is_another_day_in_the_middle_of_the_fourth_week(self):
        self.assertEqual(meetup(2013, 10, "4th", "Thursday"), date(2013, 10, 24))

    def test_when_fourth_friday_is_the_22nd_the_first_day_of_the_fourth_week(self):
        self.assertEqual(meetup(2013, 11, "4th", "Friday"), date(2013, 11, 22))

    def test_when_fourth_friday_is_some_day_in_the_middle_of_the_fourth_week(self):
        self.assertEqual(meetup(2013, 12, "4th", "Friday"), date(2013, 12, 27))

    def test_when_fourth_saturday_is_some_day_in_the_middle_of_the_fourth_week(self):
        self.assertEqual(meetup(2013, 1, "4th", "Saturday"), date(2013, 1, 26))

    def test_when_fourth_saturday_is_another_day_in_the_middle_of_the_fourth_week(self):
        self.assertEqual(meetup(2013, 2, "4th", "Saturday"), date(2013, 2, 23))

    def test_when_fourth_sunday_is_some_day_in_the_middle_of_the_fourth_week(self):
        self.assertEqual(meetup(2013, 3, "4th", "Sunday"), date(2013, 3, 24))

    def test_when_fourth_sunday_is_the_28th_the_last_day_of_the_fourth_week(self):
        self.assertEqual(meetup(2013, 4, "4th", "Sunday"), date(2013, 4, 28))

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
        self.assertEqual(meetup(2012, 12, "1st", "Friday"), date(2012, 12, 7))

    # Additional tests for this track

    def test_fifth_monday_of_march_2015(self):
        self.assertEqual(meetup(2015, 3, "5th", "Monday"), date(2015, 3, 30))

    def test_fifth_thursday_of_february_2024(self):
        self.assertEqual(meetup(2024, 2, "5th", "Thursday"), date(2024, 2, 29))

    def test_fifth_saturday_of_february_2020(self):
        self.assertEqual(meetup(2020, 2, "5th", "Saturday"), date(2020, 2, 29))

    def test_last_sunday_of_june_2024(self):
        self.assertEqual(meetup(2024, 6, "last", "Sunday"), date(2024, 6, 30))

    def test_teenth_friday_of_may_2022(self):
        self.assertEqual(meetup(2022, 5, "teenth", "Friday"), date(2022, 5, 13))

    def test_nonexistent_fifth_monday_of_february_2022(self):
        with self.assertRaises(MeetupDayException) as err:
            meetup(2022, 2, "5th", "Monday")
        self.assertEqual(type(err.exception), MeetupDayException)
        self.assertEqual(err.exception.args[0], "That day does not exist.")

    def test_nonexistent_fifth_friday_of_august_2022(self):
        with self.assertRaises(MeetupDayException) as err:
            meetup(2022, 8, "5th", "Friday")
        self.assertEqual(type(err.exception), MeetupDayException)
        self.assertEqual(err.exception.args[0], "That day does not exist.")

    def test_nonexistent_fifth_thursday_of_may_2023(self):
        with self.assertRaises(MeetupDayException) as err:
            meetup(2023, 5, "5th", "Thursday")
        self.assertEqual(type(err.exception), MeetupDayException)
        self.assertEqual(err.exception.args[0], "That day does not exist.")
