class HighScores(object):
    def __init__(self, scores):
        self.scores = scores

    def latest(self):
        return self.scores[-1]

    def highest(self):
        return max(self.scores)

    def top(self):
        return sorted(self.scores, reverse=True)[:3]

    def report(self):
        difference = self.highest() - self.latest()
        result_qualifier = (
            "" if difference <= 0 else "{} short of ".format(difference)
        )
        return "Your latest score was {}. That's {}your personal best!".format(
            self.latest(), result_qualifier
        )
