import unittest

from allergies import Allergies

# Tests adapted from `problem-specifications//canonical-data.json` @ v2.0.0


class AllergiesTest(unittest.TestCase):
    def test_eggs_not_allergic_to_anything(self):
        self.assertIs(Allergies(0).allergic_to("eggs"), False)

    def test_allergic_only_to_eggs(self):
        self.assertIs(Allergies(1).allergic_to("eggs"), True)

    def test_allergic_to_eggs_and_something_else(self):
        self.assertIs(Allergies(3).allergic_to("eggs"), True)

    def test_allergic_to_something_but_not_eggs(self):
        self.assertIs(Allergies(2).allergic_to("eggs"), False)

    def test_eggs_allergic_to_everything(self):
        self.assertIs(Allergies(255).allergic_to("eggs"), True)

    def test_peanuts_not_allergic_to_anything(self):
        self.assertIs(Allergies(0).allergic_to("peanuts"), False)

    def test_allergic_only_to_peanuts(self):
        self.assertIs(Allergies(2).allergic_to("peanuts"), True)

    def test_allergic_to_peanuts_and_something_else(self):
        self.assertIs(Allergies(7).allergic_to("peanuts"), True)

    def test_allergic_to_something_but_not_peanuts(self):
        self.assertIs(Allergies(5).allergic_to("peanuts"), False)

    def test_peanuts_allergic_to_everything(self):
        self.assertIs(Allergies(255).allergic_to("peanuts"), True)

    def test_shellfish_not_allergic_to_anything(self):
        self.assertIs(Allergies(0).allergic_to("shellfish"), False)

    def test_allergic_only_to_shellfish(self):
        self.assertIs(Allergies(4).allergic_to("shellfish"), True)

    def test_allergic_to_shellfish_and_something_else(self):
        self.assertIs(Allergies(14).allergic_to("shellfish"), True)

    def test_allergic_to_something_but_not_shellfish(self):
        self.assertIs(Allergies(10).allergic_to("shellfish"), False)

    def test_shellfish_allergic_to_everything(self):
        self.assertIs(Allergies(255).allergic_to("shellfish"), True)

    def test_strawberries_not_allergic_to_anything(self):
        self.assertIs(Allergies(0).allergic_to("strawberries"), False)

    def test_allergic_only_to_strawberries(self):
        self.assertIs(Allergies(8).allergic_to("strawberries"), True)

    def test_allergic_to_strawberries_and_something_else(self):
        self.assertIs(Allergies(28).allergic_to("strawberries"), True)

    def test_allergic_to_something_but_not_strawberries(self):
        self.assertIs(Allergies(20).allergic_to("strawberries"), False)

    def test_strawberries_allergic_to_everything(self):
        self.assertIs(Allergies(255).allergic_to("strawberries"), True)

    def test_tomatoes_not_allergic_to_anything(self):
        self.assertIs(Allergies(0).allergic_to("tomatoes"), False)

    def test_allergic_only_to_tomatoes(self):
        self.assertIs(Allergies(16).allergic_to("tomatoes"), True)

    def test_allergic_to_tomatoes_and_something_else(self):
        self.assertIs(Allergies(56).allergic_to("tomatoes"), True)

    def test_allergic_to_something_but_not_tomatoes(self):
        self.assertIs(Allergies(40).allergic_to("tomatoes"), False)

    def test_tomatoes_allergic_to_everything(self):
        self.assertIs(Allergies(255).allergic_to("tomatoes"), True)

    def test_chocolate_not_allergic_to_anything(self):
        self.assertIs(Allergies(0).allergic_to("chocolate"), False)

    def test_allergic_only_to_chocolate(self):
        self.assertIs(Allergies(32).allergic_to("chocolate"), True)

    def test_allergic_to_chocolate_and_something_else(self):
        self.assertIs(Allergies(112).allergic_to("chocolate"), True)

    def test_allergic_to_something_but_not_chocolate(self):
        self.assertIs(Allergies(80).allergic_to("chocolate"), False)

    def test_chocolate_allergic_to_everything(self):
        self.assertIs(Allergies(255).allergic_to("chocolate"), True)

    def test_pollen_not_allergic_to_anything(self):
        self.assertIs(Allergies(0).allergic_to("pollen"), False)

    def test_allergic_only_to_pollen(self):
        self.assertIs(Allergies(64).allergic_to("pollen"), True)

    def test_allergic_to_pollen_and_something_else(self):
        self.assertIs(Allergies(224).allergic_to("pollen"), True)

    def test_allergic_to_something_but_not_pollen(self):
        self.assertIs(Allergies(160).allergic_to("pollen"), False)

    def test_pollen_allergic_to_everything(self):
        self.assertIs(Allergies(255).allergic_to("pollen"), True)

    def test_cats_not_allergic_to_anything(self):
        self.assertIs(Allergies(0).allergic_to("cats"), False)

    def test_allergic_only_to_cats(self):
        self.assertIs(Allergies(128).allergic_to("cats"), True)

    def test_allergic_to_cats_and_something_else(self):
        self.assertIs(Allergies(192).allergic_to("cats"), True)

    def test_allergic_to_something_but_not_cats(self):
        self.assertIs(Allergies(64).allergic_to("cats"), False)

    def test_cats_allergic_to_everything(self):
        self.assertIs(Allergies(255).allergic_to("cats"), True)

    def test_no_allergies(self):
        self.assertEqual(Allergies(0).lst, [])

    def test_just_eggs(self):
        self.assertEqual(Allergies(1).lst, ["eggs"])

    def test_just_peanuts(self):
        self.assertEqual(Allergies(2).lst, ["peanuts"])

    def test_just_strawberries(self):
        self.assertEqual(Allergies(8).lst, ["strawberries"])

    def test_eggs_and_peanuts(self):
        self.assertCountEqual(Allergies(3).lst, ["eggs", "peanuts"])

    def test_more_than_eggs_but_not_peanuts(self):
        self.assertCountEqual(Allergies(5).lst, ["eggs", "shellfish"])

    def test_lots_of_stuff(self):
        self.assertCountEqual(
            Allergies(248).lst,
            ["strawberries", "tomatoes", "chocolate", "pollen", "cats"],
        )

    def test_everything(self):
        self.assertCountEqual(
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
        self.assertCountEqual(
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
