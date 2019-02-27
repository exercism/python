# Game status categories
# Change the values as you see fit
STATUS_WIN = None
STATUS_LOSE = None
STATUS_ONGOING = None


class Hangman(object):
    def __init__(self, word):
        self.remainingGuesses = 9
        self.status = STATUS_ONGOING

    def guess(self, char):
        pass

    def get_masked_word(self):
        pass

    def get_status(self):
        pass
