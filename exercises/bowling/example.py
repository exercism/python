

class BowlingGame(object):
    def __init__(self):
        self.rolls = []
        self.totalScore = 0

    def roll(self, pins):
        self.rolls.append(pins)

    def score(self):
        for roll in self.rolls:
            self.totalScore += roll

        return self.totalScore
