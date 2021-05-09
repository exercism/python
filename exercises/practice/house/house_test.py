import unittest

from house import (
    recite,
)

# Tests adapted from `problem-specifications//canonical-data.json`


class HouseTest(unittest.TestCase):

    # Utility functions
    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")


if __name__ == "__main__":
    unittest.main()
