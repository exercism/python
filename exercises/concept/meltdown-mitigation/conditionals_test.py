# unit test here
import unittest
import pytest
from conditionals import (is_criticality_balanced,
                          reactor_efficiency,
                          fail_safe
                          )


class TestConditionals(unittest.TestCase):
    # Checking the first condition using assertTrue and assertFalse
    # The values for arguments is not final and should be considered as placeholders
    # More test-cases  required for full testing

    @pytest.mark.task(taskno=1)
    def test_is_criticality_balanced_set1(self):

        self.assertTrue(is_criticality_balanced(
            temperature=750, neutrons_emitted=650), msg="Expected True but returned False")

    @pytest.mark.task(taskno=1)
    def test_is_criticality_balanced_set2(self):

        self.assertTrue(is_criticality_balanced(
            temperature=799, neutrons_emitted=501), msg="Expected True but returned False")

    @pytest.mark.task(taskno=1)
    def test_is_criticality_balanced_set3(self):

        self.assertTrue(
            is_criticality_balanced(temperature=500, neutrons_emitted=600), msg="Expected True but returned False"
        )

    @pytest.mark.task(taskno=1)
    def test_is_criticality_balanced_set4(self):

        self.assertFalse(
            is_criticality_balanced(temperature=800, neutrons_emitted=500), msg="Expected False but returned True"
        )

# End of first functions testing

# Test case for reactor_ efficiency()
    # Checking the second condition using assertEqual
    # The values for arguments is not final and should be considered as placeholders
    # More test-cases  required for full testing
    # need to add more info to messages
    # Need to verify if f-string based errors allowed

    @pytest.mark.task(taskno=2)
    def test_reactor_efficiency_set1(self):

        test_return = reactor_efficiency(
            voltage=100, current=50, theoretical_max_power=5000)
        self.assertEqual(
            test_return, 'green', msg=f"Expected green but returned {test_return}"
        )

    @pytest.mark.task(taskno=2)
    def test_reactor_efficiency_set2(self):
        test_return = reactor_efficiency(
            voltage=100, current=30, theoretical_max_power=5000)
        self.assertEqual(
            test_return, 'orange', msg=f"Expected orange but returned {test_return}"
        )

    @pytest.mark.task(taskno=2)
    def test_reactor_efficiency_set3(self):
        test_return = reactor_efficiency(
            voltage=100, current=28, theoretical_max_power=5000)
        self.assertEqual(
            test_return, 'red', msg=f"Expected red but returned {test_return}"
        )

    @pytest.mark.task(taskno=2)
    def test_reactor_efficiency_set4(self):
        test_return = reactor_efficiency(
            voltage=100, current=10, theoretical_max_power=5000)
        self.assertEqual(
            test_return, 'black', msg=f"Expected black but returned {test_return}"
        )

# End of second function testing


# Test case for fail_safe()
    # Checking the third condition using assertEqual
    # The values for arguments is not final and should be considered as placeholders
    # More test-cases  required for full testing
    # need to add more info to messages
    # Need to verify if f-string based errors allowed

    @pytest.mark.task(taskno=3)
    def test_fail_safe_set1(self):
        test_return = fail_safe(
            temperature=100, neutrons_produced_per_second=18, threshold=5000)
        self.assertEqual(
            test_return, 'LOW', msg=f"Expected LOW but returned {test_return}"
        )

    @pytest.mark.task(taskno=3)
    def test_fail_safe_set2(self):
        test_return = fail_safe(
            temperature=100, neutrons_produced_per_second=12, threshold=4000)
        self.assertEqual(
            test_return, 'LOW', msg=f"Expected LOW but returned {test_return}"
        )

    @pytest.mark.task(taskno=3)
    def test_fail_safe_set3(self):
        test_return = fail_safe(
            temperature=100, neutrons_produced_per_second=10, threshold=3000)
        self.assertEqual(
            test_return, 'LOW', msg=f"Expected LOW but returned {test_return}"
        )

    @pytest.mark.task(taskno=3)
    def test_fail_safe_set4(self):
        test_return = fail_safe(
            temperature=100, neutrons_produced_per_second=55, threshold=5000)
        self.assertEqual(
            test_return, 'NORMAL', msg=f"Expected NORMAL but returned {test_return}"
        )

    @pytest.mark.task(taskno=3)
    def test_fail_safe_set5(self):
        test_return = fail_safe(
            temperature=100, neutrons_produced_per_second=45, threshold=5000)
        self.assertEqual(
            test_return, 'NORMAL', msg=f"Expected NORMAL but returned {test_return}"
        )

    @pytest.mark.task(taskno=3)
    def test_fail_safe_set6(self):
        test_return = fail_safe(
            temperature=100, neutrons_produced_per_second=50, threshold=5000)
        self.assertEqual(
            test_return, 'NORMAL', msg=f"Expected NORMAL but returned {test_return}"
        )

    @pytest.mark.task(taskno=3)
    def test_fail_safe_set7(self):
        test_return = fail_safe(
            temperature=1000, neutrons_produced_per_second=35, threshold=5000)
        self.assertEqual(
            test_return, 'DANGER', msg=f"Expected DANGER but returned {test_return}"
        )

    @pytest.mark.task(taskno=3)
    def test_fail_safe_set8(self):
        test_return = fail_safe(
            temperature=1000, neutrons_produced_per_second=30, threshold=5000)
        self.assertEqual(
            test_return, 'DANGER', msg=f"Expected DANGER but returned {test_return}"
        )

    @pytest.mark.task(taskno=3)
    def test_fail_safe_set9(self):
        test_return = fail_safe(
            temperature=1000, neutrons_produced_per_second=25, threshold=5000)
        self.assertEqual(
            test_return, 'DANGER', msg=f"Expected DANGER but returned {test_return}"
        )
