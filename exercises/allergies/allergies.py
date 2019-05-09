class Allergies(object):

    def __init__(self, score):
        pass

    def allergic_to(self, allergy):
        return bool(self.score & 1 << self._allergies.index(allergy))

    @property
    def lst(self):
        pass
