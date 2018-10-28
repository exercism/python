class HighScores(object):
    def __init__(self, scores):
        self.scores = scores

    @property
    def latest(self):
        return self.scores[-1]

    @property
    def highest(self):
        return max(self.scores)

    @property
    def top(self):
        return sorted(self.scores, reverse=True)[:3]

    @property
    def report(self):
        difference = self.highest - self.latest
        result_qualifier = (
            "" if difference <= 0 else "{} short of ".format(difference)
        )
        return "Your latest score was {}. That's {}your personal best!".format(
            self.latest, result_qualifier
        )
