class Hangman:
    def __init__(self, word):
        self.remainingGuesses = 9
        self.status = 'busy'
        self.word = word
        self.masked_word = ''
        self.guesses = []
        for i in self.word:
            self.masked_word += '_'

    def guess(self, char):
        self.update_remaining_guesses(char)
        self.update_masked_word()
        self.update_status()

    def update_masked_word(self):
        self.masked_word = ''
        for i in self.word:
            if i not in self.guesses:
                self.masked_word += '_'
            else:
                self.masked_word += i

    def update_remaining_guesses(self, char):
        if char not in self.word or char in self.guesses:
            self.remainingGuesses -= 1
        else:
            self.guesses.append(char)

    def update_status(self):
        if self.masked_word == self.word:
            self.status = 'win'
        elif self.remainingGuesses < 0:
            self.status = 'lose'
        else:
            self.status = 'busy'

    def get_masked_word(self):
        return self.masked_word

    def get_status(self):
        return self.status
