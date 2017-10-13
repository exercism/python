MAX_PINS = 10
NUM_FRAMES = 10
NUM_ROLLS = 20


class BowlingGame(object):
    def __init__(self):
        self.rolls = []
        self.totalScore = 0
        self.currentFrame = Frame()
        self.bonusRolls = 0

    def roll(self, pins):
        if (self.currentFrame.isOpen() == False):
            self.currentFrame = Frame()
        # valid roll between 0-10
        if (self.isBonusRoll()):
            self.bonusRolls += 1
        if (pins in range(MAX_PINS + 1)):
                self.currentFrame.roll(pins)
                # if we closed it add it to our rolls
                if (self.currentFrame.isOpen() == False or self.bonusRolls >= 2):
                    self.rolls.append(self.currentFrame)
        else:
            raise ValueError

    def score(self):
        frame_index = 0

        while (frame_index <= NUM_FRAMES-1):
            print()
            frame = self.rolls[frame_index].getFrame()

            roll1 = frame[0]
            roll2 = frame[1]

            print ("roll1: " + str(roll1) + " roll2: " + str(roll2) + " frame: " + str(frame_index) + "/" + str(NUM_FRAMES-1))

            if (self.isStrike(roll1)):
                print("adding " + str(roll1)  + " strike bonus " + str(self.stikeBonus(frame_index)))
                self.totalScore += roll1 + self.stikeBonus(frame_index)

            else:
                # Check that this is even a valid frame
                if (roll1 + roll2 > MAX_PINS):
                    raise ValueError

                if(self.isSpare(roll1, roll2)):
                    print("adding " + str(roll1) + " + " + str(roll2) + " spare bonus " + str(self.spareBonus(frame_index)))
                    self.totalScore += roll1 + roll2 + \
                                       self.spareBonus(frame_index)
                else:
                    print("adding " + str(roll1) + " + " + str(roll2))
                    self.totalScore += roll1 + roll2

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

    def isBonusRoll(self):
        if (len(self.rolls) >= NUM_FRAMES):
            return True
        else:
            return False

    def stikeBonus(self, frame_index):
        bonusroll1 = self.rolls[frame_index+1].getFrame()[0]
        bonusroll2 = 0
        # need to go further out if the next on is a strike
        if (bonusroll1 == 10):
            #if (self.isLastFrame(frame_index + 1) == False):
                #print("next frame")
            bonusroll2 = self.rolls[frame_index+2].getFrame()[0]
        else:
            bonusroll2 = self.rolls[frame_index+1].getFrame()[1]
        # edge case - if the last roll is a stike the bonus rolls needs to be
        # validated
        print("Bonus roll: ", str(bonusroll1) + " + " + str(bonusroll2))
        if (not self.isStrike(bonusroll1) and (bonusroll1 + bonusroll2 > MAX_PINS)):
            raise ValueError
        else:
            return bonusroll1 + bonusroll2

    def spareBonus(self, frame_index):
        return self.rolls[frame_index+1].getFrame()[0]

    def isLastFrame(self, frame_index):
        if(frame_index >= len(self.rolls)-1):
            return True
        return False


class Frame(object):

    def __init__(self):
        self.rolls = [None, None]
        self.open = True

    def roll(self, roll):
        # if it's a strike we close the frame
        if (roll == 10):
            self.rolls[0] = 10
            self.rolls[1] = 0
            self.open = False
        else:
            # first roll, but frame is still open
            if (self.rolls[0] is None):
                self.rolls[0] = roll
            else:
                # second roll, closes frame
                self.rolls[1] = roll
                self.open = False

    def isOpen(self):
        return self.open

    def getFrame(self):
        return self.rolls
