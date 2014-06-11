import unittest

from hamming import hamming

# If the sequences have different lengths, assume the shorter one is extended
# with nucleotides in such a way to guarantee the extra nucleotides are all
# different between the two strands.

class hammingdecimalTest(unittest.TestCase):
    def test_hamming_empty(self):
        self.assertEqual(0, hamming('',''))

    def test_hamming_onenucleotide_same(self):
        self.assertEqual(0, hamming('A','A'))

    def test_hamming_onenucleotide_different(self):
        self.assertEqual(1, hamming('A','G'))

    def test_hamming_short1(self):
        self.assertEqual(1, hamming('AT','CT'))

    def test_hamming_short2(self):
        self.assertEqual(2, hamming('AG','CT'))

    def test_hamming_large(self):
        self.assertEqual(4, hamming('GGATCG','CCTGCG'))

    def test_hamming_small(self):
        self.assertEqual(1, hamming('GGACGA','GGTCGA'))

    def test_hamming_very_long(self):
        self.assertEqual(9, hamming('GGACGGATTCTG','AGGACGGATTCT'))

    def test_hamming_different_length1(self):
        self.assertEqual(4, hamming('AAGCTAC','ACGTT'))

    def test_hamming_different_length2(self):
        self.assertEqual(5, hamming('AAGCTAC','ACGTTACGTC'))


if __name__ == '__main__':
    unittest.main()
