#time the lasagna should be in the oven according to the cookbook.
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time):
    '''Return remaining bake time in minutes.

    This function takes an integer representing the elapsed bake time and
    returns the bake time remaining for the lasagna based on the EXPECTED_BAKE_TIME.
    '''

    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    '''Return preparation time calculation in minutes.

    This function takes an integer representing the number of layers added to the dish,
    calculating the preparation time using a time of 2 minutes per layer added.
    '''

    return number_of_layers * PREPARATION_TIME


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    '''Return elapsed cooking time.

    This function takes two integers representing te number of layers and the time already spent baking
     and calculates the total elapsed minutes spent cooking the lasagna.
    '''

    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
