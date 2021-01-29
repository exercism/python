import re


class PhoneNumber:
    def __init__(self, number):
        self.number = self._clean(number)
        self.area_code = self.number[:3]
        self.exchange_code = self.number[3:6]
        self.subscriber_number = self.number[-4:]

    def pretty(self):
        return "({})-{}-{}".format(
            self.area_code, self.exchange_code, self.subscriber_number
        )

    def _clean(self, number):
        return self._normalize(re.sub(r"[^\d]", "", number))

    def _normalize(self, number):
        if len(number) == 10 or len(number) == 11 and number.startswith("1"):
            valid = number[-10] in "23456789" and number[-7] in "23456789"
        else:
            valid = False

        if valid:
            return number[-10:]
        else:
            raise ValueError("{} is not a valid phone number".format(number))
