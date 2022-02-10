from math import gcd


class Rational:
    def __init__(self, numer, denom):
        # abs used for backward compatibility with fractions.gcd
        gcd_num = abs(gcd(numer, denom))

        self.numer = numer // gcd_num
        self.denom = denom // gcd_num

        if self.denom < 0:
            self.numer *= -1
            self.denom *= -1

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return f'{self.numer}/{self.denom}'

    def __add__(self, other):
        numer = (self.numer * other.denom) + (other.numer * self.denom)
        return Rational(numer, other.denom * self.denom)

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        return Rational(self.numer * other.numer, self.denom * other.denom)

    def __truediv__(self, other):
        return Rational(self.numer * other.denom, self.denom * other.numer)

    def __abs__(self):
        return Rational(abs(self.numer), self.denom)

    def __pow__(self, power):
        if power < 0:
            return Rational(pow(self.denom, -power), pow(self.numer, -power))

        else:
            return Rational(pow(self.numer, power), pow(self.denom, power))

    def __rpow__(self, base):
        return base ** (self.numer / self.denom)

    def __neg__(self):
        return Rational(self.numer * (-1), self.denom)
