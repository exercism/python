import math

class ComplexNumber:
    def __init__(self, real=0, imaginary=0):
        self.real = real
        self.imaginary = imaginary

    def __eq__(self, other):
        if not isinstance(other, ComplexNumber):
            other = ComplexNumber(other)
        return self.real == other.real and self.imaginary == other.imaginary

    def __add__(self, other):

        if not isinstance(other, ComplexNumber):
            other = ComplexNumber(other)

        real_part = self.real + other.real
        imaginary_part = self.imaginary + other.imaginary

        return ComplexNumber(real_part, imaginary_part)

    def __radd__(self, other):

        if not isinstance(other, ComplexNumber):
            other = ComplexNumber(other)

        real_part = self.real + other.real
        imaginary_part = self.imaginary + other.imaginary

        return ComplexNumber(real_part, imaginary_part)

    def __mul__(self, other):
        if not isinstance(other, ComplexNumber):
            other = ComplexNumber(other)

        real_part = self.real * other.real - self.imaginary * other.imaginary
        imaginary_part = self.real * other.imaginary + self.imaginary * other.real
        return ComplexNumber(real_part, imaginary_part)

    def __rmul__(self, other):
        if not isinstance(other, ComplexNumber):
            other = ComplexNumber(other)

        real_part = self.real * other.real - self.imaginary * other.imaginary
        imaginary_part = self.real * other.imaginary + self.imaginary * other.real
        return ComplexNumber(real_part, imaginary_part)

    def __sub__(self, other):
        if not isinstance(other, ComplexNumber):
            other = ComplexNumber(other)
        real_part = self.real - other.real
        imaginary_part = self.imaginary - other.imaginary
        return ComplexNumber(real_part, imaginary_part)

    def __rsub__(self, other):
        if not isinstance(other, ComplexNumber):
            other = ComplexNumber(other)

        real_part = other.real - self.real
        imaginary_part = other.imaginary - self.imaginary
        return ComplexNumber(real_part, imaginary_part)

    def __truediv__(self, other):
        if not isinstance(other, ComplexNumber):
            other = ComplexNumber(other)

        conjugation = other.conjugate()
        denominator_all = other * conjugation
        denominator = denominator_all.real
        numerator = self * conjugation

        return ComplexNumber((numerator.real / denominator), (numerator.imaginary / denominator))

    def __rtruediv__(self, other):
        if not isinstance(other, ComplexNumber):
            other = ComplexNumber(other)

        conjugation = self.conjugate()
        denominator_all = self * conjugation
        denominator = float(denominator_all.real)
        numerator = other * conjugation

        return ComplexNumber((numerator.real / denominator), (numerator.imaginary / denominator))

    def __abs__(self):
        square_sum = self.real * self.real + self.imaginary * self.imaginary
        return math.sqrt(square_sum)

    def conjugate(self):
        return ComplexNumber(self.real, -1 * self.imaginary)

    def exp(self):
        real_part = math.cos(self.imaginary) * math.exp(self.real)
        imaginary_part = math.sin(self.imaginary) * math.exp(self.real)
        return ComplexNumber(real_part, imaginary_part)
