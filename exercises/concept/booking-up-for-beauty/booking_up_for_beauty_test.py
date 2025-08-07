import unittest
import pytest
import datetime

from booking_up_for_beauty import (
    schedule_numeric,
    schedule_mixed,
    has_passed,
    is_afternoon_appointment,
    description,
    anniversary)


class BookingUpForBeautyTest(unittest.TestCase):

    @pytest.mark.task(taskno=1)
    def test_schedule_numeric_date(self):

        test_data = ["07/25/2019 13:45:00",]
        result_data = [datetime.datetime(2019, 7, 25, 13, 45, 0),]

        for variant, (date_string, expected) in enumerate(zip(test_data, result_data), start=1):
            with self.subTest(f'variation #{variant}', date_string=date_string, expected=expected):

                actual_result = schedule_numeric(date_string)
                error_message = (f'Called schedule_numeric({date_string}). '
                                 f'The function returned {actual_result}, but '
                                 f'the tests expected {expected}.')

                self.assertEqual(actual_result, expected, msg=error_message)

    @pytest.mark.task(taskno=2)
    def test_schedule_mixed_date(self):

        test_data = ["Thursday, December 5, 2019 09:00:00",]
        result_data = [datetime.datetime(2019, 12, 5, 9, 0, 0),]

        for variant, (date_string, expected) in enumerate(zip(test_data, result_data), start=1):
            with self.subTest(f'variation #{variant}', date_string=date_string, expected=expected):

                actual_result = schedule_mixed(date_string)
                error_message = (f'Called schedule({date_string}). '
                                 f'The function returned {actual_result}, but '
                                 f'the tests expected {expected}.')

                self.assertEqual(actual_result, expected, msg=error_message)

    @pytest.mark.task(taskno=3)
    def test_has_passed(self):

        now = datetime.datetime.now()
        test_data = [now + datetime.timedelta(weeks=-52, hours=2),
                     now + datetime.timedelta(weeks=-8),
                     now + datetime.timedelta(days=-23),
                     now + datetime.timedelta(hours=-12),
                     now + datetime.timedelta(minutes=-55),
                     now + datetime.timedelta(minutes=-1),
                     now + datetime.timedelta(minutes=1),
                     now + datetime.timedelta(minutes=5),
                     ]
        result_data = [True,
                       True,
                       True,
                       True,
                       True,
                       True,
                       False,
                       False]

        for variant, (appointment, expected) in enumerate(zip(test_data, result_data), start=1):
            with self.subTest(f'variation #{variant}', appointment=appointment, expected=expected):

                actual_result = has_passed(appointment)
                error_message = (f'Called schedule({appointment}). '
                                 f'The function returned {actual_result}, but '
                                 f'the tests expected {expected}.')

                self.assertEqual(actual_result, expected, msg=error_message)

    @pytest.mark.task(taskno=4)
    def test_is_afternoon_appointment(self):

        test_data = [datetime.datetime(2019, 6, 17, 8, 15, 0),
                     datetime.datetime(2019, 2, 23, 11, 59, 59),
                     datetime.datetime(2019, 8, 9, 12, 0, 0),
                     datetime.datetime(2019, 8, 9, 12, 0, 1),
                     datetime.datetime(2019, 9, 1, 17, 59, 59),
                     datetime.datetime(2019, 9, 1, 18, 0, 0),
                     datetime.datetime(2019, 9, 1, 23, 59, 59)]
        result_data = [False,
                       False,
                       True,
                       True,
                       True,
                       False,
                       False]

        for variant, (appointment, expected) in enumerate(zip(test_data, result_data), start=1):
            with self.subTest(f'variation #{variant}', appointment=appointment, expected=expected):

                actual_result = is_afternoon_appointment(appointment)
                error_message = (f'Called schedule({appointment}). '
                                 f'The function returned {actual_result}, but '
                                 f'the tests expected {expected}.')

                self.assertEqual(actual_result, expected, msg=error_message)

    @pytest.mark.task(taskno=5)
    def test_description(self):

        test_data = [datetime.datetime(2019, 3, 29, 15, 0, 0),
                     datetime.datetime(2019, 7, 25, 13, 45, 0),
                     datetime.datetime(2020, 9, 9, 9, 9, 9)]
        result_data = ["You have an appointment on 03/29/19 03:00:00 PM.",
                       "You have an appointment on 07/25/19 01:45:00 PM.",
                       "You have an appointment on 09/09/20 09:09:09 AM."]

        for variant, (appointment, expected) in enumerate(zip(test_data, result_data), start=1):
            with self.subTest(f'variation #{variant}', appointment=appointment, expected=expected):

                actual_result = description(appointment)
                error_message = (f'Called schedule({appointment}). '
                                 f'The function returned {actual_result}, but '
                                 f'the tests expected {expected}.')

                self.assertEqual(actual_result, expected, msg=error_message)

    @pytest.mark.task(taskno=6)
    def test_anniversary(self):

        actual_result = anniversary()
        expected = datetime.date(datetime.datetime.now().year, 9, 15)
        error_message = (f'Called anniversary()'
                         f'The function returned {actual_result}, but '
                         f'the tests expected {expected}.')

        self.assertEqual(actual_result, expected, msg=error_message)
