# unit test here
import unittest
import pytest
from conditionals import (is_criticality_balanced,
                          reactor_efficiency,
                          fail_safe)


class TestConditionals(unittest.TestCase):
    # Test cases for is_criticality_balanced()

    # Testing border cases around typical points T, n == (800, 500), (625, 800), (500, 1000)
    @pytest.mark.task(taskno=1)
    def test_is_criticality_balanced(self):
        for temperature, neutrons_emitted, expected in (
            (750, 650, True), (799, 501, True), (500, 600, True), (1000, 800, False),
            (800, 500, False), (800, 500.01, False), (799.99, 500, False), (500.01, 999.99, False),
            (625, 800, False), (625.99, 800, False), (625.01, 799.99, False),
            (799.99, 500.01, True), (624.99, 799.99, True),
            (500, 1000, False), (500.01, 1000, False), (499.99, 1000, True),
            ):
            got = is_criticality_balanced(temperature=temperature, neutrons_emitted=neutrons_emitted)
            self.assertEqual(
                got,
                expected,
                msg=f"Expected {expected} but returned {got} with {temperature=} and {neutrons_emitted=}"
            )


    # End of first functions testing

    # Test cases for reactor_ efficiency()

    @pytest.mark.task(taskno=2)
    def test_reactor_efficiency(self):
        voltage = 10
        theoretical_max_power = 10000
        # The numbers are chosen so that current == 10 x percentage
        for current, expected in (
            (1000, 'green'), (999, 'green'), (800, 'green'),
            (799, 'orange'), (700, 'orange'), (600, 'orange'),
            (599, 'red'), (560, 'red'), (400, 'red'), (300, 'red'),
            (299, 'black'), (200, 'black'), (0, 'black'),
            ):
            got = reactor_efficiency(voltage=voltage, current=current, theoretical_max_power=theoretical_max_power)
            self.assertEqual(
                got,
                expected,
                msg=f"Expected {expected} but returned {got} with {voltage=}, {current=}, {theoretical_max_power=}"
            )



    # End of second function testing

    # Test cases for fail_safe()

    @pytest.mark.task(taskno=3)
    def test_fail_safe(self):
        temperature = 10
        threshold = 10000
        for neutrons_produced_per_second, expected in (
            (399, 'LOW'), (300, 'LOW'), (1, 'LOW'), (0, 'LOW'),
            (901, 'NORMAL'), (1000, 'NORMAL'), (1099, 'NORMAL'),
            (899, 'DANGER'), (700, 'DANGER'), (400, 'DANGER'), (1101, 'DANGER'), (1200, 'DANGER'),
            ):
            got = fail_safe(
                temperature=temperature, neutrons_produced_per_second=neutrons_produced_per_second, threshold=threshold
                )
            self.assertEqual(
                got,
                expected,
                msg=f"Expected {expected} but returned {got} with {temperature=}, {neutrons_produced_per_second=}, {threshold=}"
            )

    # End of third function testing
