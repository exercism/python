# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/tournament/canonical-data.json
# File last updated on 2023-07-19

import unittest

from tournament import (
    tally,
)


class TournamentTest(unittest.TestCase):
    def test_just_the_header_if_no_input(self):
        results = []
        table = ["Team                           | MP |  W |  D |  L |  P"]
        self.assertEqual(tally(results), table)

    def test_a_win_is_three_points_a_loss_is_zero_points(self):
        results = ["Allegoric Alaskans;Blithering Badgers;win"]
        table = [
            "Team                           | MP |  W |  D |  L |  P",
            "Allegoric Alaskans             |  1 |  1 |  0 |  0 |  3",
            "Blithering Badgers             |  1 |  0 |  0 |  1 |  0",
        ]
        self.assertEqual(tally(results), table)

    def test_a_win_can_also_be_expressed_as_a_loss(self):
        results = ["Blithering Badgers;Allegoric Alaskans;loss"]
        table = [
            "Team                           | MP |  W |  D |  L |  P",
            "Allegoric Alaskans             |  1 |  1 |  0 |  0 |  3",
            "Blithering Badgers             |  1 |  0 |  0 |  1 |  0",
        ]
        self.assertEqual(tally(results), table)

    def test_a_different_team_can_win(self):
        results = ["Blithering Badgers;Allegoric Alaskans;win"]
        table = [
            "Team                           | MP |  W |  D |  L |  P",
            "Blithering Badgers             |  1 |  1 |  0 |  0 |  3",
            "Allegoric Alaskans             |  1 |  0 |  0 |  1 |  0",
        ]
        self.assertEqual(tally(results), table)

    def test_a_draw_is_one_point_each(self):
        results = ["Allegoric Alaskans;Blithering Badgers;draw"]
        table = [
            "Team                           | MP |  W |  D |  L |  P",
            "Allegoric Alaskans             |  1 |  0 |  1 |  0 |  1",
            "Blithering Badgers             |  1 |  0 |  1 |  0 |  1",
        ]
        self.assertEqual(tally(results), table)

    def test_there_can_be_more_than_one_match(self):
        results = [
            "Allegoric Alaskans;Blithering Badgers;win",
            "Allegoric Alaskans;Blithering Badgers;win",
        ]
        table = [
            "Team                           | MP |  W |  D |  L |  P",
            "Allegoric Alaskans             |  2 |  2 |  0 |  0 |  6",
            "Blithering Badgers             |  2 |  0 |  0 |  2 |  0",
        ]
        self.assertEqual(tally(results), table)

    def test_there_can_be_more_than_one_winner(self):
        results = [
            "Allegoric Alaskans;Blithering Badgers;loss",
            "Allegoric Alaskans;Blithering Badgers;win",
        ]
        table = [
            "Team                           | MP |  W |  D |  L |  P",
            "Allegoric Alaskans             |  2 |  1 |  0 |  1 |  3",
            "Blithering Badgers             |  2 |  1 |  0 |  1 |  3",
        ]
        self.assertEqual(tally(results), table)

    def test_there_can_be_more_than_two_teams(self):
        results = [
            "Allegoric Alaskans;Blithering Badgers;win",
            "Blithering Badgers;Courageous Californians;win",
            "Courageous Californians;Allegoric Alaskans;loss",
        ]
        table = [
            "Team                           | MP |  W |  D |  L |  P",
            "Allegoric Alaskans             |  2 |  2 |  0 |  0 |  6",
            "Blithering Badgers             |  2 |  1 |  0 |  1 |  3",
            "Courageous Californians        |  2 |  0 |  0 |  2 |  0",
        ]
        self.assertEqual(tally(results), table)

    def test_typical_input(self):
        results = [
            "Allegoric Alaskans;Blithering Badgers;win",
            "Devastating Donkeys;Courageous Californians;draw",
            "Devastating Donkeys;Allegoric Alaskans;win",
            "Courageous Californians;Blithering Badgers;loss",
            "Blithering Badgers;Devastating Donkeys;loss",
            "Allegoric Alaskans;Courageous Californians;win",
        ]
        table = [
            "Team                           | MP |  W |  D |  L |  P",
            "Devastating Donkeys            |  3 |  2 |  1 |  0 |  7",
            "Allegoric Alaskans             |  3 |  2 |  0 |  1 |  6",
            "Blithering Badgers             |  3 |  1 |  0 |  2 |  3",
            "Courageous Californians        |  3 |  0 |  1 |  2 |  1",
        ]
        self.assertEqual(tally(results), table)

    def test_incomplete_competition_not_all_pairs_have_played(self):
        results = [
            "Allegoric Alaskans;Blithering Badgers;loss",
            "Devastating Donkeys;Allegoric Alaskans;loss",
            "Courageous Californians;Blithering Badgers;draw",
            "Allegoric Alaskans;Courageous Californians;win",
        ]
        table = [
            "Team                           | MP |  W |  D |  L |  P",
            "Allegoric Alaskans             |  3 |  2 |  0 |  1 |  6",
            "Blithering Badgers             |  2 |  1 |  1 |  0 |  4",
            "Courageous Californians        |  2 |  0 |  1 |  1 |  1",
            "Devastating Donkeys            |  1 |  0 |  0 |  1 |  0",
        ]
        self.assertEqual(tally(results), table)

    def test_ties_broken_alphabetically(self):
        results = [
            "Courageous Californians;Devastating Donkeys;win",
            "Allegoric Alaskans;Blithering Badgers;win",
            "Devastating Donkeys;Allegoric Alaskans;loss",
            "Courageous Californians;Blithering Badgers;win",
            "Blithering Badgers;Devastating Donkeys;draw",
            "Allegoric Alaskans;Courageous Californians;draw",
        ]
        table = [
            "Team                           | MP |  W |  D |  L |  P",
            "Allegoric Alaskans             |  3 |  2 |  1 |  0 |  7",
            "Courageous Californians        |  3 |  2 |  1 |  0 |  7",
            "Blithering Badgers             |  3 |  0 |  1 |  2 |  1",
            "Devastating Donkeys            |  3 |  0 |  1 |  2 |  1",
        ]
        self.assertEqual(tally(results), table)

    def test_ensure_points_sorted_numerically(self):
        results = [
            "Devastating Donkeys;Blithering Badgers;win",
            "Devastating Donkeys;Blithering Badgers;win",
            "Devastating Donkeys;Blithering Badgers;win",
            "Devastating Donkeys;Blithering Badgers;win",
            "Blithering Badgers;Devastating Donkeys;win",
        ]
        table = [
            "Team                           | MP |  W |  D |  L |  P",
            "Devastating Donkeys            |  5 |  4 |  0 |  1 | 12",
            "Blithering Badgers             |  5 |  1 |  0 |  4 |  3",
        ]
        self.assertEqual(tally(results), table)
