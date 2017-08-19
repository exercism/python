import unittest

import two_fer


class Two_Fer_test(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(two_fer.two_fer(), 'One for you, one for me.')

    def test_eve(self):
        self.assertEqual(two_fer.two_fer("Eve"), "One for Eve, one for me.")

    def test_bob(self):
        self.assertEqual(two_fer.two_fer("Bob"), "One for Bob, one for me.")


if __name__ == '__main__':
    unittest.main()
