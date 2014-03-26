def powers_of_2(n):
    """Return a list of the powers of 2 whose sum is the input number."""
    return [2 ** exponent
            for exponent, bit in enumerate(bin(n)[:1:-1])
            if bit == '1']


class Allergies(object):

    __allergens = {2 ** exponent: allergen
                   for exponent, allergen in enumerate(
                       ("eggs peanuts shellfish strawberries tomatoes "
                        "chocolate pollen cats").split())}

    def __init__(self, score):
        self.score = score
        self.list = [self.__allergens[p]
                     for p in powers_of_2(score)
                     if p in self.__allergens]

    def is_allergic_to(self, allergen):
        return allergen in self.list
