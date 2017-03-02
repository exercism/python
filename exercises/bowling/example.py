from enum import Enum


class State(Enum):
    OPEN = 1
    SPARE = 2
    STRIKE = 3


class BowlingGame:
    def __init__(self):
        self._score = 0
        self._roll = 1
        self._frame_score = 0
        self._current_frame = 1
        self._max_frame_score = self._max_frames = 10
        self._frame_states = []
        self._game_finished = False
        self._last_frame = False
        self._rolls = []

    def roll(self, pins):
        if self._game_finished:
            raise Exception('Cannot roll after game is over')
        elif 0 <= pins <= 10:
            self._last_frame = self._current_frame == self._max_frames
            self._rolls.append(pins)
            self._add_bonuses(pins)
            self._frame_score += pins

            if self._roll == 1:
                self._roll += 1 if self._last_frame or not self._is_strike(pins) else 0
                if self._is_strike(pins):
                    self._frame_states.append(State.STRIKE)
                    if not self._last_frame:
                        self._next_frame()
            elif self._roll == 2:
                if self._last_frame and self._frame_states[-1] == State.STRIKE:
                    if self._is_strike(pins):
                        self._frame_states.append(State.STRIKE)
                    self._roll += 1
                elif self._is_spare():
                    self._frame_states.append(State.SPARE)
                    if self._last_frame:
                        self._roll += 1
                    else:
                        self._next_frame()
                elif self._is_valid_frame(limit=self._max_frame_score):
                    self._frame_states.append(State.OPEN)
                    if self._last_frame:
                        self._score += self._frame_score
                        self._game_finished = True
                    else:
                        self._next_frame()
                else:
                    raise Exception('Pin count exceeds pins on the lane')
            elif self._roll == 3:
                if self._is_valid_frame(last_roll=True):
                    self._score += self._frame_score
                    self._game_finished = True
                else:
                    raise Exception('Pin count exceeds pins on the lane')
        elif pins < 0:
            raise Exception('Negative roll is invalid')
        else:
            raise Exception('Pin count exceeds pins on the lane')

    def _add_bonuses(self, pins):
        if self._frame_states:
            if self._frame_states[-1] == State.STRIKE and not self._last_frame:
                self._score += pins
            elif self._frame_states[-1] == State.SPARE:
                self._score += pins if self._roll == 1 else 0

            if len(self._frame_states) >= 2 and self._roll == 1 and \
                    self._frame_states[-2] == self._frame_states[-1] == State.STRIKE:
                self._score += pins if not self._last_frame else 3 * pins

    def _next_frame(self):
        self._current_frame += 1
        self._score += self._frame_score
        self._frame_score = 0
        self._roll = 1

    def _is_strike(self, pins):
        return pins == self._max_frame_score

    def _is_spare(self):
        return self._frame_score == self._max_frame_score

    def _is_valid_frame(self, limit=None, last_roll=False):
        if last_roll:
            if self._frame_states[-1] == State.SPARE:
                return self._rolls[-1] <= self._max_frame_score
            elif self._frame_states[-1] == State.STRIKE:
                if self._frame_states[-2] == State.STRIKE:
                    return self._rolls[-1] <= self._max_frame_score
                else:
                    return sum(self._rolls[-2:]) <= self._max_frame_score

        else:
            return self._frame_score <= limit

    def score(self):
        if not self._game_finished:
            raise Exception('Score cannot be taken until the end of the game')
        else:
            return self._score
