import unittest

from global_meeting import meeting_time

class GlobalMeetingTest(unittest.TestCase):
    def test_same_working_times(self):
        self.assertEqual(meeting_time({
            111: [2, (8, 17)],
            112: [8, (8, 17)],
            113: [10, (8, 17)],
        }), [6])

    def test_different_working_times(self):
        self.assertEqual(meeting_time({
            201: [5.5, (8, 17)],
            202: [-4, (15, 0)],
            203: [-10, (12, 21)],
            204: [3, (4, 13)],
        }), [3])

    def test_wrong_values(self):
        with self.assertRaises(ValueError) as err:
            meeting_time({
                201: [2, (5, 15)],
                202: [5, (13, 22)],
            })
        self.assertEqual("some employees are working for more or less than 9 hours", str(err.exception))

    def test_impossible(self):
        with self.assertRaises(ValueError) as err:
            meeting_time({
                201: [2, (13, 22)],
                202: [5, (5, 14)],
            })
        self.assertEqual("there's no possible meeting time for the provided employees", str(err.exception))

if __name__ == "__main__":
    unittest.main()
