# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/swift-scheduling/canonical-data.json
# File last updated on 2025-06-25

import unittest

from swift_scheduling import (
    delivery_date,
)


class SwiftSchedulingTest(unittest.TestCase):
    def test_now_translates_to_two_hours_later(self):
        self.assertEqual(
            delivery_date("2012-02-13T09:00:00", "NOW"), "2012-02-13T11:00:00"
        )

    def test_asap_before_one_in_the_afternoon_translates_to_today_at_five_in_the_afternoon(
        self,
    ):
        self.assertEqual(
            delivery_date("1999-06-03T09:45:00", "ASAP"), "1999-06-03T17:00:00"
        )

    def test_asap_at_one_in_the_afternoon_translates_to_tomorrow_at_one_in_the_afternoon(
        self,
    ):
        self.assertEqual(
            delivery_date("2008-12-21T13:00:00", "ASAP"), "2008-12-22T13:00:00"
        )

    def test_asap_after_one_in_the_afternoon_translates_to_tomorrow_at_one_in_the_afternoon(
        self,
    ):
        self.assertEqual(
            delivery_date("2008-12-21T14:50:00", "ASAP"), "2008-12-22T13:00:00"
        )

    def test_eow_on_monday_translates_to_friday_at_five_in_the_afternoon(self):
        self.assertEqual(
            delivery_date("2025-02-03T16:00:00", "EOW"), "2025-02-07T17:00:00"
        )

    def test_eow_on_tuesday_translates_to_friday_at_five_in_the_afternoon(self):
        self.assertEqual(
            delivery_date("1997-04-29T10:50:00", "EOW"), "1997-05-02T17:00:00"
        )

    def test_eow_on_wednesday_translates_to_friday_at_five_in_the_afternoon(self):
        self.assertEqual(
            delivery_date("2005-09-14T11:00:00", "EOW"), "2005-09-16T17:00:00"
        )

    def test_eow_on_thursday_translates_to_sunday_at_eight_in_the_evening(self):
        self.assertEqual(
            delivery_date("2011-05-19T08:30:00", "EOW"), "2011-05-22T20:00:00"
        )

    def test_eow_on_friday_translates_to_sunday_at_eight_in_the_evening(self):
        self.assertEqual(
            delivery_date("2022-08-05T14:00:00", "EOW"), "2022-08-07T20:00:00"
        )

    def test_eow_translates_to_leap_day(self):
        self.assertEqual(
            delivery_date("2008-02-25T10:30:00", "EOW"), "2008-02-29T17:00:00"
        )

    def test_2_m_before_the_second_month_of_this_year_translates_to_the_first_workday_of_the_second_month_of_this_year(
        self,
    ):
        self.assertEqual(
            delivery_date("2007-01-02T14:15:00", "2M"), "2007-02-01T08:00:00"
        )

    def test_11_m_in_the_eleventh_month_translates_to_the_first_workday_of_the_eleventh_month_of_next_year(
        self,
    ):
        self.assertEqual(
            delivery_date("2013-11-21T15:30:00", "11M"), "2014-11-03T08:00:00"
        )

    def test_4_m_in_the_ninth_month_translates_to_the_first_workday_of_the_fourth_month_of_next_year(
        self,
    ):
        self.assertEqual(
            delivery_date("2019-11-18T15:15:00", "4M"), "2020-04-01T08:00:00"
        )

    def test_q1_in_the_first_quarter_translates_to_the_last_workday_of_the_first_quarter_of_this_year(
        self,
    ):
        self.assertEqual(
            delivery_date("2003-01-01T10:45:00", "Q1"), "2003-03-31T08:00:00"
        )

    def test_q4_in_the_second_quarter_translates_to_the_last_workday_of_the_fourth_quarter_of_this_year(
        self,
    ):
        self.assertEqual(
            delivery_date("2001-04-09T09:00:00", "Q4"), "2001-12-31T08:00:00"
        )

    def test_q3_in_the_fourth_quarter_translates_to_the_last_workday_of_the_third_quarter_of_next_year(
        self,
    ):
        self.assertEqual(
            delivery_date("2022-10-06T11:00:00", "Q3"), "2023-09-29T08:00:00"
        )
