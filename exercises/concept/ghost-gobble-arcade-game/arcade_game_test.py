import unittest
import pytest
from arcade_game import eat_ghost, score, lose, win


class GhostGobbleGameTest(unittest.TestCase):

    @pytest.mark.task(taskno=1)
    def test_ghost_gets_eaten(self):
        self.assertIs(
            eat_ghost(True, True),
            True,
            msg="ghost should get eaten"
        )

    @pytest.mark.task(taskno=1)
    def test_ghost_does_not_get_eaten_because_no_power_pellet_active(self):
        self.assertIs(
            eat_ghost(False, True),
            False,
            msg="ghost does not get eaten because no power pellet active"
        )

    @pytest.mark.task(taskno=1)
    def test_ghost_does_not_get_eaten_because_not_touching_ghost(self):
        self.assertIs(
            eat_ghost(True, False),
            False,
            msg="ghost does not get eaten because not touching ghost"
        )

    @pytest.mark.task(taskno=2)
    def test_score_when_eating_dot(self):
        self.assertIs(
          score(False, True),
          True,
          msg="score when eating dot"
        )

    @pytest.mark.task(taskno=2)
    def test_score_when_eating_power_pellet(self):
        self.assertIs(
            score(True, False),
            True,
            msg="score when eating power pellet"
        )

    @pytest.mark.task(taskno=2)
    def test_no_score_when_nothing_eaten(self):
        self.assertIs(
            score(False, False),
            False,
            msg="no score when nothing eaten"
        )

    @pytest.mark.task(taskno=3)
    def test_lose_if_touching_a_ghost_without_a_power_pellet_active(self):
        self.assertIs(
            lose(False, True),
            True,
            msg="lose if touching a ghost without a power pellet active"
        )

    @pytest.mark.task(taskno=3)
    def test_dont_lose_if_touching_a_ghost_with_a_power_pellet_active(self):
        self.assertIs(
            lose(True, True),
            False,
            msg="don't lose if touching a ghost with a power pellet active"
        )

    @pytest.mark.task(taskno=3)
    def test_dont_lose_if_not_touching_a_ghost(self):
        self.assertIs(
            lose(True, False),
            False,
            msg="don't lose if not touching a ghost"
        )

    @pytest.mark.task(taskno=4)
    def test_win_if_all_dots_eaten(self):
        self.assertIs(
            win(True, False, False),
            True,
            msg="win if all dots eaten"
        )

    @pytest.mark.task(taskno=4)
    def test_dont_win_if_all_dots_eaten_but_touching_a_ghost(self):
        self.assertIs(
            win(True, False, True),
            False,
            msg="don't win if all dots eaten, but touching a ghost"
        )

    @pytest.mark.task(taskno=4)
    def test_win_if_all_dots_eaten_and_touching_a_ghost_with_a_power_pellet_active(self):
        self.assertIs(
            win(True, True, True),
            True,
            msg="win if all dots eaten and touching a ghost with a power pellet active"
        )

    @pytest.mark.task(taskno=4)
    def test_dont_win_if_not_all_dots_eaten(self):
        self.assertIs(
            win(False, True, True),
            False,
            msg="don't win if not all dots eaten and touching a ghost with a power pellet active"
        )
