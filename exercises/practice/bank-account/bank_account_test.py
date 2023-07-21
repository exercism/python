# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/bank-account/canonical-data.json
# File last updated on 2023-07-20

import unittest

from bank_account import (
    BankAccount,
)


class BankAccountTest(unittest.TestCase):
    def test_newly_opened_account_has_zero_balance(self):
        account = BankAccount()
        account.open()
        self.assertEqual(account.get_balance(), 0)

    def test_single_deposit(self):
        account = BankAccount()
        account.open()
        account.deposit(100)
        self.assertEqual(account.get_balance(), 100)

    def test_multiple_deposits(self):
        account = BankAccount()
        account.open()
        account.deposit(100)
        account.deposit(50)
        self.assertEqual(account.get_balance(), 150)

    def test_withdraw_once(self):
        account = BankAccount()
        account.open()
        account.deposit(100)
        account.withdraw(75)
        self.assertEqual(account.get_balance(), 25)

    def test_withdraw_twice(self):
        account = BankAccount()
        account.open()
        account.deposit(100)
        account.withdraw(80)
        account.withdraw(20)
        self.assertEqual(account.get_balance(), 0)

    def test_can_do_multiple_operations_sequentially(self):
        account = BankAccount()
        account.open()
        account.deposit(100)
        account.deposit(110)
        account.withdraw(200)
        account.deposit(60)
        account.withdraw(50)
        self.assertEqual(account.get_balance(), 20)

    def test_cannot_check_balance_of_closed_account(self):
        account = BankAccount()
        account.open()
        account.close()
        with self.assertRaises(ValueError) as err:
            account.get_balance()
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "account not open")

    def test_cannot_deposit_into_closed_account(self):
        account = BankAccount()
        account.open()
        account.close()
        with self.assertRaises(ValueError) as err:
            account.deposit(50)
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "account not open")

    def test_cannot_deposit_into_unopened_account(self):
        account = BankAccount()
        with self.assertRaises(ValueError) as err:
            account.deposit(50)
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "account not open")

    def test_cannot_withdraw_from_closed_account(self):
        account = BankAccount()
        account.open()
        account.close()
        with self.assertRaises(ValueError) as err:
            account.withdraw(50)
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "account not open")

    def test_cannot_close_an_account_that_was_not_opened(self):
        account = BankAccount()
        with self.assertRaises(ValueError) as err:
            account.close()
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "account not open")

    def test_cannot_open_an_already_opened_account(self):
        account = BankAccount()
        account.open()
        with self.assertRaises(ValueError) as err:
            account.open()
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "account already open")

    def test_reopened_account_does_not_retain_balance(self):
        account = BankAccount()
        account.open()
        account.deposit(50)
        account.close()
        account.open()
        self.assertEqual(account.get_balance(), 0)

    def test_cannot_withdraw_more_than_deposited(self):
        account = BankAccount()
        account.open()
        account.deposit(25)
        with self.assertRaises(ValueError) as err:
            account.withdraw(50)
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "amount must be less than balance")

    def test_cannot_withdraw_negative(self):
        account = BankAccount()
        account.open()
        account.deposit(100)
        with self.assertRaises(ValueError) as err:
            account.withdraw(-50)
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "amount must be greater than 0")

    def test_cannot_deposit_negative(self):
        account = BankAccount()
        account.open()
        with self.assertRaises(ValueError) as err:
            account.deposit(-50)
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "amount must be greater than 0")
