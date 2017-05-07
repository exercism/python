import unittest

from tournament import tally


# test cases adapted from `x-common//canonical-data.json` @ version: 1.1.0

class TestTournament(unittest.TestCase):
    def test_typical_input(self):
        results = ('Allegoric Alaskans;Blithering Badgers;win\n'
                   'Devastating Donkeys;Courageous Californians;draw\n'
                   'Devastating Donkeys;Allegoric Alaskans;win\n'
                   'Courageous Californians;Blithering Badgers;loss\n'
                   'Blithering Badgers;Devastating Donkeys;loss\n'
                   'Allegoric Alaskans;Courageous Californians;win')

        table = ('Team                           | MP |  W |  D |  L |  P\n'
                 'Devastating Donkeys            |  3 |  2 |  1 |  0 |  7\n'
                 'Allegoric Alaskans             |  3 |  2 |  0 |  1 |  6\n'
                 'Blithering Badgers             |  3 |  1 |  0 |  2 |  3\n'
                 'Courageous Californians        |  3 |  0 |  1 |  2 |  1')

        self.assertEqual(tally(results), table)

    def test_incomplete_competitionnot_all_pairs_have_played(self):
        results = ('Allegoric Alaskans;Blithering Badgers;loss\n'
                   'Devastating Donkeys;Allegoric Alaskans;loss\n'
                   'Courageous Californians;Blithering Badgers;draw\n'
                   'Allegoric Alaskans;Courageous Californians;win')

        table = ('Team                           | MP |  W |  D |  L |  P\n'
                 'Allegoric Alaskans             |  3 |  2 |  0 |  1 |  6\n'
                 'Blithering Badgers             |  2 |  1 |  1 |  0 |  4\n'
                 'Courageous Californians        |  2 |  0 |  1 |  1 |  1\n'
                 'Devastating Donkeys            |  1 |  0 |  0 |  1 |  0')

        self.assertEqual(tally(results), table)

    def test_ties_broken_alphabetically(self):
        results = ('Courageous Californians;Devastating Donkeys;win\n'
                   'Allegoric Alaskans;Blithering Badgers;win\n'
                   'Devastating Donkeys;Allegoric Alaskans;loss\n'
                   'Courageous Californians;Blithering Badgers;win\n'
                   'Blithering Badgers;Devastating Donkeys;draw\n'
                   'Allegoric Alaskans;Courageous Californians;draw')

        table = ('Team                           | MP |  W |  D |  L |  P\n'
                 'Allegoric Alaskans             |  3 |  2 |  1 |  0 |  7\n'
                 'Courageous Californians        |  3 |  2 |  1 |  0 |  7\n'
                 'Blithering Badgers             |  3 |  0 |  1 |  2 |  1\n'
                 'Devastating Donkeys            |  3 |  0 |  1 |  2 |  1')

        self.assertEqual(tally(results), table)

    def test_mostly_invalid_lines(self):
        results = ('\n'
                   'Allegoric Alaskans@Blithering Badgers;draw\n'
                   'Blithering Badgers;Devastating Donkeys;loss\n'
                   'Devastating Donkeys;Courageous Californians;win;5\n'
                   'Courageous Californians;Allegoric Alaskans;los')

        table = ('Team                           | MP |  W |  D |  L |  P\n'
                 'Devastating Donkeys            |  1 |  1 |  0 |  0 |  3\n'
                 'Blithering Badgers             |  1 |  0 |  0 |  1 |  0')

        self.assertEqual(tally(results), table)


if __name__ == '__main__':
    unittest.main()
