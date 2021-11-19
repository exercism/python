STATUS_WIN = 'win'
STATUS_LOSE = 'lose'
STATUS_ONGOING = 'ongoing'


class Hangman:
    def __init__(self, word):
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self.word = word
        self.masked_word = ''
        self.guesses = []
        for _ in self.word:
            self.masked_word += '_'

    def guess(self, char):
        if self.status != STATUS_ONGOING:
            raise ValueError('The game has already ended.')

        self.update_remaining_guesses(char)
        self.update_masked_word()
        self.update_status()

    def update_masked_word(self):
        self.masked_word = ''
        for idx in self.word:
            if idx not in self.guesses:
                self.masked_word += '_'
            else:
                self.masked_word += idx

    def update_remaining_guesses(self, char):
        if char not in self.word or char in self.guesses:
            self.remaining_guesses -= 1
        else:
            self.guesses.append(char)

    def update_status(self):
        if self.masked_word == self.word:
            self.status = STATUS_WIN
        elif self.remaining_guesses < 0:
            self.status = STATUS_LOSE
        else:
            self.status = STATUS_ONGOING

    def get_masked_word(self):
        return self.masked_word

    def get_status(self):
        return self.status
