import unittest

from etl import (
    transform,
)

# Tests adapted from `problem-specifications//canonical-data.json`


class EtlTest(unittest.TestCase):

    # Utility functions
    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")


if __name__ == "__main__":
    unittest.main()
