import unittest

from two_fer import two_fer

# Tests adapted from `problem-specifications//canonical-data.json` @ v1.2.0


class TwoFerTest(unittest.TestCase):
    def test_no_name_given(self):
        self.assertEqual(two_fer(), "One for you, one for me.")

    def test_a_name_given(self):
        self.assertEqual(two_fer("Alice"), "One for Alice, one for me.")

    def test_another_name_given(self):
        self.assertEqual(two_fer("Bob"), "One for Bob, one for me.")


if __name__ == "__main__":
    unittest.main()
