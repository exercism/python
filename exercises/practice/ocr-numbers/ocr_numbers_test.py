import unittest

from ocr_numbers import (
    convert,
)

# Tests adapted from `problem-specifications//canonical-data.json`


class OcrNumbersTest(unittest.TestCase):

    # Utility functions
    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")


if __name__ == "__main__":
    unittest.main()
