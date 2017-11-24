import unittest

from ledger import Ledger


class LedgerTest(unittest.TestCase):
    def test_empty_ledger(self):
        currency = "USD"
        locale = "en-US"
        entries = []
        expected = "Date       | Description               | Change       "

        self.assertEqual(Ledger.Format(currency, locale, entries), expected)

    def test_one_entry(self):
        currency = 'USD'
        locale = 'en-US'
        entries = [
            Ledger.CreateEntry('2015-01-01', 'Buy present', -1000),
        ]
        expected = "Date       | Description               | Change       \n" \
                   "01/01/2015 | Buy present               |      ($10.00)"

        self.assertEqual(Ledger.Format(currency, locale, entries), expected)

    def test_credit_and_debit(self):
        currency = 'USD'
        locale = 'en-US'
        entries = [
            Ledger.CreateEntry('2015-01-02', 'Get present', 1000),
            Ledger.CreateEntry('2015-01-01', 'Buy present', -1000),
        ]
        expected = 'Date       | Description               | Change       \n' \
                   '01/01/2015 | Buy present               |      ($10.00)\n' \
                   '01/02/2015 | Get present               |       $10.00 '

        self.assertEqual(Ledger.Format(currency, locale, entries), expected)

    def test_multiple_entries_with_same_date_ordered_by_description(self):
        currency = 'USD'
        locale = 'en-US'
        entries = [
            Ledger.CreateEntry('2015-01-01', 'Buy present', -1000),
            Ledger.CreateEntry('2015-01-01', 'Get present', 1000),
        ]
        expected = 'Date       | Description               | Change       \n' \
                   '01/01/2015 | Buy present               |      ($10.00)\n' \
                   '01/01/2015 | Get present               |       $10.00 '

        self.assertEqual(Ledger.Format(currency, locale, entries), expected)

    def test_multiple_entries_with_same_date_and_desc_ordered_by_change(self):
        currency = 'USD'
        locale = 'en-US'
        entries = [
            Ledger.CreateEntry('2015-01-01', 'Something', 0),
            Ledger.CreateEntry('2015-01-01', 'Something', -1),
            Ledger.CreateEntry('2015-01-01', 'Something', 1),
        ]
        expected = 'Date       | Description               | Change       \n' \
                   '01/01/2015 | Something                 |       ($0.01)\n' \
                   '01/01/2015 | Something                 |        $0.00 \n' \
                   '01/01/2015 | Something                 |        $0.01 '

        self.assertEqual(Ledger.Format(currency, locale, entries), expected)

    def test_overlong_description(self):
        currency = 'USD'
        locale = 'en-US'
        entries = [
            Ledger.CreateEntry('2015-01-01',
                               'This is too long of a description', -123456),
        ]
        expected = 'Date       | Description               | Change       \n' \
                   '01/01/2015 | This is too long of a ... |   ($1,234.56)'

        self.assertEqual(Ledger.Format(currency, locale, entries), expected)

    def test_euro_currency(self):
        currency = 'EUR'
        locale = 'en-US'
        entries = [
            Ledger.CreateEntry('2015-01-01', 'Buy present', -1000),
        ]
        expected = 'Date       | Description               | Change       \n' \
                   '01/01/2015 | Buy present               |      (€10.00)'

        self.assertEqual(Ledger.Format(currency, locale, entries), expected)

    def test_dutch_locale(self):
        currency = 'USD'
        locale = 'nl-NL'
        entries = [
            Ledger.CreateEntry('2015-03-12', 'Buy present', 123456),
        ]
        expected = 'Datum      | Omschrijving              | Verandering  \n' \
                   '12/03/2015 | Buy present               |   $ 1.234,56 '

        self.assertEqual(Ledger.Format(currency, locale, entries), expected)

    def test_dutch_negative_number_with_3_digits_before_decimal_point(self):
        currency = 'USD'
        locale = 'nl-NL'
        entries = [
            Ledger.CreateEntry('2015-03-12', 'Buy present', -12345),
        ]
        expected = 'Datum      | Omschrijving              | Verandering  \n' \
                   '12/03/2015 | Buy present               |     $ -123,45'

        self.assertEqual(Ledger.Format(currency, locale, entries), expected)

    def test_us_negative_number_with_3_digits_before_decimal_point(self):
        currency = 'USD'
        locale = 'en-US'
        entries = [
            Ledger.CreateEntry('2015-03-12', 'Buy present', -12345),
        ]
        expected = 'Date       | Description               | Change       \n' \
                   '03/12/2015 | Buy present               |     ($123.45)'

        self.assertEqual(Ledger.Format(currency, locale, entries), expected)


if __name__ == '__main__':
    unittest.main()
