import unittest

from fibonacci_generator import (
    fibo
)

class FibonacciGeneratorTest(unittest.TestCase):
    def test_fibo_is_generator(self):
        fib = fibo()
        self.assertEqual(type(fib).__name__, 'generator')

    def test_fibo_using_next(self):
        fib = fibo()
        self.assertEqual(next(fib), 0)
        self.assertEqual(next(fib), 1)
        self.assertEqual(next(fib), 1)
        self.assertEqual(next(fib), 2)
        self.assertEqual(next(fib), 3)
        self.assertEqual(next(fib), 5)
        self.assertEqual(next(fib), 8)
        self.assertEqual(next(fib), 13)
        self.assertEqual(next(fib), 21)
        self.assertEqual(next(fib), 34)

    def test_fibo_using_for(self):
        numbers = []
        for num in fibo():
            numbers.append(num)
            if num > 100:
                break
        self.assertEqual(numbers, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144])

