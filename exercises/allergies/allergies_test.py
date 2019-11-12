import unittest

from allergies import Allergies

# Tests adapted from `problem-specifications//canonical-data.json` @ v2.0.0


class AllergiesTest(unittest.TestCase):
    def test_not_allergic_to_anything(self):
        self.assertEqual(Allergies(0).allergicTo("eggs"), False)

    def test_allergic_only_to_eggs(self):
        self.assertEqual(Allergies(1).allergicTo("eggs"), True)

    def test_allergic_to_eggs_and_something_else(self):
        self.assertEqual(Allergies(3).allergicTo("eggs"), True)

    def test_allergic_to_something_but_not_eggs(self):
        self.assertEqual(Allergies(2).allergicTo("eggs"), False)

    def test_allergic_to_everything(self):
        self.assertEqual(Allergies(255).allergicTo("eggs"), True)

    def test_not_allergic_to_anything(self):
        self.assertEqual(Allergies(0).allergicTo("peanuts"), False)

    def test_allergic_only_to_peanuts(self):
        self.assertEqual(Allergies(2).allergicTo("peanuts"), True)

    def test_allergic_to_peanuts_and_something_else(self):
        self.assertEqual(Allergies(7).allergicTo("peanuts"), True)

    def test_allergic_to_something_but_not_peanuts(self):
        self.assertEqual(Allergies(5).allergicTo("peanuts"), False)

    def test_allergic_to_everything(self):
        self.assertEqual(Allergies(255).allergicTo("peanuts"), True)

    def test_not_allergic_to_anything(self):
        self.assertEqual(Allergies(0).allergicTo("shellfish"), False)

    def test_allergic_only_to_shellfish(self):
        self.assertEqual(Allergies(4).allergicTo("shellfish"), True)

    def test_allergic_to_shellfish_and_something_else(self):
        self.assertEqual(Allergies(14).allergicTo("shellfish"), True)

    def test_allergic_to_something_but_not_shellfish(self):
        self.assertEqual(Allergies(10).allergicTo("shellfish"), False)

    def test_allergic_to_everything(self):
        self.assertEqual(Allergies(255).allergicTo("shellfish"), True)

    def test_not_allergic_to_anything(self):
        self.assertEqual(Allergies(0).allergicTo("strawberries"), False)

    def test_allergic_only_to_strawberries(self):
        self.assertEqual(Allergies(8).allergicTo("strawberries"), True)

    def test_allergic_to_strawberries_and_something_else(self):
        self.assertEqual(Allergies(28).allergicTo("strawberries"), True)

    def test_allergic_to_something_but_not_strawberries(self):
        self.assertEqual(Allergies(20).allergicTo("strawberries"), False)

    def test_allergic_to_everything(self):
        self.assertEqual(Allergies(255).allergicTo("strawberries"), True)

    def test_not_allergic_to_anything(self):
        self.assertEqual(Allergies(0).allergicTo("tomatoes"), False)

    def test_allergic_only_to_tomatoes(self):
        self.assertEqual(Allergies(16).allergicTo("tomatoes"), True)

    def test_allergic_to_tomatoes_and_something_else(self):
        self.assertEqual(Allergies(56).allergicTo("tomatoes"), True)

    def test_allergic_to_something_but_not_tomatoes(self):
        self.assertEqual(Allergies(40).allergicTo("tomatoes"), False)

    def test_allergic_to_everything(self):
        self.assertEqual(Allergies(255).allergicTo("tomatoes"), True)

    def test_not_allergic_to_anything(self):
        self.assertEqual(Allergies(0).allergicTo("chocolate"), False)

    def test_allergic_only_to_chocolate(self):
        self.assertEqual(Allergies(32).allergicTo("chocolate"), True)

    def test_allergic_to_chocolate_and_something_else(self):
        self.assertEqual(Allergies(112).allergicTo("chocolate"), True)

    def test_allergic_to_something_but_not_chocolate(self):
        self.assertEqual(Allergies(80).allergicTo("chocolate"), False)

    def test_allergic_to_everything(self):
        self.assertEqual(Allergies(255).allergicTo("chocolate"), True)

    def test_not_allergic_to_anything(self):
        self.assertEqual(Allergies(0).allergicTo("pollen"), False)

    def test_allergic_only_to_pollen(self):
        self.assertEqual(Allergies(64).allergicTo("pollen"), True)

    def test_allergic_to_pollen_and_something_else(self):
        self.assertEqual(Allergies(224).allergicTo("pollen"), True)

    def test_allergic_to_something_but_not_pollen(self):
        self.assertEqual(Allergies(160).allergicTo("pollen"), False)

    def test_allergic_to_everything(self):
        self.assertEqual(Allergies(255).allergicTo("pollen"), True)

    def test_not_allergic_to_anything(self):
        self.assertEqual(Allergies(0).allergicTo("cats"), False)

    def test_allergic_only_to_cats(self):
        self.assertEqual(Allergies(128).allergicTo("cats"), True)

    def test_allergic_to_cats_and_something_else(self):
        self.assertEqual(Allergies(192).allergicTo("cats"), True)

    def test_allergic_to_something_but_not_cats(self):
        self.assertEqual(Allergies(64).allergicTo("cats"), False)

    def test_allergic_to_everything(self):
        self.assertEqual(Allergies(255).allergicTo("cats"), True)

    def test_no_allergies(self):
        self.assertEqual(Allergies(0).lst, [])

    def test_just_eggs(self):
        self.assertEqual(Allergies(1).lst, ["eggs"])

    def test_just_peanuts(self):
        self.assertEqual(Allergies(2).lst, ["peanuts"])

    def test_just_strawberries(self):
        self.assertEqual(Allergies(8).lst, ["strawberries"])

    def test_eggs_and_peanuts(self):
        self.assertEqual(Allergies(3).lst, ["eggs", "peanuts"])

    def test_more_than_eggs_but_not_peanuts(self):
        self.assertEqual(Allergies(5).lst, ["eggs", "shellfish"])

    def test_lots_of_stuff(self):
        self.assertEqual(
            Allergies(248).lst,
            ["strawberries", "tomatoes", "chocolate", "pollen", "cats"],
        )

    def test_everything(self):
        self.assertEqual(
            Allergies(255).lst,
            [
                "eggs",
                "peanuts",
                "shellfish",
                "strawberries",
                "tomatoes",
                "chocolate",
                "pollen",
                "cats",
            ],
        )

    def test_no_allergen_score_parts(self):
        self.assertEqual(
            Allergies(509).lst,
            [
                "eggs",
                "shellfish",
                "strawberries",
                "tomatoes",
                "chocolate",
                "pollen",
                "cats",
            ],
        )


if __name__ == "__main__":
    unittest.main()
