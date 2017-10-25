import unittest

import two_fer

# Tests adapted from `problem-specifications//canonical-data.json` @ v1.1.0


class Two_Fer_test(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(two_fer.two_fer(), 'One for you, one for me.')

    def test_alice(self):
        self.assertEqual(two_fer.two_fer("Alice"),
                         "One for Alice, one for me.")

    def test_bob(self):
        self.assertEqual(two_fer.two_fer("Bob"), "One for Bob, one for me.")


if __name__ == '__main__':
    unittest.main()
