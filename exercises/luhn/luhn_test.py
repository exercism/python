from collections import Counter
import unittest

from luhn import Luhn


class LuhnTests(unittest.TestCase):
    def test_addends(self):
        # uses a Counter to avoid specifying order of return value
        self.assertEqual(Counter([1, 4, 1, 4, 1]),
                         Counter(Luhn(12121).addends()))

    def test_addends_large(self):
        # uses a Counter to avoid specifying order of return value
        self.assertEqual(Counter([7, 6, 6, 1]),
                         Counter(Luhn(8631).addends()))

    def test_checksum1(self):
        self.assertEqual(22, Luhn(4913).checksum())

    def test_ckecksum2(self):
        self.assertEqual(21, Luhn(201773).checksum())

    def test_invalid_number(self):
        self.assertFalse(Luhn(738).is_valid())

    def test_valid_number(self):
        self.assertTrue(Luhn(8739567).is_valid())

    def test_create_valid_number1(self):
        self.assertEqual(1230, Luhn.create(123))

    def test_create_valid_number2(self):
        self.assertEqual(8739567, Luhn.create(873956))

    def test_create_valid_number3(self):
        self.assertEqual(8372637564, Luhn.create(837263756))

    def test_is_valid_can_be_called_repeatedly(self):
        # This test was added, because we saw many implementations
        # in which the first call to is_valid() worked, but the
        # second call failed().
        number = Luhn(8739567)
        self.assertTrue(number.is_valid())
        self.assertTrue(number.is_valid())


if __name__ == '__main__':
    unittest.main()
