import unittest
from example import isogram


class TestIsogram(unittest.TestCase):

    def test_isogram(self):
        tests = ['lumberjacks', 'background', 'downstream']
        for test in tests:
            string = isogram(test)
            self.assertTrue(string, True)

    def test_isogram_false(self):
        tests = ['isograms', 'aba', '  ']
        for test in tests:
            string = isogram(test)
            self.assertFalse(string, False)

if __name__ == '__main__':
    unittest.main()
