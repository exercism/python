import unittest

from high_scores import latest, personal_best, personal_top_three


# Tests adapted from `problem-specifications//canonical-data.json` @ v4.0.0


class HighScoreTest(unittest.TestCase):

    def test_latest_score(self):
        scores = [100, 0, 90, 30]
        expected = 30
        self.assertEqual(latest(scores), expected)

    def test_personal_best(self):
        scores = [40, 100, 70]
        expected = 100
        self.assertEqual(personal_best(scores), expected)

    def test_personal_top_three_from_a_long_list(self):
        scores = [10, 30, 90, 30, 100, 20, 10, 0, 30, 40, 40, 70, 70]
        expected = [100, 90, 70]
        self.assertEqual(personal_top_three(scores), expected)

    def test_personal_top_three_highest_to_lowest(self):
        scores = [20, 10, 30]
        expected = [30, 20, 10]
        self.assertEqual(personal_top_three(scores), expected)

    def test_personal_top_three_when_there_is_a_tie(self):
        scores = [40, 20, 40, 30]
        expected = [40, 40, 30]
        self.assertEqual(personal_top_three(scores), expected)

    def test_personal_top_three_when_there_are_less_than_3(self):
        scores = [30, 70]
        expected = [70, 30]
        self.assertEqual(personal_top_three(scores), expected)

    def test_personal_top_three_when_there_is_only_one(self):
        scores = [40]
        expected = [40]
        self.assertEqual(personal_top_three(scores), expected)


if __name__ == "__main__":
    unittest.main()
