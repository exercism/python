import re


class Phone(object):
    def __init__(self, number):
        self.number = self._clean(number)

    def area_code(self):
        return self.number[:3]

    def exchange_code(self):
        return self.number[3:6]

    def subscriber_number(self):
        return self.number[-4:]

    def pretty(self):
        return "(%s) %s-%s" % (
            self.area_code(),
            self.exchange_code(),
            self.subscriber_number()
        )

    def _clean(self, number):
        return self._normalize(
            re.sub(r'[^\d]', '', number)
        )

    def _normalize(self, number):
        if len(number) == 10 or len(number) == 11 and number.startswith('1'):
            valid = number[-10] in "23456789" and number[-7] in "23456789"
        else:
            valid = False

        if valid:
            return number[-10:]
        else:
            return '0' * 10
