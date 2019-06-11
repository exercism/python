import unittest

from raindrops import convert


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.1.0

class RaindropsTest(unittest.TestCase):
    def test_the_sound_for_1_is_1(self):
        self.assertEqual(convert(1), "1")

    def test_the_sound_for_3_is_pling(self):
        self.assertEqual(convert(3), "Pling")

    def test_the_sound_for_5_is_plang(self):
        self.assertEqual(convert(5), "Plang")

    def test_the_sound_for_7_is_plong(self):
        self.assertEqual(convert(7), "Plong")

    def test_the_sound_for_6_is_pling(self):
        self.assertEqual(convert(6), "Pling")

    def test_2_to_the_power_3_does_not_make_sound(self):
        self.assertEqual(convert(8), "8")

    def test_the_sound_for_9_is_pling(self):
        self.assertEqual(convert(9), "Pling")

    def test_the_sound_for_10_is_plang(self):
        self.assertEqual(convert(10), "Plang")

    def test_the_sound_for_14_is_plong(self):
        self.assertEqual(convert(14), "Plong")

    def test_the_sound_for_15_is_plingplang(self):
        self.assertEqual(convert(15), "PlingPlang")

    def test_the_sound_for_21_is_plingplong(self):
        self.assertEqual(convert(21), "PlingPlong")

    def test_the_sound_for_25_is_plang(self):
        self.assertEqual(convert(25), "Plang")

    def test_the_sound_for_27_is_pling(self):
        self.assertEqual(convert(27), "Pling")

    def test_the_sound_for_35_is_plangplong(self):
        self.assertEqual(convert(35), "PlangPlong")

    def test_the_sound_for_49_is_plong(self):
        self.assertEqual(convert(49), "Plong")

    def test_the_sound_for_52_is_52(self):
        self.assertEqual(convert(52), "52")

    def test_the_sound_for_105_is_plingplangplong(self):
        self.assertEqual(convert(105), "PlingPlangPlong")

    def test_the_sound_for_12121_is_12121(self):
        self.assertEqual(convert(12121), "12121")


if __name__ == '__main__':
    unittest.main()
