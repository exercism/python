import unittest

from high_scores import HighScores


# Tests adapted from `problem-specifications//canonical-data.json` @ v2.0.0


class HighScoreTest(unittest.TestCase):
    def test_list_of_scores(self):
        scores = [30, 50, 20, 70]
        expected = [30, 50, 20, 70]
        self.assertEqual(HighScores(scores).scores, expected)

    def test_latest_score(self):
        scores = [100, 0, 90, 30]
        expected = 30
        self.assertEqual(HighScores(scores).latest(), expected)

    def test_personal_best(self):
        scores = [40, 100, 70]
        expected = 100
        self.assertEqual(HighScores(scores).personal_best(), expected)

    def test_personal_top(self):
        scores = [50, 30, 10]
        expected = [50, 30, 10]
        self.assertEqual(HighScores(scores).personal_top(), expected)

    def test_personal_top_highest_to_lowest(self):
        scores = [20, 10, 30]
        expected = [30, 20, 10]
        self.assertEqual(HighScores(scores).personal_top(), expected)

    def test_personal_top_when_there_is_a_tie(self):
        scores = [40, 20, 40, 30]
        expected = [40, 40, 30]
        self.assertEqual(HighScores(scores).personal_top(), expected)

    def test_personal_top_when_there_are_less_than_3(self):
        scores = [30, 70]
        expected = [70, 30]
        self.assertEqual(HighScores(scores).personal_top(), expected)

    def test_personal_top_when_there_is_only_one(self):
        scores = [40]
        expected = [40]
        self.assertEqual(HighScores(scores).personal_top(), expected)

    def test_personal_top_from_a_long_list(self):
        scores = [10, 30, 90, 30, 100, 20, 10, 0, 30, 40, 40, 70, 70]
        expected = [100, 90, 70]
        self.assertEqual(HighScores(scores).personal_top(), expected)

    def test_message_for_new_personal_best(self):
        scores = [20, 40, 0, 30, 70]
        expected = "Your latest score was 70. That's your personal best!"
        self.assertEqual(HighScores(scores).report(), expected)

    def test_message_when_latest_score_is_not_the_highest_score(self):
        scores = [20, 100, 0, 30, 70]
        expected = (
            "Your latest score was 70. That's 30 short of your personal best!"
        )
        self.assertEqual(HighScores(scores).report(), expected)

    def test_message_for_repeated_personal_best(self):
        scores = [20, 70, 50, 70, 30]
        expected = (
            "Your latest score was 30. That's 40 short of your personal best!"
        )
        self.assertEqual(HighScores(scores).report(), expected)


if __name__ == "__main__":
    unittest.main()
