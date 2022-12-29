import unittest

from dnd_character import (
    Character,
    modifier,
)

# Tests adapted from `problem-specifications//canonical-data.json`


class DndCharacterTest(unittest.TestCase):
    def test_ability_modifier_for_score_3_is_n4(self):
        self.assertEqual(modifier(3), -4)

    def test_ability_modifier_for_score_4_is_n3(self):
        self.assertEqual(modifier(4), -3)

    def test_ability_modifier_for_score_5_is_n3(self):
        self.assertEqual(modifier(5), -3)

    def test_ability_modifier_for_score_6_is_n2(self):
        self.assertEqual(modifier(6), -2)

    def test_ability_modifier_for_score_7_is_n2(self):
        self.assertEqual(modifier(7), -2)

    def test_ability_modifier_for_score_8_is_n1(self):
        self.assertEqual(modifier(8), -1)

    def test_ability_modifier_for_score_9_is_n1(self):
        self.assertEqual(modifier(9), -1)

    def test_ability_modifier_for_score_10_is_0(self):
        self.assertEqual(modifier(10), 0)

    def test_ability_modifier_for_score_11_is_0(self):
        self.assertEqual(modifier(11), 0)

    def test_ability_modifier_for_score_12_is_1(self):
        self.assertEqual(modifier(12), 1)

    def test_ability_modifier_for_score_13_is_1(self):
        self.assertEqual(modifier(13), 1)

    def test_ability_modifier_for_score_14_is_2(self):
        self.assertEqual(modifier(14), 2)

    def test_ability_modifier_for_score_15_is_2(self):
        self.assertEqual(modifier(15), 2)

    def test_ability_modifier_for_score_16_is_3(self):
        self.assertEqual(modifier(16), 3)

    def test_ability_modifier_for_score_17_is_3(self):
        self.assertEqual(modifier(17), 3)

    def test_ability_modifier_for_score_18_is_4(self):
        self.assertEqual(modifier(18), 4)

    def test_random_ability_is_within_range(self):
        score = Character().ability()
        self.assertIs(score >= 3 and score <= 18, True)

    def test_random_character_is_valid(self):
        Char = Character()
        self.assertIs(Char.strength >= 3 and Char.strength <= 18, True)
        self.assertIs(Char.dexterity >= 3 and Char.dexterity <= 18, True)
        self.assertIs(Char.constitution >= 3 and Char.constitution <= 18, True)
        self.assertIs(Char.intelligence >= 3 and Char.intelligence <= 18, True)
        self.assertIs(Char.wisdom >= 3 and Char.wisdom <= 18, True)
        self.assertIs(Char.charisma >= 3 and Char.charisma <= 18, True)
        self.assertIs(Char.hitpoints == 10 + modifier(Char.constitution), True)

    def test_each_ability_is_only_calculated_once(self):
        Char = Character()
        self.assertIs(Char.strength == Char.strength, True)
