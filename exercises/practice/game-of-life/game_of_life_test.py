# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/game-of-life/canonical-data.json
# File last updated on 2026-01-26

import unittest

from game_of_life import (
    tick,
)


class GameOfLifeTest(unittest.TestCase):
    def test_empty_matrix(self):
        matrix = []
        expected = []
        self.assertEqual(tick(matrix), expected)

    def test_live_cells_with_zero_live_neighbors_die(self):
        matrix = [
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0],
        ]
        expected = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ]
        self.assertEqual(tick(matrix), expected)

    def test_live_cells_with_only_one_live_neighbor_die(self):
        matrix = [
            [0, 0, 0],
            [0, 1, 0],
            [0, 1, 0],
        ]
        expected = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ]
        self.assertEqual(tick(matrix), expected)

    def test_live_cells_with_two_live_neighbors_stay_alive(self):
        matrix = [
            [1, 0, 1],
            [1, 0, 1],
            [1, 0, 1],
        ]
        expected = [
            [0, 0, 0],
            [1, 0, 1],
            [0, 0, 0],
        ]
        self.assertEqual(tick(matrix), expected)

    def test_live_cells_with_three_live_neighbors_stay_alive(self):
        matrix = [
            [0, 1, 0],
            [1, 0, 0],
            [1, 1, 0],
        ]
        expected = [
            [0, 0, 0],
            [1, 0, 0],
            [1, 1, 0],
        ]
        self.assertEqual(tick(matrix), expected)

    def test_dead_cells_with_three_live_neighbors_become_alive(self):
        matrix = [
            [1, 1, 0],
            [0, 0, 0],
            [1, 0, 0],
        ]
        expected = [
            [0, 0, 0],
            [1, 1, 0],
            [0, 0, 0],
        ]
        self.assertEqual(tick(matrix), expected)

    def test_live_cells_with_four_or_more_neighbors_die(self):
        matrix = [
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1],
        ]
        expected = [
            [1, 0, 1],
            [0, 0, 0],
            [1, 0, 1],
        ]
        self.assertEqual(tick(matrix), expected)

    def test_bigger_matrix(self):
        matrix = [
            [1, 1, 0, 1, 1, 0, 0, 0],
            [1, 0, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 1, 1, 1],
            [0, 0, 0, 0, 0, 1, 1, 0],
            [1, 0, 0, 0, 1, 1, 0, 0],
            [1, 1, 0, 0, 0, 1, 1, 1],
            [0, 0, 1, 0, 1, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 1, 1],
        ]
        expected = [
            [1, 1, 0, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 1, 0],
            [1, 0, 1, 1, 1, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 0, 0, 1, 0, 0, 1],
            [1, 1, 0, 1, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 1],
        ]
        self.assertEqual(tick(matrix), expected)
