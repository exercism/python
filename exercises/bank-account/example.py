import threading


class BankAccount(object):
    def __init__(self):
        self.is_open = False
        self.balance = 0
        self.lock = threading.Lock()

    def get_balance(self):
        with self.lock:
            if self.is_open:
                return self.balance
            else:
                raise ValueError

    def open(self):
        self.is_open = True

    def deposit(self, amount):
        with self.lock:
            if self.is_open and amount > 0:
                self.balance += amount
            else:
                raise ValueError

    def withdraw(self, amount):
        with self.lock:
            if self.is_open and 0 < amount <= self.balance:
                self.balance -= amount
            else:
                raise ValueError

    def close(self):
        self.is_open = False
