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


def clean_ingredients(dish_name, dish_ingredients):
    return dish_name, set(dish_ingredients)


def check_drinks(drink_name, drink_ingredients):
    if ALCOHOLS.isdisjoint(drink_ingredients):
        return drink_name + ' Mocktail'
    else:
        return drink_name + ' Cocktail'


def categorize_dish(dish_name, dish_ingredients):
    categories = ((VEGAN,'VEGAN'), (VEGETARIAN,'VEGETARIAN'), (KETO,'KETO'), (PALEO,'PALEO'), (OMNIVORE,'OMNIVORE'))

    for category in categories:
        if set(dish_ingredients) <= category[0]:
            return dish_name + ': ' + category[1]


def tag_special_ingredients(dish):
    return dish[0], (SPECIAL_INGREDIENTS & set(dish[1]))


def compile_ingredients(dishes):
    combined_ingredients = set()

    for ingredients in dishes:
        combined_ingredients = combined_ingredients.union(ingredients)

    return combined_ingredients


def separate_appetizers(dishes, appetizers):
    return list(set(dishes) - set(appetizers))


def singleton_ingredients(dishes, intersections):
    all_ingredients = set()

    for ingredients in dishes:
        all_ingredients = all_ingredients ^ ingredients

    return all_ingredients - intersections
