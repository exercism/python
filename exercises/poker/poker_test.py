import unittest

from poker import poker


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.0.0

class PokerTest(unittest.TestCase):
    def test_single_hand_wins(self):
        hand = '4S 5S 7H 8D JC'.split()
        self.assertEqual(poker([hand]), [hand])

    def highest_card_wins(self):
        first = '4D 5S 6S 8D 3C'.split()
        second = '2S 4C 7S 9H 10H'.split()
        third = '3S 4S 5D 6H JH'.split()
        self.assertEqual(poker([first, second, third]), [third])

    def tie_has_multiple_winners(self):
        first = '4D 5S 6S 8D 3C'.split()
        second = '2S 4C 7S 9H 10H'.split()
        third = '3S 4S 5D 6H JH'.split()
        fourth = '3H 4H 5C 6C JD'.split()
        self.assertEqual(
            poker([first, second, third, fourth]),
            [third, fourth])

    def tie_compares_multiple(self):
        higher = '3S 5H 6S 8D 7H'.split()
        lower = '2S 5D 6D 8C 7S'.split()
        self.assertEqual(poker([higher, lower]), [higher])

    def pair_beats_high_card(self):
        nothing = '4S 5H 6C 8D KH'.split()
        pairOf4 = '2S 4H 6S 4D JH'.split()
        self.assertEqual(poker([nothing, pairOf4]), [pairOf4])

    def highest_pair_wins(self):
        pairOf2 = '4S 2H 6S 2D JH'.split()
        pairOf4 = '2S 4H 6C 4D JD'.split()
        self.assertEqual(poker([pairOf2, pairOf4]), [pairOf4])

    def two_pairs_beats_one_pair(self):
        pairOf8 = '2S 8H 6S 8D JH'.split()
        doublePair = '4S 5H 4C 8C 5C'.split()
        self.assertEqual(poker([pairOf8, doublePair]), [doublePair])

    def test_two_double_pair(self):
        doublePair2and8 = '2S 8H 2D 8D 3H'.split()
        doublePair4and5 = '4S 5H 4C 8S 5D'.split()
        self.assertEqual(
            poker([doublePair2and8, doublePair4and5]), [doublePair2and8])

    def test_two_double_pair_higher_tie(self):
        doublePair2andQ = '2S QS 2C QD JH'.split()
        doublePairJandQ = 'JD QH JS 8D QC'.split()
        self.assertEqual(
            poker([doublePair2andQ, doublePairJandQ]), [doublePairJandQ])

    def test_two_double_pair_tie_kicker(self):
        doublePair2and8high = 'JD QH JS 8D QC'.split()
        doublePair2and8 = 'JS QS JC 2D QD'.split()
        self.assertEqual(
            poker([doublePair2and8high, doublePair2and8]),
            [doublePair2and8high])

    def three_beats_two_pair(self):
        doublePair2and8 = '2S 8H 2H 8D JH'.split()
        threeOf4 = '4S 5H 4C 8S 4H'.split()
        self.assertEqual(poker([doublePair2and8, threeOf4]), [threeOf4])

    def test_two_three(self):
        threeOf2 = '2S 2H 2C 8D JH'.split()
        threeOf1 = '4S AH AS 8C AD'.split()
        self.assertEqual(poker([threeOf2, threeOf1]), [threeOf1])

    def test_two_three_multiple_decks(self):
        threeOf1Low = '4S AH AS 7C AD'.split()
        threeOf1High = '4S AH AS 8C AD'.split()
        self.assertEqual(poker([threeOf1Low, threeOf1High]), [threeOf1High])

    def test_three_vs_straight(self):
        threeOf4 = '4S 5H 4C 8D 4H'.split()
        straight = '3S 4D 2S 6D 5C'.split()
        self.assertEqual(poker([threeOf4, straight]), [straight])

    def aces_can_end_straight(self):
        threeOf4 = '4S 5H 4C 8D 4H'.split()
        straight = '10D JH QS KD AC'.split()
        self.assertEqual(poker([threeOf4, straight]), [straight])

    def aces_can_start_straight(self):
        threeOf4 = '4S 5H 4C 8D 4H'.split()
        straight = '4D AH 3S 2D 5C'.split()
        self.assertEqual(poker([threeOf4, straight]), [straight])

    def test_two_straights(self):
        straightTo8 = '4S 6C 7S 8D 5H'.split()
        straightTo9 = '5S 7H 8S 9D 6H'.split()
        self.assertEqual(poker([straightTo8, straightTo9]), [straightTo9])

    def test_two_straights_lowest(self):
        straightTo6 = '2H 3C 4D 5D 6H'.split()
        straightTo5 = '4S AH 3S 2D 5H'.split()
        self.assertEqual(poker([straightTo6, straightTo5]), [straightTo6])

    def test_straight_vs_flush(self):
        straightTo8 = '4C 6H 7D 8D 5H'.split()
        flushTo7 = '2S 4S 5S 6S 7S'.split()
        self.assertEqual(poker([straightTo8, flushTo7]), [flushTo7])

    def test_two_flushes(self):
        flushTo9 = '4H 7H 8H 9H 6H'.split()
        flushTo7 = '2S 4S 5S 6S 7S'.split()
        self.assertEqual(poker([flushTo9, flushTo7]), [flushTo9])

    def test_flush_vs_full(self):
        flushTo8 = '3H 6H 7H 8H 5H'.split()
        full = '4S 5H 4C 5D 4H'.split()
        self.assertEqual(poker([full, flushTo8]), [full])

    def test_two_fulls(self):
        fullOf4by9 = '4H 4S 4D 9S 9D'.split()
        fullOf5by8 = '5H 5S 5D 8S 8D'.split()
        self.assertEqual(poker([fullOf4by9, fullOf5by8]), [fullOf5by8])

    def test_two_fulls_same_triplet(self):
        fullOf5by9 = '5H 5S 5D 9S 9D'.split()
        fullOf5by8 = '5H 5S 5D 8S 8D'.split()
        self.assertEqual(poker([fullOf5by9, fullOf5by8]), [fullOf5by9])

    def test_full_vs_four(self):
        full = '4S 5H 4D 5D 4H'.split()
        fourOf3 = '3S 3H 2S 3D 3C'.split()
        self.assertEqual(poker([full, fourOf3]), [fourOf3])

    def test_two_fours(self):
        fourOf2 = '2S 2H 2C 8D 2D'.split()
        fourOf5 = '4S 5H 5S 5D 5C'.split()
        self.assertEqual(poker([fourOf2, fourOf5]), [fourOf5])

    def test_two_fours_kicker(self):
        fourOf3low = '3S 3H 2S 3D 3C'.split()
        fourOf3high = '3S 3H 4S 3D 3C'.split()
        self.assertEqual(poker([fourOf3low, fourOf3high]), [fourOf3high])

    def test_four_vs_straight_flush(self):
        fourOf5 = '4S 5H 5S 5D 5C'.split()
        straightFlushTo9 = '7S 8S 9S 6S 5S'.split()
        self.assertEqual(
            poker([fourOf5, straightFlushTo9]), [straightFlushTo9])

    def test_two_straight_flushes(self):
        straightFlushTo8 = '4H 6H 7H 8H 5H'.split()
        straightFlushTo9 = '5S 7S 8S 9S 6S'.split()
        self.assertEqual(
            poker([straightFlushTo8, straightFlushTo9]), [straightFlushTo9])


if __name__ == '__main__':
    unittest.main()
