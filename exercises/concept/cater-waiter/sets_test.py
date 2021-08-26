import unittest
import pytest

from sets import (clean_ingredients,
                  check_drinks,
                  categorize_dish,
                  tag_special_ingredients,
                  compile_ingredients,
                  separate_appetizers,
                  singleton_ingredients)


from sets_categories_data import (VEGAN,
                                  VEGETARIAN,
                                  KETO, PALEO,
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
        input_data =  recipes_with_duplicates
        result_data = recipes_without_duplicates
        number_of_variants = range(1, len(input_data) + 1)

        for variant, item, result  in zip(number_of_variants, input_data, result_data):
            with self.subTest(f"variation #{variant}", item=item, result=result):
                self.assertEqual(clean_ingredients(item[0], item[1]), (result[1], result[2]))

    @pytest.mark.task(taskno=2)
    def test_check_drinks(self):
        input_data = all_drinks
        result_data = drink_names
        number_of_variants = range(1, len(input_data) + 1)

        for variant, item, result  in zip(number_of_variants, input_data, result_data):
            with self.subTest(f"variation #{variant}", item=item, result=result):
                self.assertEqual(check_drinks(item[0], item[1]), (result))

    @pytest.mark.task(taskno=3)
    def test_categorize_dish(self):
        input_data = sorted(recipes_without_duplicates, reverse=True)
        result_data = dishes_categorized
        number_of_variants = range(1, len(input_data) + 1)

        for variant, item, result  in zip(number_of_variants, input_data, result_data):
            with self.subTest(f"variation #{variant}", item=item, result=result):
                self.assertEqual(categorize_dish(item[1], item[2]), (result))

    @pytest.mark.task(taskno=4)
    def test_tag_special_ingredients(self):
        input_data = dishes_to_special_label
        result_data = dishes_labeled
        number_of_variants = range(1, len(input_data) + 1)

        for variant, item, result  in zip(number_of_variants, input_data, result_data):
            with self.subTest(f"variation #{variant}", item=item, result=result):
                self.assertEqual(tag_special_ingredients(item), (result))

    @pytest.mark.task(taskno=5)
    def test_compile_ingredients(self):
        input_data = ingredients_only
        result_data = [VEGAN, VEGETARIAN, PALEO, KETO, OMNIVORE]
        number_of_variants = number_of_variants = range(1, len(input_data) + 1)

        for variant, item, result  in zip(number_of_variants, input_data, result_data):
            with self.subTest(f"variation #{variant}", item=item, result=result):
                self.assertEqual(compile_ingredients(item), (result))

    @pytest.mark.task(taskno=6)
    def test_separate_appetizers(self):
        input_data = dishes_and_appetizers
        result_data = dishes_cleaned
        number_of_variants = number_of_variants = range(1, len(input_data) + 1)

        for variant, item, result  in zip(number_of_variants, input_data, result_data):
            with self.subTest(f"variation #{variant}", item=item, result=result):
                self.assertEqual(sorted(separate_appetizers(item[0], item[1])), (sorted(result)))

    @pytest.mark.task(taskno=7)
    def test_singleton_ingredients(self):
        input_data = dishes_and_overlap
        result_data = singletons
        number_of_variants = number_of_variants = range(1, len(input_data) + 1)

        for variant, item, result  in zip(number_of_variants, input_data, result_data):
            with self.subTest(f"variation #{variant}", item=item, result=result):
                self.assertEqual(singleton_ingredients(item[0], item[1]), (result))
