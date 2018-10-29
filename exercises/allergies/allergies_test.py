import unittest

from allergies import Allergies

# Python 2/3 compatibility
if not hasattr(unittest.TestCase, 'assertCountEqual'):
    unittest.TestCase.assertCountEqual = unittest.TestCase.assertItemsEqual


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.2.0

class AllergiesTest(unittest.TestCase):
    def test_no_allergies_means_not_allergic(self):
        allergies = Allergies(0)
        self.assertIs(allergies.is_allergic_to('peanuts'), False)
        self.assertIs(allergies.is_allergic_to('cats'), False)
        self.assertIs(allergies.is_allergic_to('strawberries'), False)

    def test_is_allergic_to_eggs(self):
        self.assertIs(Allergies(1).is_allergic_to('eggs'), True)

    def test_allergic_to_eggs_in_addition_to_other_stuff(self):
        allergies = Allergies(5)
        self.assertIs(allergies.is_allergic_to('eggs'), True)
        self.assertIs(allergies.is_allergic_to('shellfish'), True)
        self.assertIs(allergies.is_allergic_to('strawberries'), False)

    def test_allergic_to_strawberries_but_not_peanuts(self):
        allergies = Allergies(9)
        self.assertIs(allergies.is_allergic_to('eggs'), True)
        self.assertIs(allergies.is_allergic_to('peanuts'), False)
        self.assertIs(allergies.is_allergic_to('shellfish'), False)
        self.assertIs(allergies.is_allergic_to('strawberries'), True)

    def test_no_allergies_at_all(self):
        self.assertEqual(Allergies(0).lst, [])

    def test_allergic_to_just_eggs(self):
        self.assertEqual(Allergies(1).lst, ['eggs'])

    def test_allergic_to_just_peanuts(self):
        self.assertEqual(Allergies(2).lst, ['peanuts'])

    def test_allergic_to_just_strawberries(self):
        self.assertEqual(Allergies(8).lst, ['strawberries'])

    def test_allergic_to_eggs_and_peanuts(self):
        self.assertCountEqual(Allergies(3).lst, ['eggs', 'peanuts'])

    def test_allergic_to_more_than_eggs_but_not_peanuts(self):
        self.assertCountEqual(Allergies(5).lst, ['eggs', 'shellfish'])

    def test_allergic_to_lots_of_stuff(self):
        self.assertCountEqual(
            Allergies(248).lst,
            ['strawberries', 'tomatoes', 'chocolate', 'pollen', 'cats'])

    def test_allergic_to_everything(self):
        self.assertCountEqual(
            Allergies(255).lst, [
                'eggs', 'peanuts', 'shellfish', 'strawberries', 'tomatoes',
                'chocolate', 'pollen', 'cats'
            ])

    def test_ignore_non_allergen_score_parts(self):
        self.assertCountEqual(
            Allergies(509).lst, [
                'eggs', 'shellfish', 'strawberries', 'tomatoes', 'chocolate',
                'pollen', 'cats'
            ])


if __name__ == '__main__':
    unittest.main()
