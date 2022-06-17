# this is really just a stub

import unittest
import pytest

from dellas-delays-at-the-dmv import (
                                      line_length,
                                      wait_minutes
                                      )


class DellasDelaysTest(unittest.TestCase):

    @pytest.mark.task(taskno=1)
    def test_line_length(self):
        data = [
                (9, 10), (10, 5), (11, 5),
                (12, 20), (1, 5), (2, 5),
                (3, 5), (4, 10)]

        for variant, (hour, length) in enumerate(data, 1):
            with self.subTest(f'variation #{variant}', input=hour, output=length):
                error_msg = f"Expected {length} for the length of the line at {hour} o'clock."

                self.assertEqual(line_length(hour), length, msg=error_msg)
                
    @pytest.mark.task(taskno=2)
        def test_wait_minutes(self):
        data = [
                (9, 50), (10, 25), (11, 25),
                (12, 100), (1, 25), (2, 25),
                (3, 25), (4, 50)]

        for variant, (hour, minutes) in enumerate(data, 1):
            with self.subTest(f'variation #{variant}', input=hour, output=minutes):
                error_msg = f"Expected {minutes} for the minutes to wait at {hour} o'clock."

                    self.assertEqual(wait_minutes(hour), minutes, msg=error_msg)
