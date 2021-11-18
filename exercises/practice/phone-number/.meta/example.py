import re
from string import punctuation


class PhoneNumber:
    def __init__(self, number):
        self.number = self._clean(number)
        self.area_code = self.number[:3]
        self.exchange_code = self.number[3:6]
        self.subscriber_number = self.number[-4:]

    def pretty(self):
        return f'({self.area_code})-{self.exchange_code}-{self.subscriber_number}'

    def _clean(self, number):
        preprocess = re.sub(r'[() +-.]', '', number)

        if any(item for item in preprocess if item.isalpha()):
            raise ValueError('letters not permitted')

        if any(item for item in preprocess if item in punctuation):
            raise ValueError('punctuations not permitted')

        return self._normalize(preprocess)

    def _normalize(self, number):
        if len(number) < 10:
            raise ValueError('incorrect number of digits')

        if len(number) > 11:
            raise ValueError('more than 11 digits')

        if len(number) == 10 or len(number) == 11 and number.startswith('1'):
            if number[-10] == '0':
                raise ValueError('area code cannot start with zero')
            elif number[-10] == '1':
                raise ValueError('area code cannot start with one')
            elif number[-7] == '0':
                raise ValueError('exchange code cannot start with zero')
            elif number[-7] == '1':
                raise ValueError('exchange code cannot start with one')
            else:
                valid = number[-10] in '23456789' and number[-7] in '23456789'

        else:
            valid = False
            if number[0] in '023456789':
                raise ValueError('11 digits must start with 1')

        if valid:
            return number[-10:]

        return None # [Pylint]: R1710;
