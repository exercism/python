import unittest
import pytest
from secrets import secret_add, secret_multiply, secret_max, secret_sort, secret_combine


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

    @pytest.mark.task(taskno=4)
    def test_sort_1(self):
        self.assertEqual(secret_sort(0)([[3, 120, 5], [1, 5, 2], [8, 2, 23]]), [[1, 5, 2], [3, 120, 5], [8, 2, 23]])

    @pytest.mark.task(taskno=4)
    def test_sort_2(self):
        self.assertEqual(secret_sort(1)([[3, 15], [520, 1, 4], [64, 7, 3, 9, 2], [0, 27, 1, 5, 4, 2]]), [[520, 1, 4], [64, 7, 3, 9, 2], [3, 15], [0, 27, 1, 5, 4, 2]])

    @pytest.mark.task(taskno=5)
    def test_combine_1(self):
        self.assertEqual(secret_combine(secret_add(4), secret_multiply(7))(6), 70)

    @pytest.mark.task(taskno=5)
    def test_combine_2(self):
        self.assertEqual(secret_combine(secret_multiply(6), secret_add(4))(11), 70)

    @pytest.mark.task(taskno=5)
    def test_combine_3(self):
        self.assertEqual(secret_combine(secret_max([3, 8]), sum)([4, 5]), 11)