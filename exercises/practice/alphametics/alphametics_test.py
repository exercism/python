import unittest

from alphametics import (
    solve,
)

# Tests adapted from `problem-specifications//canonical-data.json`


class AlphameticsTest(unittest.TestCase):

    # Utility functions
    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")


if __name__ == "__main__":
    unittest.main()
