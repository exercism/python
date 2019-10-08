import unittest

from space_age import SpaceAge

# Tests adapted from `problem-specifications//canonical-data.json` @ v1.2.0


class SpaceAgeTest(unittest.TestCase):
    def test_age_on_earth(self):
        self.assertEqual(SpaceAge(1000000000).on_earth(), 31.69)

    def test_age_on_mercury(self):
        self.assertEqual(SpaceAge(2134835688).on_mercury(), 280.88)

    def test_age_on_venus(self):
        self.assertEqual(SpaceAge(189839836).on_venus(), 9.78)

    def test_age_on_mars(self):
        self.assertEqual(SpaceAge(2129871239).on_mars(), 35.88)

    def test_age_on_jupiter(self):
        self.assertEqual(SpaceAge(901876382).on_jupiter(), 2.41)

    def test_age_on_saturn(self):
        self.assertEqual(SpaceAge(2000000000).on_saturn(), 2.15)

    def test_age_on_uranus(self):
        self.assertEqual(SpaceAge(1210123456).on_uranus(), 0.46)

    def test_age_on_neptune(self):
        self.assertEqual(SpaceAge(1821023456).on_neptune(), 0.35)


if __name__ == "__main__":
    unittest.main()
