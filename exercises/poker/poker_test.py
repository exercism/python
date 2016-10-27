import unittest

from poker import poker


class PokerTest(unittest.TestCase):
    def test_one_hand(self):
        hand = '4S 5S 7H 8D JC'.split()
        self.assertEqual([hand], poker([hand]))

    def test_nothing_vs_one_pair(self):
        nothing = '4S 5H 6S 8D JH'.split()
        pairOf4 = '2S 4H 6S 4D JH'.split()
        self.assertEqual([pairOf4], poker([nothing, pairOf4]))

    def test_two_pair(self):
        pairOf2 = '4S 2H 6S 2D JH'.split()
        pairOf4 = '2S 4H 6S 4D JH'.split()
        self.assertEqual([pairOf4], poker([pairOf2, pairOf4]))

    def test_one_pair_vs_double_pair(self):
        pairOf8 = '2S 8H 6S 8D JH'.split()
        doublePair = '4S 5H 4S 8D 5H'.split()
        self.assertEqual([doublePair], poker([pairOf8, doublePair]))

    def test_two_double_pair(self):
        doublePair2and8 = '2S 8H 2S 8D JH'.split()
        doublePair4and5 = '4S 5H 4S 8D 5H'.split()
        self.assertEqual([doublePair2and8],
                         poker([doublePair2and8, doublePair4and5]))

    def test_double_pair_vs_three(self):
        doublePair2and8 = '2S 8H 2S 8D JH'.split()
        threeOf4 = '4S 5H 4S 8D 4H'.split()
        self.assertEqual([threeOf4], poker([doublePair2and8, threeOf4]))

    def test_two_three(self):
        threeOf2 = '2S 2H 2S 8D JH'.split()
        threeOf1 = '4S AH AS 8D AH'.split()
        self.assertEqual([threeOf1], poker([threeOf2, threeOf1]))

    def test_three_vs_straight(self):
        threeOf4 = '4S 5H 4S 8D 4H'.split()
        straight = '3S 4H 2S 6D 5H'.split()
        self.assertEqual([straight], poker([threeOf4, straight]))

    def test_two_straights(self):
        straightTo8 = '4S 6H 7S 8D 5H'.split()
        straightTo9 = '5S 7H 8S 9D 6H'.split()
        self.assertEqual([straightTo9], poker([straightTo8, straightTo9]))
        straightTo1 = 'AS QH KS TD JH'.split()
        straightTo5 = '4S AH 3S 2D 5H'.split()
        self.assertEqual([straightTo1], poker([straightTo1, straightTo5]))

    def test_straight_vs_flush(self):
        straightTo8 = '4S 6H 7S 8D 5H'.split()
        flushTo7 = '2S 4S 5S 6S 7S'.split()
        self.assertEqual([flushTo7], poker([straightTo8, flushTo7]))

    def test_two_flushes(self):
        flushTo8 = '3H 6H 7H 8H 5H'.split()
        flushTo7 = '2S 4S 5S 6S 7S'.split()
        self.assertEqual([flushTo8], poker([flushTo8, flushTo7]))

    def test_flush_vs_full(self):
        flushTo8 = '3H 6H 7H 8H 5H'.split()
        full = '4S 5H 4S 5D 4H'.split()
        self.assertEqual([full], poker([full, flushTo8]))

    def test_two_fulls(self):
        fullOf4by9 = '4H 4S 4D 9S 9D'.split()
        fullOf5by8 = '5H 5S 5D 8S 8D'.split()
        self.assertEqual([fullOf5by8], poker([fullOf4by9, fullOf5by8]))

    def test_full_vs_square(self):
        full = '4S 5H 4S 5D 4H'.split()
        squareOf3 = '3S 3H 2S 3D 3H'.split()
        self.assertEqual([squareOf3], poker([full, squareOf3]))

    def test_two_square(self):
        squareOf2 = '2S 2H 2S 8D 2H'.split()
        squareOf5 = '4S 5H 5S 5D 5H'.split()
        self.assertEqual([squareOf5], poker([squareOf2, squareOf5]))

    def test_square_vs_straight_flush(self):
        squareOf5 = '4S 5H 5S 5D 5H'.split()
        straightFlushTo9 = '5S 7S 8S 9S 6S'.split()
        self.assertEqual([straightFlushTo9],
                         poker([squareOf5, straightFlushTo9]))

    def test_two_straight_flushes(self):
        straightFlushTo8 = '4H 6H 7H 8H 5H'.split()
        straightFlushTo9 = '5S 7S 8S 9S 6S'.split()
        self.assertEqual([straightFlushTo9],
                         poker([straightFlushTo8, straightFlushTo9]))

    def test_three_hand_with_tie(self):
        spadeStraightTo9 = "9S 8S 7S 6S 5S".split()
        diamondStraightTo9 = "9D 8D 7D 6D 5D".split()
        threeOf4 = "4D 4S 4H QS KS".split()
        self.assertEqual([spadeStraightTo9, diamondStraightTo9],
                         poker([spadeStraightTo9, diamondStraightTo9, threeOf4]))

if __name__ == '__main__':
    unittest.main()
