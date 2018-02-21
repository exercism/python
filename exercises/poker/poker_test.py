import unittest

from poker import best_hands


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.1.0

class PokerTest(unittest.TestCase):
    def test_single_hand_always_wins(self):
        hands = ["4S 5S 7H 8D JC"]
        expected = ["4S 5S 7H 8D JC"]
        self.assertEqual(best_hands(hands), expected)

    def test_highest_card_out_of_all_hands_wins(self):
        hands = [
            "4D 5S 6S 8D 3C",
            "2S 4C 7S 9H 10H",
            "3S 4S 5D 6H JH",
        ]
        expected = ["3S 4S 5D 6H JH"]
        self.assertEqual(best_hands(hands), expected)

    def test_tie_has_multiple_winners(self):
        hands = [
            "4D 5S 6S 8D 3C",
            "2S 4C 7S 9H 10H",
            "3S 4S 5D 6H JH",
            "3H 4H 5C 6C JD",
        ]
        expected = [
            "3S 4S 5D 6H JH",
            "3H 4H 5C 6C JD",
        ]
        self.assertEqual(best_hands(hands), expected)

    def test_tie_compares_multiple(self):
        hands = [
            "3S 5H 6S 8D 7H",
            "2S 5D 6D 8C 7S",
        ]
        expected = ["3S 5H 6S 8D 7H"]
        self.assertEqual(best_hands(hands), expected)

    def test_one_pair_beats_high_card(self):
        hands = [
            "4S 5H 6C 8D KH",
            "2S 4H 6S 4D JH",
        ]
        expected = ["2S 4H 6S 4D JH"]
        self.assertEqual(best_hands(hands), expected)

    def test_highest_pair_wins(self):
        hands = [
            "4S 2H 6S 2D JH",
            "2S 4H 6C 4D JD",
        ]
        expected = ["2S 4H 6C 4D JD"]
        self.assertEqual(best_hands(hands), expected)

    def test_two_pairs_beats_one_pair(self):
        hands = [
            "2S 8H 6S 8D JH",
            "4S 5H 4C 8C 5C",
        ]
        expected = ["4S 5H 4C 8C 5C"]
        self.assertEqual(best_hands(hands), expected)

    def test_two_double_pair(self):
        hands = [
            "2S 8H 2D 8D 3H",
            "4S 5H 4C 8S 5D",
        ]
        expected = ["2S 8H 2D 8D 3H"]
        self.assertEqual(best_hands(hands), expected)

    def test_two_double_pair_higher_tie(self):
        hands = [
            "2S QS 2C QD JH",
            "JD QH JS 8D QC",
        ]
        expected = ["JD QH JS 8D QC"]
        self.assertEqual(best_hands(hands), expected)

    def test_two_double_pair_tie_kicker(self):
        hands = [
            "JD QH JS 8D QC",
            "JS QS JC 2D QD",
        ]
        expected = ["JD QH JS 8D QC"]
        self.assertEqual(best_hands(hands), expected)

    def test_three_of_a_kind_beats_two_pair(self):
        hands = [
            "2S 8H 2H 8D JH",
            "4S 5H 4C 8S 4H",
        ]
        expected = ["4S 5H 4C 8S 4H"]
        self.assertEqual(best_hands(hands), expected)

    def test_two_triple_pair(self):
        hands = [
            "2S 2H 2C 8D JH",
            "4S AH AS 8C AD",
        ]
        expected = ["4S AH AS 8C AD"]
        self.assertEqual(best_hands(hands), expected)

    def test_two_three_multiple_decks(self):
        hands = [
            "4S AH AS 7C AD",
            "4S AH AS 8C AD",
        ]
        expected = ["4S AH AS 8C AD"]
        self.assertEqual(best_hands(hands), expected)

    def test_three_vs_straight(self):
        hands = [
            "4S 5H 4C 8D 4H",
            "3S 4D 2S 6D 5C",
        ]
        expected = ["3S 4D 2S 6D 5C"]
        self.assertEqual(best_hands(hands), expected)

    def test_aces_can_end_straight(self):
        hands = [
            "4S 5H 4C 8D 4H",
            "10D JH QS KD AC",
        ]
        expected = ["10D JH QS KD AC"]
        self.assertEqual(best_hands(hands), expected)

    def test_aces_can_start_straight(self):
        hands = [
            "4S 5H 4C 8D 4H",
            "4D AH 3S 2D 5C",
        ]
        expected = ["4D AH 3S 2D 5C"]
        self.assertEqual(best_hands(hands), expected)

    def test_two_straights(self):
        hands = [
            "4S 6C 7S 8D 5H",
            "5S 7H 8S 9D 6H",
        ]
        expected = ["5S 7H 8S 9D 6H"]
        self.assertEqual(best_hands(hands), expected)

    def test_lowest_straight(self):
        hands = [
            "2H 3C 4D 5D 6H",
            "4S AH 3S 2D 5H",
        ]
        expected = ["2H 3C 4D 5D 6H"]
        self.assertEqual(best_hands(hands), expected)

    def test_straight_vs_flush(self):
        hands = [
            "4C 6H 7D 8D 5H",
            "2S 4S 5S 6S 7S",
        ]
        expected = ["2S 4S 5S 6S 7S"]
        self.assertEqual(best_hands(hands), expected)

    def test_two_flushes(self):
        hands = [
            "4H 7H 8H 9H 6H",
            "2S 4S 5S 6S 7S",
        ]
        expected = ["4H 7H 8H 9H 6H"]
        self.assertEqual(best_hands(hands), expected)

    def test_flush_vs_full(self):
        hands = [
            "3H 6H 7H 8H 5H",
            "4S 5H 4C 5D 4H",
        ]
        expected = ["4S 5H 4C 5D 4H"]
        self.assertEqual(best_hands(hands), expected)

    def test_two_fulls(self):
        hands = [
            "4H 4S 4D 9S 9D",
            "5H 5S 5D 8S 8D",
        ]
        expected = ["5H 5S 5D 8S 8D"]
        self.assertEqual(best_hands(hands), expected)

    def test_two_fulls_same_triplet(self):
        hands = [
            "5H 5S 5D 9S 9D",
            "5H 5S 5D 8S 8D",
        ]
        expected = ["5H 5S 5D 9S 9D"]
        self.assertEqual(best_hands(hands), expected)

    def test_full_vs_four(self):
        hands = [
            "4S 5H 4D 5D 4H",
            "3S 3H 2S 3D 3C",
        ]
        expected = ["3S 3H 2S 3D 3C"]
        self.assertEqual(best_hands(hands), expected)

    def test_two_fours(self):
        hands = [
            "2S 2H 2C 8D 2D",
            "4S 5H 5S 5D 5C",
        ]
        expected = ["4S 5H 5S 5D 5C"]
        self.assertEqual(best_hands(hands), expected)

    def test_two_fours_kicker(self):
        hands = [
            "3S 3H 2S 3D 3C",
            "3S 3H 4S 3D 3C",
        ]
        expected = ["3S 3H 4S 3D 3C"]
        self.assertEqual(best_hands(hands), expected)

    def test_four_vs_straight_flush(self):
        hands = [
            "4S 5H 5S 5D 5C",
            "7S 8S 9S 6S 10S",
        ]
        expected = ["7S 8S 9S 6S 10S"]
        self.assertEqual(best_hands(hands), expected)

    def test_two_straight_flushes(self):
        hands = [
            "4H 6H 7H 8H 5H",
            "5S 7S 8S 9S 6S",
        ]
        expected = ["5S 7S 8S 9S 6S"]
        self.assertEqual(best_hands(hands), expected)


if __name__ == '__main__':
    unittest.main()
