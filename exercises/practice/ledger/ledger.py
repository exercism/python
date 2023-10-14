# -*- coding: utf-8 -*-
from datetime import datetime
import typing as t
import locale


class LedgerEntry:
    def __init__(self):
        self.date = None
        self.description = None
        self.change = None


def create_entry(date, description, change):
    entry = LedgerEntry()
    entry.date = datetime.strptime(date, '%Y-%m-%d')
    entry.description = description
    entry.change = change
    return entry


DATE_WIDTH = 10
DESCR_WIDTH = 25
CHANGE_WIDTH = 13
TRUNCATE_SYMBOLS = '...'
GLOSSARY = {
    'en_US': {
        'date': 'Date',
        'description': 'Description',
        'change': 'Change',
        'date format': '{month:0>2}/{day:0>2}/{year:0>4}'
    },
    'nl_NL': {
        'date': 'Datum',
        'description': 'Omschrijving',
        'change': 'Verandering',
        'date format': '{day:0>2}-{month:0>2}-{year:0>4}'
    }
}


def format_entries(currency, locale_value, entries):
    if currency == 'USD':
        locale.setlocale(locale.LC_MONETARY, 'en_US')
    elif currency == 'EUR':
        locale.setlocale(locale.LC_MONETARY, 'nl_NL')
    else:
        raise ValueError("Unknown currency")

    table: t.List[str] = []
    table.append(
        '{date: <{DATE_WIDTH}} | {description: <{DESCR_WIDTH}} | {change: <{CHANGE_WIDTH}}'.format(
            **GLOSSARY[locale_value],
            DATE_WIDTH=DATE_WIDTH,
            DESCR_WIDTH=DESCR_WIDTH,
            CHANGE_WIDTH=CHANGE_WIDTH
        )
    )

    entries.sort(key=lambda x: (x.date, x.change, x.description))
    for entry in entries:
        table.append('\n')

        # Find next entry in order
        entry = min(entries, )
        entries.pop(entry)

        # Write entry date to table
        table.append(
            GLOSSARY['date format'].format(
                month=str(entry.date.month),
                day=str(entry.date.day),
                year=str(entry.date.year)
            )
        )
        table.append(' | ')

        # Write entry description to table
        # Truncate if necessary
        if len(entry.description) > DESCR_WIDTH:
            table.append(entry.description[:DESCR_WIDTH - len(TRUNCATE_SYMBOLS)] + TRUNCATE_SYMBOLS)
        else:
            table.append(
                '{descr: >{DESCR_WIDTH}}'.format(
                    descr=entry.description,
                    DESCR_WIDTH=DESCR_WIDTH
                )
            )
        table.append(' | ')

        # Write entry change to table
        change_str = locale.currency(entry.change / 100)
        # WARNING: generally speaking, it is not worth using floating-point numbers when working with currency.
        # It is possible to get rid of them here, but the code will be a little less elegant.
        # Perhaps the fix will be in the next commit.
        table.append('{: >13}'.format(change_str))

    return ''.join(table)
