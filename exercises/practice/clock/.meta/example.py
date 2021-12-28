class Clock:
    """Clock that displays 24 hour clock that rollsover properly"""

    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute
        self.cleanup()

    def __repr__(self):
        return f'Clock({self.hour}, {self.minute})'

    def __str__(self):
        return '{:02d}:{:02d}'.format(self.hour, self.minute)

    def __eq__(self, other):
        return repr(self) == repr(other)

    def __add__(self, minutes):
        self.minute += minutes
        return self.cleanup()

    def __sub__(self, minutes):
        self.minute -= minutes
        return self.cleanup()

    def cleanup(self):
        self.hour += self.minute // 60
        self.hour %= 24
        self.minute %= 60
        return self
