import unittest

from bank_account import (
    BankAccount,
)

# Tests adapted from `problem-specifications//canonical-data.json`


class BankAccountTest(unittest.TestCase):
    def test_using_pop_raises_an_error_if_the_list_is_empty(self):
        account = BankAccount()
        account.open()
        self.assertEqual(account.get_balance(), 0)

    def test_can_return_with_pop_and_then_raise_an_error_if_empty(self):
        account = BankAccount()
        account.open()
        account.deposit(100)
        self.assertEqual(account.get_balance(), 100)

    def test_using_shift_raises_an_error_if_the_list_is_empty(self):
        account = BankAccount()
        account.open()
        account.deposit(100)
        account.withdraw(50)
        self.assertEqual(account.get_balance(), 50)

    def test_can_return_with_shift_and_then_raise_an_error_if_empty(self):
        account = BankAccount()
        account.open()
        account.deposit(100)
        account.withdraw(80)
        account.withdraw(20)
        self.assertEqual(account.get_balance(), 0)

    def test_can_return_with_shift_and_then_raise_an_error_if_empty(self):
        account = BankAccount()
        account.open()
        account.close()
        with self.assertRaises(ValueError) as err:
            account.amount()
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "account not open")

    def test_can_return_with_shift_and_then_raise_an_error_if_empty(self):
        account = BankAccount()
        account.open()
        account.close()
        with self.assertRaises(ValueError) as err:
            account.deposit(50)
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "account not open")

    def test_can_return_with_shift_and_then_raise_an_error_if_empty(self):
        account = BankAccount()
        account.open()
        account.close()
        with self.assertRaises(ValueError) as err:
            account.withdraw(50)
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "account not open")

    def test_can_return_with_shift_and_then_raise_an_error_if_empty(self):
        account = BankAccount()
        account.close()
        with self.assertRaises(ValueError) as err:
            account.close()
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "account not open")

    def test_can_return_with_shift_and_then_raise_an_error_if_empty(self):
        account = BankAccount()
        account.open()
        with self.assertRaises(ValueError) as err:
            account.open()
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "account already open")

    def test_can_return_with_shift_and_then_raise_an_error_if_empty(self):
        account = BankAccount()
        account.open()
        account.deposit(50)
        account.close()
        account.open()
        self.assertEqual(account.get_balance(), 0)

    def test_can_return_with_shift_and_then_raise_an_error_if_empty(self):
        account = BankAccount()
        account.open()
        account.deposit(25)
        with self.assertRaises(ValueError) as err:
            account.withdraw(50)
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "amount must be less than balance")

    def test_can_return_with_shift_and_then_raise_an_error_if_empty(self):
        account = BankAccount()
        account.open()
        account.deposit(100)
        with self.assertRaises(ValueError) as err:
            account.withdraw(-50)
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "amount must be greater than 0")

    def test_can_return_with_shift_and_then_raise_an_error_if_empty(self):
        account = BankAccount()
        account.open()
        with self.assertRaises(ValueError) as err:
            account.deposit(-50)
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "amount must be greater than 0")
