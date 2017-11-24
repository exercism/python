import locale
from datetime import datetime


class LocaleInfo:
    def __init__(self, loc):
        self.loc = loc
        self.CurrencySymbol = None
        self.CurrencyNegativePattern = None
        self.SignPosition = None
        self.ThousandsSeparator = None
        self.ShortDatePattern = None


class LedgerEntry(object):
    def __init__(self, date: datetime, desc: str, chg: float):
        self.Date = date
        self.Desc = desc
        self.Chg = chg


class Ledger(object):
    @staticmethod
    def CreateEntry(date: str, desc: str, chng: int):
        return LedgerEntry(datetime.strptime(date, '%Y-%m-%d'), desc, chng / 100.0)

    @staticmethod
    def CreateCulture(cur: str, loc: str):
        curSymb = None
        curNeg = 0
        thoSep = None
        sigPos = 0  # Currency and value are surrounded by parentheses.
        datPat = None

        if cur != "USD" and cur != "EUR":
            raise Exception("Invalid currency")
        else:
            if loc != "nl-NL" and loc != "en-US":
                raise Exception("Invalid currency")

            if cur == "USD":
                if loc == "en-US":
                    curSymb = "$"
                    thoSep = ','
                    datPat = "%m/%d/%Y"
                elif loc == "nl-NL":
                    curSymb = "$"
                    curNeg = 12
                    thoSep = '.'
                    sigPos = 3  # The sign should immediately precede the value.
                    datPat = "%d/%m/%Y"

            if cur == "EUR":
                if loc == "en-US":
                    curSymb = "€"
                    thoSep = ','
                    datPat = "%m/%d/%Y"
                elif loc == "nl-NL":
                    curSymb = "€"
                    curNeg = 12
                    thoSep = '.'
                    sigPos = 3  # The sign should immediately precede the value.
                    datPat = "%d/%m/%Y"

        loc_info = LocaleInfo(loc)
        loc_info.CurrencySymbol = curSymb
        loc_info.CurrencyNegativePattern = curNeg
        loc_info.ThousandsSeparator = thoSep
        loc_info.SignPosition = sigPos
        loc_info.ShortDatePattern = datPat
        return loc_info

    @staticmethod
    def PrintHead(loc: str):
        if loc == "en-US":
            return "Date       | Description               | Change       "

        else:
            if loc == "nl-NL":
                return "Datum      | Omschrijving              | Verandering  "
            else:
                raise Exception("Invalid locale")

    @staticmethod
    def Date(loc_info, date: datetime) -> str:
        return datetime.strftime(date, loc_info.ShortDatePattern)

    @staticmethod
    def Description(desc):
        if len(desc) > 25:
            trunc = desc[0:22]
            trunc += "..."
            return trunc

        return desc

    @staticmethod
    def Change(loc_info: LocaleInfo, cgh: float):

        locale.setlocale(locale.LC_ALL, loc_info.loc.replace('-', '_'))  # Convert "nl-NL" to "nl_NL"
        locale._override_localeconv = {
            'mon_thousands_sep': loc_info.ThousandsSeparator,
            'currency_symbol': loc_info.CurrencySymbol,
            'n_sign_posn': loc_info.SignPosition,
        }

        res = locale.currency(cgh, True, True) if cgh < 0.0 else locale.currency(cgh, True, True) + " "

        return res

    @staticmethod
    def PrintEntry(loc_info, entry: LedgerEntry):

        formatted = ""

        date = Ledger.Date(loc_info, entry.Date)
        description = Ledger.Description(entry.Desc)
        change = Ledger.Change(loc_info, entry.Chg)

        formatted += date
        formatted += " | "
        formatted += '{0: <25}'.format(description)
        formatted += " | "
        formatted += '{0: >13}'.format(change)

        return formatted

    @staticmethod
    def Sort(entries):
        return sorted(entries, key=lambda x: x.Chg)

    @staticmethod
    def Format(currency: str, locale: str, entries: list):

        formatted = ""
        formatted += Ledger.PrintHead(locale)

        loc_info = Ledger.CreateCulture(currency, locale)

        if len(entries) > 0:
            entriesForOutput = Ledger.Sort(entries)
            for entry in entriesForOutput:
                formatted += "\n" + Ledger.PrintEntry(loc_info, entry)

        return formatted
