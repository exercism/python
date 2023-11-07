import unittest
import pytest
from arcade_game import eat_ghost, score, lose, win


class GhostGobbleGameTest(unittest.TestCase):

    @pytest.mark.task(taskno=1)
    def test_ghost_gets_eaten(self):
        actual_result = eat_ghost(True, True)
        error_message = ('Called eat_ghost(True, True).'
                        f'The function returned {actual_result}, but the '
                        f'tests expected that the ghost gets eaten (True).')

        self.assertIs(actual_result, True, msg=error_message)

    @pytest.mark.task(taskno=1)
    def test_ghost_does_not_get_eaten_because_no_power_pellet_active(self):
        actual_result = eat_ghost(False, True)
        error_message = ('Called eat_ghost(False, True).'
                         f'The function returned {actual_result}, but the '
                         f'tests expected that the '
                         'ghost **does not** get eaten because '
                         'no power pellet was active.')

        self.assertIs(actual_result, False, msg=error_message)

    @pytest.mark.task(taskno=1)
    def test_ghost_does_not_get_eaten_because_not_touching_ghost(self):
        actual_result = eat_ghost(True, False)
        error_message = ('Called eat_ghost(True, False).'
                         f'The function returned {actual_result}, but the '
                         f'tests expected that the '
                         'ghost **does not** get eaten because '
                         'the player was not touching the ghost.')

        self.assertIs(actual_result, False, msg=error_message)

    @pytest.mark.task(taskno=2)
    def test_score_when_eating_dot(self):
        actual_result = score(False, True)
        error_message = ('Called score(False, True).'
                         f'The function returned {actual_result}, but the '
                         f'tests expected that the '
                         'player scores because they were touching a dot.')

        self.assertIs(actual_result, True, msg=error_message)

    @pytest.mark.task(taskno=2)
    def test_score_when_eating_power_pellet(self):
        actual_result = score(True, False)
        error_message = ('Called score(True, False).'
                         f'The function returned {actual_result}, but the '
                         f'tests expected that the '
                         'player scores because they '
                         'were touching a power pellet.')

        self.assertIs(actual_result,True,msg=error_message)

    @pytest.mark.task(taskno=2)
    def test_no_score_when_nothing_eaten(self):
        actual_result = score(False, False)
        error_message = ('Called score(False, False).'
                         f'The function returned {actual_result}, but the '
                         f'tests expected that the '
                         'player **does not** score because they '
                         'were not touching anything.')
        self.assertIs(actual_result, False,msg=error_message)

    @pytest.mark.task(taskno=3)
    def test_lose_if_touching_a_ghost_without_a_power_pellet_active(self):
        actual_result = lose(False, True)
        error_message = ('Called lose(False, True).'
                         f'The function returned {actual_result}, but the '
                         f'tests expected that the '
                         'player loses because they touched a '
                         'ghost without a power pellet activated.')
        self.assertIs(
            actual_result, True, msg=error_message)

    @pytest.mark.task(taskno=3)
    def test_dont_lose_if_touching_a_ghost_with_a_power_pellet_active(self):
        actual_result = lose(True, True)
        error_message = ('Called lose(True, True).'
                         f'The function returned {actual_result}, but the '
                         f'tests expected that the '
                         'player **does not** lose because when they touched a '
                         'ghost, a power pellet was active.')

        self.assertIs(actual_result, False, msg=error_message)

    @pytest.mark.task(taskno=3)
    def test_dont_lose_if_not_touching_a_ghost(self):
        actual_result = lose(True, False)
        error_message = ('Called lose(True, False).'
                         f'The function returned {actual_result}, but the '
                         f'tests expected that the '
                         'player **does not** lose because they were '
                         'not touching a ghost.')

        self.assertIs(actual_result, False, msg=error_message)

    @pytest.mark.task(taskno=4)
    def test_win_if_all_dots_eaten(self):
        actual_result = win(True, False, False)
        error_message = ('Called win(True, False, False).'
                         f'The function returned {actual_result}, but the '
                         f'tests expected that the '
                         'player wins because all the dots were eaten.')

        self.assertIs(actual_result, True, msg=error_message)

    @pytest.mark.task(taskno=4)
    def test_dont_win_if_all_dots_eaten_but_touching_a_ghost(self):
        actual_result = win(True, False, True)
        error_message = ('Called win(True, False, True).'
                         f'The function returned {actual_result}, but the '
                         f'tests expected that the '
                         'player **does not** win, because '
                         'the player was touching a ghost.')

        self.assertIs(actual_result, False, msg=error_message)

    @pytest.mark.task(taskno=4)
    def test_win_if_all_dots_eaten_and_touching_a_ghost_with_a_power_pellet_active(self):
        actual_result = win(True, True, True)
        error_message = ('Called win(True, True, True).'
                         f'The function returned {actual_result}, but the '
                         f'tests expected that the player wins, '
                         f'because a power pellet was active when they '
                         f'touched a ghost.')

        self.assertIs(actual_result, True, msg=error_message)

    @pytest.mark.task(taskno=4)
    def test_dont_win_if_not_all_dots_eaten(self):
        actual_result = win(False, True, True)
        error_message = ('Called win(False, True, True).'
                         f'The function returned {actual_result}, but the '
                         f'tests expected that the player **does not** win, '
                         f'because the player did not eat all of the dots.')

        self.assertIs(actual_result, False, msg=error_message)

