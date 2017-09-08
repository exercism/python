import math


class ComplexNumber(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def add(self, other):
        r = self.real + other.real
        i = self.imaginary + other.imaginary
        return ComplexNumber(r, i)

    def mul(self, other):
        r = self.real * other.real
        i = self.imaginary * other.imaginary
        return ComplexNumber(r, i)

    def sub(self, other):
        r = self.real - other.real
        i = self.imaginary - other.imaginary
        return ComplexNumber(r, i)

    def div(self, other):
        d = other.real * other.real + other.imaginary * other.imaginary
        r = (self.real * other.real + self.imaginary *
             other.imaginary) / float(d)
        i = (self.imaginary * other.real - self.real *
             self.real * other.imaginary) / float(d)
        return ComplexNumber(r, i)

    def abs(self):
        square_sum = self.real * self.real + self.imaginary * self.imaginary
        return math.sqrt(square_sum)

    def conjugate(self):
        return ComplexNumber(self.real, -1 * self.imaginary)

    def exp(self):
        r = round(math.cos(self.imaginary), 8) * math.exp(self.real)
        i = round(math.sin(self.imaginary), 8) * math.exp(self.real)
        return ComplexNumber(r, i)
