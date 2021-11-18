# -*- coding: utf-8 -*-
from datetime import datetime

ROW_FMT = '{{:<{1}}} | {{:<{2}}} | {{:{0}{3}}}'


def truncate(s, length=25):
    if len(s) <= length:
        return s
    return s[:length - 3] + '...'


class LCInfo:
    def __init__(self, locale, currency, columns):
        self.columns = columns
        if locale == 'en_US':
            headers = ['Date', 'Description', 'Change']
            self.datefmt = '{0.month:02}/{0.day:02}/{0.year:04}'
            self.cur_fmt = '{}{}{}{}'
            self.lead_neg = '('
            self.trail_neg = ')'
            self.thousands = ','
            self.decimal = '.'
        elif locale == 'nl_NL':
            headers = ['Datum', 'Omschrijving', 'Verandering']
            self.datefmt = '{0.day:02}-{0.month:02}-{0.year:04}'
            self.cur_fmt = '{1} {0}{2}{3}'
            self.lead_neg = '-'
            self.trail_neg = ' '
            self.thousands = '.'
            self.decimal = ','
        fmt = ROW_FMT.format('<', *columns)
        self.headers = fmt.format(*headers)
        self.cur_symbol = {
            'USD': '$',
            'EUR': '€',
        }.get(currency)

    def number(self, n):
        n_int, n_float = divmod(abs(n), 100)
        n_int_parts = []
        while n_int > 0:
            n_int, idx = divmod(n_int, 1000)
            n_int_parts.insert(0, str(idx))
        return '{}{}{:02}'.format(
            self.thousands.join(n_int_parts) or '0',
            self.decimal,
            n_float,
        )

    def currency(self, change):
        return self.cur_fmt.format(
            self.lead_neg if change < 0 else '',
            self.cur_symbol,
            self.number(change),
            self.trail_neg if change < 0 else ' ',
        )

    def entry(self, entry):
        date, change, desc = entry
        fmt = ROW_FMT.format('>', *self.columns)
        return fmt.format(
            self.datefmt.format(date),
            truncate(desc),
            self.currency(change),
        )

    def table(self, entries):
        lines = [self.headers]
        lines.extend(map(self.entry, sorted(entries)))
        return '\n'.join(lines)


def create_entry(date, description, change):
    return (
        datetime.strptime(date, '%Y-%m-%d'),
        change,
        description
    )


def format_entries(currency, locale, entries):
    columns = (10, 25, 13)
    lcinfo = LCInfo(locale, currency, columns)
    return lcinfo.table(entries)
