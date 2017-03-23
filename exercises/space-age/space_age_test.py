import unittest

from space_age import SpaceAge


class SpaceAgeTest(unittest.TestCase):
    def test_age_in_seconds(self):
        age = SpaceAge(1e6)
        self.assertEqual(age.seconds, 1e6)

    def test_age_in_earth_years(self):
        age = SpaceAge(1e9)
        self.assertEqual(age.on_earth(), 31.69)

    def test_age_in_mercury_years(self):
        age = SpaceAge(2134835688)
        self.assertEqual(age.on_earth(), 67.65)
        self.assertEqual(age.on_mercury(), 280.88)

    def test_age_in_venus_years(self):
        age = SpaceAge(189839836)
        self.assertEqual(age.on_earth(), 6.02)
        self.assertEqual(age.on_venus(), 9.78)

    def test_age_on_mars(self):
        age = SpaceAge(2329871239)
        self.assertEqual(age.on_earth(), 73.83)
        self.assertEqual(age.on_mars(), 39.25)

    def test_age_on_jupiter(self):
        age = SpaceAge(901876382)
        self.assertEqual(age.on_earth(), 28.58)
        self.assertEqual(age.on_jupiter(), 2.41)

    def test_age_on_saturn(self):
        age = SpaceAge(3e9)
        self.assertEqual(age.on_earth(), 95.06)
        self.assertEqual(age.on_saturn(), 3.23)

    def test_age_on_uranus(self):
        age = SpaceAge(3210123456)
        self.assertEqual(age.on_earth(), 101.72)
        self.assertEqual(age.on_uranus(), 1.21)

    def test_age_on_neptune(self):
        age = SpaceAge(8210123456)
        self.assertEqual(age.on_earth(), 260.16)
        self.assertEqual(age.on_neptune(), 1.58)


if __name__ == '__main__':
    unittest.main()
