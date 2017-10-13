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
        if (self.currentFrame.isOpen() == False):
            self.currentFrame = Frame()
        if (pins in range(MAX_PINS + 1)):
                self.currentFrame.roll(pins)
                # if we closed it add it to our rolls
                if (self.currentFrame.isOpen() == False):
                    self.rolls.append(self.currentFrame)
                #self.rolls.append(pins)
        else:
            raise ValueError

    def score(self):
        roll_index = 0
        frame_index = 0

        while (frame_index <= NUM_FRAMES-1):
            frame = self.rolls[frame_index].getFrame()
            if(self.isLastFrame(frame_index) == False):
                next_frame = self.rolls[frame_index+1].getFrame()
            # get the two rolls that make up a frame
            roll1 = frame[0]
            if(not self.isLastFrame(frame_index)):
                roll2 = frame[1]
            else:
                roll2 = 0

            print ("roll1: " + str(roll1) + " roll2: " + str(roll2) + " frame: " + str(frame_index) + "/" + str(NUM_FRAMES))

            if (self.isStrike(roll1)):
                print("adding " + str(roll1)  + " strike bonus " + str(self.stikeBonus(next_frame, frame_index)))
                self.totalScore += roll1 + self.stikeBonus(next_frame, frame_index)
                # frame should only advance by 1 roll if it was a strike
                roll_index += 1
            else:
                # Check that this is even a valid frame
                if (roll1 + roll2 > MAX_PINS):
                    raise ValueError

                if(self.isSpare(roll1, roll2)):
                    print("adding " + str(roll1) + " + " + str(roll2) + " spare bonus " + str(self.spareBonus(next_frame)))
                    self.totalScore += roll1 + roll2 + \
                                       self.spareBonus(next_frame)
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

    def stikeBonus(self, next_frame, frame_index):
        bonusroll1 = next_frame[0]
        bonusroll2 = 0
        # need to go further out if the next on is a strike
        if (next_frame[0] == 10):
            print( str(frame_index + 1) + " is the frame")
            if (self.isLastFrame((frame_index + 1) == False)):
                bonusroll2 = self.rolls[frame_index+2].getFrame()[0]
        else:
            bonusroll2 = next_frame[1]
        # edge case - if the last roll is a stike the bonus rolls needs to be
        # validated
        if (bonusroll1 != 10 and (bonusroll1 + bonusroll2 > MAX_PINS)):
            raise ValueError
        else:
            return bonusroll1 + bonusroll2

    def spareBonus(self, next_frame):
        return next_frame[0]

    def isLastFrame(self, frame_index):
        if(frame_index == NUM_FRAMES-1):
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
