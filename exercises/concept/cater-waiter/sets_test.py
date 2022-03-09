import unittest
import pytest

# pylint: disable=deprecated-module
from sets import (clean_ingredients,
                  check_drinks,
                  categorize_dish,
                  tag_special_ingredients,
                  compile_ingredients,
                  separate_appetizers,
                  singleton_ingredients)


from sets_categories_data import (VEGAN,
                                  VEGETARIAN,
                                  KETO,
                                  PALEO,
                                  OMNIVORE,
                                  ALCOHOLS,
                                  SPECIAL_INGREDIENTS,
                                  VEGAN_INTERSECTIONS,
                                  VEGETARIAN_INTERSECTIONS,
                                  PALEO_INTERSECTIONS,
                                  KETO_INTERSECTIONS,
                                  OMNIVORE_INTERSECTIONS)

from sets_test_data import (recipes_with_duplicates,
                            recipes_without_duplicates,
                            all_drinks,
                            drink_names,
                            dishes_categorized,
                            dishes_to_special_label,
                            dishes_labeled,
                            ingredients_only,
                            dishes_and_appetizers,
                            dishes_cleaned,
                            dishes_and_overlap,
                            singletons)


class SetsTest(unittest.TestCase):

    @pytest.mark.task(taskno=1)
    def test_clean_ingredients(self):
        test_data = zip(recipes_with_duplicates[::3], recipes_without_duplicates[::3])

        for variant, (item, result) in enumerate(test_data, start=1):
            with self.subTest(f"variation #{variant}", inputs="recipes with duplicated ingredients",
                              result="recipe ingredients de-duped"):

                error_msg = (f"Expected a cleaned ingredient list for {item[0]}, "
                            "but the ingredients aren't cleaned as expected.")

                self.assertEqual(clean_ingredients(item[0], item[1]), (result[1], result[2]), msg=error_msg)

    @pytest.mark.task(taskno=2)
    def test_check_drinks(self):
        test_data = zip(all_drinks[::2], drink_names[::2])

        for variant, (item, result) in enumerate(test_data, start=1):
            with self.subTest(f"variation #{variant}", iputs="all drinks", results="drinks classified"):

                error_msg = f"Expected {result} for {item}, but got something else instead."
                self.assertEqual(check_drinks(item[0], item[1]), (result), msg=error_msg)

    @pytest.mark.task(taskno=3)
    def test_categorize_dish(self):
        test_data = zip(sorted(recipes_without_duplicates, reverse=True)[::3], dishes_categorized[::3])

        for variant, (item, result) in enumerate(test_data, start=1):
            with self.subTest(f"variation #{variant}", inputs="all recipes list", results="categorized dishes"):

                error_message = f"Exptected category {result} for {item[0]}, but got a different category instead."
                self.assertEqual(categorize_dish(item[1], item[2]), (result), msg=error_message)

    @pytest.mark.task(taskno=4)
    def test_tag_special_ingredients(self):
        test_data = zip(dishes_to_special_label[::3], dishes_labeled[::3])

        for variant, (item, result)  in enumerate(test_data, start=1):
            with self.subTest(f"variation #{variant}", inputs="all recipes list", results="special ingredients tagged"):

                error_message = f"Expected {result} for {item}, but got something else instead."
                self.assertEqual(tag_special_ingredients(item), (result), msg=error_message)

    @pytest.mark.task(taskno=5)
    def test_compile_ingredients(self):
        test_data = zip(ingredients_only, [VEGAN, VEGETARIAN, PALEO, KETO, OMNIVORE])

        for variant, (item, result) in enumerate(test_data, start=1):
            with self.subTest(f"variation #{variant}", inputs="all ingredients for all recipes",
                              result="combined list of ingredients for all dishes"):

                error_message = "Expected a proper set of combined ingredients, but something went wrong."
                self.assertEqual(compile_ingredients(item), (result), msg=error_message)

    @pytest.mark.task(taskno=6)
    def test_separate_appetizers(self):
        test_data = zip(dishes_and_appetizers, dishes_cleaned)

        for variant, (item, result) in enumerate(test_data, start=1):
            with self.subTest(f"variation #{variant}", inputs="dishes with appetizers", results="appetizers only"):

                error_message = "Expected only appetizers returned, but some dishes remain in the group."
                self.assertEqual(sorted(separate_appetizers(item[0], item[1])), (sorted(result)), msg=error_message)

    @pytest.mark.task(taskno=7)
    def test_singleton_ingredients(self):
        test_data = zip(dishes_and_overlap, singletons)

        for variant, (item, result) in enumerate(test_data, start=1):
            with self.subTest(f"variation #{variant}", inputs="overlapping ingredients",
                              results="ingredients in only one dish"):

                error_message = ("Expected only ingredients that belong to exactly "
                                "one dish, but got multi-dish ingredients instead.")
                self.assertEqual(singleton_ingredients(item[0], item[1]), (result), msg=error_message)
