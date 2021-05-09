import unittest

from rotational_cipher import (
    rotate,
)

# Tests adapted from `problem-specifications//canonical-data.json`


class RotationalCipherTest(unittest.TestCase):

    # Utility functions
    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")


if __name__ == "__main__":
    unittest.main()
