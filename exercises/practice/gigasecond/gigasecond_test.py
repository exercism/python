from datetime import datetime
import unittest

from gigasecond import (
    add,
)

# Tests adapted from `problem-specifications//canonical-data.json`


class GigasecondTest(unittest.TestCase):

    # Utility functions
    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")


if __name__ == "__main__":
    unittest.main()
