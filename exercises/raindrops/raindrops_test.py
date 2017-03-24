import unittest

from raindrops import raindrops


class RaindropsTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(raindrops(1), "1")

    def test_3(self):
        self.assertEqual(raindrops(3), "Pling")

    def test_5(self):
        self.assertEqual(raindrops(5), "Plang")

    def test_7(self):
        self.assertEqual(raindrops(7), "Plong")

    def test_6(self):
        self.assertEqual(raindrops(6), "Pling")

    def test_9(self):
        self.assertEqual(raindrops(9), "Pling")

    def test_10(self):
        self.assertEqual(raindrops(10), "Plang")

    def test_14(self):
        self.assertEqual(raindrops(14), "Plong")

    def test_15(self):
        self.assertEqual(raindrops(15), "PlingPlang")

    def test_21(self):
        self.assertEqual(raindrops(21), "PlingPlong")

    def test_25(self):
        self.assertEqual(raindrops(25), "Plang")

    def test_35(self):
        self.assertEqual(raindrops(35), "PlangPlong")

    def test_49(self):
        self.assertEqual(raindrops(49), "Plong")

    def test_52(self):
        self.assertEqual(raindrops(52), "52")

    def test_105(self):
        self.assertEqual(raindrops(105), "PlingPlangPlong")

    def test_12121(self):
        self.assertEqual(raindrops(12121), "12121")


if __name__ == '__main__':
    unittest.main()
