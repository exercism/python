from datetime import datetime
import unittest

from gigasecond import add

# Tests adapted from `problem-specifications//canonical-data.json` @ v2.0.0


class GigasecondTest(unittest.TestCase):
    def test_date_only_specification_of_time(self):
        self.assertEqual(
            add(datetime.fromisoformat("2011-04-25")),
            datetime.fromisoformat("2043-01-01T01:46:40"),
        )

    def test_second_test_for_date_only_specification_of_time(self):
        self.assertEqual(
            add(datetime.fromisoformat("1977-06-13")),
            datetime.fromisoformat("2009-02-19T01:46:40"),
        )

    def test_third_test_for_date_only_specification_of_time(self):
        self.assertEqual(
            add(datetime.fromisoformat("1959-07-19")),
            datetime.fromisoformat("1991-03-27T01:46:40"),
        )

    def test_full_time_specified(self):
        self.assertEqual(
            add(datetime.fromisoformat("2015-01-24T22:00:00")),
            datetime.fromisoformat("2046-10-02T23:46:40"),
        )

    def test_full_time_with_day_roll_over(self):
        self.assertEqual(
            add(datetime.fromisoformat("2015-01-24T23:59:59")),
            datetime.fromisoformat("2046-10-03T01:46:39"),
        )


if __name__ == "__main__":
    unittest.main()
