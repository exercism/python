import unittest

from etl import transform


# Tests adapted from `problem-specifications//canonical-data.json` @ v2.0.0

class EtlTest(unittest.TestCase):
    def test_a_single_letter(self):
        self.assertEqual(transform({1: ['A']}), {'a': 1})

    def test_single_score_with_multiple_letters(self):
        legacy_data = {1: ["A", "E", "I", "O", "U"]}
        data = {"a": 1, "e": 1, "i": 1, "o": 1, "u": 1}
        self.assertEqual(transform(legacy_data), data)

    def test_multiple_scores_with_multiple_letters(self):
        legacy_data = {1: ["A", "E"], 2: ["D", "G"]}
        data = {"a": 1, "d": 2, "e": 1, "g": 2}
        self.assertEqual(transform(legacy_data), data)

    def test_multiple_scores_with_differing_numbers_of_letters(self):
        legacy_data = {
            1: ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"],
            2: ["D", "G"],
            3: ["B", "C", "M", "P"],
            4: ["F", "H", "V", "W", "Y"],
            5: ["K"],
            8: ["J", "X"],
            10: ["Q", "Z"]
        }
        data = {
            "a": 1, "b": 3, "c": 3, "d": 2, "e": 1, "f": 4,
            "g": 2, "h": 4, "i": 1, "j": 8, "k": 5, "l": 1,
            "m": 3, "n": 1, "o": 1, "p": 3, "q": 10, "r": 1,
            "s": 1, "t": 1, "u": 1, "v": 4, "w": 4, "x": 8,
            "y": 4, "z": 10
        }
        self.assertEqual(transform(legacy_data), data)


if __name__ == '__main__':
    unittest.main()
