import unittest

from dnd_character import Character


# Tests adapted from 'problem-specifications//canonical-data.json' @ v1.0.0

class DnDCharacterTest(unittest.TestCase):
    def test_modifier_for_score_3_is_n4(self):
        self.assertEqual(Character().modifier(3), -4)

    def test_modifier_for_score_4_is_n3(self):
        self.assertEqual(Character().modifier(4), -3)

    def test_modifier_for_score_5_is_n3(self):
        self.assertEqual(Character().modifier(5), -3)

    def test_modifier_for_score_6_is_n2(self):
        self.assertEqual(Character().modifier(6), -2)

    def test_modifier_for_score_7_is_n2(self):
        self.assertEqual(Character().modifier(7), -2)

    def test_modifier_for_score_8_is_n1(self):
        self.assertEqual(Character().modifier(8), -1)

    def test_modifier_for_score_9_is_n1(self):
        self.assertEqual(Character().modifier(9), -1)

    def test_modifier_for_score_10_is_0(self):
        self.assertEqual(Character().modifier(10), 0)

    def test_modifier_for_score_11_is_0(self):
        self.assertEqual(Character().modifier(11), 0)

    def test_modifier_for_score_12_is_1(self):
        self.assertEqual(Character().modifier(12), 1)

    def test_modifier_for_score_13_is_1(self):
        self.assertEqual(Character().modifier(13), 1)

    def test_modifier_for_score_14_is_2(self):
        self.assertEqual(Character().modifier(14), 2)

    def test_modifier_for_score_15_is_2(self):
        self.assertEqual(Character().modifier(15), 2)

    def test_modifier_for_score_16_is_3(self):
        self.assertEqual(Character().modifier(16), 3)

    def test_modifier_for_score_17_is_3(self):
        self.assertEqual(Character().modifier(17), 3)

    def test_modifier_for_score_18_is_4(self):
        self.assertEqual(Character().modifier(18), 4)

    def test_random_ability_is_within_range(self):
        self.assertIn(Character().ability(), range(3, 18))

    def test_random_character_is_valid(self):
        Char = Character()
        self.assertIn(Char.character['strength'], range(3, 18))
        self.assertIn(Char.character['dexterity'], range(3, 18))
        self.assertIn(Char.character['constitution'], range(3, 18))
        self.assertIn(Char.character['intelligence'], range(3, 18))
        self.assertIn(Char.character['wisdom'], range(3, 18))
        self.assertIn(Char.character['charisma'], range(3, 18))
        self.assertEqual(
            Char.character['hitpoints'],
            10 + Char.modifier(Char.character['constitution']))


if __name__ == '__main__':
    unittest.main()
