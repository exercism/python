import unittest

from complex_numbers import ComplexNumber

class ComplexNumbersTest(unittest.TestCase):

    def test_real_part_of_a_purely_real_number(self):
        c = ComplexNumber(1, 0)
        self.assertEqual(c.real, 1)

    def test_real_part_of_a_purely_imaginary_number(self):
        c = ComplexNumber(0, 1)
        self.assertEqual(c.real, 0)

if __name__ == '__main__':
    unittest.main()