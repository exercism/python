# For 1kg cake
BASE_PRICE = 200
TIME_TO_BAKE_BASE = 40

def calculate_base_price(weight_of_base, number_of_layers): # Positional Args
    return BASE_PRICE * weight_of_base * number_of_layers

def calculate_time_for_baking_base(weight_of_base, number_of_layers=1): # Deafult Args/Keyword Args
    return TIME_TO_BAKE_BASE * weight_of_base * number_of_layers

def total_ingredients_price(*ingredients_prices): # *args method
    PRICE = 0
    for price in ingredients_prices:
        PRICE += price
    return PRICE

def calculate_total_price(weight_of_base=1, number_of_layers=1, **ingredients_prices): # *kwargs method
    return (calculate_base_price(weight_of_base) * number_of_layers) + total_ingredients_price(*ingredients_prices.values())

def make_cake():
    # Don't know what to put in here yet or whether we need this
    pass

