MAX_PINS = 10
NUM_FRAMES = 10
NUM_ROLLS = 20


class BowlingGame(object):
    def __init__(self):
        self.rolls = []
        self.totalScore = 0
        self.currentFrame = Frame()

    def roll(self, pins):
        # valid roll between 0-10
        if (not self.currentFrame.isOpen()):
            self.currentFrame = Frame()
        if (pins in range(MAX_PINS + 1)):
                self.currentFrame.roll(pins)
                self.rolls.append(self.currentFrame)
                #self.rolls.append(pins)
        else:
            raise ValueError

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

            print ("roll1: " + str(roll1) + " roll2: " + str(roll2) + " frame: " + str(frame_index) + "/" + str(NUM_FRAMES))

            if (self.isStrike(roll1)):
                print("adding " + str(roll1)  + " strike bonus " + str(self.stikeBonus(roll_index)))
                self.totalScore += roll1 + self.stikeBonus(roll_index)
                # frame should only advance by 1 roll if it was a strike
                roll_index += 1
            else:
                # Check that this is even a valid frame
                if (roll1 + roll2 > MAX_PINS):
                    raise ValueError

                if(self.isSpare(roll1, roll2)):
                    print("adding " + str(roll1) + " + " + str(roll2) + " spare bonus " + str(self.spareBonus(roll_index)))
                    self.totalScore += roll1 + roll2 + \
                                       self.spareBonus(roll_index)
                else:
                    print("adding " + str(roll1) + " + " + str(roll2))
                    self.totalScore += roll1 + roll2
                # frame should advance by 2 rolls normally
                roll_index += 2

            frame_index += 1

        print(self.totalScore)
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
        bonusroll1 = self.rolls[rollindex + 1]
        bonusroll2 = self.rolls[rollindex + 2]
        # edge case - if the last roll is a stike the bonus rolls needs to be
        # validated
        if (bonusroll1 != 10 and (bonusroll1 + bonusroll2 > MAX_PINS)):
            raise ValueError
        else:
            return bonusroll1 + bonusroll2

    def spareBonus(self, rollindex):
        return self.rolls[rollindex + 2]

    def isLastFrame(self, roll_index):
        if(roll_index == len(self.rolls)):
            return True
        return False


class Frame(object):

    def __init__(self):
        self.roll1 = None
        self.roll2 = None
        self.open = True

    def roll(self, roll):
        # if it's a strike we close the frame
        if (roll > 10):
            self.roll1 = 10
            self.open = False
        else:
            # first roll, but frame is still open
            if (self.roll1 is not None):
                self.roll1 = roll
            else:
                # second roll, closes frame
                self.roll2 = roll
                self.open = False

    def isOpen(self):
        return self.open
