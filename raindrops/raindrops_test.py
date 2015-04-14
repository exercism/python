import unittest

from raindrops import raindrops


class RaindropsTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual("1", raindrops(1))

    @unittest.skip("")
    def test_3(self):
        self.assertEqual("Pling", raindrops(3))

    @unittest.skip("")
    def test_5(self):
        self.assertEqual("Plang", raindrops(5))

    @unittest.skip("")
    def test_7(self):
        self.assertEqual("Plong", raindrops(7))

    @unittest.skip("")
    def test_6(self):
        self.assertEqual("Pling", raindrops(6))

    @unittest.skip("")
    def test_9(self):
        self.assertEqual("Pling", raindrops(9))

    @unittest.skip("")
    def test_10(self):
        self.assertEqual("Plang", raindrops(10))

    @unittest.skip("")
    def test_14(self):
        self.assertEqual("Plong", raindrops(14))

    @unittest.skip("")
    def test_15(self):
        self.assertEqual("PlingPlang", raindrops(15))

    @unittest.skip("")
    def test_21(self):
        self.assertEqual("PlingPlong", raindrops(21))

    @unittest.skip("")
    def test_25(self):
        self.assertEqual("Plang", raindrops(25))

    @unittest.skip("")
    def test_35(self):
        self.assertEqual("PlangPlong", raindrops(35))

    @unittest.skip("")
    def test_49(self):
        self.assertEqual("Plong", raindrops(49))

    @unittest.skip("")
    def test_52(self):
        self.assertEqual("52", raindrops(52))

    @unittest.skip("")
    def test_105(self):
        self.assertEqual("PlingPlangPlong", raindrops(105))

    @unittest.skip("")
    def test_12121(self):
        self.assertEqual("12121", raindrops(12121))

if __name__ == '__main__':
    unittest.main()
