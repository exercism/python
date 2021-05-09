import unittest

from protein_translation import (
    proteins,
)

# Tests adapted from `problem-specifications//canonical-data.json`


class ProteinTranslationTest(unittest.TestCase):

    # Utility functions
    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")


if __name__ == "__main__":
    unittest.main()
