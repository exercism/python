import timeit

loops = 1_000_000

val = timeit.timeit("""Luhn("9999999999 9999999999 9999999999 9999999999").valid()""",
                    """
class Luhn:

    def __init__(self, card_num):
        self.isValid = Luhn.luhny_bin(card_num)

    def valid(self):
        return self.isValid

    @staticmethod
    def luhny_tune(num):
        return dbl - 9 if (dbl := 2 * num) > 9 else dbl

    @staticmethod
    def luhny_bin(num):
        total = 0
        pos = 0
        for ltr in reversed(num):
            if ltr.isdigit():
                if not pos % 2:
                    total+= int(ltr)
                else:
                    total += Luhn.luhny_tune(int(ltr))
                pos += 1
            elif ltr != " ":
                return False
        return pos > 1 and not total % 10

""", number=loops) / loops

print(f"reversed for:                 {val}")

val = timeit.timeit("""Luhn("9999999999 9999999999 9999999999 9999999999").valid()""",
                    """
class Luhn:

    def __init__(self, card_num):
        self.isValid = Luhn.luhny_bin(card_num)

    def valid(self):
        return self.isValid

    @staticmethod
    def luhny_tune(num):
        return dbl - 9 if (dbl := 2 * num) > 9 else dbl

    @staticmethod
    def luhny_bin(num):
        num = num.replace(' ', '')
        if not num.isdigit():
            return False
        total = 0
        for pos, ltr in enumerate(num[::-1]):
            if not pos % 2:
                total+= int(ltr)
            else:
                total += Luhn.luhny_tune(int(ltr))
            pos += 1
        return pos > 1 and not total % 10

""", number=loops) / loops

print(f"replace reverse enumerate:    {val}")

val = timeit.timeit("""Luhn("9999999999 9999999999 9999999999 9999999999").valid()""",
                    """
class Luhn:
    def __init__(self, card_num):
        self.isValid = Luhn.luhny_bin(0, 0, list(card_num[::-1]))

    def valid(self):
        return self.isValid

    @staticmethod
    def luhny_tune(num):
        return dbl - 9 if (dbl := 2 * num) > 9 else dbl

    @staticmethod
    def luhny_bin(pos, sum, chars):
        if not chars:
            return pos  > 1 and sum % 10 == 0
        else:
            head, *tail = chars
            if head.isdigit():
                if not pos % 2:
                    return Luhn.luhny_bin(pos + 1, sum + int(head), tail)
                else:
                    return Luhn.luhny_bin(pos + 1, sum + Luhn.luhny_tune(int(head)), tail)
            if head == " ":
                return Luhn.luhny_bin(pos, sum, tail)
            return False

""", number=loops) / loops

print(f"recursion:                    {val}")
