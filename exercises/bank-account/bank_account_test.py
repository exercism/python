import unittest
import threading

from example import BankAccount #to be changed later

class BankAccountTests(unittest.TestCase):

    def test_newly_opened_account_has_zero_balance(self):
        self.account = BankAccount()
        self.account.open()

        self.assertEqual(self.account.getBalance(), 0)

    def test_get_balance_0(self):
        self.account = BankAccount()
        self.account.open()

        self.assertEqual(self.account.getBalance(), 0)

    def test_get_balance_with_amount(self):
        self.account = BankAccount()
        self.account.open()
        self.account.deposit(100)

        self.assertEqual(self.account.getBalance(), 100)

    def test_get_balance_0(self):
        self.account = BankAccount()
        self.account.open()

        self.assertEqual(self.account.getBalance(), 0)

    def test_get_balance_with_amount(self):
        self.account = BankAccount()
        self.account.open()
        self.account.deposit(100)

        self.assertEqual(self.account.getBalance(), 100)

    def test_deposit_into_account(self):
        self.account = BankAccount()
        self.account.open()
        self.account.deposit(100)

        self.assertEqual(self.account.getBalance(), 100)

    def test_two_deposits_in_a_row(self):
        self.account = BankAccount()
        self.account.open()
        self.account.deposit(100)
        self.account.deposit(50)

        self.assertEqual(self.account.getBalance(), 150)

    def test_can_withdraw(self):
        self.account = BankAccount()
        self.account.open()
        self.account.deposit(100)
        self.account.withdraw(50)

        self.assertEqual(self.account.getBalance(), 50)

    def test_checking_balance_of_closed_account_throws_error(self):
        self.account = BankAccount()
        self.account.open()
        self.account.close()

        with self.assertRaises(Exception):
            self.account.getBalance()

    def test_deposit_into_closed_account(self):
        self.account = BankAccount()
        self.account.open()
        self.account.close()

        with self.assertRaises(Exception):
            self.account.deposit(50)



    def test_withdraw_from_closed_account(self):
        self.account = BankAccount()
        self.account.open()
        self.account.close()

        with self.assertRaises(Exception):
            self.account.withdraw(50)

    def test_cannot_withdraw_more_than_deposited(self):
        self.account = BankAccount()
        self.account.open()
        self.account.deposit(25)

        with self.assertRaises(Exception):
            self.account.withdraw(50)

    def test_cannot_withdraw_negative(self):
        self.account = BankAccount()
        self.account.open()
        self.account.deposit(100)

        with self.assertRaises(Exception):
            self.account.withdraw(-50)

    def test_cannot_deposit_negative(self):
        self.account = BankAccount()
        self.account.open()

        with self.assertRaises(Exception):
            self.account.deposit(-50)



    def test_can_handle_concurrent_transactions(self):
        def increment_and_decrement(self):
            self.account.deposit(10)
            self.account.withdraw(1)

        with self.assertRaises(Exception):
            self.account.withdraw(-50)

        self.account = BankAccount()
        self.account.open()

        threadlist = []
        threads = 100
        i=0
        while (i<threads):
            thread = threading.Thread(target=increment_and_decrement, args=(self, ))
            threadlist.append(thread)
            i += 1

        for thread in threadlist:
            thread.start()

        for thread in threadlist:
            thread.join()

        self.assertEqual(self.account.getBalance(), 900)

if __name__ == '__main__':
    unittest.main();
