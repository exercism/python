MAX_PINS = 10
NUM_FRAMES = 10
NUM_ROLLS = 20


class BowlingGame(object):
    def __init__(self):
        self.rolls = []
        self.totalScore = 0

    def roll(self, pins):
        self.rolls.append(pins)

    def score(self):
        roll_index = 0
        frame_index = 1

        while (frame_index <= NUM_FRAMES):
            # get the two rolls that make up a frame
            roll1 = self.rolls[roll_index]
            if(not self.isLastFrame(roll_index)):
                roll2 = self.rolls[roll_index + 1]
            else:
                roll2 = 0

            if (self.isStrike(roll1)):
                self.totalScore += roll1 + self.stikeBonus(roll_index)
                # frame should only advance by 1 roll if it was a strike
                roll_index += 1
            else:
                if(self.isSpare(roll1, roll2)):
                    self.totalScore += roll1 + roll2 + \
                                       self.spareBonus(roll_index)
                else:
                    self.totalScore += roll1 + roll2
                # frame should advance by 2 rolls normally
                roll_index += 2

            frame_index += 1

        return self.totalScore

    def isStrike(self, pins):
        if (pins == MAX_PINS):
            return True
        else:
            return False

    def isSpare(self, roll1, roll2):
        if (roll1 + roll2 == MAX_PINS):
            return True
        else:
            return False

    def stikeBonus(self, rollindex):
        return self.rolls[rollindex + 1] + self.rolls[rollindex + 2]

    def spareBonus(self, rollindex):
        return self.rolls[rollindex + 2]

    def isLastFrame(self, roll_index):
        if(roll_index == len(self.rolls)):
            return True
        return False
