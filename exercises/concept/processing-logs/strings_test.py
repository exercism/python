import unittest
from strings import extract_message, change_log_level, reformat


class TestLogLines(unittest.TestCase):
    def test_message(self):
        self.assertEqual(
            extract_message("[INFO] Hello there."),
            "Hello there.",
            msg="Should correctly extract a basic message.",
        )

    def test_message_with_punctuation(self):
        self.assertEqual(
            extract_message("[WARN] File not found: exercism_practice.py"),
            "File not found: exercism_practice.py",
            msg="Should preserve punctuation and whitespace from original message.",
        )

    def test_level_word_remains_in_message(self):
        self.assertEqual(
            extract_message("[ERROR] Error while serializing data."),
            "Error while serializing data.",
            msg="Should preserve a loglevel word that is actually part of the message.",
        )

    def test_change_loglevel(self):
        self.assertEqual(
            change_log_level("[ERROR] No configs found, but not a big deal.", "INFO"),
            "[INFO] No configs found, but not a big deal.",
            msg="Should replace the loglevel.",
        )

    def test_change_loglevel_with_loglevel_in_message(self):
        self.assertEqual(
            change_log_level("[WARN] Warning: file does not exist.", "INFO"),
            "[INFO] Warning: file does not exist.",
            msg="Should not replace loglevel names that are part of the message.",
        )

    def test_reformat(self):
        self.assertEqual(
            reformat("[WARN] Warning: file not found."),
            "Warning: file not found. (warn)",
            msg="Should reformat with lowercase loglevel. ",
        )

    def test_capture_message_when_contains_loglevel_string(self):
        self.assertEqual(
            extract_message("[WARN] Warning: file not found. Will WARN once."),
            "Warning: file not found. Will WARN once.",
            msg="Should extract loglevel inside brackets, not from messsage, even if message contains something that looks like a loglevel.",
        )
