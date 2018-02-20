from __future__ import division

from fractions import gcd


class Rational(object):
    """
    Toyish implementation of rational numbers. For production purpose,
    please use `fractions.Fraction` in standard library instead.
    """
    def __init__(self, numer, denom):
        self.numer, self.denom = self._reduce(numer, denom)

    def _reduce(self, numer, denom):
        if numer == 0:
            n, d = 0, 1
        else:
            g = gcd(numer, denom)
            n, d = int(numer/g), int(denom/g)
            if n > 0 and d < 0:
                n, d = -n, -d
        return n, d

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        return Rational(
            self.numer*other.denom + self.denom*other.numer,
            self.denom*other.denom
        )

    def __sub__(self, other):
        return Rational(
            self.numer*other.denom - self.denom*other.numer,
            self.denom*other.denom
        )

    def __mul__(self, other):
        return Rational(self.numer * other.numer, self.denom * other.denom)

    def __truediv__(self, other):
        return Rational(self.numer * other.denom, self.denom * other.numer)

    def __abs__(self):
        if self.numer >= 0:
            return self
        else:
            return Rational(-self.numer, self.denom)

    def __pow__(self, power):
        return Rational(self.numer ** power, self.denom ** power)

    def __rpow__(self, base):
        return base ** (self.numer / self.denom)
