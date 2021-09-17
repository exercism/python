import unittest
import pytest
from secrets import secret_add, secret_multiply, secret_max, secret_combine


class TestLambdas(unittest.TestCase):
    @pytest.mark.task(taskno=1)
    def test_add_3(self):
        self.assertEqual(secret_add(3)(3), 6)

    @pytest.mark.task(taskno=1)
    def test_add_6(self):
        self.assertEqual(secret_add(6)(9), 15)

    @pytest.mark.task(taskno=2)
    def test_multiply_by_3(self):
        self.assertEqual(secret_multiply(3)(6), 18)

    @pytest.mark.task(taskno=2)
    def test_multiply_by_6(self):
        self.assertEqual(secret_multiply(6)(7), 42)

    @pytest.mark.task(taskno=3)
    def test_max_1(self):
        self.assertEqual(secret_max([2, 11])([7, 3]), [2, 11])

    @pytest.mark.task(taskno=3)
    def test_max_2(self):
        self.assertEqual(secret_max([4, 6])([5, 5]), [5, 5])

    @pytest.mark.task(taskno=3)
    def test_max_3(self):
        self.assertEqual(secret_max([25, 73])([56, 32]), [25, 73])