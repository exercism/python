# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/nth-prime/canonical-data.json
# File last updated on 2023-07-19

import unittest

from nth_prime import (
    prime,
)


def prime_range(n):
    """Returns a list of the first n primes"""
    return [prime(i) for i in range(1, n + 1)]


class NthPrimeTest(unittest.TestCase):
    def test_first_prime(self):
        self.assertEqual(prime(1), 2)

    def test_second_prime(self):
        self.assertEqual(prime(2), 3)

    def test_sixth_prime(self):
        self.assertEqual(prime(6), 13)

    def test_big_prime(self):
        self.assertEqual(prime(10001), 104743)

    def test_there_is_no_zeroth_prime(self):
        with self.assertRaises(ValueError) as err:
            prime(0)
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "there is no zeroth prime")

    # Additional tests for this track

    def test_first_twenty_primes(self):
        self.assertEqual(
            prime_range(20),
            [
                2,
                3,
                5,
                7,
                11,
                13,
                17,
                19,
                23,
                29,
                31,
                37,
                41,
                43,
                47,
                53,
                59,
                61,
                67,
                71,
            ],
        )
