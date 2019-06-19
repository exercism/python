import unittest

from anagram import find_anagrams

# Python 2/3 compatibility
if not hasattr(unittest.TestCase, 'assertCountEqual'):
    unittest.TestCase.assertCountEqual = unittest.TestCase.assertItemsEqual


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.4.1

class AnagramTest(unittest.TestCase):
    def test_no_matches(self):
        candidates = ["hello", "world", "zombies", "pants"]
        self.assertEqual(find_anagrams("diaper", candidates), [])

    def test_detects_two_anagrams(self):
        candidates = ["stream", "pigeon", "maters"]
        self.assertCountEqual(
            find_anagrams("master", candidates), ["stream", "maters"])

    def test_does_not_detect_anagram_subsets(self):
        self.assertEqual(find_anagrams("good", ["dog", "goody"]), [])

    def test_detects_anagram(self):
        candidates = ["enlists", "google", "inlets", "banana"]
        self.assertEqual(find_anagrams("listen", candidates), ["inlets"])

    def test_detects_three_anagrams(self):
        candidates = [
            "gallery", "ballerina", "regally", "clergy", "largely", "leading"
        ]
        self.assertCountEqual(
            find_anagrams("allergy", candidates),
            ["gallery", "regally", "largely"])

    def test_does_not_detect_non_anagrams_with_identical_checksum(self):
        self.assertEqual(find_anagrams("mass", ["last"]), [])

    def test_detects_anagrams_case_insensitively(self):
        candidates = ["cashregister", "Carthorse", "radishes"]
        self.assertEqual(
            find_anagrams("Orchestra", candidates), ["Carthorse"])

    def test_detects_anagrams_using_case_insensitive_subject(self):
        candidates = ["cashregister", "carthorse", "radishes"]
        self.assertEqual(
            find_anagrams("Orchestra", candidates), ["carthorse"])

    def test_detects_anagrams_using_case_insensitive_possible_matches(self):
        candidates = ["cashregister", "Carthorse", "radishes"]
        self.assertEqual(
            find_anagrams("orchestra", candidates), ["Carthorse"])

    def test_does_not_detect_an_anagram_if_the_original_word_is_repeated(self):
        self.assertEqual(find_anagrams("go", ["go Go GO"]), [])

    def test_anagrams_must_use_all_letters_exactly_once(self):
        self.assertEqual(find_anagrams("tapper", ["patter"]), [])

    def test_words_are_not_anagrams_of_themselves_case_insensitive(self):
        candidates = ["BANANA", "Banana", "banana"]
        self.assertEqual(find_anagrams("BANANA", candidates), [])


if __name__ == '__main__':
    unittest.main()
