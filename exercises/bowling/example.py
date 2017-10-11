

class BowlingGame(object):
    def __init__(self):
        self.rolls = []
        self.totalScore = 0

    def roll(self, pins):
        self.rolls.append(pins)

    def score(self):
        i = 0
        while (i < len(self.rolls)):
            pins = self.rolls[i]
            if (i % 2 == 0): #even numbers start a new frame
                #previous frame is a spare
                if ((self.rolls[i-1] + self.rolls[i-2]) == 10):
                    pins = pins * 2

            self.totalScore += pins
            i += 1

        return self.totalScore
