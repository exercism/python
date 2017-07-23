import unittest

from scale_generator import Scale


class ScaleGeneratorTest(unittest.TestCase):

    def test_naming_scale(self):
        chromatic = Scale('c', 'chromatic')
        expected = 'C chromatic'
        actual = chromatic.name
        self.assertEqual(expected, actual)

    def test_chromatic_scale(self):
        chromatic = Scale('C', 'chromatic')
        expected = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#',
                    'B']
        actual = chromatic.pitches
        self.assertEqual(expected, actual)

    def test_another_chromatic_scale(self):
        chromatic = Scale('F', 'chromatic')
        expected = ['F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb',
                    'E']
        actual = chromatic.pitches
        self.assertEqual(expected, actual)

    def test_naming_major_scale(self):
        major = Scale('G', 'major', 'MMmMMMm')
        expected = 'G major'
        actual = major.name
        self.assertEqual(expected, actual)

    def test_major_scale(self):
        major = Scale('C', 'major', 'MMmMMMm')
        expected = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
        actual = major.pitches
        self.assertEqual(expected, actual)

    def test_another_major_scale(self):
        major = Scale('G', 'major', 'MMmMMMm')
        expected = ['G', 'A', 'B', 'C', 'D', 'E', 'F#']
        actual = major.pitches
        self.assertEqual(expected, actual)

    def test_minor_scale(self):
        minor = Scale('f#', 'minor', 'MmMMmMM')
        expected = ['F#', 'G#', 'A', 'B', 'C#', 'D', 'E']
        actual = minor.pitches
        self.assertEqual(expected, actual)

    def test_another_minor_scale(self):
        minor = Scale('bb', 'minor', 'MmMMmMM')
        expected = ['Bb', 'C', 'Db', 'Eb', 'F', 'Gb', 'Ab']
        actual = minor.pitches
        self.assertEqual(expected, actual)

    def test_dorian_mode(self):
        dorian = Scale('d', 'dorian', 'MmMMMmM')
        expected = ['D', 'E', 'F', 'G', 'A', 'B', 'C']
        actual = dorian.pitches
        self.assertEqual(expected, actual)

    def test_mixolydian_mode(self):
        mixolydian = Scale('Eb', 'mixolydian', 'MMmMMmM')
        expected = ['Eb', 'F', 'G', 'Ab', 'Bb', 'C', 'Db']
        actual = mixolydian.pitches
        self.assertEqual(expected, actual)

    def test_lydian_mode(self):
        lydian = Scale('a', 'lydian', 'MMMmMMm')
        expected = ['A', 'B', 'C#', 'D#', 'E', 'F#', 'G#']
        actual = lydian.pitches
        self.assertEqual(expected, actual)

    def test_phrygian_mode(self):
        phrygian = Scale('e', 'phrygian', 'mMMMmMM')
        expected = ['E', 'F', 'G', 'A', 'B', 'C', 'D']
        actual = phrygian.pitches
        self.assertEqual(expected, actual)

    def test_locrian_mode(self):
        locrian = Scale('g', 'locrian', 'mMMmMMM')
        expected = ['G', 'Ab', 'Bb', 'C', 'Db', 'Eb', 'F']
        actual = locrian.pitches
        self.assertEqual(expected, actual)

    def test_harmonic_minor(self):
        harmonic_minor = Scale('d', 'harmonic_minor', 'MmMMmAm')
        expected = ['D', 'E', 'F', 'G', 'A', 'Bb', 'Db']
        actual = harmonic_minor.pitches
        self.assertEqual(expected, actual)

    def test_octatonic(self):
        octatonic = Scale('C', 'octatonic', 'MmMmMmMm')
        expected = ['C', 'D', 'D#', 'F', 'F#', 'G#', 'A', 'B']
        actual = octatonic.pitches
        self.assertEqual(expected, actual)

    def test_hexatonic(self):
        hexatonic = Scale('Db', 'hexatonic', 'MMMMMM')
        expected = ['Db', 'Eb', 'F', 'G', 'A', 'B']
        actual = hexatonic.pitches
        self.assertEqual(expected, actual)

    def test_pentatonic(self):
        pentatonic = Scale('A', 'pentatonic', 'MMAMA')
        expected = ['A', 'B', 'C#', 'E', 'F#']
        actual = pentatonic.pitches
        self.assertEqual(expected, actual)

    def test_enigmatic(self):
        enigmatic = Scale('G', 'enigmatic', 'mAMMMmm')
        expected = ['G', 'G#', 'B', 'C#', 'D#', 'F', 'F#']
        actual = enigmatic.pitches
        self.assertEqual(expected, actual)

    def test_brokeninterval(self):
        with self.assertRaises(ValueError):
            Scale('G', 'enigmatic', 'mAMMMmM')


if __name__ == '__main__':
    unittest.main()
