import math


class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __eq__(self, other):
        return self.real == other.real and self.imaginary == other.imaginary

    def __add__(self, other):
        r = self.real + other.real
        i = self.imaginary + other.imaginary
        return ComplexNumber(r, i)

    def __mul__(self, other):
        r = self.real * other.real - self.imaginary * other.imaginary
        i = self.real * other.imaginary + self.imaginary * other.real
        return ComplexNumber(r, i)

    def __sub__(self, other):
        r = self.real - other.real
        i = self.imaginary - other.imaginary
        return ComplexNumber(r, i)

    def __truediv__(self, other):
        d = other.real * other.real + other.imaginary * other.imaginary
        r = (self.real * other.real + self.imaginary *
             other.imaginary) / float(d)
        i = (self.imaginary * other.real - self.real *
             self.real * other.imaginary) / float(d)
        return ComplexNumber(r, i)

    def __abs__(self):
        square_sum = self.real * self.real + self.imaginary * self.imaginary
        return math.sqrt(square_sum)

    def conjugate(self):
        return ComplexNumber(self.real, -1 * self.imaginary)

    def exp(self):
        r = math.cos(self.imaginary) * math.exp(self.real)
        i = math.sin(self.imaginary) * math.exp(self.real)
        return ComplexNumber(r, i)
