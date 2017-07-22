class TwoBucket(object):

    def __init__(self, first_size, second_size, goal, start_bucket):
        self.first_size = first_size
        self.second_size = second_size
        self.goal = goal
        self.start_bucket = start_bucket

    def moves(self):
        if self.start_bucket == 'one':
            self.levels = [self.first_size, 0]
            return self._solve('start_from_first')
        else:
            self.levels = [0, self.second_size]
            return self._solve('start_from_second')

    def _solve(self, strategy):
        moves_count = 1

        while not self._solved():
            if strategy == 'start_from_first':
                self._start_from_first()
            else:
                self._start_from_second()
            moves_count += 1

        return moves_count

    def _solved(self):
        if self.goal in self.levels:
            if self.levels[0] == self.goal:
                self.goal_bucket = 'one'
                self.other_bucket = self.levels[1]
            else:
                self.goal_bucket = 'two'
                self.other_bucket = self.levels[0]

            return True

    def _start_from_first(self):
        if self._first_bucket_empty():
            self._fill_first_bucket()
        elif self._second_bucket_full():
            self._empty_second_bucket()
        elif self._can_move_to_second_bucket():
            self._fill_second_bucket_from_first()

    def _start_from_second(self):
        if self._first_bucket_full():
            self._empty_first_bucket()
        elif self._second_bucket_empty():
            self._fill_second_bucket()
        elif self._can_move_to_first_bucket():
            self._fill_first_bucket_from_second()

    def _first_bucket_empty(self):
        return self.levels[0] == 0

    def _first_bucket_full(self):
        return self.levels[0] == self.first_size

    def _second_bucket_empty(self):
        return self.levels[1] == 0

    def _second_bucket_full(self):
        return self.levels[1] == self.second_size

    def _can_move_to_second_bucket(self):
        return (self._first_bucket_full() and not self._second_bucket_full()) \
            or (not self._first_bucket_full() and self._second_bucket_empty())

    def _can_move_to_first_bucket(self):
        return sum(self.levels) != self.first_size

    def _empty_first_bucket(self):
        self.levels = [0, self.levels[1]]

    def _fill_first_bucket(self):
        self.levels = [self.first_size, self.levels[1]]

    def _empty_second_bucket(self):
        self.levels = [self.levels[0], 0]

    def _fill_second_bucket(self):
        self.levels = [self.levels[0], self.second_size]

    def _fill_first_bucket_from_second(self):
        self.levels = [min([sum(self.levels), self.first_size]),
                       max([sum(self.levels) - self.first_size, 0])]

    def _fill_second_bucket_from_first(self):
        self.levels = [max([sum(self.levels) - self.second_size, 0]),
                       min([sum(self.levels), self.second_size])]
