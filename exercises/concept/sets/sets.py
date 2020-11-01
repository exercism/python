def dedupe_ingredients(ingredients):
    return set(ingredients)

def create_combined_ingredients(ingredients):
    combined_ingredients = set()

    for ingredient_list in ingredients:
        combined_ingredients = combined_ingredients | dedupe_ingredients(ingredient_list)

    return combined_ingredients

def check_for_(set_1, set_2):
    return set_1 & set_2

def sets_difference(set_1, set_2):
    return set_1 - set_2

def remove_shared_elements(set_1, set_2):
    return set_1 ^ set_2

def sub_and_super_sets(set_1, set_2):

