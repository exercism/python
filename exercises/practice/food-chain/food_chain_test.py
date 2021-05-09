import unittest

from food_chain import (
    recite,
)

# Tests adapted from `problem-specifications//canonical-data.json`


class FoodChainTest(unittest.TestCase):

    # Utility functions
    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")


if __name__ == "__main__":
    unittest.main()
