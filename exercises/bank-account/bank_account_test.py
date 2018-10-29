import sys
import threading
import time
import unittest

from bank_account import BankAccount


class BankAccountTest(unittest.TestCase):

    def setUp(self):
        self.account = BankAccount()

    def test_newly_opened_account_has_zero_balance(self):
        self.account.open()
        self.assertEqual(self.account.get_balance(), 0)

    def test_can_deposit_money(self):
        self.account.open()
        self.account.deposit(100)
        self.assertEqual(self.account.get_balance(), 100)

    def test_can_deposit_money_sequentially(self):
        self.account.open()
        self.account.deposit(100)
        self.account.deposit(50)

        self.assertEqual(self.account.get_balance(), 150)

    def test_can_withdraw_money(self):
        self.account.open()
        self.account.deposit(100)
        self.account.withdraw(50)

        self.assertEqual(self.account.get_balance(), 50)

    def test_can_withdraw_money_sequentially(self):
        self.account.open()
        self.account.deposit(100)
        self.account.withdraw(20)
        self.account.withdraw(80)

        self.assertEqual(self.account.get_balance(), 0)

    def test_checking_balance_of_closed_account_throws_error(self):
        self.account.open()
        self.account.close()

        with self.assertRaises(ValueError):
            self.account.get_balance()

    def test_deposit_into_closed_account(self):
        self.account.open()
        self.account.close()

        with self.assertRaises(ValueError):
            self.account.deposit(50)

    def test_withdraw_from_closed_account(self):
        self.account.open()
        self.account.close()

        with self.assertRaises(ValueError):
            self.account.withdraw(50)

    def test_cannot_withdraw_more_than_deposited(self):
        self.account.open()
        self.account.deposit(25)

        with self.assertRaises(ValueError):
            self.account.withdraw(50)

    def test_cannot_withdraw_negative(self):
        self.account.open()
        self.account.deposit(100)

        with self.assertRaises(ValueError):
            self.account.withdraw(-50)

    def test_cannot_deposit_negative(self):
        self.account.open()

        with self.assertRaises(ValueError):
            self.account.deposit(-50)

    def test_can_handle_concurrent_transactions(self):
        self.account.open()
        self.account.deposit(1000)

        for _ in range(10):
            self.adjust_balance_concurrently()

    def adjust_balance_concurrently(self):
        def transact():
            self.account.deposit(5)
            time.sleep(0.001)
            self.account.withdraw(5)

        # Greatly improve the chance of an operation being interrupted
        # by thread switch, thus testing synchronization effectively
        try:
            sys.setswitchinterval(1e-12)
        except AttributeError:
            # For Python 2 compatibility
            sys.setcheckinterval(1)

        threads = []
        for _ in range(1000):
            t = threading.Thread(target=transact)
            threads.append(t)
            t.start()

        for thread in threads:
            thread.join()

        self.assertEqual(self.account.get_balance(), 1000)


if __name__ == '__main__':
    unittest.main()
