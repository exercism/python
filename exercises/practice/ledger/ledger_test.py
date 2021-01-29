# -*- coding: utf-8 -*-
import unittest

from ledger import format_entries, create_entry


class LedgerTest(unittest.TestCase):
    maxDiff = 5000

    def test_empty_ledger(self):
        currency = 'USD'
        locale = 'en_US'
        entries = []
        expected = 'Date       | Description               | Change       '
        self.assertEqual(format_entries(currency, locale, entries), expected)

    def test_one_entry(self):
        currency = 'USD'
        locale = 'en_US'
        entries = [
            create_entry('2015-01-01', 'Buy present', -1000),
        ]
        expected = '\n'.join([
            'Date       | Description               | Change       ',
            '01/01/2015 | Buy present               |      ($10.00)',
        ])
        self.assertEqual(format_entries(currency, locale, entries), expected)

    def test_credit_and_debit(self):
        currency = 'USD'
        locale = 'en_US'
        entries = [
            create_entry('2015-01-02', 'Get present', 1000),
            create_entry('2015-01-01', 'Buy present', -1000),
        ]
        expected = '\n'.join([
            'Date       | Description               | Change       ',
            '01/01/2015 | Buy present               |      ($10.00)',
            '01/02/2015 | Get present               |       $10.00 ',
        ])
        self.assertEqual(format_entries(currency, locale, entries), expected)

    def test_multiple_entries_on_same_date_ordered_by_description(self):
        currency = 'USD'
        locale = 'en_US'
        entries = [
            create_entry('2015-01-02', 'Get present', 1000),
            create_entry('2015-01-01', 'Buy present', -1000),
        ]
        expected = '\n'.join([
            'Date       | Description               | Change       ',
            '01/01/2015 | Buy present               |      ($10.00)',
            '01/02/2015 | Get present               |       $10.00 ',
        ])
        self.assertEqual(format_entries(currency, locale, entries), expected)

    def test_final_order_tie_breaker_is_change(self):
        currency = 'USD'
        locale = 'en_US'
        entries = [
            create_entry('2015-01-01', 'Something', 0),
            create_entry('2015-01-01', 'Something', -1),
            create_entry('2015-01-01', 'Something', 1),
        ]
        expected = '\n'.join([
            'Date       | Description               | Change       ',
            '01/01/2015 | Something                 |       ($0.01)',
            '01/01/2015 | Something                 |        $0.00 ',
            '01/01/2015 | Something                 |        $0.01 ',
        ])
        self.assertEqual(format_entries(currency, locale, entries), expected)

    def test_overlong_description(self):
        currency = 'USD'
        locale = 'en_US'
        entries = [
            create_entry('2015-01-01', 'Freude schoner Gotterfunken', -123456),
        ]
        expected = '\n'.join([
            'Date       | Description               | Change       ',
            '01/01/2015 | Freude schoner Gotterf... |   ($1,234.56)',
        ])
        self.assertEqual(format_entries(currency, locale, entries), expected)

    def test_euros(self):
        currency = 'EUR'
        locale = 'en_US'
        entries = [
            create_entry('2015-01-01', 'Buy present', -1000),
        ]
        expected = '\n'.join([
            'Date       | Description               | Change       ',
            u'01/01/2015 | Buy present               |      (€10.00)',
        ])
        self.assertEqual(format_entries(currency, locale, entries), expected)

    def test_dutch_locale(self):
        currency = 'USD'
        locale = 'nl_NL'
        entries = [
            create_entry('2015-03-12', 'Buy present', 123456),
        ]
        expected = '\n'.join([
            'Datum      | Omschrijving              | Verandering  ',
            '12-03-2015 | Buy present               |   $ 1.234,56 ',
        ])
        self.assertEqual(format_entries(currency, locale, entries), expected)

    def test_dutch_locale_and_euros(self):
        currency = 'EUR'
        locale = 'nl_NL'
        entries = [
            create_entry('2015-03-12', 'Buy present', 123456),
        ]
        expected = '\n'.join([
            'Datum      | Omschrijving              | Verandering  ',
            u'12-03-2015 | Buy present               |   € 1.234,56 ',
        ])
        self.assertEqual(format_entries(currency, locale, entries), expected)

    def test_dutch_negative_number_with_3_digits_before_decimal_point(self):
        currency = 'USD'
        locale = 'nl_NL'
        entries = [
            create_entry('2015-03-12', 'Buy present', -12345),
        ]
        expected = '\n'.join([
            'Datum      | Omschrijving              | Verandering  ',
            '12-03-2015 | Buy present               |    $ -123,45 ',
        ])
        self.assertEqual(format_entries(currency, locale, entries), expected)

    def test_american_negative_number_with_3_digits_before_decimal_point(self):
        currency = 'USD'
        locale = 'en_US'
        entries = [
            create_entry('2015-03-12', 'Buy present', -12345),
        ]
        expected = '\n'.join([
            'Date       | Description               | Change       ',
            '03/12/2015 | Buy present               |     ($123.45)',
        ])
        self.assertEqual(format_entries(currency, locale, entries), expected)


if __name__ == '__main__':
    unittest.main()
