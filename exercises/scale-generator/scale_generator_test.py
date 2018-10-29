import unittest

from scale_generator import Scale


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.0.0

class ScaleGeneratorTest(unittest.TestCase):

    # Test chromatic scales
    def test_chromatic_scale_with_sharps(self):
        expected = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#',
                    'G', 'G#', 'A', 'A#', 'B']
        self.assertEqual(Scale('C').pitches, expected)

    def test_chromatic_scale_with_flats(self):
        expected = ['F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B',
                    'C', 'Db', 'D', 'Eb', 'E']
        self.assertEqual(Scale('F').pitches, expected)

    # Test scales with specified intervals
    def test_simple_major_scale(self):
        expected = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
        self.assertEqual(Scale('C', 'MMmMMMm').pitches, expected)

    def test_major_scale_with_sharps(self):
        expected = ['G', 'A', 'B', 'C', 'D', 'E', 'F#']
        self.assertEqual(Scale('G', 'MMmMMMm').pitches, expected)

    def test_major_scale_with_flats(self):
        expected = ['F', 'G', 'A', 'Bb', 'C', 'D', 'E']
        self.assertEqual(Scale('F', 'MMmMMMm').pitches, expected)

    def test_minor_scale_with_sharps(self):
        expected = ['F#', 'G#', 'A', 'B', 'C#', 'D', 'E']
        self.assertEqual(Scale('f#', 'MmMMmMM').pitches, expected)

    def test_minor_scale_with_flats(self):
        expected = ['Bb', 'C', 'Db', 'Eb', 'F', 'Gb', 'Ab']
        self.assertEqual(Scale('bb', 'MmMMmMM').pitches, expected)

    def test_dorian_mode(self):
        expected = ['D', 'E', 'F', 'G', 'A', 'B', 'C']
        self.assertEqual(Scale('d', 'MmMMMmM').pitches, expected)

    def test_mixolydian_mode(self):
        expected = ['Eb', 'F', 'G', 'Ab', 'Bb', 'C', 'Db']
        self.assertEqual(Scale('Eb', 'MMmMMmM').pitches, expected)

    def test_lydian_mode(self):
        expected = ['A', 'B', 'C#', 'D#', 'E', 'F#', 'G#']
        self.assertEqual(Scale('a', 'MMMmMMm').pitches, expected)

    def test_phrygian_mode(self):
        expected = ['E', 'F', 'G', 'A', 'B', 'C', 'D']
        self.assertEqual(Scale('e', 'mMMMmMM').pitches, expected)

    def test_locrian_mode(self):
        expected = ['G', 'Ab', 'Bb', 'C', 'Db', 'Eb', 'F']
        self.assertEqual(Scale('g', 'mMMmMMM').pitches, expected)

    def test_harmonic_minor(self):
        expected = ['D', 'E', 'F', 'G', 'A', 'Bb', 'Db']
        self.assertEqual(Scale('d', 'MmMMmAm').pitches, expected)

    def test_octatonic(self):
        expected = ['C', 'D', 'D#', 'F', 'F#', 'G#', 'A', 'B']
        self.assertEqual(Scale('C', 'MmMmMmMm').pitches, expected)

    def test_hexatonic(self):
        expected = ['Db', 'Eb', 'F', 'G', 'A', 'B']
        self.assertEqual(Scale('Db', 'MMMMMM').pitches, expected)

    def test_pentatonic(self):
        expected = ['A', 'B', 'C#', 'E', 'F#']
        self.assertEqual(Scale('A', 'MMAMA').pitches, expected)

    def test_enigmatic(self):
        expected = ['G', 'G#', 'B', 'C#', 'D#', 'F', 'F#']
        self.assertEqual(Scale('G', 'mAMMMmm').pitches, expected)

    # Track-specific tests
    def test_brokeninterval(self):
        with self.assertRaisesWithMessage(ValueError):
            Scale('G', 'mAMMMmM')

    # Utility functions
    def setUp(self):
        try:
            self.assertRaisesRegex
        except AttributeError:
            self.assertRaisesRegex = self.assertRaisesRegexp

    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")


if __name__ == '__main__':
    unittest.main()
