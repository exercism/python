import unittest

from micro_blog import (
    truncate,
)

# Tests adapted from `problem-specifications//canonical-data.json`


class MicroBlogTest(unittest.TestCase):
    def test_english_language_short(self):

        self.assertEqual(truncate("Hi"), "Hi")

    def test_english_language_long(self):

        self.assertEqual(truncate("Hello there"), "Hello")

    def test_german_language_short_broth(self):

        self.assertEqual(truncate("brühe"), "brühe")

    def test_german_language_long(self):

        self.assertEqual(truncate("Bärteppich"), "Bärte")

    def test_bulgarian_language_short_good(self):

        self.assertEqual(truncate("Добър"), "Добър")

    def test_greek_language_short_health(self):

        self.assertEqual(truncate("υγειά"), "υγειά")

    def test_maths_short(self):

        self.assertEqual(truncate("a=πr²"), "a=πr²")

    def test_maths_long(self):

        self.assertEqual(truncate("∅⊊ℕ⊊ℤ⊊ℚ⊊ℝ⊊ℂ"), "∅⊊ℕ⊊ℤ")

    def test_english_and_emoji_short(self):

        self.assertEqual(truncate("Fly 🛫"), "Fly 🛫")

    def test_emoji_short(self):

        self.assertEqual(truncate("💇"), "💇")

    def test_emoji_long(self):

        self.assertEqual(truncate("❄🌡🤧🤒🏥🕰😀"), "❄🌡🤧🤒🏥")

    def test_royal_flush(self):

        self.assertEqual(truncate("🃎🂸🃅🃋🃍🃁🃊"), "🃎🂸🃅🃋🃍")
