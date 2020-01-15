import sys
import threading
import time
import unittest

from bank_account import BankAccount


class BankAccountTest(unittest.TestCase):
    def test_newly_opened_account_has_zero_balance(self):
        account = BankAccount()
        account.open()
        self.assertEqual(account.get_balance(), 0)

    def test_can_deposit_money(self):
        account = BankAccount()
        account.open()
        account.deposit(100)
        self.assertEqual(account.get_balance(), 100)

    def test_can_deposit_money_sequentially(self):
        account = BankAccount()
        account.open()
        account.deposit(100)
        account.deposit(50)

        self.assertEqual(account.get_balance(), 150)

    def test_can_withdraw_money(self):
        account = BankAccount()
        account.open()
        account.deposit(100)
        account.withdraw(50)

        self.assertEqual(account.get_balance(), 50)

    def test_can_withdraw_money_sequentially(self):
        account = BankAccount()
        account.open()
        account.deposit(100)
        account.withdraw(20)
        account.withdraw(80)

        self.assertEqual(account.get_balance(), 0)

    def test_checking_balance_of_closed_account_throws_error(self):
        account = BankAccount()
        account.open()
        account.close()

        with self.assertRaisesWithMessage(ValueError):
            account.get_balance()

    def test_deposit_into_closed_account(self):
        account = BankAccount()
        account.open()
        account.close()

        with self.assertRaisesWithMessage(ValueError):
            account.deposit(50)

    def test_withdraw_from_closed_account(self):
        account = BankAccount()
        account.open()
        account.close()

        with self.assertRaisesWithMessage(ValueError):
            account.withdraw(50)

    def test_close_already_closed_account(self):
        account = BankAccount()
        with self.assertRaisesWithMessage(ValueError):
            account.close()

    def test_open_already_opened_account(self):
        account = BankAccount()
        account.open()
        with self.assertRaisesWithMessage(ValueError):
            account.open()

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

        with self.assertRaises(ValueError):
            account.withdraw(50)

    def test_cannot_withdraw_negative(self):
        account = BankAccount()
        account.open()
        account.deposit(100)

        with self.assertRaisesWithMessage(ValueError):
            account.withdraw(-50)

    def test_cannot_deposit_negative(self):
        account = BankAccount()
        account.open()

        with self.assertRaisesWithMessage(ValueError):
            account.deposit(-50)

    def test_can_handle_concurrent_transactions(self):
        account = BankAccount()
        account.open()
        account.deposit(1000)

        self.adjust_balance_concurrently(account)

        self.assertEqual(account.get_balance(), 1000)

    def adjust_balance_concurrently(self, account):
        def transact():
            account.deposit(5)
            time.sleep(0.001)
            account.withdraw(5)

        # Greatly improve the chance of an operation being interrupted
        # by thread switch, thus testing synchronization effectively
        try:
            sys.setswitchinterval(1e-12)
        except AttributeError:
            # For Python 2 compatibility
            sys.setcheckinterval(1)

        threads = [threading.Thread(target=transact) for _ in range(1000)]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()

    # Utility functions
    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")


if __name__ == '__main__':
    unittest.main()
