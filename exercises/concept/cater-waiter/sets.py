"""Functions for compiling dishes and ingredients for a catering company."""


from sets_categories_data import (VEGAN,
                                  VEGETARIAN,
                                  KETO,
                                  PALEO,
                                  OMNIVORE,
                                  ALCOHOLS,
                                  SPECIAL_INGREDIENTS)


def clean_ingredients(dish_name, dish_ingredients):
    """Remove duplicates from `dish_ingredients` and return a tuple containing `dish_name` and the cleaned list.

    :param dish_name: str - containing the dish name.
    :param dish_ingredients: list - dish ingredients.
    :return: tuple - containing (dish_name, ingredient set).

    This function should return a `tuple` with the name of the dish as the first item,
    followed by the de-duped `set` of ingredients as the second item.
    """

    pass


def check_drinks(drink_name, drink_ingredients):
    """Append "Mocktail" or "Cocktail" to `dish_name` if alcoholic ingredients are present in `drink_ingredients`.

    :param drink_name: str - name of the drink.
    :param drink_ingredients: list - ingredients in the drink.
    :return: str - drink name appended with "Mocktail" or "Cocktail".

    The function should return the name of the drink followed by "Mocktail" if the drink has
    no alcoholic ingredients, and drink name followed by "Cocktail" if the drink includes alcohol.
    """

    pass


def categorize_dish(dish_name, dish_ingredients):
    """Categorize `dish_name` by appending its classification based on the `dish_ingredients` list.

    :param dish_name: str - dish to be categorized.
    :param dish_ingredients: list - of ingredients for the dish.
    :return: str - the dish name appended with ": <CATEGORY>".

    This function should return a string with the `dish name: <CATEGORY>` (which meal category the dish belongs to).
    All dishes will "fit" into one of the categories imported from `sets_categories_data.py`
    (VEGAN, VEGETARIAN, PALEO, KETO, or OMNIVORE).
    """

    pass


def tag_special_ingredients(dish):
    """Compare `dish` ingredients to `SPECIAL_INGREDIENTS`, return a tuple with dish name and matching items in a set.

    :param dish: tuple - of (str of dish name, list of dish ingredients).
    :return: tuple - of (str of dish name, set of dish special ingredients).

    Return the dish name followed by the `set` of ingredients that require a special note on the dish description.
    For the purposes of this exercise, all allergens or special ingredients that need to be tracked are in the
    SPECIAL_INGREDIENTS constant imported from `sets_categories_data.py`.
    """

    pass


def compile_ingredients(dishes):
    """Create a master list of ingredients using the list of sets of ingredients from `dishes`.

    :param dishes: list - of dish ingredient sets.
    :return: set - of dishes compiled from ingredients sets.

    This function should return a `set` of all ingredients from all listed dishes.
    """

    pass


def separate_appetizers(dishes, appetizers):
    """From the list of `dishes`, determine which are `appetizers` and return the result as a list.

    :param dishes: list - of dish names.
    :param appetizers: list - of appetizer names.
    :return: list - of dish names.

    The function should return the list of dish names with appetizer names removed.
    Either list could contain duplicates and may require de-duping.
    """

    pass


def singleton_ingredients(dishes, intersection):
    """Use `example_dishes` and `EXAMPLE_INTERSECTION` to determine which dishes have a singleton ingredient.

    :param dishes: list - of ingredient sets.
    :param intersection: constant - can be one of `EXAMPLE_INTERSECTION` constants.
    :return: set - containing singleton ingredients.

    Each dish is represented by a `set` of its ingredients.

    Each `<CATEGORY>_INTERSECTION` is an `intersection` of all dishes in the category and can be either:
        VEGAN_INTERSECTION, VEGETARIAN_INTERSECTION, PALEO_INTERSECTION, KETO_INTERSECTION, or OMNIVORE_INTERSECTION.

    The function should return a `set` of ingredients that only appear in a single dish.
    """

    pass
