import threading


class BankAccount(object):
    def __init__(self):
        self.isOpen = False
        self.lock = threading.Lock()

    def getBalance(self):
        self.lock.acquire()
        if (self.isOpen):
            self.lock.release()
            return self.balance
        else:
            self.lock.release()
            raise ValueError

    def open(self):
        self.lock.acquire()
        self.balance = 0
        self.isOpen = True
        self.lock.release()

    def deposit(self, amount):
        self.lock.acquire()
        if (self.isOpen and amount > 0):
            self.balance += amount
            self.lock.release()
        else:
            self.lock.release()
            raise ValueError

    def withdraw(self, amount):
        self.lock.acquire()
        if (self.isOpen and self.balance >= amount and amount > 0):
            self.balance -= amount
            self.lock.release()
        else:
            self.lock.release()
            raise ValueError

    def close(self):
        self.lock.acquire()
        self.isOpen = False
        self.lock.release()
