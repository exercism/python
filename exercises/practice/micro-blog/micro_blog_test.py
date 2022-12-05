import unittest

from micro_blog import (
    truncate,
)

# Tests adapted from `problem-specifications//canonical-data.json`


class MicroBlogTest(unittest.TestCase):
    def test_some1(self):
        self.assertEqual(truncate("Hi"), "Hi")

    def test_some2(self):
        self.assertEqual(truncate("Hello there"), "Hello")

    def test_some3(self):
        self.assertEqual(truncate("brühe"), "brühe")

    def test_some4(self):
        self.assertEqual(truncate("Bärteppich"), "Bärte")

    def test_some5(self):
        self.assertEqual(truncate("Добър"), "Добър")

    def test_some6(self):
        self.assertEqual(truncate("υγειά"), "υγειά")

    def test_some7(self):
        self.assertEqual(truncate("a=πr²"), "a=πr²")

    def test_some8(self):
        self.assertEqual(truncate("∅⊊ℕ⊊ℤ⊊ℚ⊊ℝ⊊ℂ"), "∅⊊ℕ⊊ℤ")

    def test_some9(self):
        self.assertEqual(truncate("Fly 🛫"), "Fly 🛫")

    def test_some10(self):
        self.assertEqual(truncate("💇"), "💇")

    def test_some11(self):
        self.assertEqual(truncate("❄🌡🤧🤒🏥🕰😀"), "❄🌡🤧🤒🏥")

    def test_some12(self):
        self.assertEqual(truncate("🃎🂸🃅🃋🃍🃁🃊"), "🃎🂸🃅🃋🃍")
