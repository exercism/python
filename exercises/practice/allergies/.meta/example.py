class Allergies:

    _allergies = [
        "eggs",
        "peanuts",
        "shellfish",
        "strawberries",
        "tomatoes",
        "chocolate",
        "pollen",
        "cats"
    ]

    def __init__(self, score):
        self.score = score

    def allergic_to(self, item):
        return bool(self.score & 1 << self._allergies.index(item))

    @property
    def lst(self):
        return [allergy for allergy in self._allergies
                if self.allergic_to(allergy)]
