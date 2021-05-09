import unittest

from secret_handshake import (
    commands,
)

# Tests adapted from `problem-specifications//canonical-data.json`


class SecretHandshakeTest(unittest.TestCase):

    # Utility functions
    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")


if __name__ == "__main__":
    unittest.main()
