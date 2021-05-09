import unittest

from prime_factors import (
    factors,
)

# Tests adapted from `problem-specifications//canonical-data.json`


class PrimeFactorsTest(unittest.TestCase):

    # Utility functions
    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")


if __name__ == "__main__":
    unittest.main()
