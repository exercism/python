MAX_FRAME = 10


class Frame:
    def __init__(self, idx):
        self.idx = idx
        self.throws = []

    @property
    def total_pins(self):
        """Total pins knocked down in a frame."""
        return sum(self.throws)

    def is_strike(self):
        return self.total_pins == 10 and len(self.throws) == 1

    def is_spare(self):
        return self.total_pins == 10 and len(self.throws) == 2

    def is_open(self):
        return self.total_pins < 10 and len(self.throws) == 2

    def is_closed(self):
        """Return whether a frame is over."""
        return self.total_pins == 10 or len(self.throws) == 2

    def throw(self, pins):
        if self.total_pins + pins > 10:
            raise ValueError("a frame's rolls cannot exceed 10")
        self.throws.append(pins)

    def score(self, next_throws):
        result = self.total_pins
        if self.is_strike():
            result += sum(next_throws[:2])
        elif self.is_spare():
            result += sum(next_throws[:1])
        return result


class BowlingGame:
    def __init__(self):
        self.current_frame_idx = 0
        self.bonus_throws = []
        self.frames = [Frame(idx) for idx in range(MAX_FRAME)]

    @property
    def current_frame(self):
        return self.frames[self.current_frame_idx]

    def next_throws(self, frame_idx):
        """Return a frame's next throws in the form of a list."""
        throws = []
        for idx in range(frame_idx + 1, MAX_FRAME):
            throws.extend(self.frames[idx].throws)
        throws.extend(self.bonus_throws)
        return throws

    def roll_bonus(self, pins):
        tenth_frame = self.frames[-1]
        if tenth_frame.is_open():
            raise IndexError('cannot throw bonus with an open tenth frame')

        self.bonus_throws.append(pins)

        # Check against invalid fill balls, e.g. [3, 10]
        if (len(self.bonus_throws) == 2 and self.bonus_throws[0] != 10 and
                sum(self.bonus_throws) > 10):
            raise ValueError('invalid fill balls')

        # Check if there are more bonuses than it should be
        if tenth_frame.is_strike() and len(self.bonus_throws) > 2:
            raise IndexError(
                'wrong number of fill balls when the tenth frame is a strike')
        elif tenth_frame.is_spare() and len(self.bonus_throws) > 1:
            raise IndexError(
                'wrong number of fill balls when the tenth frame is a spare')

    def roll(self, pins):
        if not 0 <= pins <= 10:
            raise ValueError('invalid pins')
        elif self.current_frame_idx == MAX_FRAME:
            self.roll_bonus(pins)
        else:
            self.current_frame.throw(pins)
            if self.current_frame.is_closed():
                self.current_frame_idx += 1

    def score(self):
        if self.current_frame_idx < MAX_FRAME:
            raise IndexError('frame less than 10')
        if self.frames[-1].is_spare() and len(self.bonus_throws) != 1:
            raise IndexError(
                'one bonus must be rolled when the tenth frame is spare')
        if self.frames[-1].is_strike() and len(self.bonus_throws) != 2:
            raise IndexError(
                'two bonuses must be rolled when the tenth frame is strike')
        return sum(frame.score(self.next_throws(frame.idx))
                   for frame in self.frames)
