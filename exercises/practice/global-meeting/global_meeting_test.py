import unittest

from global_meeting import meeting_time


class GlobalMeetingTest(unittest.TestCase):
    def test_different_working_times(self):
        self.assertEqual(
            meeting_time(
                "06/21/2023",
                {
                    110: (5.5, "08:00 AM", "05:00 PM"),
                    111: (-10, "12:00 PM", "09:00 PM"),
                    112: (3, "04:00 AM", "01:00 PM"),
                    113: (-4, "04:00 PM", "01:00 AM"),
                },
            ),
            {
                "03:00 AM": {
                    110: "06/21/2023 08:30 AM",
                    111: "06/20/2023 05:00 PM",
                    112: "06/21/2023 06:00 AM",
                    113: "06/20/2023 11:00 PM",
                },
                "04:00 AM": {
                    110: "06/21/2023 09:30 AM",
                    111: "06/20/2023 06:00 PM",
                    112: "06/21/2023 07:00 AM",
                    113: "06/21/2023 12:00 AM",
                },
            },
        )


    unittest.main()
