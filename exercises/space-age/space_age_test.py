import unittest

from space_age import SpaceAge


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.1.0

class SpaceAgeTest(unittest.TestCase):

    def test_age_on_mercury(self):
        self.assertEqual(SpaceAge(2134835688).on_mercury(), 280.88)

    def test_age_on_venus(self):
        self.assertEqual(SpaceAge(189839836).on_venus(), 9.78)

    def test_age_on_earth(self):
        self.assertEqual(SpaceAge(1000000000).on_earth(), 31.69)

    def test_age_on_mars(self):
        self.assertEqual(SpaceAge(2329871239).on_mars(), 39.25)

    def test_age_on_jupiter(self):
        self.assertEqual(SpaceAge(901876382).on_jupiter(), 2.41)

    def test_age_on_saturn(self):
        self.assertEqual(SpaceAge(3000000000).on_saturn(), 3.23)

    def test_age_on_uranus(self):
        self.assertEqual(SpaceAge(3210123456).on_uranus(), 1.21)

    def test_age_on_neptune(self):
        self.assertEqual(SpaceAge(8210123456).on_neptune(), 1.58)

    # Additional tests for this track

    def test_age_in_seconds(self):
        self.assertEqual(SpaceAge(1e6).seconds, 1e6)


if __name__ == '__main__':
    unittest.main()
