from collections import Counter
import unittest

from luhn import Luhn


class LuhnTests(unittest.TestCase):
    def test_addends(self):
        # uses a Counter to avoid specifying order of return value
        self.assertEqual(Counter([1, 4, 1, 4, 1]),
                         Counter(Luhn(12121).addends()))

    @unittest.skip("")
    def test_addends_large(self):
        # uses a Counter to avoid specifying order of return value
        self.assertEqual(Counter([7, 6, 6, 1]),
                         Counter(Luhn(8631).addends()))

    @unittest.skip("")
    def test_checksum1(self):
        self.assertEqual(2, Luhn(4913).checksum())

    @unittest.skip("")
    def test_ckecksum2(self):
        self.assertEqual(1, Luhn(201773).checksum())

    @unittest.skip("")
    def test_invalid_number(self):
        self.assertFalse(Luhn(738).is_valid())

    @unittest.skip("")
    def test_valid_number(self):
        self.assertTrue(Luhn(8739567).is_valid())

    @unittest.skip("")
    def test_create_valid_number1(self):
        self.assertEqual(1230, Luhn.create(123))

    @unittest.skip("")
    def test_create_valid_number2(self):
        self.assertEqual(8739567, Luhn.create(873956))

    @unittest.skip("")
    def test_create_valid_number3(self):
        self.assertEqual(8372637564, Luhn.create(837263756))

    @unittest.skip("")
    def test_is_valid_can_be_called_repeatedly(self):
        # This test was added, because we saw many implementations
        # in which the first call to is_valid() worked, but the
        # second call failed().
        number = Luhn(8739567)
        self.assertTrue(number.is_valid())
        self.assertTrue(number.is_valid())


if __name__ == '__main__':
    unittest.main()
