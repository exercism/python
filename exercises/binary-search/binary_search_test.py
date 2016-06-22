import unittest

from example import binary_search


class BinarySearchTests(unittest.TestCase):

    def test_is_this_thing_on(self):
        self.assertEqual('is this thing on', binary_search())


if __name__ == '__main__':
    unittest.main()
