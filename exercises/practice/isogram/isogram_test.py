import unittest

from isogram import (
    is_isogram,
)

# Tests adapted from `problem-specifications//canonical-data.json`


class IsogramTest(unittest.TestCase):

    # Utility functions
    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")


if __name__ == "__main__":
    unittest.main()
